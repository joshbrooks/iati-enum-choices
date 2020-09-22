from django.db import models
from django.utils.translation import pgettext_lazy


class TiedStatus(models.IntegerChoices):
    PARTIALLY_TIED = (
        3,
        pgettext_lazy("IATI codelist TiedStatus", "Partially tied"),
    )
    TIED = (
        4,
        pgettext_lazy("IATI codelist TiedStatus", "Tied"),
    )
    UNTIED = (
        5,
        pgettext_lazy("IATI codelist TiedStatus", "Untied"),
    )
