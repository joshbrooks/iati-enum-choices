from django.db import models
from django.utils.translation import pgettext_lazy


class VerificationStatus(models.IntegerChoices):
    NOT_VERIFIED = (
        0,
        pgettext_lazy("IATI codelist VerificationStatus", "Not verified"),
    )
    VERIFIED = (
        1,
        pgettext_lazy("IATI codelist VerificationStatus", "Verified"),
    )
