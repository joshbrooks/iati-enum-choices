from django.db import models
from django.utils.translation import pgettext_lazy


class RelatedActivityType(models.IntegerChoices):
    PARENT = (
        1,
        pgettext_lazy("RelatedActivityType", "Parent"),
    )
    CHILD = (
        2,
        pgettext_lazy("RelatedActivityType", "Child"),
    )
    SIBLING = (
        3,
        pgettext_lazy("RelatedActivityType", "Sibling"),
    )
    CO_FUNDED = (
        4,
        pgettext_lazy("RelatedActivityType", "Co-funded"),
    )
    THIRD_PARTY = (
        5,
        pgettext_lazy("RelatedActivityType", "Third Party"),
    )
