from django.db import models
from django.utils.translation import pgettext_lazy


class FlowType(models.IntegerChoices):
    """
    DAC/CRS distinction between ODA (official development assistance) and other types of resource flow.
    """

    ODA = (
        10,
        pgettext_lazy("IATI codelist FlowType", "ODA"),
    )
    OOF = (
        20,
        pgettext_lazy("IATI codelist FlowType", "OOF"),
    )
    NON_EXPORT_CREDIT_OOF = (
        21,
        pgettext_lazy("IATI codelist FlowType", "Non-export credit OOF"),
    )
    OFFICIALLY_SUPPORTED_EXPORT_CREDITS = (
        22,
        pgettext_lazy("IATI codelist FlowType", "Officially supported export credits"),
    )
    PRIVATE_DEVELOPMENT_FINANCE = (
        30,
        pgettext_lazy("IATI codelist FlowType", "Private Development Finance"),
    )
    PRIVATE_MARKET = (
        35,
        pgettext_lazy("IATI codelist FlowType", "Private Market"),
    )
    PRIVATE_FOREIGN_DIRECT_INVESTMENT = (
        36,
        pgettext_lazy("IATI codelist FlowType", "Private Foreign Direct Investment"),
    )
    OTHER_PRIVATE_FLOWS_AT_MARKET_TERMS = (
        37,
        pgettext_lazy("IATI codelist FlowType", "Other Private flows at market terms"),
    )
    NON_FLOW = (
        40,
        pgettext_lazy("IATI codelist FlowType", "Non flow"),
    )
    OTHER_FLOWS = (
        50,
        pgettext_lazy("IATI codelist FlowType", "Other flows"),
    )
