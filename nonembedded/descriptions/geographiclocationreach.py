from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicLocationReachDescription(models.IntegerChoices):
    ACTIVITY = (
        1,
        pgettext_lazy(
            "IATI codelist GeographicLocationReach description",
            "The location specifies where the activity is carried out",
        ),
    )
    INTENDED_BENEFICIARIES = (
        2,
        pgettext_lazy(
            "IATI codelist GeographicLocationReach description",
            "The location specifies where the intended beneficiaries of the activity live",
        ),
    )
