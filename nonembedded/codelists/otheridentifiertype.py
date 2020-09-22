from django.db import models
from django.utils.translation import pgettext_lazy


class OtherIdentifierType(models.TextChoices):
    REPORTING_ORGANISATION_S_INTERNAL_ACTIVITY_IDENTIFIER = (
        "A1",
        pgettext_lazy(
            "OtherIdentifierType",
            "Reporting Organisation's internal activity identifier",
        ),
    )
    CRS_ACTIVITY_IDENTIFIER = (
        "A2",
        pgettext_lazy("OtherIdentifierType", "CRS Activity identifier"),
    )
    PREVIOUS_ACTIVITY_IDENTIFIER = (
        "A3",
        pgettext_lazy("OtherIdentifierType", "Previous Activity Identifier"),
    )
    OTHER_ACTIVITY_IDENTIFIER = (
        "A9",
        pgettext_lazy("OtherIdentifierType", "Other Activity Identifier"),
    )
    PREVIOUS_REPORTING_ORGANISATION_IDENTIFIER = (
        "B1",
        pgettext_lazy(
            "OtherIdentifierType",
            "Previous Reporting Organisation Identifier",
        ),
    )
    OTHER_ORGANISATION_IDENTIFIER = (
        "B9",
        pgettext_lazy("OtherIdentifierType", "Other Organisation Identifier"),
    )
