from django.db import models
from django.utils.translation import pgettext_lazy


class BudgetIdentifier(models.TextChoices):
    """
    IATI Functional and Administrative Common Code : One of several possible Budget Identifier Vocabularies. As of version 2.03 this codelist has been deprecated.
    """

    EXECUTIVE_EXECUTIVE = (
        "1.1.1",
        pgettext_lazy("BudgetIdentifier", "Executive - executive"),
    )
    LEGISLATIVE_LEGISLATIVE = (
        "1.2.1",
        pgettext_lazy("BudgetIdentifier", "Legislative - legislative"),
    )
    ACCOUNTABILITY_MACROECONOMIC_POLICY = (
        "1.3.1",
        pgettext_lazy("BudgetIdentifier", "Accountability - macroeconomic policy"),
    )
    ACCOUNTABILITY_BUDGETING = (
        "1.3.2",
        pgettext_lazy("BudgetIdentifier", "Accountability - budgeting"),
    )
    ACCOUNTABILITY_PLANNING = (
        "1.3.3",
        pgettext_lazy("BudgetIdentifier", "Accountability - planning"),
    )
    ACCOUNTABILITY_TREASURY_ACCOUNTS = (
        "1.3.4",
        pgettext_lazy("BudgetIdentifier", "Accountability - Treasury/Accounts"),
    )
    ACCOUNTABILITY_DEBT_AND_AID_MANAGEMENT = (
        "1.3.5",
        pgettext_lazy("BudgetIdentifier", "Accountability - debt and aid management"),
    )
    ACCOUNTABILITY_TAX_POLICY = (
        "1.3.6",
        pgettext_lazy("BudgetIdentifier", "Accountability - tax policy"),
    )
    ACCOUNTABILITY_TAX_COLLECTION = (
        "1.3.7",
        pgettext_lazy("BudgetIdentifier", "Accountability - tax collection"),
    )
    ACCOUNTABILITY_LOCAL_GOVERNMENT_FINANCE = (
        "1.3.8",
        pgettext_lazy(
            "BudgetIdentifier",
            "Accountability - local government finance",
        ),
    )
    ACCOUNTABILITY_OTHER_CENTRAL_TRANSFERS_TO_INSTITUTIONS = (
        "1.3.9",
        pgettext_lazy(
            "BudgetIdentifier",
            "Accountability - other central transfers to institutions ",
        ),
    )
    ACCOUNTABILITY_NATIONAL_AUDIT = (
        "1.3.10",
        pgettext_lazy("BudgetIdentifier", "Accountability - national audit"),
    )
    ACCOUNTABILITY_NATIONAL_MONITORING_AND_EVALUATION = (
        "1.3.11",
        pgettext_lazy(
            "BudgetIdentifier",
            "Accountability - national monitoring and evaluation",
        ),
    )
    ACCOUNTABILITY_MONETARY_INSTITUTIONS = (
        "1.3.12",
        pgettext_lazy("BudgetIdentifier", "Accountability - monetary institutions"),
    )
    ACCOUNTABILITY_FINANCIAL_SECTOR_POLICY_AND_REGULATION = (
        "1.3.13",
        pgettext_lazy(
            "BudgetIdentifier",
            "Accountability - financial sector policy and regulation",
        ),
    )
    EXTERNAL_AFFAIRS_FOREIGN_AFFAIRS = (
        "1.4.1",
        pgettext_lazy("BudgetIdentifier", "External Affairs - foreign affairs "),
    )
    EXTERNAL_AFFAIRS_DIPLOMATIC_MISSIONS = (
        "1.4.2",
        pgettext_lazy("BudgetIdentifier", "External Affairs - diplomatic missions"),
    )
    EXTERNAL_AFFAIRS_OFFICIAL_DEVELOPMENT_ASSISTANCE = (
        "1.4.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "External Affairs - official development assistance",
        ),
    )
    GENERAL_PERSONNEL_SERVICES_GENERAL_PERSONNEL_SERVICES = (
        "1.5.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Personnel Services - general personnel services",
        ),
    )
    STATISTICS_STATISTICS = (
        "1.6.1",
        pgettext_lazy("BudgetIdentifier", "Statistics - statistics"),
    )
    OTHER_GENERAL_SERVICES_SUPPORT_TO_CIVIL_SOCIETY = (
        "1.7.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Other General Services - support to civil society ",
        ),
    )
    OTHER_GENERAL_SERVICES_CENTRAL_PROCUREMENT = (
        "1.7.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Other General Services - central procurement",
        ),
    )
    OTHER_GENERAL_SERVICES_LOCAL_GOVERNMENT_ADMINISTRATION = (
        "1.7.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Other General Services - Local Government Administration",
        ),
    )
    OTHER_GENERAL_SERVICES_OTHER_GENERAL_SERVICES = (
        "1.7.4",
        pgettext_lazy(
            "BudgetIdentifier",
            "Other General Services - other general services",
        ),
    )
    ELECTIONS_ELECTIONS = (
        "1.8.1",
        pgettext_lazy("BudgetIdentifier", "Elections - elections"),
    )
    JUSTICE__LAW_AND_ORDER_POLICY__PLANNING_AND_ADMINISTRATION = (
        "2.1.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Justice, Law and Order - policy, planning and administration",
        ),
    )
    JUSTICE__LAW_AND_ORDER_FIRE_OR_POLICE = (
        "2.1.2",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - fire or police"),
    )
    JUSTICE__LAW_AND_ORDER_JUDICIAL_AFFAIRS = (
        "2.1.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Justice, Law and Order - judicial affairs",
        ),
    )
    JUSTICE__LAW_AND_ORDER_OMBUDSMAN = (
        "2.1.4",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - Ombudsman"),
    )
    JUSTICE__LAW_AND_ORDER_HUMAN_RIGHTS_AFFAIRS = (
        "2.1.5",
        pgettext_lazy(
            "BudgetIdentifier",
            "Justice, Law and Order - human rights affairs",
        ),
    )
    JUSTICE__LAW_AND_ORDER_IMMIGRATION = (
        "2.1.6",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - immigration"),
    )
    JUSTICE__LAW_AND_ORDER_ANTI_CORRUPTION = (
        "2.1.7",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - anti corruption"),
    )
    JUSTICE__LAW_AND_ORDER_PRISONS = (
        "2.1.8",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - prisons"),
    )
    JUSTICE__LAW_AND_ORDER_PEACE_BUILDING = (
        "2.1.9",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - peace building"),
    )
    JUSTICE__LAW_AND_ORDER_DEMOBILISATION = (
        "2.1.10",
        pgettext_lazy("BudgetIdentifier", "Justice, Law and Order - demobilisation"),
    )
    DEFENCE_POLICY__PLANNING_AND_ADMINISTRATION = (
        "2.2.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Defence - policy, planning and administration",
        ),
    )
    DEFENCE_MILITARY = (
        "2.2.2",
        pgettext_lazy("BudgetIdentifier", "Defence - military"),
    )
    DEFENCE_CIVIL_DEFENCE = (
        "2.2.3",
        pgettext_lazy("BudgetIdentifier", "Defence - civil defence"),
    )
    DEFENCE_FOREIGN_MILITARY_AID = (
        "2.2.4",
        pgettext_lazy("BudgetIdentifier", "Defence - foreign military aid"),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.1.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - policy, planning and administration",
        ),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_GENERAL_ECONOMIC_AFFAIRS = (
        "3.1.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - general economic affairs",
        ),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_INVESTMENT_PROMOTION = (
        "3.1.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - investment promotion",
        ),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_PRIVATISATION = (
        "3.1.4",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - privatisation",
        ),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_TRADE = (
        "3.1.5",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - trade",
        ),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_LABOUR = (
        "3.1.6",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - labour",
        ),
    )
    GENERAL_ECONOMIC__COMMERCIAL_AND_LABOUR_AFFAIRS_NATIONAL_STANDARDS_DEVELOPMENT = (
        "3.1.7",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Economic, Commercial and Labour Affairs - national standards development",
        ),
    )
    PUBLIC_WORKS_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.2.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Public Works - policy, planning and administration",
        ),
    )
    PUBLIC_WORKS_CONSTRUCTION_REGULATION = (
        "3.2.2",
        pgettext_lazy("BudgetIdentifier", "Public Works - construction regulation"),
    )
    PUBLIC_WORKS_MECHANICAL_SERVICES = (
        "3.2.3",
        pgettext_lazy("BudgetIdentifier", "Public Works - mechanical services"),
    )
    AGRICULTURE_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.3.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Agriculture - policy, planning and administration",
        ),
    )
    AGRICULTURE_IRRIGATION = (
        "3.3.2",
        pgettext_lazy("BudgetIdentifier", "Agriculture - irrigation"),
    )
    AGRICULTURE_INPUTS = (
        "3.3.3",
        pgettext_lazy("BudgetIdentifier", "Agriculture - inputs"),
    )
    AGRICULTURE_FOOD_CROP = (
        "3.3.4",
        pgettext_lazy("BudgetIdentifier", "Agriculture - food crop"),
    )
    AGRICULTURE_INDUSTRIAL_CROP = (
        "3.3.5",
        pgettext_lazy("BudgetIdentifier", "Agriculture - industrial crop"),
    )
    AGRICULTURE_LIVESTOCK = (
        "3.3.6",
        pgettext_lazy("BudgetIdentifier", "Agriculture - livestock"),
    )
    AGRICULTURE_AGRICULTURAL_TRAINING_AND_EXTENSION = (
        "3.3.7",
        pgettext_lazy(
            "BudgetIdentifier",
            "Agriculture - agricultural training and extension",
        ),
    )
    AGRICULTURE_RESEARCH = (
        "3.3.8",
        pgettext_lazy("BudgetIdentifier", "Agriculture - research"),
    )
    AGRICULTURE_OTHER_SERVICES = (
        "3.3.9",
        pgettext_lazy("BudgetIdentifier", "Agriculture - other services"),
    )
    FORESTRY_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.4.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Forestry - policy, planning and administration",
        ),
    )
    FORESTRY_DEVELOPMENT_AND_SERVICES = (
        "3.4.2",
        pgettext_lazy("BudgetIdentifier", "Forestry - development and services"),
    )
    FORESTRY_EDUCATION_TRAINING = (
        "3.4.3",
        pgettext_lazy("BudgetIdentifier", "Forestry - education/training"),
    )
    FORESTRY_RESEARCH = (
        "3.4.4",
        pgettext_lazy("BudgetIdentifier", "Forestry - research"),
    )
    FISHING_AND_HUNTING_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.5.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Fishing and Hunting - policy, planning and administration",
        ),
    )
    FISHING_AND_HUNTING_DEVELOPMENT_AND_SERVICES = (
        "3.5.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Fishing and Hunting - development and services",
        ),
    )
    FISHING_AND_HUNTING_EDUCATION_AND_TRAINING = (
        "3.5.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Fishing and Hunting - education and training",
        ),
    )
    FISHING_AND_HUNTING_RESEARCH = (
        "3.5.4",
        pgettext_lazy("BudgetIdentifier", "Fishing and Hunting - research"),
    )
    ENERGY_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.6.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Energy - policy, planning and administration",
        ),
    )
    ENERGY_EDUCATION_AND_TRAINING = (
        "3.6.2",
        pgettext_lazy("BudgetIdentifier", "Energy - education and training"),
    )
    ENERGY_ENERGY_REGULATION = (
        "3.6.3",
        pgettext_lazy("BudgetIdentifier", "Energy - energy regulation"),
    )
    ENERGY_ELECTRICITY_TRANSMISSION = (
        "3.6.4",
        pgettext_lazy("BudgetIdentifier", "Energy - electricity transmission"),
    )
    ENERGY_NUCLEAR = (
        "3.6.5",
        pgettext_lazy("BudgetIdentifier", "Energy - nuclear"),
    )
    ENERGY_POWER_GENERATION = (
        "3.6.6",
        pgettext_lazy("BudgetIdentifier", "Energy - power generation"),
    )
    ENERGY_GAS = (
        "3.6.7",
        pgettext_lazy("BudgetIdentifier", "Energy - gas "),
    )
    MINING_AND_MINERAL_DEVELOPMENT_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.7.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Mining and Mineral Development - policy, planning and administration",
        ),
    )
    MINING_AND_MINERAL_DEVELOPMENT_PROSPECTION_AND_EXPLORATION = (
        "3.7.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Mining and Mineral Development - prospection and exploration",
        ),
    )
    MINING_AND_MINERAL_DEVELOPMENT_COAL_AND_OTHER_SOLID_MINERAL_FUELS = (
        "3.7.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Mining and Mineral Development - coal and other solid mineral fuels",
        ),
    )
    MINING_AND_MINERAL_DEVELOPMENT_PETROLEUM_AND_GAS = (
        "3.7.4",
        pgettext_lazy(
            "BudgetIdentifier",
            "Mining and Mineral Development - petroleum and gas",
        ),
    )
    MINING_AND_MINERAL_DEVELOPMENT_OTHER_FUEL = (
        "3.7.6",
        pgettext_lazy(
            "BudgetIdentifier",
            "Mining and Mineral Development - other fuel",
        ),
    )
    MINING_AND_MINERAL_DEVELOPMENT_NON_FUEL_MINERALS = (
        "3.7.7",
        pgettext_lazy(
            "BudgetIdentifier",
            "Mining and Mineral Development - non fuel minerals",
        ),
    )
    TRANSPORT_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.8.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Transport - policy, planning and administration",
        ),
    )
    TRANSPORT_TRANSPORT_REGULATION = (
        "3.8.2",
        pgettext_lazy("BudgetIdentifier", "Transport - transport regulation"),
    )
    TRANSPORT_FEEDER_ROAD_CONSTRUCTION = (
        "3.8.3",
        pgettext_lazy("BudgetIdentifier", "Transport - feeder road construction"),
    )
    TRANSPORT_FEEDER_ROAD_MAINTENANCE = (
        "3.8.4",
        pgettext_lazy("BudgetIdentifier", "Transport - feeder road maintenance"),
    )
    TRANSPORT_NATIONAL_ROAD_CONSTRUCTION = (
        "3.8.5",
        pgettext_lazy("BudgetIdentifier", "Transport - national road construction"),
    )
    TRANSPORT_NATIONAL_ROAD_MAINTENANCE = (
        "3.8.6",
        pgettext_lazy("BudgetIdentifier", "Transport - national road maintenance"),
    )
    TRANSPORT_RAIL = (
        "3.8.7",
        pgettext_lazy("BudgetIdentifier", "Transport - rail"),
    )
    TRANSPORT_WATER = (
        "3.8.8",
        pgettext_lazy("BudgetIdentifier", "Transport - water"),
    )
    TRANSPORT_AIR = (
        "3.8.9",
        pgettext_lazy("BudgetIdentifier", "Transport - air"),
    )
    TRANSPORT_PIPELINE = (
        "3.8.10",
        pgettext_lazy("BudgetIdentifier", "Transport - pipeline"),
    )
    TRANSPORT_STORAGE_AND_DISTRIBUTION = (
        "3.8.11",
        pgettext_lazy("BudgetIdentifier", "Transport - storage and distribution"),
    )
    TRANSPORT_PUBLIC_TRANSPORT_SERVICES = (
        "3.8.12",
        pgettext_lazy("BudgetIdentifier", "Transport - public transport services"),
    )
    TRANSPORT_METEOROLOGICAL_SERVICES = (
        "3.8.13",
        pgettext_lazy("BudgetIdentifier", "Transport - meteorological services"),
    )
    TRANSPORT_EDUCATION_AND_TRAINING = (
        "3.8.14",
        pgettext_lazy("BudgetIdentifier", "Transport - education and training"),
    )
    INDUSTRY_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.9.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Industry - policy, planning and administration",
        ),
    )
    INDUSTRY_DEVELOPMENT_AND_SERVICES = (
        "3.9.2",
        pgettext_lazy("BudgetIdentifier", "Industry - development and services"),
    )
    INDUSTRY_INDUSTRIAL_RESEARCH = (
        "3.9.3",
        pgettext_lazy("BudgetIdentifier", "Industry - industrial research"),
    )
    INDUSTRY__INVESTMENT_IN_INDUSTRY_ = (
        "3.9.4",
        pgettext_lazy("BudgetIdentifier", "Industry - (investment in industry)"),
    )
    COMMUNICATIONS_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.10.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Communications - policy, planning and administration",
        ),
    )
    COMMUNICATIONS_ICT_INFRASTRUCTURE = (
        "3.10.2",
        pgettext_lazy("BudgetIdentifier", "Communications - ICT Infrastructure"),
    )
    COMMUNICATIONS_TELECOMS_AND_POSTAL_SERVICES = (
        "3.10.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Communications - telecoms and postal services",
        ),
    )
    COMMUNICATIONS_INFORMATION_SERVICES = (
        "3.10.4",
        pgettext_lazy("BudgetIdentifier", "Communications - information services"),
    )
    TOURISM_POLICY__PLANNING_AND_ADMINISTRATION = (
        "3.11.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Tourism - policy, planning and administration",
        ),
    )
    TOURISM_SERVICES = (
        "3.11.2",
        pgettext_lazy("BudgetIdentifier", "Tourism - services"),
    )
    MICROFINANCE_AND_FINANCIAL_SERVICES_MICROFINANCE_AND_FINANCIAL_SERVICES = (
        "3.12.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Microfinance and financial services - Microfinance and financial services",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_POLICY__PLANNING_AND_ADMINISTRATION = (
        "4.1.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - policy, planning and administration",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_EDUCATION_TRAINING = (
        "4.1.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - education/training",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_RURAL_WATER_SUPPLY_AND_SANITATION = (
        "4.1.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - rural water supply and sanitation",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_URBAN_WATER_SUPPLY_AND_SANITATION = (
        "4.1.4",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - urban water supply and sanitation",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_RURAL_WATER_SUPPLY = (
        "4.1.5",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - rural water supply",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_URBAN_WATER_SUPPLY = (
        "4.1.6",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - urban water supply",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_RURAL_SANITATION = (
        "4.1.7",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - rural sanitation",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_URBAN_SANITATION = (
        "4.1.8",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - urban sanitation",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_SEWAGE_AND_WASTE_MANAGEMENT = (
        "4.1.9",
        pgettext_lazy(
            "BudgetIdentifier",
            "Water supply and Sanitation - sewage and waste management",
        ),
    )
    ENVIRONMENT_POLICY__PLANNING_AND_ADMINISTRATION = (
        "4.2.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Environment - policy, planning and administration",
        ),
    )
    ENVIRONMENT_RESEARCH__EDUCATION_AND_TRAINING = (
        "4.2.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Environment - research/ education and training",
        ),
    )
    ENVIRONMENT_NATURAL_RESOURCE_MANAGEMENT = (
        "4.2.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Environment - natural resource management",
        ),
    )
    ENVIRONMENT_WATER_RESOURCES_MANAGEMENT = (
        "4.2.4",
        pgettext_lazy("BudgetIdentifier", "Environment - water resources management"),
    )
    ENVIRONMENT_WILDLIFE_PROTECTION__PARKS_AND_SITE_PRESERVATION = (
        "4.2.5",
        pgettext_lazy(
            "BudgetIdentifier",
            "Environment - wildlife protection, parks and site preservation",
        ),
    )
    HEALTH_POLICY__PLANNING_AND_ADMINISTRATION = (
        "5.1.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Health - policy, planning and administration",
        ),
    )
    RECREATION__CULTURE_AND_RELIGION_RECREATION_AND_SPORT = (
        "5.2.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Recreation, Culture and Religion - recreation and sport",
        ),
    )
    RECREATION__CULTURE_AND_RELIGION_CULTURE = (
        "5.2.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Recreation, Culture and Religion - culture",
        ),
    )
    RECREATION__CULTURE_AND_RELIGION_BROADCASTING_AND_PUBLISHING = (
        "5.2.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Recreation, Culture and Religion - broadcasting and publishing",
        ),
    )
    RECREATION__CULTURE_AND_RELIGION_RELIGION = (
        "5.2.4",
        pgettext_lazy(
            "BudgetIdentifier",
            "Recreation, Culture and Religion - religion",
        ),
    )
    EDUCATION_ADMINISTRATION__POLICY_AND_PLANNING = (
        "5.3.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Education - administration, policy and planning",
        ),
    )
    EDUCATION_RESEARCH = (
        "5.3.2",
        pgettext_lazy("BudgetIdentifier", "Education - research"),
    )
    EDUCATION_PRE_PRIMARY = (
        "5.3.3",
        pgettext_lazy("BudgetIdentifier", "Education - pre-primary"),
    )
    EDUCATION_PRIMARY = (
        "5.3.4",
        pgettext_lazy("BudgetIdentifier", "Education - primary"),
    )
    EDUCATION_LOWER_SECONDARY = (
        "5.3.5",
        pgettext_lazy("BudgetIdentifier", "Education - lower secondary"),
    )
    EDUCATION_UPPER_SECONDARY = (
        "5.3.6",
        pgettext_lazy("BudgetIdentifier", "Education - upper secondary"),
    )
    EDUCATION_POST_SECONDARY_NON_TERTIARY = (
        "5.3.7",
        pgettext_lazy("BudgetIdentifier", "Education - post secondary non tertiary "),
    )
    EDUCATION_TERTIARY = (
        "5.3.8",
        pgettext_lazy("BudgetIdentifier", "Education - tertiary"),
    )
    EDUCATION_VOCATIONAL_TRAINING = (
        "5.3.9",
        pgettext_lazy("BudgetIdentifier", "Education - vocational training"),
    )
    EDUCATION_ADVANCED_TECHNICAL_AND_MANAGERIAL_TRAINING = (
        "5.3.10",
        pgettext_lazy(
            "BudgetIdentifier",
            "Education - advanced technical and managerial training",
        ),
    )
    EDUCATION_BASIC_ADULT_EDUCATION = (
        "5.3.11",
        pgettext_lazy("BudgetIdentifier", "Education - basic adult education"),
    )
    EDUCATION_TEACHER_TRAINING = (
        "5.3.12",
        pgettext_lazy("BudgetIdentifier", "Education - teacher training"),
    )
    EDUCATION_SUBSIDIARY_SERVICES = (
        "5.3.13",
        pgettext_lazy("BudgetIdentifier", "Education - subsidiary services"),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_POLICY__PLANNING_AND_ADMINISTRATION = (
        "5.4.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - policy, planning and administration",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_SOCIAL_SECURITY__EXCL_PENSIONS_ = (
        "5.4.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - social security (excl pensions)",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_GENERAL_PENSIONS = (
        "5.4.3",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - general pensions",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_CIVIL_SERVICE_AND_MILITARY_PENSIONS = (
        "5.4.4",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - civil service and military pensions",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_SOCIAL_SERVICES__INCL_YOUTH_DEVELOPMENT_AND_WOMEN__CHILDREN_ = (
        "5.4.5",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - social services (incl youth development and women+ children)",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_LAND_POLICY_AND_MANAGEMENT = (
        "5.4.6",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - land policy and management",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_RURAL_DEVT = (
        "5.4.7",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - rural devt",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_URBAN_DEVT = (
        "5.4.8",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - urban devt",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_HOUSING_AND_COMMUNITY_AMENITIES = (
        "5.4.9",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - housing and community amenities",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_EMERGENCY_RELIEF = (
        "5.4.10",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - emergency relief",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_DISASTER_PREVENTION_AND_PREPAREDNESS = (
        "5.4.11",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - disaster prevention and preparedness",
        ),
    )
    SOCIAL_PROTECTION__LAND_HOUSING_AND_COMMUNITY_AMENITIES_SUPPORT_TO_REFUGEES_AND_INTERNALLY_DISPLACED_PERSONS = (
        "5.4.12",
        pgettext_lazy(
            "BudgetIdentifier",
            "Social Protection, Land Housing and Community Amenities - support to refugees and internally displaced persons",
        ),
    )
    DEVELOPMENT_PARTNER_AFFAIRS_POLICY_PLANNING_AND_ADMINISTRATION = (
        "6.1.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "Development Partner affairs - policy planning and administration",
        ),
    )
    DEVELOPMENT_PARTNER_AFFAIRS_TECHNICAL_STAFF_SERVICES = (
        "6.1.2",
        pgettext_lazy(
            "BudgetIdentifier",
            "Development Partner affairs - Technical staff services",
        ),
    )
    EXTERNAL_TO_GOVERNMENT_SECTOR_EXTERNAL_TO_GENERAL_GOVERNMENT_SECTOR = (
        "7.1.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "External to government sector - External to general government sector",
        ),
    )
    GENERAL_BUDGET_SUPPORT_GENERAL_BUDGET_SUPPORT = (
        "7.2.1",
        pgettext_lazy(
            "BudgetIdentifier",
            "General Budget Support - General Budget Support",
        ),
    )
