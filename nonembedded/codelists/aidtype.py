from django.db import models
from django.utils.translation import pgettext_lazy


class AidType(models.TextChoices):
    GENERAL_BUDGET_SUPPORT = (
        "A01",
        pgettext_lazy("IATI codelist AidType", "General budget support"),
    )
    SECTOR_BUDGET_SUPPORT = (
        "A02",
        pgettext_lazy("IATI codelist AidType", "Sector budget support"),
    )
    CORE_SUPPORT_TO_NGOS__OTHER_PRIVATE_BODIES__PPPS_AND_RESEARCH_INSTITUTES = (
        "B01",
        pgettext_lazy(
            "IATI codelist AidType",
            "Core support to NGOs, other private bodies, PPPs and research institutes",
        ),
    )
    CORE_CONTRIBUTIONS_TO_MULTILATERAL_INSTITUTIONS = (
        "B02",
        pgettext_lazy(
            "IATI codelist AidType", "Core contributions to multilateral institutions"
        ),
    )
    CONTRIBUTIONS_TO_SPECIFIC_PURPOSE_PROGRAMMES_AND_FUNDS_MANAGED_BY_IMPLEMENTING_PARTNERS = (
        "B03",
        pgettext_lazy(
            "IATI codelist AidType",
            "Contributions to specific-purpose programmes and funds managed by implementing partners",
        ),
    )
    BASKET_FUNDS_POOLED_FUNDING = (
        "B04",
        pgettext_lazy("IATI codelist AidType", "Basket funds/pooled funding"),
    )
    PROJECT_TYPE_INTERVENTIONS = (
        "C01",
        pgettext_lazy("IATI codelist AidType", "Project-type interventions"),
    )
    DONOR_COUNTRY_PERSONNEL = (
        "D01",
        pgettext_lazy("IATI codelist AidType", "Donor country personnel"),
    )
    OTHER_TECHNICAL_ASSISTANCE = (
        "D02",
        pgettext_lazy("IATI codelist AidType", "Other technical assistance"),
    )
    SCHOLARSHIPS_TRAINING_IN_DONOR_COUNTRY = (
        "E01",
        pgettext_lazy(
            "IATI codelist AidType", "Scholarships/training in donor country"
        ),
    )
    IMPUTED_STUDENT_COSTS = (
        "E02",
        pgettext_lazy("IATI codelist AidType", "Imputed student costs"),
    )
    DEBT_RELIEF = (
        "F01",
        pgettext_lazy("IATI codelist AidType", "Debt relief"),
    )
    ADMINISTRATIVE_COSTS_NOT_INCLUDED_ELSEWHERE = (
        "G01",
        pgettext_lazy(
            "IATI codelist AidType", "Administrative costs not included elsewhere"
        ),
    )
    DEVELOPMENT_AWARENESS = (
        "H01",
        pgettext_lazy("IATI codelist AidType", "Development awareness"),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES = (
        "H02",
        pgettext_lazy(
            "IATI codelist AidType", "Refugees/asylum seekers in donor countries"
        ),
    )
    ASYLUM_SEEKERS_ULTIMATELY_ACCEPTED = (
        "H03",
        pgettext_lazy("IATI codelist AidType", "Asylum-seekers ultimately accepted"),
    )
    ASYLUM_SEEKERS_ULTIMATELY_REJECTED = (
        "H04",
        pgettext_lazy("IATI codelist AidType", "Asylum-seekers ultimately rejected"),
    )
    RECOGNISED_REFUGEES = (
        "H05",
        pgettext_lazy("IATI codelist AidType", "Recognised refugees"),
    )
