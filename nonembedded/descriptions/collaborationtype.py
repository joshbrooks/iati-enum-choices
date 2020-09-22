from django.db import models
from django.utils.translation import pgettext_lazy


class CollaborationTypeDescription(models.IntegerChoices):
    """
    OECD DAC classification used to determine the character of resource flows (bilateral or multilateral).
    """

    BILATERAL__TRIANGULAR_CO_OPERATION_ = (
        8,
        pgettext_lazy(
            "CollaborationType description",
            "Activities where one or more bilateral providers of development co-operation or international organisations support South-South co-operation, joining forces with developing countries to facilitate a sharing of knowledge and experience among all partners involved. (Activities that only involve bilateral providers or multilateral agencies without a South-South co-operation element (e.g. joint programming, pooled funding or delegated co-operation) should not be assigned bi_multi 8.)",
        ),
    )
