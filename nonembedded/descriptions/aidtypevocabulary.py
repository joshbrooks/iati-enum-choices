from django.db import models
from django.utils.translation import pgettext_lazy


class AidTypeVocabularyDescription(models.IntegerChoices):
    """
    The AidTypeVocabulary codelist defines a range of external codelists which themselves provide codes and descriptions for aid type.
    """

    OECD_DAC = (
        1,
        pgettext_lazy(
            "IATI codelist AidTypeVocabulary description",
            "List of codes provided by the OECD DAC used to distinguish types of aid",
        ),
    )
    EARMARKING_CATEGORY = (
        2,
        pgettext_lazy(
            "IATI codelist AidTypeVocabulary description",
            "This vocabulary has been created by IATI and is derived from the Grand Bargain Earmarking Modality codelist",
        ),
    )
    EARMARKING_MODALITY = (
        3,
        pgettext_lazy(
            "IATI codelist AidTypeVocabulary description",
            "Codes A to L replicated directly from Grand Bargain document found in Annex 1 (pg.16)",
        ),
    )
    CASH_AND_VOUCHER_MODALITIES = (
        4,
        pgettext_lazy(
            "IATI codelist AidTypeVocabulary description",
            "This vocabulary has been created by IATI, following agreements and recommendations of the Tracking Cash and Voucher Assistance (CVA) Working Group.",
        ),
    )
