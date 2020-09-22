from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityStatusDescription(models.IntegerChoices):
    """
    Lifecycle status of the activity from pipeline to completion
    """

    PIPELINE_IDENTIFICATION = (
        1,
        pgettext_lazy(
            "IATI codelist ActivityStatus description",
            "The activity is being scoped or planned ",
        ),
    )
    IMPLEMENTATION = (
        2,
        pgettext_lazy(
            "IATI codelist ActivityStatus description",
            "The activity is currently being implemented",
        ),
    )
    FINALISATION = (
        3,
        pgettext_lazy(
            "IATI codelist ActivityStatus description",
            "Physical activity is complete or the final disbursement has been made, but the activity remains open pending financial sign off or M&E",
        ),
    )
    CLOSED = (
        4,
        pgettext_lazy(
            "IATI codelist ActivityStatus description",
            "Physical activity is complete or the final disbursement has been made.",
        ),
    )
    CANCELLED = (
        5,
        pgettext_lazy(
            "IATI codelist ActivityStatus description",
            "The activity has been cancelled",
        ),
    )
    SUSPENDED = (
        6,
        pgettext_lazy(
            "IATI codelist ActivityStatus description",
            "The activity has been temporarily suspended",
        ),
    )
