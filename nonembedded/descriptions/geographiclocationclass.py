from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicLocationClassDescription(models.IntegerChoices):
    ADMINISTRATIVE_REGION = (
        1,
        pgettext_lazy(
            "GeographicLocationClass description",
            "The designated geographic location is an administrative region (state, county, province, district, municipality etc.)",
        ),
    )
    POPULATED_PLACE = (
        2,
        pgettext_lazy(
            "GeographicLocationClass description",
            "The designated geographic location is a populated place (town, village, farm etc.)",
        ),
    )
    STRUCTURE = (
        3,
        pgettext_lazy(
            "GeographicLocationClass description",
            "The designated geopgraphic location is a structure (such as a school or a clinic)",
        ),
    )
    OTHER_TOPOGRAPHICAL_FEATURE = (
        4,
        pgettext_lazy(
            "GeographicLocationClass description",
            "The designated geographic location is a topographical feature, such as a mountain, a river, a forest",
        ),
    )
