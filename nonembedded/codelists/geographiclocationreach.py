from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicLocationReach(models.IntegerChoices):
    ACTIVITY = (
        1,
        pgettext_lazy("GeographicLocationReach", "Activity"),
    )
    INTENDED_BENEFICIARIES = (
        2,
        pgettext_lazy("GeographicLocationReach", "Intended Beneficiaries"),
    )
