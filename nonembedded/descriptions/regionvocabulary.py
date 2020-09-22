from django.db import models
from django.utils.translation import pgettext_lazy


class RegionVocabularyDescription(models.IntegerChoices):
    OECD_DAC = (
        1,
        pgettext_lazy(
            "RegionVocabulary description",
            "Supra-national regions according to OECD DAC CRS recipient codes",
        ),
    )
    UN = (
        2,
        pgettext_lazy(
            "RegionVocabulary description",
            "Supra-national regions maintained by UN Statistics Division (M49 standard)",
        ),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy(
            "RegionVocabulary description",
            "The region reported corresponds to a region vocabulary maintained by the reporting organisation for this activity.",
        ),
    )
