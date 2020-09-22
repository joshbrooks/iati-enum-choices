from django.db import models
from django.utils.translation import pgettext_lazy


class SectorVocabularyDescription(models.IntegerChoices):
    OECD_DAC_CRS_PURPOSE_CODES__5_DIGIT_ = (
        1,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to an OECD DAC CRS 5-digit purpose code",
        ),
    )
    OECD_DAC_CRS_PURPOSE_CODES__3_DIGIT_ = (
        2,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to an OECD DAC CRS 3-digit purpose code",
        ),
    )
    CLASSIFICATION_OF_THE_FUNCTIONS_OF_GOVERNMENT__UN_ = (
        3,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to the UN Classification of the Functions of Government (CoFoG)",
        ),
    )
    STATISTICAL_CLASSIFICATION_OF_ECONOMIC_ACTIVITIES_IN_THE_EUROPEAN_COMMUNITY = (
        4,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to the statistical classifications of economic activities in the European Community",
        ),
    )
    NATIONAL_TAXONOMY_FOR_EXEMPT_ENTITIES__USA_ = (
        5,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to the National Taxonomy for Exempt Entities (NTEE) - USA",
        ),
    )
    AIDDATA = (
        6,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to AidData classifications",
        ),
    )
    SDG_GOAL = (
        7,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "A value from the top-level list of UN sustainable development goals (SDGs) (e.g. ‘1’)",
        ),
    )
    SDG_TARGET = (
        8,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "A value from the second-level list of UN sustainable development goals (SDGs) (e.g. ‘1.1’)",
        ),
    )
    SDG_INDICATOR = (
        9,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "A value from the second-level list of UN sustainable development (SDG) indicators",
        ),
    )
    HUMANITARIAN_GLOBAL_CLUSTERS__INTER_AGENCY_STANDING_COMMITTEE_ = (
        10,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to an Inter-Agency Standard Committee Humanitarian Global Cluster code",
        ),
    )
    NORTH_AMERICAN_INDUSTRY_CLASSIFICATION_SYSTEM__NAICS_ = (
        11,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to the NAICS codelist",
        ),
    )
    REPORTING_ORGANISATION = (
        99,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to a sector vocabulary maintained by the reporting organisation for this activity",
        ),
    )
    REPORTING_ORGANISATION_2 = (
        98,
        pgettext_lazy(
            "IATI codelist SectorVocabulary description",
            "The sector reported corresponds to a sector vocabulary maintained by the reporting organisation for this activity (if they are referencing more than one)",
        ),
    )
