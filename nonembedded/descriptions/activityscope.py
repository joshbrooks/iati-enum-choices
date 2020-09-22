from django.db import models
from django.utils.translation import pgettext_lazy


class ActivityScopeDescription(models.IntegerChoices):
    """
    Geographic scope of activity
    """

    GLOBAL = (
        1,
        pgettext_lazy("ActivityScope description", "The activity scope is global"),
    )
    REGIONAL = (
        2,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope is a supranational region",
        ),
    )
    MULTI_NATIONAL = (
        3,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope covers multiple countries, that don't constitute a region",
        ),
    )
    NATIONAL = (
        4,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope covers one country",
        ),
    )
    SUB_NATIONAL__MULTI_FIRST_LEVEL_ADMINISTRATIVE_AREAS = (
        5,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope covers more than one first-level subnational administrative areas (e.g. counties, provinces, states)",
        ),
    )
    SUB_NATIONAL__SINGLE_FIRST_LEVEL_ADMINISTRATIVE_AREA = (
        6,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope covers one first-level subnational administrative area (e.g. country, province, state)",
        ),
    )
    SUB_NATIONAL__SINGLE_SECOND_LEVEL_ADMINISTRATIVE_AREA = (
        7,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope covers one second-level subnational administrative area (e.g. municipality or district)",
        ),
    )
    SINGLE_LOCATION = (
        8,
        pgettext_lazy(
            "ActivityScope description",
            "The activity scope covers one single location (e.g. town, village, farm)",
        ),
    )
