from django.db import models
from django.utils.translation import pgettext_lazy


class LoanRepaymentType(models.IntegerChoices):
    """
    used in additional CRS elements
    """

    EQUAL_PRINCIPAL_PAYMENTS__EPP_ = (
        1,
        pgettext_lazy("LoanRepaymentType", "Equal Principal Payments (EPP)"),
    )
    ANNUITY = (
        2,
        pgettext_lazy("LoanRepaymentType", "Annuity"),
    )
    LUMP_SUM = (
        3,
        pgettext_lazy("LoanRepaymentType", "Lump sum"),
    )
    OTHER = (
        5,
        pgettext_lazy("LoanRepaymentType", "Other"),
    )
