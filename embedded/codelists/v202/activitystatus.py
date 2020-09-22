from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityStatus(models.IntegerChoices):
    """
    Lifecycle status of the activity from pipeline to completion
    """

    PIPELINE_IDENTIFICATION = (
        1,
        pgettext_lazy("IATI codelist ActivityStatus", "Pipeline/identification"),
    )
    IMPLEMENTATION = (
        2,
        pgettext_lazy("IATI codelist ActivityStatus", "Implementation"),
    )
    FINALISATION = (
        3,
        pgettext_lazy("IATI codelist ActivityStatus", "Finalisation"),
    )
    CLOSED = (
        4,
        pgettext_lazy("IATI codelist ActivityStatus", "Closed"),
    )
    CANCELLED = (
        5,
        pgettext_lazy("IATI codelist ActivityStatus", "Cancelled"),
    )
    SUSPENDED = (
        6,
        pgettext_lazy("IATI codelist ActivityStatus", "Suspended"),
    )
