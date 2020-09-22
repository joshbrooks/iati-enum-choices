from django.db import models
from django.utils.translation import pgettext_lazy


class EarmarkingCategoryDescription(models.IntegerChoices):
    """
    This codelist has been created by IATI and is derived from the Grand Bargain Earmarking Modality codelist.
    """

    UNEARMARKED = (
        1,
        pgettext_lazy(
            "IATI codelist EarmarkingCategory description",
            "Any or all of the Earmarking Modality codes A,B or C.",
        ),
    )
    SOFTLY_EARMARKED = (
        2,
        pgettext_lazy(
            "IATI codelist EarmarkingCategory description",
            "Any or all of the Earmarking Modality codes D,E or F.",
        ),
    )
    EARMARKED = (
        3,
        pgettext_lazy(
            "IATI codelist EarmarkingCategory description",
            "Any or all of the Earmarking Modality codes G or H.",
        ),
    )
    TIGHTLY_EARMARKED = (
        4,
        pgettext_lazy(
            "IATI codelist EarmarkingCategory description",
            "Any or all of the Earmarking Modality codes I,J or K.",
        ),
    )
