from django.db import models
from django.utils.translation import pgettext_lazy


class RegionVocabulary(models.IntegerChoices):
    OECD_DAC = (
        1,
        pgettext_lazy("IATI codelist RegionVocabulary", "OECD DAC"),
    )
    UN = (
        2,
        pgettext_lazy("IATI codelist RegionVocabulary", "UN"),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy("IATI codelist RegionVocabulary", "Reporting Organisation"),
    )
