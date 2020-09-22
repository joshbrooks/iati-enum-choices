from django.db import models
from django.utils.translation import pgettext_lazy


class ContactTypeDescription(models.IntegerChoices):
    GENERAL_ENQUIRIES = (
        1,
        pgettext_lazy("ContactType description", "General Enquiries"),
    )
    PROJECT_MANAGEMENT = (
        2,
        pgettext_lazy("ContactType description", "Project Management"),
    )
    FINANCIAL_MANAGEMENT = (
        3,
        pgettext_lazy("ContactType description", "Financial Management"),
    )
    COMMUNICATIONS = (
        4,
        pgettext_lazy("ContactType description", "Communications"),
    )
