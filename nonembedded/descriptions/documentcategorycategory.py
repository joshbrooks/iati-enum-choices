from django.db import models
from django.utils.translation import pgettext_lazy


class DocumentCategoryCategoryDescription(models.TextChoices):
    """
    This codelists exists to group the Document Category codelist into categories. It is not used as a codelist in its own right.
    """

    ACTIVITY_LEVEL = (
        "A",
        pgettext_lazy(
            "IATI codelist DocumentCategory-category description",
            "The document is relevant to a specific activity",
        ),
    )
    ORGANISATION_LEVEL = (
        "B",
        pgettext_lazy(
            "IATI codelist DocumentCategory-category description",
            "The document is relevant to the organisation as a whole",
        ),
    )
