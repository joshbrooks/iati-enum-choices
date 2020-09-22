from django.db import models
from django.utils.translation import pgettext_lazy


class HumanitarianScopeType(models.IntegerChoices):
    """
    The Humanitarian Scope Type codelist defines codes for types of humanitarian events and actions.
    """

    EMERGENCY = (
        1,
        pgettext_lazy("IATI codelist HumanitarianScopeType", "Emergency"),
    )
    APPEAL = (
        2,
        pgettext_lazy("IATI codelist HumanitarianScopeType", "Appeal"),
    )
