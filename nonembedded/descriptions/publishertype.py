from django.db import models
from django.utils.translation import pgettext_lazy


class PublisherTypeDescription(models.IntegerChoices):
    AID_PROVIDER = (
        1,
        pgettext_lazy(
            "PublisherType description",
            "A government, organisation, agency or institution that provides aid funds.",
        ),
    )
    AID_RECIPIENT = (
        2,
        pgettext_lazy(
            "PublisherType description",
            "A government, organisation, agency or institution that recieves aid funds.",
        ),
    )
    AGGREGATOR = (
        3,
        pgettext_lazy(
            "PublisherType description",
            "An organisation that collects and reproduces information from other providers or recipients",
        ),
    )
