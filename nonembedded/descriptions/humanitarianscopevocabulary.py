from django.db import models
from django.utils.translation import pgettext_lazy


class HumanitarianScopeVocabularyDescription(models.TextChoices):
    """
    The Humanitarian Scope Vocabulary codelist defines a range of external codelists which themselves provide codes and descriptions for humanitarian events and actions.
    """

    # There are no valid items in this enums
    pass
