from django.db import models
from django.utils.translation import pgettext_lazy


class HumanitarianScopeVocabulary(models.TextChoices):
    """
    The Humanitarian Scope Vocabulary codelist defines a range of external codelists which themselves provide codes and descriptions for humanitarian events and actions.
    """

    GLIDE = (
        "1-2",
        pgettext_lazy("HumanitarianScopeVocabulary", "Glide"),
    )
    HUMANITARIAN_PLAN = (
        "2-1",
        pgettext_lazy("HumanitarianScopeVocabulary", "Humanitarian Plan"),
    )
    REPORTING_ORGANISATION = (
        "99",
        pgettext_lazy("HumanitarianScopeVocabulary", "Reporting Organisation"),
    )
