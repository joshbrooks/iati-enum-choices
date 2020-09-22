from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityDateType(models.IntegerChoices):
    """
    Types of date for activities. There are many different business models and dates that can be used to describe the start and end of activities. It is recommended that each publisher adopts their own consistent approach that provides users with a meaningful indication of the lifespan of an activity.
    """

    PLANNED_START = (
        1,
        pgettext_lazy("IATI codelist ActivityDateType", "Planned start"),
    )
    ACTUAL_START = (
        2,
        pgettext_lazy("IATI codelist ActivityDateType", "Actual start"),
    )
    PLANNED_END = (
        3,
        pgettext_lazy("IATI codelist ActivityDateType", "Planned End"),
    )
    ACTUAL_END = (
        4,
        pgettext_lazy("IATI codelist ActivityDateType", "Actual end"),
    )
