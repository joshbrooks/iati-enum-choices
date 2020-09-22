from django.db import models
from django.utils.translation import pgettext_lazy


class Sector(models.IntegerChoices):
    EDUCATION_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        11110,
        pgettext_lazy(
            "IATI codelist Sector", "Education policy and administrative management"
        ),
    )
    EDUCATION_FACILITIES_AND_TRAINING = (
        11120,
        pgettext_lazy("IATI codelist Sector", "Education facilities and training"),
    )
    TEACHER_TRAINING = (
        11130,
        pgettext_lazy("IATI codelist Sector", "Teacher training"),
    )
    EDUCATIONAL_RESEARCH = (
        11182,
        pgettext_lazy("IATI codelist Sector", "Educational research"),
    )
    PRIMARY_EDUCATION = (
        11220,
        pgettext_lazy("IATI codelist Sector", "Primary education"),
    )
    BASIC_LIFE_SKILLS_FOR_YOUTH_AND_ADULTS = (
        11230,
        pgettext_lazy("IATI codelist Sector", "Basic life skills for youth and adults"),
    )
    BASIC_LIFE_SKILLS_FOR_YOUTH = (
        11231,
        pgettext_lazy("IATI codelist Sector", "Basic life skills for youth"),
    )
    PRIMARY_EDUCATION_EQUIVALENT_FOR_ADULTS = (
        11232,
        pgettext_lazy(
            "IATI codelist Sector", "Primary education equivalent for adults"
        ),
    )
    EARLY_CHILDHOOD_EDUCATION = (
        11240,
        pgettext_lazy("IATI codelist Sector", "Early childhood education"),
    )
    SCHOOL_FEEDING = (
        11250,
        pgettext_lazy("IATI codelist Sector", "School feeding"),
    )
    SECONDARY_EDUCATION = (
        11320,
        pgettext_lazy("IATI codelist Sector", "Secondary education"),
    )
    LOWER_SECONDARY_EDUCATION = (
        11321,
        pgettext_lazy("IATI codelist Sector", "Lower secondary education"),
    )
    UPPER_SECONDARY_EDUCATION = (
        11322,
        pgettext_lazy("IATI codelist Sector", "Upper secondary education"),
    )
    VOCATIONAL_TRAINING = (
        11330,
        pgettext_lazy("IATI codelist Sector", "Vocational training"),
    )
    HIGHER_EDUCATION = (
        11420,
        pgettext_lazy("IATI codelist Sector", "Higher education"),
    )
    ADVANCED_TECHNICAL_AND_MANAGERIAL_TRAINING = (
        11430,
        pgettext_lazy(
            "IATI codelist Sector", "Advanced technical and managerial training"
        ),
    )
    HEALTH_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        12110,
        pgettext_lazy(
            "IATI codelist Sector", "Health policy and administrative management"
        ),
    )
    MEDICAL_EDUCATION_TRAINING = (
        12181,
        pgettext_lazy("IATI codelist Sector", "Medical education/training"),
    )
    MEDICAL_RESEARCH = (
        12182,
        pgettext_lazy("IATI codelist Sector", "Medical research"),
    )
    MEDICAL_SERVICES = (
        12191,
        pgettext_lazy("IATI codelist Sector", "Medical services"),
    )
    HEALTH_STATISTICS_AND_DATA = (
        12196,
        pgettext_lazy("IATI codelist Sector", "Health statistics and data"),
    )
    BASIC_HEALTH_CARE = (
        12220,
        pgettext_lazy("IATI codelist Sector", "Basic health care"),
    )
    BASIC_HEALTH_INFRASTRUCTURE = (
        12230,
        pgettext_lazy("IATI codelist Sector", "Basic health infrastructure"),
    )
    BASIC_NUTRITION = (
        12240,
        pgettext_lazy("IATI codelist Sector", "Basic nutrition"),
    )
    INFECTIOUS_DISEASE_CONTROL = (
        12250,
        pgettext_lazy("IATI codelist Sector", "Infectious disease control"),
    )
    HEALTH_EDUCATION = (
        12261,
        pgettext_lazy("IATI codelist Sector", "Health education"),
    )
    MALARIA_CONTROL = (
        12262,
        pgettext_lazy("IATI codelist Sector", "Malaria control"),
    )
    TUBERCULOSIS_CONTROL = (
        12263,
        pgettext_lazy("IATI codelist Sector", "Tuberculosis control"),
    )
    HEALTH_PERSONNEL_DEVELOPMENT = (
        12281,
        pgettext_lazy("IATI codelist Sector", "Health personnel development"),
    )
    NCDS_CONTROL__GENERAL = (
        12310,
        pgettext_lazy("IATI codelist Sector", "NCDs control, general"),
    )
    TOBACCO_USE_CONTROL = (
        12320,
        pgettext_lazy("IATI codelist Sector", "Tobacco use control"),
    )
    CONTROL_OF_HARMFUL_USE_OF_ALCOHOL_AND_DRUGS = (
        12330,
        pgettext_lazy(
            "IATI codelist Sector", "Control of harmful use of alcohol and drugs"
        ),
    )
    PROMOTION_OF_MENTAL_HEALTH_AND_WELL_BEING = (
        12340,
        pgettext_lazy(
            "IATI codelist Sector", "Promotion of mental health and well-being"
        ),
    )
    OTHER_PREVENTION_AND_TREATMENT_OF_NCDS = (
        12350,
        pgettext_lazy("IATI codelist Sector", "Other prevention and treatment of NCDs"),
    )
    RESEARCH_FOR_PREVENTION_AND_CONTROL_OF_NCDS = (
        12382,
        pgettext_lazy(
            "IATI codelist Sector", "Research for prevention and control of NCDs"
        ),
    )
    POPULATION_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        13010,
        pgettext_lazy(
            "IATI codelist Sector", "Population policy and administrative management"
        ),
    )
    REPRODUCTIVE_HEALTH_CARE = (
        13020,
        pgettext_lazy("IATI codelist Sector", "Reproductive health care"),
    )
    FAMILY_PLANNING = (
        13030,
        pgettext_lazy("IATI codelist Sector", "Family planning"),
    )
    STD_CONTROL_INCLUDING_HIV_AIDS = (
        13040,
        pgettext_lazy("IATI codelist Sector", "STD control including HIV/AIDS"),
    )
    PERSONNEL_DEVELOPMENT_FOR_POPULATION_AND_REPRODUCTIVE_HEALTH = (
        13081,
        pgettext_lazy(
            "IATI codelist Sector",
            "Personnel development for population and reproductive health",
        ),
    )
    POPULATION_STATISTICS_AND_DATA = (
        13096,
        pgettext_lazy("IATI codelist Sector", "Population statistics and data"),
    )
    WATER_SECTOR_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        14010,
        pgettext_lazy(
            "IATI codelist Sector", "Water sector policy and administrative management"
        ),
    )
    WATER_RESOURCES_CONSERVATION__INCLUDING_DATA_COLLECTION_ = (
        14015,
        pgettext_lazy(
            "IATI codelist Sector",
            "Water resources conservation (including data collection)",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_LARGE_SYSTEMS = (
        14020,
        pgettext_lazy(
            "IATI codelist Sector", "Water supply and sanitation - large systems"
        ),
    )
    WATER_SUPPLY_LARGE_SYSTEMS = (
        14021,
        pgettext_lazy("IATI codelist Sector", "Water supply - large systems"),
    )
    SANITATION_LARGE_SYSTEMS = (
        14022,
        pgettext_lazy("IATI codelist Sector", "Sanitation - large systems"),
    )
    BASIC_DRINKING_WATER_SUPPLY_AND_BASIC_SANITATION = (
        14030,
        pgettext_lazy(
            "IATI codelist Sector", "Basic drinking water supply and basic sanitation"
        ),
    )
    BASIC_DRINKING_WATER_SUPPLY = (
        14031,
        pgettext_lazy("IATI codelist Sector", "Basic drinking water supply"),
    )
    BASIC_SANITATION = (
        14032,
        pgettext_lazy("IATI codelist Sector", "Basic sanitation"),
    )
    RIVER_BASINS_DEVELOPMENT = (
        14040,
        pgettext_lazy("IATI codelist Sector", "River basins development"),
    )
    WASTE_MANAGEMENT_DISPOSAL = (
        14050,
        pgettext_lazy("IATI codelist Sector", "Waste management/disposal"),
    )
    EDUCATION_AND_TRAINING_IN_WATER_SUPPLY_AND_SANITATION = (
        14081,
        pgettext_lazy(
            "IATI codelist Sector",
            "Education and training in water supply and sanitation",
        ),
    )
    PUBLIC_SECTOR_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        15110,
        pgettext_lazy(
            "IATI codelist Sector", "Public sector policy and administrative management"
        ),
    )
    PUBLIC_FINANCE_MANAGEMENT__PFM_ = (
        15111,
        pgettext_lazy("IATI codelist Sector", "Public finance management (PFM)"),
    )
    DECENTRALISATION_AND_SUPPORT_TO_SUBNATIONAL_GOVERNMENT = (
        15112,
        pgettext_lazy(
            "IATI codelist Sector",
            "Decentralisation and support to subnational government",
        ),
    )
    ANTICORRUPTION_ORGANISATIONS_AND_INSTITUTIONS = (
        15113,
        pgettext_lazy(
            "IATI codelist Sector", "Anti-corruption organisations and institutions"
        ),
    )
    DOMESTIC_REVENUE_MOBILISATION = (
        15114,
        pgettext_lazy("IATI codelist Sector", "Domestic revenue mobilisation"),
    )
    TAX_COLLECTION = (
        15116,
        pgettext_lazy("IATI codelist Sector", "Tax collection"),
    )
    BUDGET_PLANNING = (
        15117,
        pgettext_lazy("IATI codelist Sector", "Budget planning"),
    )
    NATIONAL_AUDIT = (
        15118,
        pgettext_lazy("IATI codelist Sector", "National audit"),
    )
    DEBT_AND_AID_MANAGEMENT = (
        15119,
        pgettext_lazy("IATI codelist Sector", "Debt and aid management"),
    )
    PUBLIC_SECTOR_FINANCIAL_MANAGEMENT = (
        15120,
        pgettext_lazy("IATI codelist Sector", "Public sector financial management"),
    )
    FOREIGN_AFFAIRS = (
        15121,
        pgettext_lazy("IATI codelist Sector", "Foreign affairs"),
    )
    DIPLOMATIC_MISSIONS = (
        15122,
        pgettext_lazy("IATI codelist Sector", "Diplomatic missions"),
    )
    ADMINISTRATION_OF_DEVELOPING_COUNTRIES__FOREIGN_AID = (
        15123,
        pgettext_lazy(
            "IATI codelist Sector",
            "Administration of developing countries' foreign aid",
        ),
    )
    GENERAL_PERSONNEL_SERVICES = (
        15124,
        pgettext_lazy("IATI codelist Sector", "General personnel services"),
    )
    PUBLIC_PROCUREMENT = (
        15125,
        pgettext_lazy("IATI codelist Sector", "Public Procurement"),
    )
    OTHER_GENERAL_PUBLIC_SERVICES = (
        15126,
        pgettext_lazy("IATI codelist Sector", "Other general public services"),
    )
    NATIONAL_MONITORING_AND_EVALUATION = (
        15127,
        pgettext_lazy("IATI codelist Sector", "National monitoring and evaluation"),
    )
    LOCAL_GOVERNMENT_FINANCE = (
        15128,
        pgettext_lazy("IATI codelist Sector", "Local government finance"),
    )
    OTHER_CENTRAL_TRANSFERS_TO_INSTITUTIONS = (
        15129,
        pgettext_lazy(
            "IATI codelist Sector", "Other central transfers to institutions"
        ),
    )
    LEGAL_AND_JUDICIAL_DEVELOPMENT = (
        15130,
        pgettext_lazy("IATI codelist Sector", "Legal and judicial development"),
    )
    JUSTICE__LAW_AND_ORDER_POLICY__PLANNING_AND_ADMINISTRATION = (
        15131,
        pgettext_lazy(
            "IATI codelist Sector",
            "Justice, law and order policy, planning and administration",
        ),
    )
    POLICE = (
        15132,
        pgettext_lazy("IATI codelist Sector", "Police"),
    )
    FIRE_AND_RESCUE_SERVICES = (
        15133,
        pgettext_lazy("IATI codelist Sector", "Fire and rescue services"),
    )
    JUDICIAL_AFFAIRS = (
        15134,
        pgettext_lazy("IATI codelist Sector", "Judicial affairs"),
    )
    OMBUDSMAN = (
        15135,
        pgettext_lazy("IATI codelist Sector", "Ombudsman"),
    )
    IMMIGRATION = (
        15136,
        pgettext_lazy("IATI codelist Sector", "Immigration"),
    )
    PRISONS = (
        15137,
        pgettext_lazy("IATI codelist Sector", "Prisons"),
    )
    GOVERNMENT_ADMINISTRATION = (
        15140,
        pgettext_lazy("IATI codelist Sector", "Government administration"),
    )
    MACROECONOMIC_POLICY = (
        15142,
        pgettext_lazy("IATI codelist Sector", "Macroeconomic policy"),
    )
    METEOROLOGICAL_SERVICES = (
        15143,
        pgettext_lazy("IATI codelist Sector", "Meteorological services"),
    )
    NATIONAL_STANDARDS_DEVELOPMENT = (
        15144,
        pgettext_lazy("IATI codelist Sector", "National standards development"),
    )
    DEMOCRATIC_PARTICIPATION_AND_CIVIL_SOCIETY = (
        15150,
        pgettext_lazy(
            "IATI codelist Sector", "Democratic participation and civil society"
        ),
    )
    ELECTIONS = (
        15151,
        pgettext_lazy("IATI codelist Sector", "Elections"),
    )
    LEGISLATURES_AND_POLITICAL_PARTIES = (
        15152,
        pgettext_lazy("IATI codelist Sector", "Legislatures and political parties"),
    )
    MEDIA_AND_FREE_FLOW_OF_INFORMATION = (
        15153,
        pgettext_lazy("IATI codelist Sector", "Media and free flow of information"),
    )
    EXECUTIVE_OFFICE = (
        15154,
        pgettext_lazy("IATI codelist Sector", "Executive office"),
    )
    TAX_POLICY_AND_ADMINISTRATION_SUPPORT = (
        15155,
        pgettext_lazy("IATI codelist Sector", "Tax policy and administration support"),
    )
    OTHER_NON_TAX_REVENUE_MOBILISATION = (
        15156,
        pgettext_lazy("IATI codelist Sector", "Other non-tax revenue mobilisation"),
    )
    HUMAN_RIGHTS = (
        15160,
        pgettext_lazy("IATI codelist Sector", "Human rights"),
    )
    ELECTIONS = (
        15161,
        pgettext_lazy("IATI codelist Sector", "Elections"),
    )
    HUMAN_RIGHTS = (
        15162,
        pgettext_lazy("IATI codelist Sector", "Human rights"),
    )
    FREE_FLOW_OF_INFORMATION = (
        15163,
        pgettext_lazy("IATI codelist Sector", "Free flow of information"),
    )
    WOMEN_S_EQUALITY_ORGANISATIONS_AND_INSTITUTIONS = (
        15164,
        pgettext_lazy(
            "IATI codelist Sector", "Women's equality organisations and institutions"
        ),
    )
    WOMEN_S_RIGHTS_ORGANISATIONS_AND_MOVEMENTS__AND_GOVERNMENT_INSTITUTIONS = (
        15170,
        pgettext_lazy(
            "IATI codelist Sector",
            "Women’s rights organisations and movements, and government institutions",
        ),
    )
    ENDING_VIOLENCE_AGAINST_WOMEN_AND_GIRLS = (
        15180,
        pgettext_lazy(
            "IATI codelist Sector", "Ending violence against women and girls"
        ),
    )
    LOCAL_GOVERNMENT_ADMINISTRATION = (
        15185,
        pgettext_lazy("IATI codelist Sector", "Local government administration"),
    )
    FACILITATION_OF_ORDERLY__SAFE__REGULAR_AND_RESPONSIBLE_MIGRATION_AND_MOBILITY = (
        15190,
        pgettext_lazy(
            "IATI codelist Sector",
            "Facilitation of orderly, safe, regular and responsible migration and mobility",
        ),
    )
    GOVERNMENT_AND_CIVIL_SOCIETY_STATISTICS_AND_DATA = (
        15196,
        pgettext_lazy(
            "IATI codelist Sector", "Government and civil society statistics and data"
        ),
    )
    SECURITY_SYSTEM_MANAGEMENT_AND_REFORM = (
        15210,
        pgettext_lazy("IATI codelist Sector", "Security system management and reform"),
    )
    CIVILIAN_PEACE_BUILDING__CONFLICT_PREVENTION_AND_RESOLUTION = (
        15220,
        pgettext_lazy(
            "IATI codelist Sector",
            "Civilian peace-building, conflict prevention and resolution",
        ),
    )
    PARTICIPATION_IN_INTERNATIONAL_PEACEKEEPING_OPERATIONS = (
        15230,
        pgettext_lazy(
            "IATI codelist Sector",
            "Participation in international peacekeeping operations",
        ),
    )
    REINTEGRATION_AND_SALW_CONTROL = (
        15240,
        pgettext_lazy("IATI codelist Sector", "Reintegration and SALW control"),
    )
    REMOVAL_OF_LAND_MINES_AND_EXPLOSIVE_REMNANTS_OF_WAR = (
        15250,
        pgettext_lazy(
            "IATI codelist Sector",
            "Removal of land mines and explosive remnants of war",
        ),
    )
    CHILD_SOLDIERS__PREVENTION_AND_DEMOBILISATION_ = (
        15261,
        pgettext_lazy(
            "IATI codelist Sector", "Child soldiers (prevention and demobilisation)"
        ),
    )
    SOCIAL_PROTECTION = (
        16010,
        pgettext_lazy("IATI codelist Sector", "Social Protection"),
    )
    SOCIAL_PROTECTION_AND_WELFARE_SERVICES_POLICY__PLANNING_AND_ADMINISTRATION = (
        16011,
        pgettext_lazy(
            "IATI codelist Sector",
            "Social protection and welfare services policy, planning and administration",
        ),
    )
    SOCIAL_SECURITY__EXCL_PENSIONS_ = (
        16012,
        pgettext_lazy("IATI codelist Sector", "Social security (excl pensions)"),
    )
    GENERAL_PENSIONS = (
        16013,
        pgettext_lazy("IATI codelist Sector", "General pensions"),
    )
    CIVIL_SERVICE_PENSIONS = (
        16014,
        pgettext_lazy("IATI codelist Sector", "Civil service pensions"),
    )
    SOCIAL_SERVICES__INCL_YOUTH_DEVELOPMENT_AND_WOMEN__CHILDREN_ = (
        16015,
        pgettext_lazy(
            "IATI codelist Sector",
            "Social services (incl youth development and women+ children)",
        ),
    )
    EMPLOYMENT_CREATION = (
        16020,
        pgettext_lazy("IATI codelist Sector", "Employment creation"),
    )
    HOUSING_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        16030,
        pgettext_lazy(
            "IATI codelist Sector", "Housing policy and administrative management"
        ),
    )
    LOWCOST_HOUSING = (
        16040,
        pgettext_lazy("IATI codelist Sector", "Low-cost housing"),
    )
    MULTISECTOR_AID_FOR_BASIC_SOCIAL_SERVICES = (
        16050,
        pgettext_lazy(
            "IATI codelist Sector", "Multisector aid for basic social services"
        ),
    )
    CULTURE_AND_RECREATION = (
        16061,
        pgettext_lazy("IATI codelist Sector", "Culture and recreation"),
    )
    STATISTICAL_CAPACITY_BUILDING = (
        16062,
        pgettext_lazy("IATI codelist Sector", "Statistical capacity building"),
    )
    NARCOTICS_CONTROL = (
        16063,
        pgettext_lazy("IATI codelist Sector", "Narcotics control"),
    )
    SOCIAL_MITIGATION_OF_HIV_AIDS = (
        16064,
        pgettext_lazy("IATI codelist Sector", "Social mitigation of HIV/AIDS"),
    )
    RECREATION_AND_SPORT = (
        16065,
        pgettext_lazy("IATI codelist Sector", "Recreation and sport"),
    )
    CULTURE = (
        16066,
        pgettext_lazy("IATI codelist Sector", "Culture"),
    )
    LABOUR_RIGHTS = (
        16070,
        pgettext_lazy("IATI codelist Sector", "Labour Rights"),
    )
    SOCIAL_DIALOGUE = (
        16080,
        pgettext_lazy("IATI codelist Sector", "Social Dialogue"),
    )
    TRANSPORT_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        21010,
        pgettext_lazy(
            "IATI codelist Sector", "Transport policy and administrative management"
        ),
    )
    TRANSPORT_POLICY__PLANNING_AND_ADMINISTRATION = (
        21011,
        pgettext_lazy(
            "IATI codelist Sector", "Transport policy, planning and administration"
        ),
    )
    PUBLIC_TRANSPORT_SERVICES = (
        21012,
        pgettext_lazy("IATI codelist Sector", "Public transport services"),
    )
    TRANSPORT_REGULATION = (
        21013,
        pgettext_lazy("IATI codelist Sector", "Transport regulation"),
    )
    ROAD_TRANSPORT = (
        21020,
        pgettext_lazy("IATI codelist Sector", "Road transport"),
    )
    FEEDER_ROAD_CONSTRUCTION = (
        21021,
        pgettext_lazy("IATI codelist Sector", "Feeder road construction"),
    )
    FEEDER_ROAD_MAINTENANCE = (
        21022,
        pgettext_lazy("IATI codelist Sector", "Feeder road maintenance"),
    )
    NATIONAL_ROAD_CONSTRUCTION = (
        21023,
        pgettext_lazy("IATI codelist Sector", "National road construction"),
    )
    NATIONAL_ROAD_MAINTENANCE = (
        21024,
        pgettext_lazy("IATI codelist Sector", "National road maintenance"),
    )
    RAIL_TRANSPORT = (
        21030,
        pgettext_lazy("IATI codelist Sector", "Rail transport"),
    )
    WATER_TRANSPORT = (
        21040,
        pgettext_lazy("IATI codelist Sector", "Water transport"),
    )
    AIR_TRANSPORT = (
        21050,
        pgettext_lazy("IATI codelist Sector", "Air transport"),
    )
    STORAGE = (
        21061,
        pgettext_lazy("IATI codelist Sector", "Storage"),
    )
    EDUCATION_AND_TRAINING_IN_TRANSPORT_AND_STORAGE = (
        21081,
        pgettext_lazy(
            "IATI codelist Sector", "Education and training in transport and storage"
        ),
    )
    COMMUNICATIONS_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        22010,
        pgettext_lazy(
            "IATI codelist Sector",
            "Communications policy and administrative management",
        ),
    )
    COMMUNICATIONS_POLICY__PLANNING_AND_ADMINISTRATION = (
        22011,
        pgettext_lazy(
            "IATI codelist Sector", "Communications policy, planning and administration"
        ),
    )
    POSTAL_SERVICES = (
        22012,
        pgettext_lazy("IATI codelist Sector", "Postal services"),
    )
    INFORMATION_SERVICES = (
        22013,
        pgettext_lazy("IATI codelist Sector", "Information services"),
    )
    TELECOMMUNICATIONS = (
        22020,
        pgettext_lazy("IATI codelist Sector", "Telecommunications"),
    )
    RADIO_TELEVISION_PRINT_MEDIA = (
        22030,
        pgettext_lazy("IATI codelist Sector", "Radio/television/print media"),
    )
    INFORMATION_AND_COMMUNICATION_TECHNOLOGY__ICT_ = (
        22040,
        pgettext_lazy(
            "IATI codelist Sector", "Information and communication technology (ICT)"
        ),
    )
    ENERGY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        23010,
        pgettext_lazy(
            "IATI codelist Sector", "Energy policy and administrative management"
        ),
    )
    POWER_GENERATION_NON_RENEWABLE_SOURCES = (
        23020,
        pgettext_lazy("IATI codelist Sector", "Power generation/non-renewable sources"),
    )
    POWER_GENERATION_RENEWABLE_SOURCES = (
        23030,
        pgettext_lazy("IATI codelist Sector", "Power generation/renewable sources"),
    )
    ELECTRICAL_TRANSMISSION__DISTRIBUTION = (
        23040,
        pgettext_lazy("IATI codelist Sector", "Electrical transmission/ distribution"),
    )
    GAS_DISTRIBUTION = (
        23050,
        pgettext_lazy("IATI codelist Sector", "Gas distribution"),
    )
    OIL_FIRED_POWER_PLANTS = (
        23061,
        pgettext_lazy("IATI codelist Sector", "Oil-fired power plants"),
    )
    GAS_FIRED_POWER_PLANTS = (
        23062,
        pgettext_lazy("IATI codelist Sector", "Gas-fired power plants"),
    )
    COAL_FIRED_POWER_PLANTS = (
        23063,
        pgettext_lazy("IATI codelist Sector", "Coal-fired power plants"),
    )
    NUCLEAR_POWER_PLANTS = (
        23064,
        pgettext_lazy("IATI codelist Sector", "Nuclear power plants"),
    )
    HYDRO_ELECTRIC_POWER_PLANTS = (
        23065,
        pgettext_lazy("IATI codelist Sector", "Hydro-electric power plants"),
    )
    GEOTHERMAL_ENERGY = (
        23066,
        pgettext_lazy("IATI codelist Sector", "Geothermal energy"),
    )
    SOLAR_ENERGY = (
        23067,
        pgettext_lazy("IATI codelist Sector", "Solar energy"),
    )
    WIND_POWER = (
        23068,
        pgettext_lazy("IATI codelist Sector", "Wind power"),
    )
    OCEAN_POWER = (
        23069,
        pgettext_lazy("IATI codelist Sector", "Ocean power"),
    )
    BIOMASS = (
        23070,
        pgettext_lazy("IATI codelist Sector", "Biomass"),
    )
    ENERGY_EDUCATION_TRAINING = (
        23081,
        pgettext_lazy("IATI codelist Sector", "Energy education/training"),
    )
    ENERGY_RESEARCH = (
        23082,
        pgettext_lazy("IATI codelist Sector", "Energy research"),
    )
    ENERGY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        23110,
        pgettext_lazy(
            "IATI codelist Sector", "Energy policy and administrative management"
        ),
    )
    ENERGY_SECTOR_POLICY__PLANNING_AND_ADMINISTRATION = (
        23111,
        pgettext_lazy(
            "IATI codelist Sector", "Energy sector policy, planning and administration"
        ),
    )
    ENERGY_REGULATION = (
        23112,
        pgettext_lazy("IATI codelist Sector", "Energy regulation"),
    )
    ENERGY_EDUCATION_TRAINING = (
        23181,
        pgettext_lazy("IATI codelist Sector", "Energy education/training"),
    )
    ENERGY_RESEARCH = (
        23182,
        pgettext_lazy("IATI codelist Sector", "Energy research"),
    )
    ENERGY_CONSERVATION_AND_DEMAND_SIDE_EFFICIENCY = (
        23183,
        pgettext_lazy(
            "IATI codelist Sector", "Energy conservation and demand-side efficiency"
        ),
    )
    ENERGY_GENERATION__RENEWABLE_SOURCES_MULTIPLE_TECHNOLOGIES = (
        23210,
        pgettext_lazy(
            "IATI codelist Sector",
            "Energy generation, renewable sources - multiple technologies",
        ),
    )
    HYDRO_ELECTRIC_POWER_PLANTS = (
        23220,
        pgettext_lazy("IATI codelist Sector", "Hydro-electric power plants"),
    )
    SOLAR_ENERGY_FOR_CENTRALISED_GRIDS = (
        23230,
        pgettext_lazy("IATI codelist Sector", "Solar energy for centralised grids"),
    )
    SOLAR_ENERGY_FOR_ISOLATED_GRIDS_AND_STANDALONE_SYSTEMS = (
        23231,
        pgettext_lazy(
            "IATI codelist Sector",
            "Solar energy for isolated grids and standalone systems",
        ),
    )
    SOLAR_ENERGY_THERMAL_APPLICATIONS = (
        23232,
        pgettext_lazy("IATI codelist Sector", "Solar energy - thermal applications"),
    )
    WIND_ENERGY = (
        23240,
        pgettext_lazy("IATI codelist Sector", "Wind energy"),
    )
    MARINE_ENERGY = (
        23250,
        pgettext_lazy("IATI codelist Sector", "Marine energy"),
    )
    GEOTHERMAL_ENERGY = (
        23260,
        pgettext_lazy("IATI codelist Sector", "Geothermal energy"),
    )
    BIOFUEL_FIRED_POWER_PLANTS = (
        23270,
        pgettext_lazy("IATI codelist Sector", "Biofuel-fired power plants"),
    )
    ENERGY_GENERATION__NON_RENEWABLE_SOURCES__UNSPECIFIED = (
        23310,
        pgettext_lazy(
            "IATI codelist Sector",
            "Energy generation, non-renewable sources, unspecified",
        ),
    )
    COAL_FIRED_ELECTRIC_POWER_PLANTS = (
        23320,
        pgettext_lazy("IATI codelist Sector", "Coal-fired electric power plants"),
    )
    OIL_FIRED_ELECTRIC_POWER_PLANTS = (
        23330,
        pgettext_lazy("IATI codelist Sector", "Oil-fired electric power plants"),
    )
    NATURAL_GAS_FIRED_ELECTRIC_POWER_PLANTS = (
        23340,
        pgettext_lazy(
            "IATI codelist Sector", "Natural gas-fired electric power plants"
        ),
    )
    FOSSIL_FUEL_ELECTRIC_POWER_PLANTS_WITH_CARBON_CAPTURE_AND_STORAGE__CCS_ = (
        23350,
        pgettext_lazy(
            "IATI codelist Sector",
            "Fossil fuel electric power plants with carbon capture and storage (CCS)",
        ),
    )
    NON_RENEWABLE_WASTE_FIRED_ELECTRIC_POWER_PLANTS = (
        23360,
        pgettext_lazy(
            "IATI codelist Sector", "Non-renewable waste-fired electric power plants"
        ),
    )
    HYBRID_ENERGY_ELECTRIC_POWER_PLANTS = (
        23410,
        pgettext_lazy("IATI codelist Sector", "Hybrid energy electric power plants"),
    )
    NUCLEAR_ENERGY_ELECTRIC_POWER_PLANTS_AND_NUCLEAR_SAFETY = (
        23510,
        pgettext_lazy(
            "IATI codelist Sector",
            "Nuclear energy electric power plants and nuclear safety",
        ),
    )
    HEAT_PLANTS = (
        23610,
        pgettext_lazy("IATI codelist Sector", "Heat plants"),
    )
    DISTRICT_HEATING_AND_COOLING = (
        23620,
        pgettext_lazy("IATI codelist Sector", "District heating and cooling"),
    )
    ELECTRIC_POWER_TRANSMISSION_AND_DISTRIBUTION__CENTRALISED_GRIDS_ = (
        23630,
        pgettext_lazy(
            "IATI codelist Sector",
            "Electric power transmission and distribution (centralised grids)",
        ),
    )
    ELECTRIC_POWER_TRANSMISSION_AND_DISTRIBUTION__ISOLATED_MINI_GRIDS_ = (
        23631,
        pgettext_lazy(
            "IATI codelist Sector",
            "Electric power transmission and distribution (isolated mini-grids)",
        ),
    )
    RETAIL_GAS_DISTRIBUTION = (
        23640,
        pgettext_lazy("IATI codelist Sector", "Retail gas distribution"),
    )
    RETAIL_DISTRIBUTION_OF_LIQUID_OR_SOLID_FOSSIL_FUELS = (
        23641,
        pgettext_lazy(
            "IATI codelist Sector",
            "Retail distribution of liquid or solid fossil fuels",
        ),
    )
    ELECTRIC_MOBILITY_INFRASTRUCTURES = (
        23642,
        pgettext_lazy("IATI codelist Sector", "Electric mobility infrastructures"),
    )
    FINANCIAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        24010,
        pgettext_lazy(
            "IATI codelist Sector", "Financial policy and administrative management"
        ),
    )
    MONETARY_INSTITUTIONS = (
        24020,
        pgettext_lazy("IATI codelist Sector", "Monetary institutions"),
    )
    FORMAL_SECTOR_FINANCIAL_INTERMEDIARIES = (
        24030,
        pgettext_lazy("IATI codelist Sector", "Formal sector financial intermediaries"),
    )
    INFORMAL_SEMI_FORMAL_FINANCIAL_INTERMEDIARIES = (
        24040,
        pgettext_lazy(
            "IATI codelist Sector", "Informal/semi-formal financial intermediaries"
        ),
    )
    REMITTANCE_FACILITATION__PROMOTION_AND_OPTIMISATION = (
        24050,
        pgettext_lazy(
            "IATI codelist Sector",
            "Remittance facilitation, promotion and optimisation",
        ),
    )
    EDUCATION_TRAINING_IN_BANKING_AND_FINANCIAL_SERVICES = (
        24081,
        pgettext_lazy(
            "IATI codelist Sector",
            "Education/training in banking and financial services",
        ),
    )
    BUSINESS_POLICY_AND_ADMINISTRATION = (
        25010,
        pgettext_lazy("IATI codelist Sector", "Business Policy and Administration"),
    )
    PRIVATISATION = (
        25020,
        pgettext_lazy("IATI codelist Sector", "Privatisation"),
    )
    BUSINESS_DEVELOPMENT_SERVICES = (
        25030,
        pgettext_lazy("IATI codelist Sector", "Business development services"),
    )
    RESPONSIBLE_BUSINESS_CONDUCT = (
        25040,
        pgettext_lazy("IATI codelist Sector", "Responsible Business Conduct"),
    )
    AGRICULTURAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        31110,
        pgettext_lazy(
            "IATI codelist Sector", "Agricultural policy and administrative management"
        ),
    )
    AGRICULTURAL_DEVELOPMENT = (
        31120,
        pgettext_lazy("IATI codelist Sector", "Agricultural development"),
    )
    AGRICULTURAL_LAND_RESOURCES = (
        31130,
        pgettext_lazy("IATI codelist Sector", "Agricultural land resources"),
    )
    AGRICULTURAL_WATER_RESOURCES = (
        31140,
        pgettext_lazy("IATI codelist Sector", "Agricultural water resources"),
    )
    AGRICULTURAL_INPUTS = (
        31150,
        pgettext_lazy("IATI codelist Sector", "Agricultural inputs"),
    )
    FOOD_CROP_PRODUCTION = (
        31161,
        pgettext_lazy("IATI codelist Sector", "Food crop production"),
    )
    INDUSTRIAL_CROPS_EXPORT_CROPS = (
        31162,
        pgettext_lazy("IATI codelist Sector", "Industrial crops/export crops"),
    )
    LIVESTOCK = (
        31163,
        pgettext_lazy("IATI codelist Sector", "Livestock"),
    )
    AGRARIAN_REFORM = (
        31164,
        pgettext_lazy("IATI codelist Sector", "Agrarian reform"),
    )
    AGRICULTURAL_ALTERNATIVE_DEVELOPMENT = (
        31165,
        pgettext_lazy("IATI codelist Sector", "Agricultural alternative development"),
    )
    AGRICULTURAL_EXTENSION = (
        31166,
        pgettext_lazy("IATI codelist Sector", "Agricultural extension"),
    )
    AGRICULTURAL_EDUCATION_TRAINING = (
        31181,
        pgettext_lazy("IATI codelist Sector", "Agricultural education/training"),
    )
    AGRICULTURAL_RESEARCH = (
        31182,
        pgettext_lazy("IATI codelist Sector", "Agricultural research"),
    )
    AGRICULTURAL_SERVICES = (
        31191,
        pgettext_lazy("IATI codelist Sector", "Agricultural services"),
    )
    PLANT_AND_POST_HARVEST_PROTECTION_AND_PEST_CONTROL = (
        31192,
        pgettext_lazy(
            "IATI codelist Sector", "Plant and post-harvest protection and pest control"
        ),
    )
    AGRICULTURAL_FINANCIAL_SERVICES = (
        31193,
        pgettext_lazy("IATI codelist Sector", "Agricultural financial services"),
    )
    AGRICULTURAL_CO_OPERATIVES = (
        31194,
        pgettext_lazy("IATI codelist Sector", "Agricultural co-operatives"),
    )
    LIVESTOCK_VETERINARY_SERVICES = (
        31195,
        pgettext_lazy("IATI codelist Sector", "Livestock/veterinary services"),
    )
    FORESTRY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        31210,
        pgettext_lazy(
            "IATI codelist Sector", "Forestry policy and administrative management"
        ),
    )
    FORESTRY_DEVELOPMENT = (
        31220,
        pgettext_lazy("IATI codelist Sector", "Forestry development"),
    )
    FUELWOOD_CHARCOAL = (
        31261,
        pgettext_lazy("IATI codelist Sector", "Fuelwood/charcoal"),
    )
    FORESTRY_EDUCATION_TRAINING = (
        31281,
        pgettext_lazy("IATI codelist Sector", "Forestry education/training"),
    )
    FORESTRY_RESEARCH = (
        31282,
        pgettext_lazy("IATI codelist Sector", "Forestry research"),
    )
    FORESTRY_SERVICES = (
        31291,
        pgettext_lazy("IATI codelist Sector", "Forestry services"),
    )
    FISHING_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        31310,
        pgettext_lazy(
            "IATI codelist Sector", "Fishing policy and administrative management"
        ),
    )
    FISHERY_DEVELOPMENT = (
        31320,
        pgettext_lazy("IATI codelist Sector", "Fishery development"),
    )
    FISHERY_EDUCATION_TRAINING = (
        31381,
        pgettext_lazy("IATI codelist Sector", "Fishery education/training"),
    )
    FISHERY_RESEARCH = (
        31382,
        pgettext_lazy("IATI codelist Sector", "Fishery research"),
    )
    FISHERY_SERVICES = (
        31391,
        pgettext_lazy("IATI codelist Sector", "Fishery services"),
    )
    INDUSTRIAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        32110,
        pgettext_lazy(
            "IATI codelist Sector", "Industrial policy and administrative management"
        ),
    )
    INDUSTRIAL_DEVELOPMENT = (
        32120,
        pgettext_lazy("IATI codelist Sector", "Industrial development"),
    )
    SMALL_AND_MEDIUM_SIZED_ENTERPRISES__SME__DEVELOPMENT = (
        32130,
        pgettext_lazy(
            "IATI codelist Sector",
            "Small and medium-sized enterprises (SME) development",
        ),
    )
    COTTAGE_INDUSTRIES_AND_HANDICRAFT = (
        32140,
        pgettext_lazy("IATI codelist Sector", "Cottage industries and handicraft"),
    )
    AGRO_INDUSTRIES = (
        32161,
        pgettext_lazy("IATI codelist Sector", "Agro-industries"),
    )
    FOREST_INDUSTRIES = (
        32162,
        pgettext_lazy("IATI codelist Sector", "Forest industries"),
    )
    TEXTILES__LEATHER_AND_SUBSTITUTES = (
        32163,
        pgettext_lazy("IATI codelist Sector", "Textiles, leather and substitutes"),
    )
    CHEMICALS = (
        32164,
        pgettext_lazy("IATI codelist Sector", "Chemicals"),
    )
    FERTILIZER_PLANTS = (
        32165,
        pgettext_lazy("IATI codelist Sector", "Fertilizer plants"),
    )
    CEMENT_LIME_PLASTER = (
        32166,
        pgettext_lazy("IATI codelist Sector", "Cement/lime/plaster"),
    )
    ENERGY_MANUFACTURING__FOSSIL_FUELS_ = (
        32167,
        pgettext_lazy("IATI codelist Sector", "Energy manufacturing (fossil fuels)"),
    )
    PHARMACEUTICAL_PRODUCTION = (
        32168,
        pgettext_lazy("IATI codelist Sector", "Pharmaceutical production"),
    )
    BASIC_METAL_INDUSTRIES = (
        32169,
        pgettext_lazy("IATI codelist Sector", "Basic metal industries"),
    )
    NON_FERROUS_METAL_INDUSTRIES = (
        32170,
        pgettext_lazy("IATI codelist Sector", "Non-ferrous metal industries"),
    )
    ENGINEERING = (
        32171,
        pgettext_lazy("IATI codelist Sector", "Engineering"),
    )
    TRANSPORT_EQUIPMENT_INDUSTRY = (
        32172,
        pgettext_lazy("IATI codelist Sector", "Transport equipment industry"),
    )
    MODERN_BIOFUELS_MANUFACTURING = (
        32173,
        pgettext_lazy("IATI codelist Sector", "Modern biofuels manufacturing"),
    )
    CLEAN_COOKING_APPLIANCES_MANUFACTURING = (
        32174,
        pgettext_lazy("IATI codelist Sector", "Clean cooking appliances manufacturing"),
    )
    TECHNOLOGICAL_RESEARCH_AND_DEVELOPMENT = (
        32182,
        pgettext_lazy("IATI codelist Sector", "Technological research and development"),
    )
    MINERAL_MINING_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        32210,
        pgettext_lazy(
            "IATI codelist Sector",
            "Mineral/mining policy and administrative management",
        ),
    )
    MINERAL_PROSPECTION_AND_EXPLORATION = (
        32220,
        pgettext_lazy("IATI codelist Sector", "Mineral prospection and exploration"),
    )
    COAL = (
        32261,
        pgettext_lazy("IATI codelist Sector", "Coal"),
    )
    OIL_AND_GAS__UPSTREAM_ = (
        32262,
        pgettext_lazy("IATI codelist Sector", "Oil and gas (upstream)"),
    )
    FERROUS_METALS = (
        32263,
        pgettext_lazy("IATI codelist Sector", "Ferrous metals"),
    )
    NONFERROUS_METALS = (
        32264,
        pgettext_lazy("IATI codelist Sector", "Nonferrous metals"),
    )
    PRECIOUS_METALS_MATERIALS = (
        32265,
        pgettext_lazy("IATI codelist Sector", "Precious metals/materials"),
    )
    INDUSTRIAL_MINERALS = (
        32266,
        pgettext_lazy("IATI codelist Sector", "Industrial minerals"),
    )
    FERTILIZER_MINERALS = (
        32267,
        pgettext_lazy("IATI codelist Sector", "Fertilizer minerals"),
    )
    OFFSHORE_MINERALS = (
        32268,
        pgettext_lazy("IATI codelist Sector", "Offshore minerals"),
    )
    CONSTRUCTION_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        32310,
        pgettext_lazy(
            "IATI codelist Sector", "Construction policy and administrative management"
        ),
    )
    TRADE_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        33110,
        pgettext_lazy(
            "IATI codelist Sector", "Trade policy and administrative management"
        ),
    )
    TRADE_FACILITATION = (
        33120,
        pgettext_lazy("IATI codelist Sector", "Trade facilitation"),
    )
    REGIONAL_TRADE_AGREEMENTS__RTAS_ = (
        33130,
        pgettext_lazy("IATI codelist Sector", "Regional trade agreements (RTAs)"),
    )
    MULTILATERAL_TRADE_NEGOTIATIONS = (
        33140,
        pgettext_lazy("IATI codelist Sector", "Multilateral trade negotiations"),
    )
    TRADE_RELATED_ADJUSTMENT = (
        33150,
        pgettext_lazy("IATI codelist Sector", "Trade-related adjustment"),
    )
    TRADE_EDUCATION_TRAINING = (
        33181,
        pgettext_lazy("IATI codelist Sector", "Trade education/training"),
    )
    TOURISM_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        33210,
        pgettext_lazy(
            "IATI codelist Sector", "Tourism policy and administrative management"
        ),
    )
    ENVIRONMENTAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        41010,
        pgettext_lazy(
            "IATI codelist Sector", "Environmental policy and administrative management"
        ),
    )
    BIOSPHERE_PROTECTION = (
        41020,
        pgettext_lazy("IATI codelist Sector", "Biosphere protection"),
    )
    BIO_DIVERSITY = (
        41030,
        pgettext_lazy("IATI codelist Sector", "Bio-diversity"),
    )
    SITE_PRESERVATION = (
        41040,
        pgettext_lazy("IATI codelist Sector", "Site preservation"),
    )
    FLOOD_PREVENTION_CONTROL = (
        41050,
        pgettext_lazy("IATI codelist Sector", "Flood prevention/control"),
    )
    ENVIRONMENTAL_EDUCATION_TRAINING = (
        41081,
        pgettext_lazy("IATI codelist Sector", "Environmental education/training"),
    )
    ENVIRONMENTAL_RESEARCH = (
        41082,
        pgettext_lazy("IATI codelist Sector", "Environmental research"),
    )
    MULTISECTOR_AID = (
        43010,
        pgettext_lazy("IATI codelist Sector", "Multisector aid"),
    )
    URBAN_DEVELOPMENT_AND_MANAGEMENT = (
        43030,
        pgettext_lazy("IATI codelist Sector", "Urban development and management"),
    )
    URBAN_LAND_POLICY_AND_MANAGEMENT = (
        43031,
        pgettext_lazy("IATI codelist Sector", "Urban land policy and management"),
    )
    URBAN_DEVELOPMENT = (
        43032,
        pgettext_lazy("IATI codelist Sector", "Urban development"),
    )
    RURAL_DEVELOPMENT = (
        43040,
        pgettext_lazy("IATI codelist Sector", "Rural development"),
    )
    RURAL_LAND_POLICY_AND_MANAGEMENT = (
        43041,
        pgettext_lazy("IATI codelist Sector", "Rural land policy and management"),
    )
    RURAL_DEVELOPMENT = (
        43042,
        pgettext_lazy("IATI codelist Sector", "Rural development"),
    )
    NON_AGRICULTURAL_ALTERNATIVE_DEVELOPMENT = (
        43050,
        pgettext_lazy(
            "IATI codelist Sector", "Non-agricultural alternative development"
        ),
    )
    DISASTER_RISK_REDUCTION = (
        43060,
        pgettext_lazy("IATI codelist Sector", "Disaster Risk Reduction"),
    )
    FOOD_SECURITY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        43071,
        pgettext_lazy(
            "IATI codelist Sector", "Food security policy and administrative management"
        ),
    )
    HOUSEHOLD_FOOD_SECURITY_PROGRAMMES = (
        43072,
        pgettext_lazy("IATI codelist Sector", "Household food security programmes"),
    )
    FOOD_SAFETY_AND_QUALITY = (
        43073,
        pgettext_lazy("IATI codelist Sector", "Food safety and quality"),
    )
    MULTISECTOR_EDUCATION_TRAINING = (
        43081,
        pgettext_lazy("IATI codelist Sector", "Multisector education/training"),
    )
    RESEARCH_SCIENTIFIC_INSTITUTIONS = (
        43082,
        pgettext_lazy("IATI codelist Sector", "Research/scientific institutions"),
    )
    GENERAL_BUDGET_SUPPORT_RELATED_AID = (
        51010,
        pgettext_lazy("IATI codelist Sector", "General budget support-related aid"),
    )
    FOOD_ASSISTANCE = (
        52010,
        pgettext_lazy("IATI codelist Sector", "Food assistance"),
    )
    IMPORT_SUPPORT__CAPITAL_GOODS_ = (
        53030,
        pgettext_lazy("IATI codelist Sector", "Import support (capital goods)"),
    )
    IMPORT_SUPPORT__COMMODITIES_ = (
        53040,
        pgettext_lazy("IATI codelist Sector", "Import support (commodities)"),
    )
    ACTION_RELATING_TO_DEBT = (
        60010,
        pgettext_lazy("IATI codelist Sector", "Action relating to debt"),
    )
    DEBT_FORGIVENESS = (
        60020,
        pgettext_lazy("IATI codelist Sector", "Debt forgiveness"),
    )
    RELIEF_OF_MULTILATERAL_DEBT = (
        60030,
        pgettext_lazy("IATI codelist Sector", "Relief of multilateral debt"),
    )
    RESCHEDULING_AND_REFINANCING = (
        60040,
        pgettext_lazy("IATI codelist Sector", "Rescheduling and refinancing"),
    )
    DEBT_FOR_DEVELOPMENT_SWAP = (
        60061,
        pgettext_lazy("IATI codelist Sector", "Debt for development swap"),
    )
    OTHER_DEBT_SWAP = (
        60062,
        pgettext_lazy("IATI codelist Sector", "Other debt swap"),
    )
    DEBT_BUY_BACK = (
        60063,
        pgettext_lazy("IATI codelist Sector", "Debt buy-back"),
    )
    MATERIAL_RELIEF_ASSISTANCE_AND_SERVICES = (
        72010,
        pgettext_lazy(
            "IATI codelist Sector", "Material relief assistance and services"
        ),
    )
    BASIC_HEALTH_CARE_SERVICES_IN_EMERGENCIES = (
        72011,
        pgettext_lazy(
            "IATI codelist Sector", "Basic Health Care Services in Emergencies"
        ),
    )
    EDUCATION_IN_EMERGENCIES = (
        72012,
        pgettext_lazy("IATI codelist Sector", "Education in emergencies"),
    )
    EMERGENCY_FOOD_ASSISTANCE = (
        72040,
        pgettext_lazy("IATI codelist Sector", "Emergency food assistance"),
    )
    RELIEF_CO_ORDINATION_AND_SUPPORT_SERVICES = (
        72050,
        pgettext_lazy(
            "IATI codelist Sector", "Relief co-ordination and support services"
        ),
    )
    IMMEDIATE_POST_EMERGENCY_RECONSTRUCTION_AND_REHABILITATION = (
        73010,
        pgettext_lazy(
            "IATI codelist Sector",
            "Immediate post-emergency reconstruction and rehabilitation",
        ),
    )
    DISASTER_PREVENTION_AND_PREPAREDNESS = (
        74010,
        pgettext_lazy("IATI codelist Sector", "Disaster prevention and preparedness"),
    )
    MULTI_HAZARD_RESPONSE_PREPAREDNESS = (
        74020,
        pgettext_lazy("IATI codelist Sector", "Multi-hazard response preparedness"),
    )
    ADMINISTRATIVE_COSTS__NON_SECTOR_ALLOCABLE_ = (
        91010,
        pgettext_lazy(
            "IATI codelist Sector", "Administrative costs (non-sector allocable)"
        ),
    )
    SUPPORT_TO_NATIONAL_NGOS = (
        92010,
        pgettext_lazy("IATI codelist Sector", "Support to national NGOs"),
    )
    SUPPORT_TO_INTERNATIONAL_NGOS = (
        92020,
        pgettext_lazy("IATI codelist Sector", "Support to international NGOs"),
    )
    SUPPORT_TO_LOCAL_AND_REGIONAL_NGOS = (
        92030,
        pgettext_lazy("IATI codelist Sector", "Support to local and regional NGOs"),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES__NON_SECTOR_ALLOCABLE_ = (
        93010,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers  in donor countries (non-sector allocable)",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_FOOD_AND_SHELTER = (
        93011,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - food and shelter",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_TRAINING = (
        93012,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - training",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_HEALTH = (
        93013,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - health",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_OTHER_TEMPORARY_SUSTENANCE = (
        93014,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - other temporary sustenance",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_VOLUNTARY_REPATRIATION = (
        93015,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - voluntary repatriation",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_TRANSPORT = (
        93016,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - transport",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_RESCUE_AT_SEA = (
        93017,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - rescue at sea",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_ADMINISTRATIVE_COSTS = (
        93018,
        pgettext_lazy(
            "IATI codelist Sector",
            "Refugees/asylum seekers in donor countries - administrative costs",
        ),
    )
    SECTORS_NOT_SPECIFIED = (
        99810,
        pgettext_lazy("IATI codelist Sector", "Sectors not specified"),
    )
    PROMOTION_OF_DEVELOPMENT_AWARENESS__NON_SECTOR_ALLOCABLE_ = (
        99820,
        pgettext_lazy(
            "IATI codelist Sector",
            "Promotion of development awareness (non-sector allocable)",
        ),
    )
