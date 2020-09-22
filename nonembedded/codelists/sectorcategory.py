from django.db import models
from django.utils.translation import pgettext_lazy


class SectorCategory(models.IntegerChoices):
    EDUCATION__LEVEL_UNSPECIFIED = (
        111,
        pgettext_lazy("IATI codelist SectorCategory", "Education, Level Unspecified"),
    )
    BASIC_EDUCATION = (
        112,
        pgettext_lazy("IATI codelist SectorCategory", "Basic Education"),
    )
    SECONDARY_EDUCATION = (
        113,
        pgettext_lazy("IATI codelist SectorCategory", "Secondary Education"),
    )
    POST_SECONDARY_EDUCATION = (
        114,
        pgettext_lazy("IATI codelist SectorCategory", "Post-Secondary Education"),
    )
    HEALTH__GENERAL = (
        121,
        pgettext_lazy("IATI codelist SectorCategory", "Health, General"),
    )
    BASIC_HEALTH = (
        122,
        pgettext_lazy("IATI codelist SectorCategory", "Basic Health"),
    )
    NONCOMMUNICABLE_DISEASES__NCDS_ = (
        123,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Non-communicable diseases (NCDs)"
        ),
    )
    POPULATION_POLICIES_PROGRAMMES___REPRODUCTIVE_HEALTH = (
        130,
        pgettext_lazy(
            "IATI codelist SectorCategory",
            "Population Policies/Programmes & Reproductive Health",
        ),
    )
    WATER_SUPPLY___SANITATION = (
        140,
        pgettext_lazy("IATI codelist SectorCategory", "Water Supply & Sanitation"),
    )
    GOVERNMENT___CIVIL_SOCIETY_GENERAL = (
        151,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Government & Civil Society-general"
        ),
    )
    CONFLICT__PEACE___SECURITY = (
        152,
        pgettext_lazy("IATI codelist SectorCategory", "Conflict, Peace & Security"),
    )
    OTHER_SOCIAL_INFRASTRUCTURE___SERVICES = (
        160,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Other Social Infrastructure & Services"
        ),
    )
    TRANSPORT___STORAGE = (
        210,
        pgettext_lazy("IATI codelist SectorCategory", "Transport & Storage"),
    )
    COMMUNICATIONS = (
        220,
        pgettext_lazy("IATI codelist SectorCategory", "Communications"),
    )
    ENERGY_GENERATION_AND_SUPPLY = (
        230,
        pgettext_lazy("IATI codelist SectorCategory", "ENERGY GENERATION AND SUPPLY"),
    )
    ENERGY_POLICY = (
        231,
        pgettext_lazy("IATI codelist SectorCategory", "Energy Policy"),
    )
    ENERGY_GENERATION__RENEWABLE_SOURCES = (
        232,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Energy generation, renewable sources"
        ),
    )
    ENERGY_GENERATION__NON_RENEWABLE_SOURCES = (
        233,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Energy generation, non-renewable sources"
        ),
    )
    HYBRID_ENERGY_PLANTS = (
        234,
        pgettext_lazy("IATI codelist SectorCategory", "Hybrid energy plants"),
    )
    NUCLEAR_ENERGY_PLANTS = (
        235,
        pgettext_lazy("IATI codelist SectorCategory", "Nuclear energy plants"),
    )
    ENERGY_DISTRIBUTION = (
        236,
        pgettext_lazy("IATI codelist SectorCategory", "Energy distribution"),
    )
    BANKING___FINANCIAL_SERVICES = (
        240,
        pgettext_lazy("IATI codelist SectorCategory", "Banking & Financial Services"),
    )
    BUSINESS___OTHER_SERVICES = (
        250,
        pgettext_lazy("IATI codelist SectorCategory", "Business & Other Services"),
    )
    AGRICULTURE = (
        311,
        pgettext_lazy("IATI codelist SectorCategory", "Agriculture"),
    )
    FORESTRY = (
        312,
        pgettext_lazy("IATI codelist SectorCategory", "Forestry"),
    )
    FISHING = (
        313,
        pgettext_lazy("IATI codelist SectorCategory", "Fishing"),
    )
    INDUSTRY = (
        321,
        pgettext_lazy("IATI codelist SectorCategory", "Industry"),
    )
    MINERAL_RESOURCES___MINING = (
        322,
        pgettext_lazy("IATI codelist SectorCategory", "Mineral Resources & Mining"),
    )
    CONSTRUCTION = (
        323,
        pgettext_lazy("IATI codelist SectorCategory", "Construction"),
    )
    TRADE_POLICIES___REGULATIONS = (
        331,
        pgettext_lazy("IATI codelist SectorCategory", "Trade Policies & Regulations"),
    )
    TOURISM = (
        332,
        pgettext_lazy("IATI codelist SectorCategory", "Tourism"),
    )
    GENERAL_ENVIRONMENT_PROTECTION = (
        410,
        pgettext_lazy("IATI codelist SectorCategory", "General Environment Protection"),
    )
    OTHER_MULTISECTOR = (
        430,
        pgettext_lazy("IATI codelist SectorCategory", "Other Multisector"),
    )
    GENERAL_BUDGET_SUPPORT = (
        510,
        pgettext_lazy("IATI codelist SectorCategory", "General Budget Support"),
    )
    DEVELOPMENT_FOOD_ASSISTANCE = (
        520,
        pgettext_lazy("IATI codelist SectorCategory", "Development Food Assistance"),
    )
    OTHER_COMMODITY_ASSISTANCE = (
        530,
        pgettext_lazy("IATI codelist SectorCategory", "Other Commodity Assistance"),
    )
    ACTION_RELATING_TO_DEBT = (
        600,
        pgettext_lazy("IATI codelist SectorCategory", "Action Relating to Debt"),
    )
    EMERGENCY_RESPONSE = (
        720,
        pgettext_lazy("IATI codelist SectorCategory", "Emergency Response"),
    )
    RECONSTRUCTION_RELIEF___REHABILITATION = (
        730,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Reconstruction Relief & Rehabilitation"
        ),
    )
    DISASTER_PREVENTION___PREPAREDNESS = (
        740,
        pgettext_lazy(
            "IATI codelist SectorCategory", "Disaster Prevention & Preparedness"
        ),
    )
    ADMINISTRATIVE_COSTS_OF_DONORS = (
        910,
        pgettext_lazy("IATI codelist SectorCategory", "Administrative Costs of Donors"),
    )
    SUPPORT_TO_NON_GOVERNMENTAL_ORGANISATIONS__NGOS_ = (
        920,
        pgettext_lazy(
            "IATI codelist SectorCategory",
            "SUPPORT TO NON- GOVERNMENTAL ORGANISATIONS (NGOs)",
        ),
    )
    REFUGEES_IN_DONOR_COUNTRIES = (
        930,
        pgettext_lazy("IATI codelist SectorCategory", "Refugees in Donor Countries"),
    )
    UNALLOCATED___UNSPECIFIED = (
        998,
        pgettext_lazy("IATI codelist SectorCategory", "Unallocated / Unspecified"),
    )
