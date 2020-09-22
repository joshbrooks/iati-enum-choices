from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityDateTypeDescription(models.IntegerChoices):
    """
    Types of date for activities. There are many different business models and dates that can be used to describe the start and end of activities. It is recommended that each publisher adopts their own consistent approach that provides users with a meaningful indication of the lifespan of an activity.
    """

    PLANNED_START = (
        1,
        pgettext_lazy(
            "IATI codelist ActivityDateType description",
            "The date on which the activity is planned to start, for example the date of the first planned disbursement or when physical activity starts.",
        ),
    )
    ACTUAL_START = (
        2,
        pgettext_lazy(
            "IATI codelist ActivityDateType description",
            "The actual date the activity starts, for example the date of the first disbursement or when physical activity starts.",
        ),
    )
    PLANNED_END = (
        3,
        pgettext_lazy(
            "IATI codelist ActivityDateType description",
            "The date on which the activity is planned to end, for example the date of the last planned disbursement or when physical activity is complete.",
        ),
    )
    ACTUAL_END = (
        4,
        pgettext_lazy(
            "IATI codelist ActivityDateType description",
            "The actual date the activity ends, for example the date of the last disbursement or when physical activity is complete.",
        ),
    )
