from django.db import models
from django.utils.translation import pgettext_lazy


class PolicyMarkerVocabularyDescription(models.IntegerChoices):
    OECD_DAC_CRS = (
        1,
        pgettext_lazy(
            "IATI codelist PolicyMarkerVocabulary description",
            "The policy marker is an OECD DAC CRS policy marker, Reported in columns 20-23, 28-31 and 54 of CRS++ reporting format.",
        ),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy(
            "IATI codelist PolicyMarkerVocabulary description",
            "The policy marker is one that is defined and tracked by the reporting organisation",
        ),
    )
