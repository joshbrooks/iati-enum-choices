from django.db import models
from django.utils.translation import pgettext_lazy


class LoanRepaymentTypeDescription(models.IntegerChoices):
    """
    used in additional CRS elements
    """

    EQUAL_PRINCIPAL_PAYMENTS__EPP_ = (
        1,
        pgettext_lazy(
            "IATI codelist LoanRepaymentType description",
            "As required and defined by CRS++ reporting format Column 44",
        ),
    )
    ANNUITY = (
        2,
        pgettext_lazy(
            "IATI codelist LoanRepaymentType description",
            "As required and defined by CRS++ reporting format Column 44",
        ),
    )
    LUMP_SUM = (
        3,
        pgettext_lazy(
            "IATI codelist LoanRepaymentType description",
            "As required and defined by CRS++ reporting format Column 44",
        ),
    )
    OTHER = (
        5,
        pgettext_lazy(
            "IATI codelist LoanRepaymentType description",
            "As required and defined by CRS++ reporting format Column 44",
        ),
    )
