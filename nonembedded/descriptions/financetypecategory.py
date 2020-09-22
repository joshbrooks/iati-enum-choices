from django.db import models
from django.utils.translation import pgettext_lazy


class FinanceTypeCategoryDescription(models.IntegerChoices):
    """
    This codelists exists to group the Finance Type codelist into categories. It is not used as a codelist in its own right.
    """

    NON_FLOW_ITEMS = (
        0,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Non resource flow items requested on DAC table 1",
        ),
    )
    INTEREST_SUBSIDY = (
        200,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Subsidies to soften the terms of private export credits, or loans or credits by the banking sector.",
        ),
    )
    CAPITAL_SUBSCRIPTION = (
        300,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Payments to multilateral agencies in the form of notes and similar instruments, unconditionally cashable at sight by the recipient institutions.",
        ),
    )
    LOAN = (
        400,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Transfers in cash or in kind for which the recipient incurs legal debt.",
        ),
    )
    DEBT_RELIEF = (
        600,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Debt cancellations, debt conversions, debt rescheduling within or outside the framework of the Paris Club.",
        ),
    )
    INVESTMENT = (
        700,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Investment made by a private entity resident in a reporting country to acquire or add to a lasting interest(1) in an enterprise in a country on the DAC List of ODA Recipients.",
        ),
    )
    BONDS = (
        800,
        pgettext_lazy(
            "IATI codelist FinanceType-category description",
            "Acquisition of bonds issued by developing countries.",
        ),
    )
