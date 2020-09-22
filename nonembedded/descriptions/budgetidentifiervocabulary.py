from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierVocabularyDescription(models.IntegerChoices):
    IATI = (
        1,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary description",
            "The budget identifier reported uses IATI budget identifier categories",
        ),
    )
    COUNTRY_CHART_OF_ACCOUNTS = (
        2,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary description",
            "The budget identifier reported corresponds to the recipient country chart of accounts",
        ),
    )
    OTHER_COUNTRY_SYSTEM = (
        3,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary description",
            "The budget identifier reported corresponds to a recipient country system other than the chart of accounts",
        ),
    )
    REPORTING_ORGANISATION = (
        4,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary description",
            "The budget identifier reported corresponds to categories that are specific to the reporting organisation",
        ),
    )
    OTHER = (
        5,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary description",
            "The budget identifier reported uses a different vocabulary, not specified in the codelist ",
        ),
    )
