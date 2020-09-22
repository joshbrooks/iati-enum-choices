from django.db import models
from django.utils.translation import pgettext_lazy


class TransactionType(models.IntegerChoices):
    INCOMING_FUNDS = (
        1,
        pgettext_lazy("IATI codelist TransactionType", "Incoming Funds"),
    )
    COMMITMENT = (
        2,
        pgettext_lazy("IATI codelist TransactionType", "Commitment"),
    )
    DISBURSEMENT = (
        3,
        pgettext_lazy("IATI codelist TransactionType", "Disbursement"),
    )
    EXPENDITURE = (
        4,
        pgettext_lazy("IATI codelist TransactionType", "Expenditure"),
    )
    INTEREST_REPAYMENT = (
        5,
        pgettext_lazy("IATI codelist TransactionType", "Interest Repayment"),
    )
    LOAN_REPAYMENT = (
        6,
        pgettext_lazy("IATI codelist TransactionType", "Loan Repayment"),
    )
    REIMBURSEMENT = (
        7,
        pgettext_lazy("IATI codelist TransactionType", "Reimbursement"),
    )
    PURCHASE_OF_EQUITY = (
        8,
        pgettext_lazy("IATI codelist TransactionType", "Purchase of Equity"),
    )
    SALE_OF_EQUITY = (
        9,
        pgettext_lazy("IATI codelist TransactionType", "Sale of Equity"),
    )
    CREDIT_GUARANTEE = (
        10,
        pgettext_lazy("IATI codelist TransactionType", "Credit Guarantee"),
    )
