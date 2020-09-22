from django.db import models
from django.utils.translation import pgettext_lazy


class PolicyMarkerDescription(models.IntegerChoices):
    """
    The Policy Marker codelist is derived from the policy markers declared by the WP-STAT. The codes themselves are created by IATI.
    """

    # There are no valid items in this enums
    pass
