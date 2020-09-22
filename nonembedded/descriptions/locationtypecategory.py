from django.db import models
from django.utils.translation import pgettext_lazy


class LocationTypeCategoryDescription(models.TextChoices):
    """
    This category is equivalent to US NGA's "Feature Class"
    """

    # There are no valid items in this enums
    pass
