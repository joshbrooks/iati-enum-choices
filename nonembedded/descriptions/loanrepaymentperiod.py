from django.db import models
from django.utils.translation import pgettext_lazy


class LoanRepaymentPeriodDescription(models.IntegerChoices):
    """
    CRS Loan Repayment No of Payments
    """

    ANNUAL = (
        1,
        pgettext_lazy(
            "IATI codelist LoanRepaymentPeriod description",
            "The loan has 1 repayment per year",
        ),
    )
    SEMI_ANNUAL = (
        2,
        pgettext_lazy(
            "IATI codelist LoanRepaymentPeriod description",
            "The loan has 2 repayments per year",
        ),
    )
    QUARTERLY = (
        4,
        pgettext_lazy(
            "IATI codelist LoanRepaymentPeriod description",
            "The loan has 4 repayments per year ",
        ),
    )
    MONTHLY = (
        12,
        pgettext_lazy(
            "IATI codelist LoanRepaymentPeriod description",
            "The loan has 12, monthly repayments per year",
        ),
    )
