from django.db import models
from django.utils.translation import pgettext_lazy


class RelatedActivityTypeDescription(models.IntegerChoices):
    PARENT = (
        1,
        pgettext_lazy(
            "RelatedActivityType description",
            "An activity that contains sub-activities (sub-components) which are reported separately to IATI",
        ),
    )
    CHILD = (
        2,
        pgettext_lazy(
            "RelatedActivityType description",
            "A sub-activity (or sub-component) that sits within a larger activity (parent) which is also reported to IATI",
        ),
    )
    SIBLING = (
        3,
        pgettext_lazy(
            "RelatedActivityType description",
            "A sub-activity (or sub-component) that is related to another sub-activity with the same parent ",
        ),
    )
    CO_FUNDED = (
        4,
        pgettext_lazy(
            "RelatedActivityType description",
            "An activity that receives funding from more than one organisation",
        ),
    )
    THIRD_PARTY = (
        5,
        pgettext_lazy(
            "RelatedActivityType description",
            "A report by another organisation on the same activity you are reporting (excluding activities reported as part of a financial transaction - e.g. provider-activity-id or a co-funded activity, using code 4)",
        ),
    )
