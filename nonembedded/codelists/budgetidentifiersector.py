from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierSector(models.TextChoices):
    """
    This codelists exists to group the Budget Identifier codelist into sectors. It is not used as a codelist in its own right.
    """

    EXECUTIVE = (
        "1.1",
        pgettext_lazy("BudgetIdentifierSector", "Executive"),
    )
    LEGISLATIVE = (
        "1.2",
        pgettext_lazy("BudgetIdentifierSector", "Legislative"),
    )
    ACCOUNTABILITY = (
        "1.3",
        pgettext_lazy("BudgetIdentifierSector", "Accountability"),
    )
    EXTERNAL_AFFAIRS = (
        "1.4",
        pgettext_lazy("BudgetIdentifierSector", "External Affairs"),
    )
    GENERAL_PERSONNEL_SERVICES = (
        "1.5",
        pgettext_lazy("BudgetIdentifierSector", "General Personnel Services"),
    )
    STATISTICS = (
        "1.6",
        pgettext_lazy("BudgetIdentifierSector", "Statistics"),
    )
    OTHER_GENERAL_SERVICES = (
        "1.7",
        pgettext_lazy("BudgetIdentifierSector", "Other General Services"),
    )
    ELECTIONS = (
        "1.8",
        pgettext_lazy("BudgetIdentifierSector", "Elections"),
    )
    JUSTICE__LAW_AND_ORDER = (
        "2.1",
        pgettext_lazy("BudgetIdentifierSector", "Justice, Law and Order"),
    )
    DEFENCE = (
        "2.2",
        pgettext_lazy("BudgetIdentifierSector", "Defence"),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS = (
        "3.1",
        pgettext_lazy(
            "BudgetIdentifierSector",
            "General Economic, Commercial and Labour Affairs",
        ),
    )
    PUBLIC_WORKS = (
        "3.2",
        pgettext_lazy("BudgetIdentifierSector", "Public Works"),
    )
    AGRICULTURE = (
        "3.3",
        pgettext_lazy("BudgetIdentifierSector", "Agriculture"),
    )
    FORESTRY = (
        "3.4",
        pgettext_lazy("BudgetIdentifierSector", "Forestry"),
    )
    FISHING_AND_HUNTING = (
        "3.5",
        pgettext_lazy("BudgetIdentifierSector", "Fishing and Hunting"),
    )
    ENERGY = (
        "3.6",
        pgettext_lazy("BudgetIdentifierSector", "Energy"),
    )
    MINING_AND_MINERAL_DEVELOPMENT = (
        "3.7",
        pgettext_lazy("BudgetIdentifierSector", "Mining and Mineral Development"),
    )
    TRANSPORT = (
        "3.8",
        pgettext_lazy("BudgetIdentifierSector", "Transport"),
    )
    INDUSTRY = (
        "3.9",
        pgettext_lazy("BudgetIdentifierSector", "Industry"),
    )
    COMMUNICATIONS = (
        "3.10",
        pgettext_lazy("BudgetIdentifierSector", "Communications"),
    )
    TOURISM = (
        "3.11",
        pgettext_lazy("BudgetIdentifierSector", "Tourism"),
    )
    MICROFINANCE_AND_FINANCIAL_SERVICES = (
        "3.12",
        pgettext_lazy(
            "BudgetIdentifierSector",
            "Microfinance and financial services",
        ),
    )
    WATER_SUPPLY_AND_SANITATION = (
        "4.1",
        pgettext_lazy("BudgetIdentifierSector", "Water supply and Sanitation"),
    )
    ENVIRONMENT = (
        "4.2",
        pgettext_lazy("BudgetIdentifierSector", "Environment"),
    )
    HEALTH = (
        "5.1",
        pgettext_lazy("BudgetIdentifierSector", "Health"),
    )
    RECREATION__CULTURE_AND_RELIGION = (
        "5.2",
        pgettext_lazy("BudgetIdentifierSector", "Recreation, Culture and Religion"),
    )
    EDUCATION = (
        "5.3",
        pgettext_lazy("BudgetIdentifierSector", "Education"),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES = (
        "5.4",
        pgettext_lazy(
            "BudgetIdentifierSector",
            "Social Protection, Land Housing and Community Amenities",
        ),
    )
    DEVELOPMENT_PARTNER_AFFAIRS = (
        "6.1",
        pgettext_lazy("BudgetIdentifierSector", "Development Partner affairs"),
    )
    EXTERNAL_TO_GOVERNMENT_SECTOR = (
        "7.1",
        pgettext_lazy("BudgetIdentifierSector", "External to government sector"),
    )
    GENERAL_BUDGET_SUPPORT = (
        "7.2",
        pgettext_lazy("BudgetIdentifierSector", "General Budget Support"),
    )
