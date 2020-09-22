from django.db import models
from django.utils.translation import pgettext_lazy


class LocationTypeCategory(models.TextChoices):
    """
    This category is equivalent to US NGA's "Feature Class"
    """

    ADMINISTRATIVE_REGION = (
        "A",
        pgettext_lazy("LocationType-category", "Administrative Region"),
    )
    HYDROGRAPHIC = (
        "H",
        pgettext_lazy("LocationType-category", "Hydrographic"),
    )
    AREA = (
        "L",
        pgettext_lazy("LocationType-category", "Area"),
    )
    POPULATED_PLACE = (
        "P",
        pgettext_lazy("LocationType-category", "Populated Place"),
    )
    STREETS_HIGHWAYS_ROADS = (
        "R",
        pgettext_lazy("LocationType-category", "Streets/Highways/Roads"),
    )
    SPOT_FEATURES = (
        "S",
        pgettext_lazy("LocationType-category", "Spot Features"),
    )
    HYPSOGRAPHIC = (
        "T",
        pgettext_lazy("LocationType-category", "Hypsographic"),
    )
    UNDERSEA = (
        "U",
        pgettext_lazy("LocationType-category", "Undersea"),
    )
    VEGETATION = (
        "V",
        pgettext_lazy("LocationType-category", "Vegetation"),
    )
