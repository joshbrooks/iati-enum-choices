from django.db import models
from django.utils.translation import pgettext_lazy


class IndicatorVocabularyDescription(models.IntegerChoices):
    """
    The Indicator Vocabulary codelist defines a range of external codelists which themselves provide codes and descriptions for indicators, for example to specify results.
    """

    # There are no valid items in this enums
    pass
