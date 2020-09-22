from django.db import models
from django.utils.translation import pgettext_lazy


class FileFormatDescription(models.TextChoices):
    """
    File format of published documents.
    """

    # There are no valid items in this enums
    pass
