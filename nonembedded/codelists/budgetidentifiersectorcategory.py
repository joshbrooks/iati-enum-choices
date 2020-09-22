from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierSectorCategory(models.IntegerChoices):
    """
    This codelists exists to group the Budget Identifier codelist into categories. It is not used as a codelist in its own right.
    """

    GENERAL_PUBLIC_SERVICE = (
        1,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category", "General Public Service"
        ),
    )
    JUSTICE__LAW__ORDER_AND_SECURITY = (
        2,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category",
            "Justice, Law, Order and Security",
        ),
    )
    ECONOMIC_AFFAIRS = (
        3,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category", "Economic Affairs"
        ),
    )
    WATER__NATURAL_RESOURCE_MANAGEMENT_AND_ENVIRONMENT = (
        4,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category",
            "Water, Natural Resource Management and Environment",
        ),
    )
    SOCIAL_AFFAIRS = (
        5,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category", "Social Affairs"
        ),
    )
    DEVELOPMENT_PARTNER_AFFAIRS = (
        6,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category",
            "Development Partner Affairs",
        ),
    )
    GENERAL_BUDGET_SUPPORT_AND_AID_SUPPORT_EXTERNAL_TO_GENERAL_GOVERNMENT_SECTOR = (
        7,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierSector-category",
            "General Budget Support and Aid support external to General Government Sector",
        ),
    )
