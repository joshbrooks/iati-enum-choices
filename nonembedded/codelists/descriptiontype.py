from django.db import models
from django.utils.translation import pgettext_lazy


class DescriptionType(models.IntegerChoices):
    """
    Activity decription types. (General, objectives, etc)
    """

    GENERAL = (
        1,
        pgettext_lazy("DescriptionType", "General"),
    )
    OBJECTIVES = (
        2,
        pgettext_lazy("DescriptionType", "Objectives"),
    )
    TARGET_GROUPS = (
        3,
        pgettext_lazy("DescriptionType", "Target Groups"),
    )
    OTHER = (
        4,
        pgettext_lazy("DescriptionType", "Other"),
    )
