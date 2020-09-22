from django.db import models
from django.utils.translation import pgettext_lazy


class VersionDescription(models.TextChoices):
    """
    Version of the IATI Standard
    """

    # There are no valid items in this enums
    pass
