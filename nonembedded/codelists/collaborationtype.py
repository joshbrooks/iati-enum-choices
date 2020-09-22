from django.db import models
from django.utils.translation import pgettext_lazy


class CollaborationType(models.IntegerChoices):
    """
    OECD DAC classification used to determine the character of resource flows (bilateral or multilateral).
    """

    BILATERAL = (
        1,
        pgettext_lazy("IATI codelist CollaborationType", "Bilateral"),
    )
    MULTILATERAL__INFLOWS_ = (
        2,
        pgettext_lazy("IATI codelist CollaborationType", "Multilateral (inflows)"),
    )
    BILATERAL__CORE_CONTRIBUTIONS_TO_NGOS_AND_OTHER_PRIVATE_BODIES___PPPS = (
        3,
        pgettext_lazy(
            "IATI codelist CollaborationType",
            "Bilateral, core contributions to NGOs and other private bodies / PPPs",
        ),
    )
    MULTILATERAL_OUTFLOWS = (
        4,
        pgettext_lazy("IATI codelist CollaborationType", "Multilateral outflows"),
    )
    PRIVATE_SECTOR_OUTFLOWS = (
        6,
        pgettext_lazy("IATI codelist CollaborationType", "Private Sector Outflows"),
    )
    BILATERAL__EX_POST_REPORTING_ON_NGOS__ACTIVITIES_FUNDED_THROUGH_CORE_CONTRIBUTIONS = (
        7,
        pgettext_lazy(
            "IATI codelist CollaborationType",
            "Bilateral, ex-post reporting on NGOs’ activities funded through core contributions",
        ),
    )
    BILATERAL__TRIANGULAR_CO_OPERATION_ = (
        8,
        pgettext_lazy(
            "IATI codelist CollaborationType", "Bilateral, triangular co-operation."
        ),
    )
