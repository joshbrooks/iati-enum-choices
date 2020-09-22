from django.db import models
from django.utils.translation import pgettext_lazy


class AidTypeCategoryDescription(models.TextChoices):
    """
    This codelists exists to group the Aid Type codelist into categories. It is not used as a codelist in its own right.
    """

    BUDGET_SUPPORT = (
        "A",
        pgettext_lazy(
            "IATI codelist AidType-category description",
            "For contributions under this category, the donor relinquishes the exclusive control of its funds by sharing the responsibility with the recipient.",
        ),
    )
    CORE_CONTRIBUTIONS_AND_POOLED_PROGRAMMES_AND_FUNDS = (
        "B",
        pgettext_lazy(
            "IATI codelist AidType-category description",
            "For contributions under this category, the donor relinquishes the exclusive control of its funds by sharing the responsibility with other stakeholders (other donors, NGOs, multilateral institutions, Public Private Partnerships). The category covers both core contributions (B01 and B02), and pooled contributions with a specific earmarking (B03 and B04).",
        ),
    )
    PROJECT_TYPE_INTERVENTIONS = (
        "C",
        pgettext_lazy(
            "IATI codelist AidType-category description",
            "N.B.  Within this category, members able to do so are requested to report the aggregate amount used for financing donor experts/consultants on Table DAC11. Where the activity consists solely of experts’ costs, report under category D.",
        ),
    )
    EXPERTS_AND_OTHER_TECHNICAL_ASSISTANCE = (
        "D",
        pgettext_lazy(
            "IATI codelist AidType-category description",
            "This category covers the provision, outside projects as described in category C, of know-how in the form of personnel, training and research.",
        ),
    )
    OTHER_IN_DONOR_EXPENDITURES = (
        "H",
        pgettext_lazy(
            "IATI codelist AidType-category description",
            "Groups a number of contributions that do not give rise to a cross-border flow.",
        ),
    )
