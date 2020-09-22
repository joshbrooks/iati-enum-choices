from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierVocabulary(models.IntegerChoices):
    IATI = (
        1,
        pgettext_lazy("IATI codelist BudgetIdentifierVocabulary", "IATI"),
    )
    COUNTRY_CHART_OF_ACCOUNTS = (
        2,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary", "Country Chart of Accounts"
        ),
    )
    OTHER_COUNTRY_SYSTEM = (
        3,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary", "Other Country System"
        ),
    )
    REPORTING_ORGANISATION = (
        4,
        pgettext_lazy(
            "IATI codelist BudgetIdentifierVocabulary", "Reporting Organisation"
        ),
    )
    OTHER = (
        5,
        pgettext_lazy("IATI codelist BudgetIdentifierVocabulary", "Other"),
    )
