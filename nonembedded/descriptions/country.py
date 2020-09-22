from django.db import models
from django.utils.translation import pgettext_lazy


class CountryDescription(models.TextChoices):
    """
    The Country codelist is generated from the ISO 3166-1 part of the ISO 3166 standard. The standard makes allowance, alongside the officially assigned codes, for code elements to be expanded by using either reserved codes or user-assigned codes. IATI currently defines additional codes in the XA -XZ range.
    """

    # There are no valid items in this enums
    pass
