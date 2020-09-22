from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationRoleDescription(models.IntegerChoices):
    """
    IATI codes for the role of an organisation within an activity. An organisation can play more than one role within an activity.
    """

    FUNDING = (
        1,
        pgettext_lazy(
            "IATI codelist OrganisationRole description",
            "The government or organisation which provides funds to the activity. ",
        ),
    )
    ACCOUNTABLE = (
        2,
        pgettext_lazy(
            "IATI codelist OrganisationRole description",
            "An organisation responsible for oversight of the activity and its outcomes",
        ),
    )
    EXTENDING = (
        3,
        pgettext_lazy(
            "IATI codelist OrganisationRole description",
            "An organisation that manages the budget and direction of an activity on behalf of the funding organisation",
        ),
    )
    IMPLEMENTING = (
        4,
        pgettext_lazy(
            "IATI codelist OrganisationRole description",
            "The organisation that physically carries out the activity or intervention. ",
        ),
    )
