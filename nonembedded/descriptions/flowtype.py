from django.db import models
from django.utils.translation import pgettext_lazy


class FlowTypeDescription(models.IntegerChoices):
    """
    DAC/CRS distinction between ODA (official development assistance) and other types of resource flow.
    """

    ODA = (
        10,
        pgettext_lazy("FlowType description", "Official Development Assistance"),
    )
    OOF = (
        20,
        pgettext_lazy("FlowType description", "Other Official Flows"),
    )
    NON_EXPORT_CREDIT_OOF = (
        21,
        pgettext_lazy(
            "FlowType description",
            "Other Official Flows, excl. export credits",
        ),
    )
    OFFICIALLY_SUPPORTED_EXPORT_CREDITS = (
        22,
        pgettext_lazy(
            "FlowType description",
            "Officially supported export credits. Covers both official direct export credits and private export credits under official guarantee or insurance",
        ),
    )
    PRIVATE_DEVELOPMENT_FINANCE = (
        30,
        pgettext_lazy(
            "FlowType description",
            "Financing by civil society organisations (NGOs, philantropic foundations, etc.)",
        ),
    )
    PRIVATE_MARKET = (
        35,
        pgettext_lazy(
            "FlowType description",
            "Private long-term (i.e. over one-year maturity) capital transactions made by residents of DAC countries",
        ),
    )
    PRIVATE_FOREIGN_DIRECT_INVESTMENT = (
        36,
        pgettext_lazy("FlowType description", "Private Foreign Direct Investment"),
    )
    OTHER_PRIVATE_FLOWS_AT_MARKET_TERMS = (
        37,
        pgettext_lazy(
            "FlowType description",
            "Private long-term (i.e. over one-year maturity) capital transactions made by residents of DAC countries",
        ),
    )
    NON_FLOW = (
        40,
        pgettext_lazy("FlowType description", "e.g. GNI, ODA%GNI, Population etc"),
    )
    OTHER_FLOWS = (
        50,
        pgettext_lazy(
            "FlowType description",
            "e.g. non-ODA component of peacebuilding operations",
        ),
    )
