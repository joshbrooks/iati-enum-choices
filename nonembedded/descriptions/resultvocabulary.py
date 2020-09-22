from django.db import models
from django.utils.translation import pgettext_lazy


class ResultVocabularyDescription(models.IntegerChoices):
    """
    The ResultVocabulary codelist currently includes only 1 code (99) that can be used by organisations to define different results frameworks they are using.
    """

    # There are no valid items in this enums
    pass
