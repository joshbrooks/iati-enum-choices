from django.db import models
from django.utils.translation import pgettext_lazy


class LocationTypeCategory(models.TextChoices):
    """
    This category is equivalent to US NGA's "Feature Class"
    """

    ADMINISTRATIVE_REGION = (
        "A",
        pgettext_lazy("IATI codelist LocationType-category", "Administrative Region"),
    )
    HYDROGRAPHIC = (
        "H",
        pgettext_lazy("IATI codelist LocationType-category", "Hydrographic"),
    )
    AREA = (
        "L",
        pgettext_lazy("IATI codelist LocationType-category", "Area"),
    )
    POPULATED_PLACE = (
        "P",
        pgettext_lazy("IATI codelist LocationType-category", "Populated Place"),
    )
    STREETS_HIGHWAYS_ROADS = (
        "R",
        pgettext_lazy("IATI codelist LocationType-category", "Streets/Highways/Roads"),
    )
    SPOT_FEATURES = (
        "S",
        pgettext_lazy("IATI codelist LocationType-category", "Spot Features"),
    )
    HYPSOGRAPHIC = (
        "T",
        pgettext_lazy("IATI codelist LocationType-category", "Hypsographic"),
    )
    UNDERSEA = (
        "U",
        pgettext_lazy("IATI codelist LocationType-category", "Undersea"),
    )
    VEGETATION = (
        "V",
        pgettext_lazy("IATI codelist LocationType-category", "Vegetation"),
    )
