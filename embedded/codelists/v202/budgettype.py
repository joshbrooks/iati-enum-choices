from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetType(models.IntegerChoices):
    """
    OECD DAC classification used to determine the character of resource flows (bilateral or multilateral).
    """

    ORIGINAL = (
        1,
        pgettext_lazy("BudgetType", "Original"),
    )
    REVISED = (
        2,
        pgettext_lazy("BudgetType", "Revised"),
    )
