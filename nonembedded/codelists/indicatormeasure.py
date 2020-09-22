from django.db import models
from django.utils.translation import pgettext_lazy


class IndicatorMeasure(models.IntegerChoices):
    """
    To specify how an indicator is being measured. This includes qualitative and quantitative values.
    """

    UNIT = (
        1,
        pgettext_lazy("IndicatorMeasure", "Unit"),
    )
    PERCENTAGE = (
        2,
        pgettext_lazy("IndicatorMeasure", "Percentage"),
    )
    NOMINAL = (
        3,
        pgettext_lazy("IndicatorMeasure", "Nominal"),
    )
    ORDINAL = (
        4,
        pgettext_lazy("IndicatorMeasure", "Ordinal"),
    )
    QUALITATIVE = (
        5,
        pgettext_lazy("IndicatorMeasure", "Qualitative"),
    )
