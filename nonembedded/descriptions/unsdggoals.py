from django.db import models
from django.utils.translation import pgettext_lazy


class UNSDG_GoalsDescription(models.IntegerChoices):
    """
    A value from the top-level list of UN sustainable development goals (SDGs) (e.g. ‘1’)
    """

    # There are no valid items in this enums
    pass
