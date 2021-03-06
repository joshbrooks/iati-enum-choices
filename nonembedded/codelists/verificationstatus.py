from django.db import models
from django.utils.translation import pgettext_lazy


class VerificationStatus(models.IntegerChoices):
    NOT_VERIFIED = (
        0,
        pgettext_lazy("VerificationStatus", "Not verified"),
    )
    VERIFIED = (
        1,
        pgettext_lazy("VerificationStatus", "Verified"),
    )
