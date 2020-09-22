from django.db import models
from django.utils.translation import pgettext_lazy


class PolicyMarkerVocabulary(models.IntegerChoices):
    OECD_DAC_CRS = (
        1,
        pgettext_lazy("PolicyMarkerVocabulary", "OECD DAC CRS"),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy("PolicyMarkerVocabulary", "Reporting Organisation"),
    )
