from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierSectorDescription(models.TextChoices):
    """
    This codelists exists to group the Budget Identifier codelist into sectors. It is not used as a codelist in its own right.
    """

    # There are no valid items in this enums
    pass
