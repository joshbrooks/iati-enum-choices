from django.db import models
from django.utils.translation import pgettext_lazy


class CRSAddOtherFlagsDescription(models.IntegerChoices):
    """
    OECD DAC classification used to distinguish aid modalities.
    """

    FREE_STANDING_TECHNICAL_COOPERATION = (
        1,
        pgettext_lazy(
            "IATI codelist CRSAddOtherFlags description",
            "Free standing technical cooperation (Col 24 in CRS++ Reporting format)",
        ),
    )
    PROGRAMME_BASED_APPROACH = (
        2,
        pgettext_lazy(
            "IATI codelist CRSAddOtherFlags description",
            "Programme-based approach (Col 25 in CRS++ Reporting format)",
        ),
    )
    INVESTMENT_PROJECT = (
        3,
        pgettext_lazy(
            "IATI codelist CRSAddOtherFlags description",
            "Investment project (Col 26 in CRS++ Reporting format)",
        ),
    )
    ASSOCIATED_FINANCING = (
        4,
        pgettext_lazy(
            "IATI codelist CRSAddOtherFlags description",
            "Associated financing (Col 27 in CRS++ Reporting format)",
        ),
    )
