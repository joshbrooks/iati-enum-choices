from django.db import models
from django.utils.translation import pgettext_lazy


class RelatedActivityType(models.IntegerChoices):
    PARENT = (
        1,
        pgettext_lazy("IATI codelist RelatedActivityType", "Parent"),
    )
    CHILD = (
        2,
        pgettext_lazy("IATI codelist RelatedActivityType", "Child"),
    )
    SIBLING = (
        3,
        pgettext_lazy("IATI codelist RelatedActivityType", "Sibling"),
    )
    CO_FUNDED = (
        4,
        pgettext_lazy("IATI codelist RelatedActivityType", "Co-funded"),
    )
    THIRD_PARTY = (
        5,
        pgettext_lazy("IATI codelist RelatedActivityType", "Third Party"),
    )
