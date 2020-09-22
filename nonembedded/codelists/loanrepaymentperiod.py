from django.db import models
from django.utils.translation import pgettext_lazy


class LoanRepaymentPeriod(models.IntegerChoices):
    """
    CRS Loan Repayment No of Payments
    """

    ANNUAL = (
        1,
        pgettext_lazy("LoanRepaymentPeriod", "Annual"),
    )
    SEMI_ANNUAL = (
        2,
        pgettext_lazy("LoanRepaymentPeriod", "Semi-annual"),
    )
    QUARTERLY = (
        4,
        pgettext_lazy("LoanRepaymentPeriod", "Quarterly"),
    )
    MONTHLY = (
        12,
        pgettext_lazy("LoanRepaymentPeriod", "Monthly"),
    )
