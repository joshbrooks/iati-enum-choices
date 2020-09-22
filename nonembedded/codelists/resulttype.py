from django.db import models
from django.utils.translation import pgettext_lazy


class ResultType(models.IntegerChoices):
    OUTPUT = (
        1,
        pgettext_lazy("ResultType", "Output"),
    )
    OUTCOME = (
        2,
        pgettext_lazy("ResultType", "Outcome"),
    )
    IMPACT = (
        3,
        pgettext_lazy("ResultType", "Impact"),
    )
    OTHER = (
        9,
        pgettext_lazy("ResultType", "Other"),
    )
