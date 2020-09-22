from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifierDescription(models.TextChoices):
    """
    IATI Functional and Administrative Common Code : One of several possible Budget Identifier Vocabularies. As of version 2.03 this codelist has been deprecated.
    """

    # There are no valid items in this enums
    pass
