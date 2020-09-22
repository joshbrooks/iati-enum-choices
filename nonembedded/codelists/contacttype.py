from django.db import models
from django.utils.translation import pgettext_lazy


class ContactType(models.IntegerChoices):
    GENERAL_ENQUIRIES = (
        1,
        pgettext_lazy("IATI codelist ContactType", "General Enquiries"),
    )
    PROJECT_MANAGEMENT = (
        2,
        pgettext_lazy("IATI codelist ContactType", "Project Management"),
    )
    FINANCIAL_MANAGEMENT = (
        3,
        pgettext_lazy("IATI codelist ContactType", "Financial Management"),
    )
    COMMUNICATIONS = (
        4,
        pgettext_lazy("IATI codelist ContactType", "Communications"),
    )
