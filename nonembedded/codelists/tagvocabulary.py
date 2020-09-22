from django.db import models
from django.utils.translation import pgettext_lazy


class TagVocabulary(models.IntegerChoices):
    """
    The Tag Vocabulary codelist defines external codelists which themselves provide codes and descriptions for tag elements.
    """

    AGROVOC = (
        1,
        pgettext_lazy("IATI codelist TagVocabulary", "Agrovoc"),
    )
    UN_SUSTAINABLE_DEVELOPMENT_GOALS__SDG_ = (
        2,
        pgettext_lazy(
            "IATI codelist TagVocabulary", "UN Sustainable Development Goals (SDG)"
        ),
    )
    UN_SUSTAINABLE_DEVELOPMENT_GOALS__SDG__TARGETS = (
        3,
        pgettext_lazy(
            "IATI codelist TagVocabulary",
            "UN Sustainable Development Goals (SDG) Targets",
        ),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy("IATI codelist TagVocabulary", "Reporting Organisation"),
    )
