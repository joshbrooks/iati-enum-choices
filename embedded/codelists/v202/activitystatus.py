from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityStatus(models.IntegerChoices):
    """
    Lifecycle status of the activity from pipeline to completion
    """

    PIPELINE_IDENTIFICATION = (
        1,
        pgettext_lazy("ActivityStatus", "Pipeline/identification"),
    )
    IMPLEMENTATION = (
        2,
        pgettext_lazy("ActivityStatus", "Implementation"),
    )
    FINALISATION = (
        3,
        pgettext_lazy("ActivityStatus", "Finalisation"),
    )
    CLOSED = (
        4,
        pgettext_lazy("ActivityStatus", "Closed"),
    )
    CANCELLED = (
        5,
        pgettext_lazy("ActivityStatus", "Cancelled"),
    )
    SUSPENDED = (
        6,
        pgettext_lazy("ActivityStatus", "Suspended"),
    )
