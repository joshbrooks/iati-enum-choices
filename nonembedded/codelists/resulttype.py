from django.db import models
from django.utils.translation import pgettext_lazy


class ResultType(models.IntegerChoices):
    OUTPUT = (
        1,
        pgettext_lazy("IATI codelist ResultType", "Output"),
    )
    OUTCOME = (
        2,
        pgettext_lazy("IATI codelist ResultType", "Outcome"),
    )
    IMPACT = (
        3,
        pgettext_lazy("IATI codelist ResultType", "Impact"),
    )
    OTHER = (
        9,
        pgettext_lazy("IATI codelist ResultType", "Other"),
    )
