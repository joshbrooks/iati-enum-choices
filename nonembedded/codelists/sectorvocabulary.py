from django.db import models
from django.utils.translation import pgettext_lazy


class SectorVocabulary(models.IntegerChoices):
    OECD_DAC_CRS_PURPOSE_CODES__5_DIGIT_ = (
        1,
        pgettext_lazy("SectorVocabulary", "OECD DAC CRS Purpose Codes (5 digit)"),
    )
    OECD_DAC_CRS_PURPOSE_CODES__3_DIGIT_ = (
        2,
        pgettext_lazy("SectorVocabulary", "OECD DAC CRS Purpose Codes (3 digit)"),
    )
    CLASSIFICATION_OF_THE_FUNCTIONS_OF_GOVERNMENT__UN_ = (
        3,
        pgettext_lazy(
            "SectorVocabulary",
            "Classification of the Functions of Government (UN)",
        ),
    )
    STATISTICAL_CLASSIFICATION_OF_ECONOMIC_ACTIVITIES_IN_THE_EUROPEAN_COMMUNITY = (
        4,
        pgettext_lazy(
            "SectorVocabulary",
            "Statistical classification of economic activities in the European Community",
        ),
    )
    NATIONAL_TAXONOMY_FOR_EXEMPT_ENTITIES__USA_ = (
        5,
        pgettext_lazy(
            "SectorVocabulary",
            "National Taxonomy for Exempt Entities (USA)",
        ),
    )
    AIDDATA = (
        6,
        pgettext_lazy("SectorVocabulary", "AidData"),
    )
    SDG_GOAL = (
        7,
        pgettext_lazy("SectorVocabulary", "SDG Goal"),
    )
    SDG_TARGET = (
        8,
        pgettext_lazy("SectorVocabulary", "SDG Target"),
    )
    SDG_INDICATOR = (
        9,
        pgettext_lazy("SectorVocabulary", "SDG Indicator"),
    )
    HUMANITARIAN_GLOBAL_CLUSTERS__INTER_AGENCY_STANDING_COMMITTEE_ = (
        10,
        pgettext_lazy(
            "SectorVocabulary",
            "Humanitarian Global Clusters (Inter-Agency Standing Committee)",
        ),
    )
    NORTH_AMERICAN_INDUSTRY_CLASSIFICATION_SYSTEM__NAICS_ = (
        11,
        pgettext_lazy(
            "SectorVocabulary",
            "North American Industry Classification System (NAICS)",
        ),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy("SectorVocabulary", "Reporting Organisation"),
    )
    REPORTING_ORGANISATION_2 = (
        98,
        pgettext_lazy("SectorVocabulary", "Reporting Organisation 2"),
    )
