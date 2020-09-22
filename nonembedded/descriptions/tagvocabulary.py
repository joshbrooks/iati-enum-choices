from django.db import models
from django.utils.translation import pgettext_lazy


class TagVocabularyDescription(models.IntegerChoices):
    """
    The Tag Vocabulary codelist defines external codelists which themselves provide codes and descriptions for tag elements.
    """

    AGROVOC = (
        1,
        pgettext_lazy(
            "TagVocabulary description",
            "A controlled vocabulary covering all areas of interest of the Food and Agriculture Organization (FAO) of the United Nations, including food, nutrition, agriculture, fisheries, forestry, environment etc.",
        ),
    )
    UN_SUSTAINABLE_DEVELOPMENT_GOALS__SDG_ = (
        2,
        pgettext_lazy(
            "TagVocabulary description",
            "A value from the top-level list of UN sustainable development goals (SDGs) (e.g. ‘1’)",
        ),
    )
    UN_SUSTAINABLE_DEVELOPMENT_GOALS__SDG__TARGETS = (
        3,
        pgettext_lazy(
            "TagVocabulary description",
            "A value from the second-level list of UN sustainable development goals (SDGs) (e.g. ‘1.1’)",
        ),
    )
