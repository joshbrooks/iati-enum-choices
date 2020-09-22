from django.db import models
from django.utils.translation import pgettext_lazy


class FinanceTypeCategory(models.IntegerChoices):
    """
    This codelists exists to group the Finance Type codelist into categories. It is not used as a codelist in its own right.
    """

    NON_FLOW_ITEMS = (
        0,
        pgettext_lazy("FinanceType-category", "NON FLOW ITEMS"),
    )
    GRANTS = (
        100,
        pgettext_lazy("FinanceType-category", "GRANTS"),
    )
    GUARANTEES_AND_OTHER_UNFUNDED_CONTINGENT_LIABILITIES = (
        1000,
        pgettext_lazy(
            "FinanceType-category",
            "GUARANTEES AND OTHER UNFUNDED CONTINGENT LIABILITIES",
        ),
    )
    INTEREST_SUBSIDY = (
        200,
        pgettext_lazy("FinanceType-category", "INTEREST SUBSIDY"),
    )
    CAPITAL_SUBSCRIPTION = (
        300,
        pgettext_lazy("FinanceType-category", "CAPITAL SUBSCRIPTION"),
    )
    LOAN = (
        400,
        pgettext_lazy("FinanceType-category", "LOAN"),
    )
    DEBT_INSTRUMENTS = (
        420,
        pgettext_lazy("FinanceType-category", "DEBT INSTRUMENTS"),
    )
    MEZZANINE_FINANCE_INSTRUMENTS = (
        430,
        pgettext_lazy("FinanceType-category", "MEZZANINE FINANCE INSTRUMENTS"),
    )
    EQUITY_AND_SHARES_IN_COLLECTIVE_INVESTMENT_VEHICLES = (
        500,
        pgettext_lazy(
            "FinanceType-category",
            "EQUITY  AND SHARES IN COLLECTIVE INVESTMENT VEHICLES",
        ),
    )
    DEBT_RELIEF = (
        600,
        pgettext_lazy("FinanceType-category", "DEBT RELIEF"),
    )
    INVESTMENT = (
        700,
        pgettext_lazy("FinanceType-category", "INVESTMENT"),
    )
    BONDS = (
        800,
        pgettext_lazy("FinanceType-category", "BONDS"),
    )
    OTHER_SECURITIES_CLAIMS = (
        900,
        pgettext_lazy("FinanceType-category", "OTHER SECURITIES/CLAIMS"),
    )
