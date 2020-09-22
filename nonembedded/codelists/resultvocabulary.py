from django.db import models
from django.utils.translation import pgettext_lazy


class ResultVocabulary(models.IntegerChoices):
    """
    The ResultVocabulary codelist currently includes only 1 code (99) that can be used by organisations to define different results frameworks they are using.
    """

    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy("IATI codelist ResultVocabulary", "Reporting Organisation"),
    )
