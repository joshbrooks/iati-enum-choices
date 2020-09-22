from django.db import models
from django.utils.translation import pgettext_lazy


class GazetteerAgencyDescription(models.IntegerChoices):
    """
    An online resource that holds coordinates and descriptions of geographic locations
    """

    # There are no valid items in this enums
    pass
