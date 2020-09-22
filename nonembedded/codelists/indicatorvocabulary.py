from django.db import models
from django.utils.translation import pgettext_lazy


class IndicatorVocabulary(models.IntegerChoices):
    """
    The Indicator Vocabulary codelist defines a range of external codelists which themselves provide codes and descriptions for indicators, for example to specify results.
    """

    WHO_REGISTRY = (
        1,
        pgettext_lazy("IndicatorVocabulary", "WHO Registry"),
    )
    SPHERE_HANDBOOK = (
        2,
        pgettext_lazy("IndicatorVocabulary", "Sphere Handbook"),
    )
    US_FOREIGN_ASSISTANCE_FRAMEWORK = (
        3,
        pgettext_lazy("IndicatorVocabulary", "US Foreign Assistance Framework"),
    )
    WORLD_BANK_WORLD_DEVELOPMENT_INDICATORS = (
        4,
        pgettext_lazy(
            "IndicatorVocabulary",
            "World Bank World Development Indicators",
        ),
    )
    UN_MILLENNIUM_DEVELOPMENT_GOALS_INDICATORS = (
        5,
        pgettext_lazy(
            "IndicatorVocabulary",
            "UN Millennium Development Goals Indicators",
        ),
    )
    UNOCHA_HUMANITARIAN_RESPONSE_INDICATORS = (
        6,
        pgettext_lazy(
            "IndicatorVocabulary",
            "UNOCHA Humanitarian Response Indicators",
        ),
    )
    HIV_AIDS_INDICATOR_REGISTRY = (
        7,
        pgettext_lazy("IndicatorVocabulary", "HIV/AIDS Indicator Registry"),
    )
    HARMONIZED_INDICATORS_FOR_PRIVATE_SECTOR__HIPSO_ = (
        8,
        pgettext_lazy(
            "IndicatorVocabulary",
            "Harmonized Indicators for Private Sector (HIPSO)",
        ),
    )
    UN_SUSTAINABLE_DEVELOPMENT_GOALS__SDG__INDICATORS = (
        9,
        pgettext_lazy(
            "IndicatorVocabulary",
            "UN Sustainable Development Goals (SDG) Indicators",
        ),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy("IndicatorVocabulary", "Reporting Organisation"),
    )
