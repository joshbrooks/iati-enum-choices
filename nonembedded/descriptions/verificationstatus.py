from django.db import models
from django.utils.translation import pgettext_lazy


class VerificationStatusDescription(models.IntegerChoices):
    NOT_VERIFIED = (
        0,
        pgettext_lazy(
            "IATI codelist VerificationStatus description",
            "The data published for the activity has not been verified",
        ),
    )
    VERIFIED = (
        1,
        pgettext_lazy(
            "IATI codelist VerificationStatus description",
            "The data published for the activity has been verified. ",
        ),
    )
