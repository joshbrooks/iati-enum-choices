from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetType(models.IntegerChoices):
    ORIGINAL = (
        1,
        pgettext_lazy("BudgetType", "Original"),
    )
    REVISED = (
        2,
        pgettext_lazy("BudgetType", "Revised"),
    )
