from django.db import models
from django.utils.translation import pgettext_lazy


class AidTypeVocabulary(models.IntegerChoices):
    """
    The AidTypeVocabulary codelist defines a range of external codelists which themselves provide codes and descriptions for aid type.
    """

    OECD_DAC = (
        1,
        pgettext_lazy("AidTypeVocabulary", "OECD DAC"),
    )
    EARMARKING_CATEGORY = (
        2,
        pgettext_lazy("AidTypeVocabulary", "Earmarking Category"),
    )
    EARMARKING_MODALITY = (
        3,
        pgettext_lazy("AidTypeVocabulary", "Earmarking Modality"),
    )
    CASH_AND_VOUCHER_MODALITIES = (
        4,
        pgettext_lazy("AidTypeVocabulary", "Cash and Voucher Modalities"),
    )
