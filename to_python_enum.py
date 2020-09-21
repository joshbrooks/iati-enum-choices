import xml.etree.ElementTree as ET
import re
import os
from typing import List, Optional
import pathlib

CAT_REPLACE = ("-c", "C")


def slugify(value):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = re.sub(r"[^\w\s-]", "_", value.lower()).strip()
    return re.sub(r"[-\s]+", "_", value)


def output_filepath(filepath):
    """
    Appropriately mangle the filepath to something
    which is importable
    """
    return (
        filepath.replace(*CAT_REPLACE)
        .replace("_", "")
        .replace("-", "")
        .replace(".xml", ".py")
        .lower()
    )


class XmlElementAsEnum:
    """
    Call with a path to an IATI XML file
    to return a Django 'Choices' text blob
    """

    def __init__(self, filepath: os.PathLike):
        tree = ET.parse(filepath)
        self.filepath = filepath
        self.root = tree.getroot()  # Expected to be a "codelist" tag
        self.choices_type = self.get_choices_type()
        self.category = self.root.attrib["name"]

    @property
    def codelist_items(self) -> List[ET.Element]:
        """
        Fetah all of the codelist items in the element
        """
        return self.root.findall("codelist-items/codelist-item")

    def get_choices_type(self) -> str:
        """
        Pick Text or Integer type choices.
        A Django choices can use strings or ints as keys (or custom types,
        but here we deal only with str and int).
        When "all" the types are digits, we choose the "int" type;
        otherwise we choose str type.
        """
        for code in self.root.findall("codelist-items/codelist-item/code"):
            if not code.text.isdigit():
                return "models.TextChoices"
        return "models.IntegerChoices"

    def codelist_item_to_enum_choice(
        self,
        item: ET.Element,
        text: str = "name/narrative",
        label_text: str = "name/narrative",
        suffix: str = "",
        include_unlabelled: bool = True,
    ):
        """
        Convert a <codelist-item/> to an enum line for Django choices
        """
        code = item.find("code").text
        name = (
            item.find(text).text
            if item.find(text) is not None
            else f"{self.category}_{code}"
        )
        # Some choices, such as FileFormat and IatiVersion, do not have a name property
        name_slug = slugify(name.replace(*CAT_REPLACE)).upper()

        try:
            label_text_value = item.find(label_text).text
            if not label_text_value:
                label = ""
            label_text_value = label_text_value.replace('"', r"\"")
            if (
                "\n" not in label_text_value
                and not label_text_value.startswith('"')
                and not label_text_value.endswith('"')
            ):
                label = f', pgettext_lazy("IATI codelist {self.category}{suffix}", "{label_text_value}")'
            else:
                label = f', pgettext_lazy("IATI codelist {self.category}{suffix}", """{label_text_value}""")'

        except AttributeError:
            # In some circumstances (ie we're generating a select for descriptions only)
            # we want to exit here with a False
            label = ""

        if self.choices_type == "models.TextChoices":
            code = f"'{code}'"
        indent = " " * 4

        if include_unlabelled is False and label == "":
            return False

        return f"""{indent}{name_slug} = {code}{label},"""

    def _class_name(self, suffix=""):
        class_name = self.category.replace(*CAT_REPLACE).replace("-", "_")
        return f"""\n\nclass {class_name}{suffix}({self.choices_type}):"""

    def class_name(self):
        return self._class_name()

    def class_docstring(self) -> str:
        try:
            s = self.root.find("metadata/description/narrative").text.replace(
                "\n", "\n    "
            )
            return " ".join(s.split())
        except:
            return None

    @property
    def wrapped_docstring(self):
        ds = self.class_docstring()
        if not ds:
            return False
        n = " " * 4
        return f'{n}"""\n{n}{ds}\n{n}"""'

    def descriptions_class_name(self):
        return self._class_name(suffix="Description")

    def codelist_items_to_emums(
        self,
        label_text: str = "name/narrative",
        suffix: str = "",
        include_unlabelled: bool = True,
    ):
        return [
            self.codelist_item_to_enum_choice(
                el,
                label_text=label_text,
                suffix=suffix,
                include_unlabelled=include_unlabelled,
            )
            for el in self.root.findall("codelist-items/codelist-item")
        ]

    def to_classes(self):
        codelist_enums = self.codelist_items_to_emums()
        if not any(codelist_enums):
            codelist_enums = [
                "    # There are no valid items in this enums",
                "    pass",
            ]

        return (
            # *imports,
            # *newlines,
            self.class_name(),
            self.wrapped_docstring,
            *codelist_enums,
            "",
            # Then another 2 blank lines,
            # *newlines,
            # Class name for the "descriptions",
            # self.descriptions_class_name(),
            # enums which use the "description" field
            # these are longer and more descriptive than the name
            # *self.codelist_items_to_emums(label_text='description/narrative', suffix=' description')
        )


class XmlElementAsDescriptionEnum(XmlElementAsEnum):
    """
    Same values as the XmlElementAsEnum
    Uses the "description" field as the label for the enum
    """

    def class_name(self):
        return super()._class_name(suffix="Description")

    def codelist_items_to_emums(self):
        return super().codelist_items_to_emums(
            label_text="description/narrative",
            suffix=" description",
            include_unlabelled=False,
        )


def main(filename: str):
    """
    Open one XML file and convert it to a Django choices
    """

    # enum_factory = XmlElementAsEnum(filename)


if __name__ == "__main__":
    # Directory to IATI repository
    IATI = pathlib.Path(
        "/media/josh/beb0eb0a-f1f5-4ef5-b5a4-b2a532d8db91/josh/github/IATI/"
    )
    nonembedded = IATI / "IATI-Codelists-NonEmbedded" / "xml"
    embedded = IATI / "IATI-Standard-SSOT" / "IATI-Codelists" / "xml"

    for filename in os.listdir(nonembedded):
        content = XmlElementAsEnum(nonembedded / filename).to_classes()
        with open(
            pathlib.Path(".") / "nonembedded" / "codelists" / output_filepath(filename),
            "w",
        ) as outfile:
            outfile.write("from django.db import models\n")
            outfile.write("from django.utils.translation import pgettext_lazy\n")
            outfile.write("\n".join([n for n in content if n is not False]))

    for filename in os.listdir(nonembedded):
        content = XmlElementAsDescriptionEnum(nonembedded / filename).to_classes()
        with open(
            pathlib.Path(".")
            / "nonembedded"
            / "descriptions"
            / output_filepath(filename),
            "w",
        ) as outfile:
            outfile.write("from django.db import models\n")
            outfile.write("from django.utils.translation import pgettext_lazy\n")
            outfile.write("\n".join([n for n in content if n is not False]))

    for filename in os.listdir(embedded):
        content = XmlElementAsEnum(embedded / filename).to_classes()
        with open(
            pathlib.Path(".") / "embedded" / "codelists" / output_filepath(filename),
            "w",
        ) as outfile:
            outfile.write("from django.db import models\n")
            outfile.write("from django.utils.translation import pgettext_lazy\n")
            outfile.write("\n".join([n for n in content if n is not False]))

    for filename in os.listdir(embedded):
        content = XmlElementAsDescriptionEnum(embedded / filename).to_classes()
        with open(
            pathlib.Path(".") / "embedded" / "descriptions" / output_filepath(filename),
            "w",
        ) as outfile:
            outfile.write("from django.db import models\n")
            outfile.write("from django.utils.translation import pgettext_lazy\n")
            outfile.write("\n".join([n for n in content if n is not False]))
