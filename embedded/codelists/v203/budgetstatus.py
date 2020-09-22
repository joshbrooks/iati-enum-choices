from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetStatus(models.IntegerChoices):
    """
    Code to denote if the described budget is binding.
    """

    INDICATIVE = (
        1,
        pgettext_lazy("BudgetStatus", "Indicative"),
    )
    COMMITTED = (
        2,
        pgettext_lazy("BudgetStatus", "Committed"),
    )
