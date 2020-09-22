from django.db import models
from django.utils.translation import pgettext_lazy


class PublisherType(models.IntegerChoices):
    AID_PROVIDER = (
        1,
        pgettext_lazy("PublisherType", "Aid Provider"),
    )
    AID_RECIPIENT = (
        2,
        pgettext_lazy("PublisherType", "Aid Recipient"),
    )
    AGGREGATOR = (
        3,
        pgettext_lazy("PublisherType", "Aggregator"),
    )
