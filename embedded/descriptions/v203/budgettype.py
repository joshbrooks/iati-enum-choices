from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetTypeDescription(models.IntegerChoices):
    ORIGINAL = (
        1,
        pgettext_lazy(
            "BudgetType description",
            "The original budget allocated to the activity",
        ),
    )
    REVISED = (
        2,
        pgettext_lazy("BudgetType description", "The updated budget for an activity"),
    )
