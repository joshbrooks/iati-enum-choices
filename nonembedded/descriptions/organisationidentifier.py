from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationIdentifierDescription(models.TextChoices):
    """
    As of 1.04 this list is no longer maintained. http://support.iatistandard.org/entries/28497976-Retire-the-Organisation-Identifier-codelist#view-post-25368673 For general guidance about constructing Organisation Identifiers, please see http://iatistandard.org/organisation-identifiers/
    """

    # There are no valid items in this enums
    pass
