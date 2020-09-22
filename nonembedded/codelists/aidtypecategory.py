from django.db import models
from django.utils.translation import pgettext_lazy


class AidTypeCategory(models.TextChoices):
    """
    This codelists exists to group the Aid Type codelist into categories. It is not used as a codelist in its own right.
    """

    BUDGET_SUPPORT = (
        "A",
        pgettext_lazy("AidType-category", "Budget support"),
    )
    CORE_CONTRIBUTIONS_AND_POOLED_PROGRAMMES_AND_FUNDS = (
        "B",
        pgettext_lazy(
            "AidType-category",
            "Core contributions and pooled programmes and funds",
        ),
    )
    PROJECT_TYPE_INTERVENTIONS = (
        "C",
        pgettext_lazy("AidType-category", "Project-type interventions"),
    )
    EXPERTS_AND_OTHER_TECHNICAL_ASSISTANCE = (
        "D",
        pgettext_lazy("AidType-category", "Experts and other technical assistance"),
    )
    SCHOLARSHIPS_AND_STUDENT_COSTS_IN_DONOR_COUNTRIES = (
        "E",
        pgettext_lazy(
            "AidType-category",
            "Scholarships and student costs in donor countries",
        ),
    )
    DEBT_RELIEF = (
        "F",
        pgettext_lazy("AidType-category", "Debt relief"),
    )
    ADMINISTRATIVE_COSTS_NOT_INCLUDED_ELSEWHERE = (
        "G",
        pgettext_lazy(
            "AidType-category",
            "Administrative costs not included elsewhere",
        ),
    )
    OTHER_IN_DONOR_EXPENDITURES = (
        "H",
        pgettext_lazy("AidType-category", "Other in-donor expenditures"),
    )
