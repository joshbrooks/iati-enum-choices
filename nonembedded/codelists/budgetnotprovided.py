from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetNotProvided(models.IntegerChoices):
    """
    A codelist defining the reasons why an activity does not contain any iati-activity/budget elements.
    """

    COMMERCIAL_RESTRICTIONS = (
        1,
        pgettext_lazy("BudgetNotProvided", "Commercial Restrictions"),
    )
    LEGAL_RESTRICTIONS = (
        2,
        pgettext_lazy("BudgetNotProvided", "Legal Restrictions"),
    )
    RAPID_ONSET_EMERGENCY = (
        3,
        pgettext_lazy("BudgetNotProvided", "Rapid Onset Emergency"),
    )
