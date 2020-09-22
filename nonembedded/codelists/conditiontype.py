from django.db import models
from django.utils.translation import pgettext_lazy


class ConditionType(models.IntegerChoices):
    """
    Condition type – e.g. policy, performance.
    """

    POLICY = (
        1,
        pgettext_lazy("ConditionType", "Policy"),
    )
    PERFORMANCE = (
        2,
        pgettext_lazy("ConditionType", "Performance"),
    )
    FIDUCIARY = (
        3,
        pgettext_lazy("ConditionType", "Fiduciary"),
    )
