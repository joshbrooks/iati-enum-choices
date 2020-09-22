from django.db import models
from django.utils.translation import pgettext_lazy


class UNSDG_TargetsDescription(models.TextChoices):
    """
    A value from the second-level list of UN sustainable development goals (SDGs) (e.g. ‘1.1’)
    """

    # There are no valid items in this enums
    pass
