from django.db import models
from django.utils.translation import pgettext_lazy


class IndicatorMeasureDescription(models.IntegerChoices):
    """
    To specify how an indicator is being measured. This includes qualitative and quantitative values.
    """

    UNIT = (
        1,
        pgettext_lazy(
            "IATI codelist IndicatorMeasure description",
            "The indicator is measured in units.",
        ),
    )
    PERCENTAGE = (
        2,
        pgettext_lazy(
            "IATI codelist IndicatorMeasure description",
            "The indicator is measured in percentages",
        ),
    )
    NOMINAL = (
        3,
        pgettext_lazy(
            "IATI codelist IndicatorMeasure description",
            "The indicator is measured as a quantitative nominal scale.",
        ),
    )
    ORDINAL = (
        4,
        pgettext_lazy(
            "IATI codelist IndicatorMeasure description",
            "The indicator is measured as a quantitative ordinal scale.",
        ),
    )
    QUALITATIVE = (
        5,
        pgettext_lazy(
            "IATI codelist IndicatorMeasure description",
            "The indicator is qualitative.",
        ),
    )
