from django.db import models
from django.utils.translation import pgettext_lazy


class CurrencyDescription(models.TextChoices):
    """
    ISO 4217 Currency used for all transactions and budgets
    """

    BELARUSSIAN_RUBLE = (
        "BYR",
        pgettext_lazy(
            "Currency description",
            "Withdrawn from ISO Currency codelist. Use code BYN.",
        ),
    )
    KROON = (
        "EEK",
        pgettext_lazy("Currency description", "Withdrawn from ISO Currency codelist"),
    )
    LITHUANIAN_LITAS = (
        "LTL",
        pgettext_lazy("Currency description", "Withdrawn from ISO Currency codelist"),
    )
    LATVIAN_LATS = (
        "LVL",
        pgettext_lazy("Currency description", "Withdrawn from ISO Currency codelist"),
    )
    OUGUIYA = (
        "MRO",
        pgettext_lazy(
            "Currency description",
            "Withdrawn from ISO Currency codelist. Use code MRU.",
        ),
    )
    DOBRA = (
        "STD",
        pgettext_lazy(
            "Currency description",
            "Withdrawn from ISO Currency codelist. Use code STN.",
        ),
    )
    US_DOLLAR__SAME_DAY_ = (
        "USS",
        pgettext_lazy(
            "Currency description",
            "Withdrawn from ISO Currency codelist.",
        ),
    )
    ZAMBIAN_KWACHA = (
        "ZMK",
        pgettext_lazy(
            "Currency description",
            "Withdrawn from ISO Country codelist. Use code ZMW.",
        ),
    )
