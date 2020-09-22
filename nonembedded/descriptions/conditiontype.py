from django.db import models
from django.utils.translation import pgettext_lazy


class ConditionTypeDescription(models.IntegerChoices):
    """
    Condition type – e.g. policy, performance.
    """

    POLICY = (
        1,
        pgettext_lazy(
            "ConditionType description",
            "The condition attached requires a particular policy to be implemented by the recipient",
        ),
    )
    PERFORMANCE = (
        2,
        pgettext_lazy(
            "ConditionType description",
            "The condition attached requires certain outputs or outcomes to be achieved by the recipient",
        ),
    )
    FIDUCIARY = (
        3,
        pgettext_lazy(
            "ConditionType description",
            "The condition attached requires use of certain public financial management or public accountability measures by the recipient",
        ),
    )
