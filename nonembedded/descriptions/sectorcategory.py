from django.db import models
from django.utils.translation import pgettext_lazy


class SectorCategoryDescription(models.IntegerChoices):
    EDUCATION__LEVEL_UNSPECIFIED = (
        111,
        pgettext_lazy(
            "SectorCategory description",
            "The codes in this category are to be used only when level of education is unspecified or unknown (e.g. training of primary school teachers should be coded under 11220).",
        ),
    )
    GOVERNMENT___CIVIL_SOCIETY_GENERAL = (
        151,
        pgettext_lazy(
            "SectorCategory description",
            "N.B. Use code 51010 for general budget support.",
        ),
    )
    CONFLICT__PEACE___SECURITY = (
        152,
        pgettext_lazy(
            "SectorCategory description",
            "N.B. Further notes on ODA eligibility (and exclusions) of conflict, peace and security related activities are given in paragraphs 76-81 of the Directives.",
        ),
    )
    TRANSPORT___STORAGE = (
        210,
        pgettext_lazy(
            "SectorCategory description",
            "Note: Manufacturing of transport equipment should be included under code 32172.",
        ),
    )
    ENERGY_GENERATION_AND_SUPPLY = (
        230,
        pgettext_lazy(
            "SectorCategory description",
            "Energy sector policy, planning and programmes; aid to energy ministries; institution capacity building and advice; unspecified energy activities including energy conservation.",
        ),
    )
    GENERAL_ENVIRONMENT_PROTECTION = (
        410,
        pgettext_lazy(
            "SectorCategory description",
            "Covers activities concerned with conservation, protection or amelioration of the physical environment without sector allocation.",
        ),
    )
    GENERAL_BUDGET_SUPPORT = (
        510,
        pgettext_lazy(
            "SectorCategory description",
            "Budget support in the form of sector-wide approaches (SWAps) should be included in the respective sectors.",
        ),
    )
    OTHER_COMMODITY_ASSISTANCE = (
        530,
        pgettext_lazy(
            "SectorCategory description",
            "Non-food commodity assistance (when benefiting sector not specified).",
        ),
    )
    EMERGENCY_RESPONSE = (
        720,
        pgettext_lazy(
            "SectorCategory description",
            "An emergency is a situation which results from man made crises and/or natural disasters.",
        ),
    )
    RECONSTRUCTION_RELIEF___REHABILITATION = (
        730,
        pgettext_lazy(
            "SectorCategory description",
            "This relates to activities during and in the aftermath of an emergency situation.  Longer-term activities to improve the level of infrastructure or social services should be reported under the relevant economic and social sector codes. See also guideline on distinguishing humanitarian from sector-allocable aid.",
        ),
    )
    DISASTER_PREVENTION___PREPAREDNESS = (
        740,
        pgettext_lazy(
            "SectorCategory description",
            "See code 43060 for disaster risk reduction.",
        ),
    )
    SUPPORT_TO_NON_GOVERNMENTAL_ORGANISATIONS__NGOS_ = (
        920,
        pgettext_lazy("SectorCategory description", "In the donor country."),
    )
    UNALLOCATED___UNSPECIFIED = (
        998,
        pgettext_lazy(
            "SectorCategory description",
            "Contributions to general development of the recipient should be included under programme assistance (51010).",
        ),
    )
