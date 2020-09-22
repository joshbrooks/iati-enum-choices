from django.db import models
from django.utils.translation import pgettext_lazy


class CRSAddOtherFlags(models.IntegerChoices):
    """
    OECD DAC classification used to distinguish aid modalities.
    """

    FREE_STANDING_TECHNICAL_COOPERATION = (
        1,
        pgettext_lazy(
            "IATI codelist CRSAddOtherFlags", "Free standing technical cooperation"
        ),
    )
    PROGRAMME_BASED_APPROACH = (
        2,
        pgettext_lazy("IATI codelist CRSAddOtherFlags", "Programme-based approach"),
    )
    INVESTMENT_PROJECT = (
        3,
        pgettext_lazy("IATI codelist CRSAddOtherFlags", "Investment project"),
    )
    ASSOCIATED_FINANCING = (
        4,
        pgettext_lazy("IATI codelist CRSAddOtherFlags", "Associated financing"),
    )
