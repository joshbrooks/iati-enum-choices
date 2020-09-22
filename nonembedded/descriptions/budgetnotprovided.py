from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetNotProvidedDescription(models.IntegerChoices):
    """
    A codelist defining the reasons why an activity does not contain any iati-activity/budget elements.
    """

    # There are no valid items in this enums
    pass
