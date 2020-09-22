from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetStatusDescription(models.IntegerChoices):
    """
    Code to denote if the described budget is binding.
    """

    INDICATIVE = (
        1,
        pgettext_lazy(
            "BudgetStatus description",
            "A non-binding estimate for the described budget.",
        ),
    )
    COMMITTED = (
        2,
        pgettext_lazy(
            "BudgetStatus description",
            "A binding agreement for the described budget.",
        ),
    )
