from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationRole(models.IntegerChoices):
    """
    IATI codes for the role of an organisation within an activity. An organisation can play more than one role within an activity.
    """

    FUNDING = (
        1,
        pgettext_lazy("OrganisationRole", "Funding"),
    )
    ACCOUNTABLE = (
        2,
        pgettext_lazy("OrganisationRole", "Accountable"),
    )
    EXTENDING = (
        3,
        pgettext_lazy("OrganisationRole", "Extending"),
    )
    IMPLEMENTING = (
        4,
        pgettext_lazy("OrganisationRole", "Implementing"),
    )
