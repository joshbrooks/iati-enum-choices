from django.db import models
from django.utils.translation import pgettext_lazy


class DocumentCategoryDescription(models.TextChoices):
    # There are no valid items in this enums
    pass
