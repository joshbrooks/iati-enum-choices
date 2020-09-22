from django.db import models
from django.utils.translation import pgettext_lazy


class DescriptionTypeDescription(models.IntegerChoices):
    """
    Activity decription types. (General, objectives, etc)
    """

    GENERAL = (
        1,
        pgettext_lazy(
            "DescriptionType description",
            "Unstructured, long description of the activity ",
        ),
    )
    OBJECTIVES = (
        2,
        pgettext_lazy(
            "DescriptionType description",
            "Specific objectives for the activity, e.g. taken from logical framework",
        ),
    )
    TARGET_GROUPS = (
        3,
        pgettext_lazy(
            "DescriptionType description",
            "Details of groups that are intended to benefit from the activity",
        ),
    )
    OTHER = (
        4,
        pgettext_lazy(
            "DescriptionType description",
            "For miscellaneous use. A further classification or breakdown may be included in the narrative",
        ),
    )
