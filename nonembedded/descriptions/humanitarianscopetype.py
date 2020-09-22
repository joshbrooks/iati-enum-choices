from django.db import models
from django.utils.translation import pgettext_lazy


class HumanitarianScopeTypeDescription(models.IntegerChoices):
    """
    The Humanitarian Scope Type codelist defines codes for types of humanitarian events and actions.
    """

    # There are no valid items in this enums
    pass
