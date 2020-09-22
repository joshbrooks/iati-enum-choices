from django.db import models
from django.utils.translation import pgettext_lazy


class SectorCategory(models.IntegerChoices):
    EDUCATION__LEVEL_UNSPECIFIED = (
        111,
        pgettext_lazy("SectorCategory", "Education, Level Unspecified"),
    )
    BASIC_EDUCATION = (
        112,
        pgettext_lazy("SectorCategory", "Basic Education"),
    )
    SECONDARY_EDUCATION = (
        113,
        pgettext_lazy("SectorCategory", "Secondary Education"),
    )
    POST_SECONDARY_EDUCATION = (
        114,
        pgettext_lazy("SectorCategory", "Post-Secondary Education"),
    )
    HEALTH__GENERAL = (
        121,
        pgettext_lazy("SectorCategory", "Health, General"),
    )
    BASIC_HEALTH = (
        122,
        pgettext_lazy("SectorCategory", "Basic Health"),
    )
    NONCOMMUNICABLE_DISEASES__NCDS_ = (
        123,
        pgettext_lazy("SectorCategory", "Non-communicable diseases (NCDs)"),
    )
    POPULATION_POLICIES_PROGRAMMES___REPRODUCTIVE_HEALTH = (
        130,
        pgettext_lazy(
            "SectorCategory",
            "Population Policies/Programmes & Reproductive Health",
        ),
    )
    WATER_SUPPLY___SANITATION = (
        140,
        pgettext_lazy("SectorCategory", "Water Supply & Sanitation"),
    )
    GOVERNMENT___CIVIL_SOCIETY_GENERAL = (
        151,
        pgettext_lazy("SectorCategory", "Government & Civil Society-general"),
    )
    CONFLICT__PEACE___SECURITY = (
        152,
        pgettext_lazy("SectorCategory", "Conflict, Peace & Security"),
    )
    OTHER_SOCIAL_INFRASTRUCTURE___SERVICES = (
        160,
        pgettext_lazy("SectorCategory", "Other Social Infrastructure & Services"),
    )
    TRANSPORT___STORAGE = (
        210,
        pgettext_lazy("SectorCategory", "Transport & Storage"),
    )
    COMMUNICATIONS = (
        220,
        pgettext_lazy("SectorCategory", "Communications"),
    )
    ENERGY_GENERATION_AND_SUPPLY = (
        230,
        pgettext_lazy("SectorCategory", "ENERGY GENERATION AND SUPPLY"),
    )
    ENERGY_POLICY = (
        231,
        pgettext_lazy("SectorCategory", "Energy Policy"),
    )
    ENERGY_GENERATION__RENEWABLE_SOURCES = (
        232,
        pgettext_lazy("SectorCategory", "Energy generation, renewable sources"),
    )
    ENERGY_GENERATION__NON_RENEWABLE_SOURCES = (
        233,
        pgettext_lazy("SectorCategory", "Energy generation, non-renewable sources"),
    )
    HYBRID_ENERGY_PLANTS = (
        234,
        pgettext_lazy("SectorCategory", "Hybrid energy plants"),
    )
    NUCLEAR_ENERGY_PLANTS = (
        235,
        pgettext_lazy("SectorCategory", "Nuclear energy plants"),
    )
    ENERGY_DISTRIBUTION = (
        236,
        pgettext_lazy("SectorCategory", "Energy distribution"),
    )
    BANKING___FINANCIAL_SERVICES = (
        240,
        pgettext_lazy("SectorCategory", "Banking & Financial Services"),
    )
    BUSINESS___OTHER_SERVICES = (
        250,
        pgettext_lazy("SectorCategory", "Business & Other Services"),
    )
    AGRICULTURE = (
        311,
        pgettext_lazy("SectorCategory", "Agriculture"),
    )
    FORESTRY = (
        312,
        pgettext_lazy("SectorCategory", "Forestry"),
    )
    FISHING = (
        313,
        pgettext_lazy("SectorCategory", "Fishing"),
    )
    INDUSTRY = (
        321,
        pgettext_lazy("SectorCategory", "Industry"),
    )
    MINERAL_RESOURCES___MINING = (
        322,
        pgettext_lazy("SectorCategory", "Mineral Resources & Mining"),
    )
    CONSTRUCTION = (
        323,
        pgettext_lazy("SectorCategory", "Construction"),
    )
    TRADE_POLICIES___REGULATIONS = (
        331,
        pgettext_lazy("SectorCategory", "Trade Policies & Regulations"),
    )
    TOURISM = (
        332,
        pgettext_lazy("SectorCategory", "Tourism"),
    )
    GENERAL_ENVIRONMENT_PROTECTION = (
        410,
        pgettext_lazy("SectorCategory", "General Environment Protection"),
    )
    OTHER_MULTISECTOR = (
        430,
        pgettext_lazy("SectorCategory", "Other Multisector"),
    )
    GENERAL_BUDGET_SUPPORT = (
        510,
        pgettext_lazy("SectorCategory", "General Budget Support"),
    )
    DEVELOPMENT_FOOD_ASSISTANCE = (
        520,
        pgettext_lazy("SectorCategory", "Development Food Assistance"),
    )
    OTHER_COMMODITY_ASSISTANCE = (
        530,
        pgettext_lazy("SectorCategory", "Other Commodity Assistance"),
    )
    ACTION_RELATING_TO_DEBT = (
        600,
        pgettext_lazy("SectorCategory", "Action Relating to Debt"),
    )
    EMERGENCY_RESPONSE = (
        720,
        pgettext_lazy("SectorCategory", "Emergency Response"),
    )
    RECONSTRUCTION_RELIEF___REHABILITATION = (
        730,
        pgettext_lazy("SectorCategory", "Reconstruction Relief & Rehabilitation"),
    )
    DISASTER_PREVENTION___PREPAREDNESS = (
        740,
        pgettext_lazy("SectorCategory", "Disaster Prevention & Preparedness"),
    )
    ADMINISTRATIVE_COSTS_OF_DONORS = (
        910,
        pgettext_lazy("SectorCategory", "Administrative Costs of Donors"),
    )
    SUPPORT_TO_NON_GOVERNMENTAL_ORGANISATIONS__NGOS_ = (
        920,
        pgettext_lazy(
            "SectorCategory",
            "SUPPORT TO NON- GOVERNMENTAL ORGANISATIONS (NGOs)",
        ),
    )
    REFUGEES_IN_DONOR_COUNTRIES = (
        930,
        pgettext_lazy("SectorCategory", "Refugees in Donor Countries"),
    )
    UNALLOCATED___UNSPECIFIED = (
        998,
        pgettext_lazy("SectorCategory", "Unallocated / Unspecified"),
    )
