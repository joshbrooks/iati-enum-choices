from django.db import models
from django.utils.translation import pgettext_lazy


class TransactionTypeDescription(models.IntegerChoices):
    INCOMING_FUNDS = (
        1,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Funds recieved for use on the activity, which can be from an external or internal source. ",
        ),
    )
    OUTGOING_COMMITMENT = (
        2,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "A firm, written obligation from a donor or provider to provide a specified amount of funds, under particular terms and conditions, for specific purposes, for the benefit of the recipient. ",
        ),
    )
    DISBURSEMENT = (
        3,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Outgoing funds that are placed at the disposal of a recipient government or organisation, or funds transferred between two separately reported activities.",
        ),
    )
    EXPENDITURE = (
        4,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Outgoing funds that are spent on goods and services for the activity.",
        ),
    )
    INTEREST_PAYMENT = (
        5,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "The actual amount of interest paid on a loan or line of credit, including fees.",
        ),
    )
    LOAN_REPAYMENT = (
        6,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "The actual amount of principal (amortisation) repaid, including any arrears. ",
        ),
    )
    REIMBURSEMENT = (
        7,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "A type of disbursement that covers funds that have already been spent by the recipient, as agreed in the terms of the grant or loan",
        ),
    )
    PURCHASE_OF_EQUITY = (
        8,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Outgoing funds that are used to purchase equity in a business",
        ),
    )
    SALE_OF_EQUITY = (
        9,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Incoming funds from the sale of equity. ",
        ),
    )
    CREDIT_GUARANTEE = (
        10,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "A commitment made by a funding organisation to underwrite a loan or line of credit entered into by a third party. ",
        ),
    )
    INCOMING_COMMITMENT = (
        11,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "A firm, written obligation from a donor or provider to provide a specified amount of funds, under particular terms and conditions, reported by a recipient for this activity.",
        ),
    )
    OUTGOING_PLEDGE = (
        12,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Indicative, non-binding advice of an intended outgoing commitment.",
        ),
    )
    INCOMING_PLEDGE = (
        13,
        pgettext_lazy(
            "IATI codelist TransactionType description",
            "Indicative, non-binding advice of an intended incoming commitment.",
        ),
    )
