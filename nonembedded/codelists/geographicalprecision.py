from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicalPrecision(models.IntegerChoices):
    """
    A system for clarifying the accuracy and usage of geographical coordinates
    """

    EXACT_LOCATION = (
        1,
        pgettext_lazy("IATI codelist GeographicalPrecision", "Exact location"),
    )
    NEAR_EXACT_LOCATION = (
        2,
        pgettext_lazy("IATI codelist GeographicalPrecision", "Near exact location"),
    )
    SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        3,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision",
            "Second order administrative division",
        ),
    )
    FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        4,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision", "First order administrative division"
        ),
    )
    ESTIMATED_COORDINATES = (
        5,
        pgettext_lazy("IATI codelist GeographicalPrecision", "Estimated coordinates"),
    )
    INDEPENDENT_POLITICAL_ENTITY = (
        6,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision", "Independent political entity"
        ),
    )
    UNCLEAR_CAPITAL = (
        7,
        pgettext_lazy("IATI codelist GeographicalPrecision", "Unclear - capital"),
    )
    LOCAL_OR_NATIONAL_CAPITAL = (
        8,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision", "Local or national capital"
        ),
    )
    UNCLEAR_COUNTRY = (
        9,
        pgettext_lazy("IATI codelist GeographicalPrecision", "Unclear - country"),
    )
