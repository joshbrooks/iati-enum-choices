from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicExactnessDescription(models.IntegerChoices):
    EXACT = (
        1,
        pgettext_lazy(
            "GeographicExactness description",
            "The designated geographic location is exact",
        ),
    )
    APPROXIMATE = (
        2,
        pgettext_lazy(
            "GeographicExactness description",
            "The designated geographic location is approximate",
        ),
    )
