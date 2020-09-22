from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicLocationClass(models.IntegerChoices):
    ADMINISTRATIVE_REGION = (
        1,
        pgettext_lazy("GeographicLocationClass", "Administrative Region"),
    )
    POPULATED_PLACE = (
        2,
        pgettext_lazy("GeographicLocationClass", "Populated Place"),
    )
    STRUCTURE = (
        3,
        pgettext_lazy("GeographicLocationClass", "Structure"),
    )
    OTHER_TOPOGRAPHICAL_FEATURE = (
        4,
        pgettext_lazy("GeographicLocationClass", "Other Topographical Feature"),
    )
