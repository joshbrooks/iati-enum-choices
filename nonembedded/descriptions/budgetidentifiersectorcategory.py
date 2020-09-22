from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierSectorCategoryDescription(models.IntegerChoices):
    """
    This codelists exists to group the Budget Identifier codelist into categories. It is not used as a codelist in its own right.
    """

    # There are no valid items in this enums
    pass
