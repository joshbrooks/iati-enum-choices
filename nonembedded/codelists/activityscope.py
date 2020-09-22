from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityScope(models.IntegerChoices):
    """
    Geographic scope of activity
    """

    GLOBAL = (
        1,
        pgettext_lazy("ActivityScope", "Global"),
    )
    REGIONAL = (
        2,
        pgettext_lazy("ActivityScope", "Regional"),
    )
    MULTI_NATIONAL = (
        3,
        pgettext_lazy("ActivityScope", "Multi-national"),
    )
    NATIONAL = (
        4,
        pgettext_lazy("ActivityScope", "National"),
    )
    SUB_NATIONAL__MULTI_FIRST_LEVEL_ADMINISTRATIVE_AREAS = (
        5,
        pgettext_lazy(
            "ActivityScope",
            "Sub-national: Multi-first-level administrative areas",
        ),
    )
    SUB_NATIONAL__SINGLE_FIRST_LEVEL_ADMINISTRATIVE_AREA = (
        6,
        pgettext_lazy(
            "ActivityScope",
            "Sub-national: Single first-level administrative area",
        ),
    )
    SUB_NATIONAL__SINGLE_SECOND_LEVEL_ADMINISTRATIVE_AREA = (
        7,
        pgettext_lazy(
            "ActivityScope",
            "Sub-national: Single second-level administrative area",
        ),
    )
    SINGLE_LOCATION = (
        8,
        pgettext_lazy("ActivityScope", "Single location"),
    )
