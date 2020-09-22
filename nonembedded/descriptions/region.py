from django.db import models
from django.utils.translation import pgettext_lazy


class RegionDescription(models.IntegerChoices):
    # There are no valid items in this enums
    pass
