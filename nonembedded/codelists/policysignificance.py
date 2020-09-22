from django.db import models
from django.utils.translation import pgettext_lazy


class PolicySignificance(models.IntegerChoices):
    NOT_TARGETED = (
        0,
        pgettext_lazy("IATI codelist PolicySignificance", "not targeted"),
    )
    SIGNIFICANT_OBJECTIVE = (
        1,
        pgettext_lazy("IATI codelist PolicySignificance", "significant objective"),
    )
    PRINCIPAL_OBJECTIVE = (
        2,
        pgettext_lazy("IATI codelist PolicySignificance", "principal objective"),
    )
    PRINCIPAL_OBJECTIVE_AND_IN_SUPPORT_OF_AN_ACTION_PROGRAMME = (
        3,
        pgettext_lazy(
            "IATI codelist PolicySignificance",
            "principal objective AND in support of an action programme",
        ),
    )
    EXPLICIT_PRIMARY_OBJECTIVE = (
        4,
        pgettext_lazy("IATI codelist PolicySignificance", "Explicit primary objective"),
    )
