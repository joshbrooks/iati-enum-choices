from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicExactness(models.IntegerChoices):
    EXACT = (
        1,
        pgettext_lazy("IATI codelist GeographicExactness", "Exact"),
    )
    APPROXIMATE = (
        2,
        pgettext_lazy("IATI codelist GeographicExactness", "Approximate"),
    )
