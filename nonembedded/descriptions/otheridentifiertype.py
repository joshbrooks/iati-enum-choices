from django.db import models
from django.utils.translation import pgettext_lazy


class OtherIdentifierTypeDescription(models.TextChoices):
    PREVIOUS_ACTIVITY_IDENTIFIER = (
        "A3",
        pgettext_lazy(
            "IATI codelist OtherIdentifierType description",
            "The standard insists that once an activity has been reported to IATI its identifier MUST NOT be changed, even if the reporting organisation changes its organisation identifier. There may be exceptional circumstances in which this rule cannot be followed, in which case the previous identifier should be reported using this code.",
        ),
    )
