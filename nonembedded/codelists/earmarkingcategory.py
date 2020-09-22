from django.db import models
from django.utils.translation import pgettext_lazy


class EarmarkingCategory(models.IntegerChoices):
    """
    This codelist has been created by IATI and is derived from the Grand Bargain Earmarking Modality codelist.
    """

    UNEARMARKED = (
        1,
        pgettext_lazy("EarmarkingCategory", "Unearmarked"),
    )
    SOFTLY_EARMARKED = (
        2,
        pgettext_lazy("EarmarkingCategory", "Softly Earmarked"),
    )
    EARMARKED = (
        3,
        pgettext_lazy("EarmarkingCategory", "Earmarked"),
    )
    TIGHTLY_EARMARKED = (
        4,
        pgettext_lazy("EarmarkingCategory", "Tightly Earmarked"),
    )
