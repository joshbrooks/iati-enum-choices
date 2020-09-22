from django.db import models
from django.utils.translation import pgettext_lazy


class CRSChannelCode(models.IntegerChoices):
    PUBLIC_SECTOR_INSTITUTIONS = (
        10000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Public Sector Institutions"),
    )
    DONOR_GOVERNMENT = (
        11000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Donor Government"),
    )
    CENTRAL_GOVERNMENT = (
        11001,
        pgettext_lazy("IATI codelist CRSChannelCode", "Central Government"),
    )
    LOCAL_GOVERNMENT = (
        11002,
        pgettext_lazy("IATI codelist CRSChannelCode", "Local Government"),
    )
    PUBLIC_CORPORATIONS = (
        11003,
        pgettext_lazy("IATI codelist CRSChannelCode", "Public corporations"),
    )
    OTHER_PUBLIC_ENTITIES_IN_DONOR_COUNTRY = (
        11004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Other public entities in donor country"
        ),
    )
    RECIPIENT_GOVERNMENT = (
        12000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Recipient Government"),
    )
    CENTRAL_GOVERNMENT = (
        12001,
        pgettext_lazy("IATI codelist CRSChannelCode", "Central Government"),
    )
    LOCAL_GOVERNMENT = (
        12002,
        pgettext_lazy("IATI codelist CRSChannelCode", "Local Government"),
    )
    PUBLIC_CORPORATIONS = (
        12003,
        pgettext_lazy("IATI codelist CRSChannelCode", "Public corporations"),
    )
    OTHER_PUBLIC_ENTITIES_IN_RECIPIENT_COUNTRY = (
        12004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Other public entities in recipient country"
        ),
    )
    THIRD_COUNTRY_GOVERNMENT__DELEGATED_CO_OPERATION_ = (
        13000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Third Country Government (Delegated co-operation)",
        ),
    )
    NON_GOVERNMENTAL_ORGANISATION__NGO__AND_CIVIL_SOCIETY = (
        20000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Non-Governmental Organisation (NGO) and Civil Society",
        ),
    )
    INTERNATIONAL_NGO = (
        21000,
        pgettext_lazy("IATI codelist CRSChannelCode", "International NGO"),
    )
    ASSOCIATION_OF_GEOSCIENTISTS_FOR_INTERNATIONAL_DEVELOPMENT = (
        21001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Association of Geoscientists for International Development",
        ),
    )
    AGENCY_FOR_INTERNATIONAL_TRADE_INFORMATION_AND_CO_OPERATION = (
        21002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Agency for International Trade Information and Co-operation",
        ),
    )
    LATIN_AMERICAN_COUNCIL_FOR_SOCIAL_SCIENCES = (
        21003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Latin American Council for Social Sciences"
        ),
    )
    COUNCIL_FOR_THE_DEVELOPMENT_OF_ECONOMIC_AND_SOCIAL_RESEARCH_IN_AFRICA = (
        21004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Council for the Development of Economic and Social Research in Africa",
        ),
    )
    CONSUMER_UNITY_AND_TRUST_SOCIETY_INTERNATIONAL = (
        21005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Consumer Unity and Trust Society International",
        ),
    )
    DEVELOPMENT_GATEWAY_FOUNDATION = (
        21006,
        pgettext_lazy("IATI codelist CRSChannelCode", "Development Gateway Foundation"),
    )
    ENVIRONMENTAL_LIAISON_CENTRE_INTERNATIONAL = (
        21007,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Environmental Liaison Centre International"
        ),
    )
    EUROSTEP = (
        21008,
        pgettext_lazy("IATI codelist CRSChannelCode", "Eurostep"),
    )
    FORUM_FOR_AGRICULTURAL_RESEARCH_IN_AFRICA = (
        21009,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Forum for Agricultural Research in Africa"
        ),
    )
    FORUM_FOR_AFRICAN_WOMEN_EDUCATIONALISTS = (
        21010,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Forum for African Women Educationalists"
        ),
    )
    GLOBAL_CAMPAIGN_FOR_EDUCATION = (
        21011,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Campaign for Education"),
    )
    HEALTH_ACTION_INTERNATIONAL = (
        21013,
        pgettext_lazy("IATI codelist CRSChannelCode", "Health Action International"),
    )
    HUMAN_RIGHTS_INFORMATION_AND_DOCUMENTATION_SYSTEMS = (
        21014,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Human Rights Information and Documentation Systems",
        ),
    )
    INTERNATIONAL_CATHOLIC_RURAL_ASSOCIATION = (
        21015,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Catholic Rural Association"
        ),
    )
    INTERNATIONAL_COMMITTEE_OF_THE_RED_CROSS = (
        21016,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Committee of the Red Cross"
        ),
    )
    INTERNATIONAL_CENTRE_FOR_TRADE_AND_SUSTAINABLE_DEVELOPMENT = (
        21017,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Trade and Sustainable Development",
        ),
    )
    INTERNATIONAL_FEDERATION_OF_RED_CROSS_AND_RED_CRESCENT_SOCIETIES = (
        21018,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Federation of Red Cross and Red Crescent Societies",
        ),
    )
    INTERNATIONAL_FEDERATION_OF_SETTLEMENTS_AND_NEIGHBOURHOOD_CENTRES = (
        21019,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Federation of Settlements and Neighbourhood Centres",
        ),
    )
    INTERNATIONAL_HIV_AIDS_ALLIANCE = (
        21020,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International HIV/AIDS Alliance"
        ),
    )
    INTERNATIONAL_INSTITUTE_FOR_ENVIRONMENT_AND_DEVELOPMENT = (
        21021,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Institute for Environment and Development",
        ),
    )
    INTERNATIONAL_NETWORK_FOR_ALTERNATIVE_FINANCIAL_INSTITUTIONS = (
        21022,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Network for Alternative Financial Institutions",
        ),
    )
    INTERNATIONAL_PLANNED_PARENTHOOD_FEDERATION = (
        21023,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Planned Parenthood Federation",
        ),
    )
    INTER_PRESS_SERVICE__INTERNATIONAL_ASSOCIATION = (
        21024,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Inter Press Service, International Association",
        ),
    )
    INTERNATIONAL_SEISMOLOGICAL_CENTRE = (
        21025,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Seismological Centre"
        ),
    )
    INTERNATIONAL_SERVICE_FOR_HUMAN_RIGHTS = (
        21026,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Service for Human Rights"
        ),
    )
    ITF_ENHANCING_HUMAN_SECURITY = (
        21027,
        pgettext_lazy("IATI codelist CRSChannelCode", "ITF Enhancing Human Security"),
    )
    INTERNATIONAL_UNIVERSITY_EXCHANGE_FUND_IUEF_STIP__IN_AFRICA_AND_LATIN_AMERICA = (
        21028,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International University Exchange Fund - IUEF Stip. in Africa and Latin America",
        ),
    )
    DOCTORS_WITHOUT_BORDERS = (
        21029,
        pgettext_lazy("IATI codelist CRSChannelCode", "Doctors Without Borders"),
    )
    PAN_AFRICAN_INSTITUTE_FOR_DEVELOPMENT = (
        21030,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Pan African Institute for Development"
        ),
    )
    PANOS_INSTITUTE = (
        21031,
        pgettext_lazy("IATI codelist CRSChannelCode", "PANOS Institute"),
    )
    POPULATION_SERVICES_INTERNATIONAL = (
        21032,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Population Services International"
        ),
    )
    TRANSPARENCY_INTERNATIONAL = (
        21033,
        pgettext_lazy("IATI codelist CRSChannelCode", "Transparency International"),
    )
    INTERNATIONAL_UNION_AGAINST_TUBERCULOSIS_AND_LUNG_DISEASE = (
        21034,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Union Against Tuberculosis and Lung Disease",
        ),
    )
    WORLD_ORGANISATION_AGAINST_TORTURE = (
        21035,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "World Organisation Against Torture"
        ),
    )
    WORLD_UNIVERSITY_SERVICE = (
        21036,
        pgettext_lazy("IATI codelist CRSChannelCode", "World University Service"),
    )
    WOMEN_S_WORLD_BANKING = (
        21037,
        pgettext_lazy("IATI codelist CRSChannelCode", "Women's World Banking"),
    )
    INTERNATIONAL_ALERT = (
        21038,
        pgettext_lazy("IATI codelist CRSChannelCode", "International Alert"),
    )
    INTERNATIONAL_INSTITUTE_FOR_SUSTAINABLE_DEVELOPMENT = (
        21039,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Institute for Sustainable Development",
        ),
    )
    INTERNATIONAL_WOMEN_S_TRIBUNE_CENTRE = (
        21040,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Women's Tribune Centre"
        ),
    )
    SOCIETY_FOR_INTERNATIONAL_DEVELOPMENT = (
        21041,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Society for International Development"
        ),
    )
    INTERNATIONAL_PEACEBUILDING_ALLIANCE = (
        21042,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Peacebuilding Alliance"
        ),
    )
    EUROPEAN_PARLIAMENTARIANS_FOR_AFRICA = (
        21043,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "European Parliamentarians for Africa"
        ),
    )
    INTERNATIONAL_COUNCIL_FOR_THE_CONTROL_OF_IODINE_DEFICIENCY_DISORDERS = (
        21044,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Council for the Control of Iodine Deficiency Disorders",
        ),
    )
    AFRICAN_MEDICAL_AND_RESEARCH_FOUNDATION = (
        21045,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "African Medical and Research Foundation"
        ),
    )
    AGENCY_FOR_COOPERATION_AND_RESEARCH_IN_DEVELOPMENT = (
        21046,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Agency for Cooperation and Research in Development",
        ),
    )
    AGRICORD = (
        21047,
        pgettext_lazy("IATI codelist CRSChannelCode", "AgriCord"),
    )
    ASSOCIATION_OF_AFRICAN_UNIVERSITIES = (
        21048,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Association of African Universities"
        ),
    )
    EUROPEAN_CENTRE_FOR_DEVELOPMENT_POLICY_MANAGEMENT = (
        21049,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Centre for Development Policy Management",
        ),
    )
    GENEVA_CALL = (
        21050,
        pgettext_lazy("IATI codelist CRSChannelCode", "Geneva Call"),
    )
    INSTITUT_SUPÉRIEUR_PANAFRICAINE_D_ECONOMIE_COOPÉRATIVE = (
        21051,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Institut Supérieur Panafricaine d’Economie Coopérative",
        ),
    )
    IPAS_PROTECTING_WOMEN_S_HEALTH__ADVANCING_WOMEN_S_REPRODUCTIVE_RIGHTS = (
        21053,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "IPAS-Protecting Women’s Health, Advancing Women’s Reproductive Rights",
        ),
    )
    LIFE_AND_PEACE_INSTITUTE = (
        21054,
        pgettext_lazy("IATI codelist CRSChannelCode", "Life and Peace Institute"),
    )
    REGIONAL_AIDS_TRAINING_NETWORK = (
        21055,
        pgettext_lazy("IATI codelist CRSChannelCode", "Regional AIDS Training Network"),
    )
    RENEWABLE_ENERGY_AND_ENERGY_EFFICIENCY_PARTNERSHIP = (
        21056,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Renewable Energy and Energy Efficiency Partnership",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_TRANSITIONAL_JUSTICE = (
        21057,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Transitional Justice",
        ),
    )
    INTERNATIONAL_CRISIS_GROUP = (
        21058,
        pgettext_lazy("IATI codelist CRSChannelCode", "International Crisis Group"),
    )
    AFRICA_SOLIDARITY_FUND = (
        21059,
        pgettext_lazy("IATI codelist CRSChannelCode", "Africa Solidarity Fund"),
    )
    ASSOCIATION_FOR_THE_PREVENTION_OF_TORTURE = (
        21060,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Association for the Prevention of Torture"
        ),
    )
    INTERNATIONAL_REHABILITATION_COUNCIL_FOR_TORTURE_VICTIMS = (
        21061,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Rehabilitation Council for Torture Victims",
        ),
    )
    THE_NATURE_CONSERVANCY = (
        21062,
        pgettext_lazy("IATI codelist CRSChannelCode", "The Nature Conservancy"),
    )
    CONSERVATION_INTERNATIONAL = (
        21063,
        pgettext_lazy("IATI codelist CRSChannelCode", "Conservation International"),
    )
    CLINTON_HEALTH_ACCESS_INITIATIVE__INC_ = (
        21064,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Clinton Health Access Initiative, Inc."
        ),
    )
    OXFAM_INTERNATIONAL = (
        21501,
        pgettext_lazy("IATI codelist CRSChannelCode", "OXFAM International"),
    )
    WORLD_VISION = (
        21502,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Vision"),
    )
    FAMILY_HEALTH_INTERNATIONAL_360 = (
        21503,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Family Health International 360"
        ),
    )
    INTERNATIONAL_RELIEF_AND_DEVELOPMENT = (
        21504,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Relief and Development"
        ),
    )
    SAVE_THE_CHILDREN = (
        21505,
        pgettext_lazy("IATI codelist CRSChannelCode", "Save the Children"),
    )
    INTERNATIONAL_RESCUE_COMMITTEE = (
        21506,
        pgettext_lazy("IATI codelist CRSChannelCode", "International Rescue Committee"),
    )
    PACT_WORLD = (
        21507,
        pgettext_lazy("IATI codelist CRSChannelCode", "Pact World"),
    )
    DONOR_COUNTRY_BASED_NGO = (
        22000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Donor country-based NGO"),
    )
    OXFAM_PROVIDER_COUNTRY_OFFICE = (
        22501,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "OXFAM - provider country office"
        ),
    )
    SAVE_THE_CHILDREN_DONOR_COUNTRY_OFFICE = (
        22502,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Save the Children - donor country office"
        ),
    )
    DEVELOPING_COUNTRY_BASED_NGO = (
        23000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Developing country-based NGO"),
    )
    NATIONAL_RED_CROSS_AND_RED_CRESCENT_SOCIETIES = (
        23501,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "National Red Cross and Red Crescent Societies",
        ),
    )
    PUBLIC_PRIVATE_PARTNERSHIPS__PPP__AND_NETWORKS = (
        30000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Public-Private Partnerships (PPP) and Networks",
        ),
    )
    GLOBAL_ALLIANCE_FOR_IMPROVED_NUTRITION = (
        30001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Global Alliance for Improved Nutrition"
        ),
    )
    GLOBAL_E_SCHOOLS_AND_COMMUNITIES_INITIATIVE = (
        30003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global e-Schools and Communities Initiative",
        ),
    )
    GLOBAL_WATER_PARTNERSHIP = (
        30004,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Water Partnership"),
    )
    INTERNATIONAL_AIDS_VACCINE_INITIATIVE = (
        30005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International AIDS Vaccine Initiative"
        ),
    )
    INTERNATIONAL_PARTNERSHIP_ON_MICROBICIDES = (
        30006,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Partnership on Microbicides"
        ),
    )
    GLOBAL_ALLIANCE_FOR_ICT_AND_DEVELOPMENT = (
        30007,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Global Alliance for ICT and Development"
        ),
    )
    CITIES_ALLIANCE = (
        30008,
        pgettext_lazy("IATI codelist CRSChannelCode", "Cities Alliance"),
    )
    SMALL_ARMS_SURVEY = (
        30009,
        pgettext_lazy("IATI codelist CRSChannelCode", "Small Arms Survey"),
    )
    INTERNATIONAL_DRUG_PURCHASE_FACILITY = (
        30010,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International drug purchase facility"
        ),
    )
    INTERNATIONAL_UNION_FOR_THE_CONSERVATION_OF_NATURE = (
        30011,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Union for the Conservation of Nature",
        ),
    )
    GLOBAL_CLIMATE_PARTNERSHIP_FUND = (
        30012,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Global Climate Partnership Fund"
        ),
    )
    MICROFINANCE_ENHANCEMENT_FACILITY = (
        30013,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Microfinance Enhancement Facility"
        ),
    )
    REGIONAL_MICRO__SMALL_AND_MEDIUM_ENTERPRISE_INVESTMENT_FUND_FOR_SUB_SAHARAN_AFRICA = (
        30014,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Regional Micro, Small and Medium Enterprise Investment Fund for Sub-Saharan Africa",
        ),
    )
    GLOBAL_ENERGY_EFFICIENCY_AND_RENEWABLE_ENERGY_FUND = (
        30015,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Energy Efficiency and Renewable Energy Fund",
        ),
    )
    EUROPEAN_FUND_FOR_SOUTHEAST_EUROPE = (
        30016,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "European Fund for Southeast Europe"
        ),
    )
    SANAD_FUND_FOR_MICRO__SMALL_AND_MEDIUM_ENTERPRISES = (
        30017,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "SANAD Fund for Micro, Small and Medium Enterprises",
        ),
    )
    PUBLIC_PRIVATE_PARTNERSHIPS__PPP_ = (
        31000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Public-Private Partnerships (PPP)"
        ),
    )
    GLOBAL_DEVELOPMENT_NETWORK = (
        31001,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Development Network"),
    )
    GLOBAL_KNOWLEDGE_PARTNERSHIP = (
        31002,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Knowledge Partnership"),
    )
    INTERNATIONAL_LAND_COALITION = (
        31003,
        pgettext_lazy("IATI codelist CRSChannelCode", "International Land Coalition"),
    )
    EXTRACTIVE_INDUSTRIES_TRANSPARENCY_INITIATIVE_INTERNATIONAL_SECRETARIAT = (
        31004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Extractive Industries Transparency Initiative International Secretariat",
        ),
    )
    PARLIAMENTARY_NETWORK_ON_THE_WORLD_BANK = (
        31005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Parliamentary Network on the World Bank"
        ),
    )
    COALITION_FOR_EPIDEMIC_PREPAREDNESS_INNOVATIONS = (
        31006,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Coalition for Epidemic Preparedness Innovations",
        ),
    )
    NETWORKS = (
        32000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Networks"),
    )
    MULTILATERAL_ORGANISATIONS = (
        40000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Multilateral Organisations"),
    )
    UNITED_NATIONS__UN__AGENCY__FUND_OR_COMMISSION = (
        41000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations (UN) agency, fund or commission",
        ),
    )
    CONVENTION_TO_COMBAT_DESERTIFICATION = (
        41101,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Convention to Combat Desertification"
        ),
    )
    DESERT_LOCUST_CONTROL_ORGANISATION_FOR_EASTERN_AFRICA = (
        41102,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Desert Locust Control Organisation for Eastern Africa",
        ),
    )
    ECONOMIC_COMMISSION_FOR_AFRICA = (
        41103,
        pgettext_lazy("IATI codelist CRSChannelCode", "Economic Commission for Africa"),
    )
    ECONOMIC_COMMISSION_FOR_LATIN_AMERICA_AND_THE_CARIBBEAN = (
        41104,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Economic Commission for Latin America and the Caribbean",
        ),
    )
    ECONOMIC_AND_SOCIAL_COMMISSION_FOR_WESTERN_ASIA = (
        41105,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Economic and Social Commission for Western Asia",
        ),
    )
    ECONOMIC_AND_SOCIAL_COMMISSION_FOR_ASIA_AND_THE_PACIFIC = (
        41106,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Economic and Social Commission for Asia and the Pacific",
        ),
    )
    INTERNATIONAL_ATOMIC_ENERGY_AGENCY__CONTRIBUTIONS_TO_TECHNICAL_COOPERATION_FUND_ONLY_ = (
        41107,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Atomic Energy Agency (Contributions to Technical Cooperation Fund Only)",
        ),
    )
    INTERNATIONAL_FUND_FOR_AGRICULTURAL_DEVELOPMENT = (
        41108,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Fund for Agricultural Development",
        ),
    )
    INTERNATIONAL_RESEARCH_AND_TRAINING_INSTITUTE_FOR_THE_ADVANCEMENT_OF_WOMEN = (
        41109,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Research and Training Institute for the Advancement of Women",
        ),
    )
    JOINT_UNITED_NATIONS_PROGRAMME_ON_HIV_AIDS = (
        41110,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Joint United Nations Programme on HIV/AIDS"
        ),
    )
    UNITED_NATIONS_CAPITAL_DEVELOPMENT_FUND = (
        41111,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Capital Development Fund"
        ),
    )
    UNITED_NATIONS_CONFERENCE_ON_TRADE_AND_DEVELOPMENT = (
        41112,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Conference on Trade and Development",
        ),
    )
    UNITED_NATIONS_DEVELOPMENT_PROGRAMME = (
        41114,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Development Programme"
        ),
    )
    UNITED_NATIONS_ENVIRONMENT_PROGRAMME = (
        41116,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Environment Programme"
        ),
    )
    UNITED_NATIONS_POPULATION_FUND = (
        41119,
        pgettext_lazy("IATI codelist CRSChannelCode", "United Nations Population Fund"),
    )
    UNITED_NATIONS_HUMAN_SETTLEMENT_PROGRAMME = (
        41120,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Human Settlement Programme"
        ),
    )
    UNITED_NATIONS_OFFICE_OF_THE_UNITED_NATIONS_HIGH_COMMISSIONER_FOR_REFUGEES = (
        41121,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Office of the United Nations High Commissioner for Refugees",
        ),
    )
    UNITED_NATIONS_CHILDREN_S_FUND = (
        41122,
        pgettext_lazy("IATI codelist CRSChannelCode", "United Nations Children’s Fund"),
    )
    UNITED_NATIONS_INDUSTRIAL_DEVELOPMENT_ORGANISATION = (
        41123,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Industrial Development Organisation",
        ),
    )
    UNITED_NATIONS_DEVELOPMENT_FUND_FOR_WOMEN = (
        41124,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Development Fund for Women"
        ),
    )
    UNITED_NATIONS_INSTITUTE_FOR_TRAINING_AND_RESEARCH = (
        41125,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Institute for Training and Research",
        ),
    )
    UNITED_NATIONS_MINE_ACTION_SERVICE = (
        41126,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Mine Action Service"
        ),
    )
    UNITED_NATIONS_OFFICE_OF_CO_ORDINATION_OF_HUMANITARIAN_AFFAIRS = (
        41127,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Office of Co-ordination of Humanitarian Affairs",
        ),
    )
    UNITED_NATIONS_OFFICE_ON_DRUGS_AND_CRIME = (
        41128,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Office on Drugs and Crime"
        ),
    )
    UNITED_NATIONS_RESEARCH_INSTITUTE_FOR_SOCIAL_DEVELOPMENT = (
        41129,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Research Institute for Social Development",
        ),
    )
    UNITED_NATIONS_RELIEF_AND_WORKS_AGENCY_FOR_PALESTINE_REFUGEES_IN_THE_NEAR_EAST = (
        41130,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Relief and Works Agency for Palestine Refugees in the Near East",
        ),
    )
    UNITED_NATIONS_SYSTEM_STAFF_COLLEGE = (
        41131,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations System Staff College"
        ),
    )
    UNITED_NATIONS_SYSTEM_STANDING_COMMITTEE_ON_NUTRITION = (
        41132,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations System Standing Committee on Nutrition",
        ),
    )
    UNITED_NATIONS_SPECIAL_INITIATIVE_ON_AFRICA = (
        41133,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Special Initiative on Africa",
        ),
    )
    UNITED_NATIONS_UNIVERSITY__INCLUDING_ENDOWMENT_FUND_ = (
        41134,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations University (including Endowment Fund)",
        ),
    )
    UNITED_NATIONS_VOLUNTEERS = (
        41135,
        pgettext_lazy("IATI codelist CRSChannelCode", "United Nations Volunteers"),
    )
    UNITED_NATIONS_VOLUNTARY_FUND_ON_DISABILITY = (
        41136,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Voluntary Fund on Disability",
        ),
    )
    UNITED_NATIONS_VOLUNTARY_FUND_FOR_TECHNICAL_CO_OPERATION_IN_THE_FIELD_OF_HUMAN_RIGHTS = (
        41137,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Voluntary Fund for Technical Co-operation in the Field of Human Rights",
        ),
    )
    UNITED_NATIONS_VOLUNTARY_FUND_FOR_VICTIMS_OF_TORTURE = (
        41138,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Voluntary Fund for Victims of Torture",
        ),
    )
    WORLD_FOOD_PROGRAMME = (
        41140,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Food Programme"),
    )
    UNITED_NATIONS_PEACEBUILDING_FUND__WINDOW_TWO__RESTRICTED_CONTRIBUTIONS_ONLY_ = (
        41141,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Peacebuilding Fund (Window Two:  Restricted Contributions Only)",
        ),
    )
    UNITED_NATIONS_DEMOCRACY_FUND = (
        41142,
        pgettext_lazy("IATI codelist CRSChannelCode", "United Nations Democracy Fund"),
    )
    WORLD_HEALTH_ORGANISATION_CORE_VOLUNTARY_CONTRIBUTIONS_ACCOUNT = (
        41143,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Health Organisation - core voluntary contributions account",
        ),
    )
    INTERNATIONAL_LABOUR_ORGANISATION_REGULAR_BUDGET_SUPPLEMENTARY_ACCOUNT = (
        41144,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Labour Organisation - Regular Budget Supplementary Account",
        ),
    )
    INTERNATIONAL_MARITIME_ORGANIZATION_TECHNICAL_CO_OPERATION_FUND = (
        41145,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Maritime Organization - Technical Co-operation Fund",
        ),
    )
    UNITED_NATIONS_ENTITY_FOR_GENDER_EQUALITY_AND_THE_EMPOWERMENT_OF_WOMEN = (
        41146,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Entity for Gender Equality and the Empowerment of Women",
        ),
    )
    CENTRAL_EMERGENCY_RESPONSE_FUND = (
        41147,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Central Emergency Response Fund"
        ),
    )
    UNITED_NATIONS_DEPARTMENT_OF_POLITICAL_AFFAIRS__TRUST_FUND_IN_SUPPORT_OF_POLITICAL_AFFAIRS = (
        41148,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Department of Political Affairs, Trust Fund in Support of Political Affairs",
        ),
    )
    UNITED_NATIONS_DEVELOPMENT_COORDINATION_OFFICE = (
        41149,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Development Coordination Office",
        ),
    )
    UNITED_NATIONS_INSTITUTE_FOR_DISARMAMENT_RESEARCH = (
        41150,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Institute for Disarmament Research",
        ),
    )
    OTHER_UN__CORE_CONTRIBUTIONS_REPORTABLE_IN_PART_ = (
        41300,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Other UN (Core Contributions Reportable in Part)",
        ),
    )
    FOOD_AND_AGRICULTURAL_ORGANISATION = (
        41301,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Food and Agricultural Organisation"
        ),
    )
    INTERNATIONAL_LABOUR_ORGANISATION_ASSESSED_CONTRIBUTIONS = (
        41302,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Labour Organisation - Assessed Contributions",
        ),
    )
    INTERNATIONAL_TELECOMMUNICATIONS_UNION = (
        41303,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Telecommunications Union"
        ),
    )
    UNITED_NATIONS_EDUCATIONAL__SCIENTIFIC_AND_CULTURAL_ORGANISATION = (
        41304,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Educational, Scientific and Cultural Organisation",
        ),
    )
    UNITED_NATIONS = (
        41305,
        pgettext_lazy("IATI codelist CRSChannelCode", "United Nations"),
    )
    UNIVERSAL_POSTAL_UNION = (
        41306,
        pgettext_lazy("IATI codelist CRSChannelCode", "Universal Postal Union"),
    )
    WORLD_HEALTH_ORGANISATION_ASSESSED_CONTRIBUTIONS = (
        41307,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Health Organisation - assessed contributions",
        ),
    )
    WORLD_INTELLECTUAL_PROPERTY_ORGANISATION = (
        41308,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "World Intellectual Property Organisation"
        ),
    )
    WORLD_METEOROLOGICAL_ORGANISATION = (
        41309,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "World Meteorological Organisation"
        ),
    )
    UNITED_NATIONS_DEPARTMENT_OF_PEACEKEEPING_OPERATIONS__ONLY_MINURSO__MINUSCA__MINUSMA__MINUJUSTH__MONUSCO__UNAMID__UNIFIL__UNISFA__UNMIK__UNMIL__UNMISS__UNOCI___REPORT_CONTRIBUTIONS_MISSION_BY_MISSION_IN_CRS___ = (
        41310,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Department of Peacekeeping Operations [only MINURSO, MINUSCA, MINUSMA, MINUJUSTH, MONUSCO, UNAMID, UNIFIL, UNISFA, UNMIK, UNMIL, UNMISS, UNOCI]. Report contributions mission by mission in CRS++.",
        ),
    )
    UNITED_NATIONS_PEACEBUILDING_FUND__WINDOW_ONE__FLEXIBLE_CONTRIBUTIONS_ONLY_ = (
        41311,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Peacebuilding Fund (Window One:  Flexible Contributions Only)",
        ),
    )
    INTERNATIONAL_ATOMIC_ENERGY_AGENCY_ASSESSED_CONTRIBUTIONS = (
        41312,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Atomic Energy Agency - assessed contributions",
        ),
    )
    UNITED_NATIONS_HIGH_COMMISSIONER_FOR_HUMAN_RIGHTS__EXTRABUDGETARY_CONTRIBUTIONS_ONLY_ = (
        41313,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations High Commissioner for Human Rights (extrabudgetary contributions only)",
        ),
    )
    UNITED_NATIONS_ECONOMIC_COMMISSION_FOR_EUROPE__EXTRABUDGETARY_CONTRIBUTIONS_ONLY_ = (
        41314,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Economic Commission for Europe (extrabudgetary contributions only)",
        ),
    )
    UNITED_NATIONS_INTERNATIONAL_STRATEGY_FOR_DISASTER_REDUCTION = (
        41315,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations International Strategy for Disaster Reduction",
        ),
    )
    UNITED_NATIONS_FRAMEWORK_CONVENTION_ON_CLIMATE_CHANGE = (
        41316,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Framework Convention on Climate Change",
        ),
    )
    GREEN_CLIMATE_FUND = (
        41317,
        pgettext_lazy("IATI codelist CRSChannelCode", "Green Climate Fund"),
    )
    GLOBAL_MECHANISM = (
        41318,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Mechanism"),
    )
    WORLD_TOURISM_ORGANIZATION = (
        41319,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Tourism Organization"),
    )
    TECHNOLOGY_BANK_FOR_LEAST_DEVELOPED_COUNTRIES = (
        41320,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Technology Bank for Least Developed Countries",
        ),
    )
    UNITED_NATIONS_REDUCING_EMISSIONS_FROM_DEFORESTATION_AND_FOREST_DEGRADATION = (
        41501,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Nations Reducing Emissions from Deforestation and Forest Degradation",
        ),
    )
    UNITED_NATIONS_OFFICE_FOR_PROJECT_SERVICES = (
        41502,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "United Nations Office for Project Services"
        ),
    )
    UN_LED_COUNTRY_BASED_POOLED_FUNDS = (
        41503,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "UN-led Country-based Pooled Funds"
        ),
    )
    EUROPEAN_UNION_INSTITUTIONS = (
        42000,
        pgettext_lazy("IATI codelist CRSChannelCode", "European Union Institutions"),
    )
    EUROPEAN_COMMISSION_DEVELOPMENT_SHARE_OF_BUDGET = (
        42001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Commission - Development Share of Budget",
        ),
    )
    EUROPEAN_COMMISSION_EUROPEAN_DEVELOPMENT_FUND = (
        42003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Commission - European Development Fund",
        ),
    )
    EUROPEAN_INVESTMENT_BANK = (
        42004,
        pgettext_lazy("IATI codelist CRSChannelCode", "European Investment Bank"),
    )
    FACILITY_FOR_EURO_MEDITERRANEAN_INVESTMENT_AND_PARTNERSHIP_TRUST_FUND = (
        42005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Facility for Euro-Mediterranean Investment and Partnership Trust Fund",
        ),
    )
    INTERNATIONAL_MONETARY_FUND__IMF_ = (
        43000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Monetary Fund (IMF)"
        ),
    )
    INTERNATIONAL_MONETARY_FUND_POVERTY_REDUCTION_AND_GROWTH_TRUST = (
        43001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Monetary Fund - Poverty Reduction and Growth Trust",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_POVERTY_REDUCTION_AND_GROWTH_HEAVILY_INDEBTED_POOR_COUNTRIES_DEBT_RELIEF_INITIATIVE_TRUST_FUND__INCLUDES_HIPC__EXTENDED_CREDIT_FACILITY__ECF___AND_ECF_HIPC_SUB_ACCOUNTS_ = (
        43002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Monetary Fund - Poverty Reduction and Growth - Heavily Indebted Poor Countries Debt Relief Initiative Trust Fund [includes HIPC, Extended Credit Facility (ECF), and ECF-HIPC sub-accounts]",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_SUBSIDIZATION_OF_EMERGENCY_POST_CONFLICT_ASSISTANCE_EMERGENCY_ASSISTANCE_FOR_NATURAL_DISASTERS_FOR_PRGT_ELIGIBLE_MEMBERS = (
        43003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Monetary Fund - Subsidization of Emergency Post Conflict Assistance/Emergency Assistance for Natural Disasters for PRGT-eligible members",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_POVERTY_REDUCTION_AND_GROWTH_MULTILATERAL_DEBT_RELIEF_INITIATIVE_TRUST = (
        43004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Monetary Fund - Poverty Reduction and Growth - Multilateral Debt Relief Initiative Trust",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_POST_CATASTROPHE_DEBT_RELIEF_TRUST = (
        43005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Monetary Fund - Post-Catastrophe Debt Relief Trust",
        ),
    )
    CATASTROPHE_CONTAINMENT_AND_RELIEF_TRUST = (
        43006,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Catastrophe Containment and Relief Trust"
        ),
    )
    WORLD_BANK_GROUP__WB_ = (
        44000,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Bank Group (WB)"),
    )
    INTERNATIONAL_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT = (
        44001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Bank for Reconstruction and Development",
        ),
    )
    INTERNATIONAL_DEVELOPMENT_ASSOCIATION = (
        44002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Development Association"
        ),
    )
    INTERNATIONAL_DEVELOPMENT_ASSOCIATION_HEAVILY_INDEBTED_POOR_COUNTRIES_DEBT_INITIATIVE_TRUST_FUND = (
        44003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Development Association - Heavily Indebted Poor Countries Debt Initiative Trust Fund",
        ),
    )
    INTERNATIONAL_FINANCE_CORPORATION = (
        44004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Finance Corporation"
        ),
    )
    MULTILATERAL_INVESTMENT_GUARANTEE_AGENCY = (
        44005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Multilateral Investment Guarantee Agency"
        ),
    )
    ADVANCE_MARKET_COMMITMENTS = (
        44006,
        pgettext_lazy("IATI codelist CRSChannelCode", "Advance Market Commitments"),
    )
    INTERNATIONAL_DEVELOPMENT_ASSOCIATION_MULTILATERAL_DEBT_RELIEF_INITIATIVE = (
        44007,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Development Association - Multilateral Debt Relief Initiative",
        ),
    )
    WORLD_TRADE_ORGANISATION__WTO_ = (
        45000,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Trade Organisation (WTO)"),
    )
    WORLD_TRADE_ORGANISATION_INTERNATIONAL_TRADE_CENTRE = (
        45001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Trade Organisation - International Trade Centre",
        ),
    )
    WORLD_TRADE_ORGANISATION_ADVISORY_CENTRE_ON_WTO_LAW = (
        45002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Trade Organisation - Advisory Centre on WTO Law",
        ),
    )
    WORLD_TRADE_ORGANISATION_DOHA_DEVELOPMENT_AGENDA_GLOBAL_TRUST_FUND = (
        45003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Trade Organisation - Doha Development Agenda Global Trust Fund",
        ),
    )
    REGIONAL_DEVELOPMENT_BANKS = (
        46000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Regional Development Banks"),
    )
    AFRICAN_DEVELOPMENT_BANK = (
        46002,
        pgettext_lazy("IATI codelist CRSChannelCode", "African Development Bank"),
    )
    AFRICAN_DEVELOPMENT_FUND = (
        46003,
        pgettext_lazy("IATI codelist CRSChannelCode", "African Development Fund"),
    )
    ASIAN_DEVELOPMENT_BANK = (
        46004,
        pgettext_lazy("IATI codelist CRSChannelCode", "Asian Development Bank"),
    )
    ASIAN_DEVELOPMENT_FUND = (
        46005,
        pgettext_lazy("IATI codelist CRSChannelCode", "Asian Development Fund"),
    )
    BLACK_SEA_TRADE_AND_DEVELOPMENT_BANK = (
        46006,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Black Sea Trade and Development Bank"
        ),
    )
    CENTRAL_AMERICAN_BANK_FOR_ECONOMIC_INTEGRATION = (
        46007,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Central American Bank for Economic Integration",
        ),
    )
    DEVELOPMENT_BANK_OF_LATIN_AMERICA = (
        46008,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Development Bank of Latin America"
        ),
    )
    CARIBBEAN_DEVELOPMENT_BANK = (
        46009,
        pgettext_lazy("IATI codelist CRSChannelCode", "Caribbean Development Bank"),
    )
    INTER_AMERICAN_DEVELOPMENT_BANK__INTER_AMERICAN_INVESTMENT_CORPORATION_AND_MULTILATERAL_INVESTMENT_FUND = (
        46012,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Inter-American Development Bank, Inter-American Investment Corporation and Multilateral Investment Fund",
        ),
    )
    INTER_AMERICAN_DEVELOPMENT_BANK__FUND_FOR_SPECIAL_OPERATIONS = (
        46013,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Inter-American Development Bank, Fund for Special Operations",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT = (
        46015,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Bank for Reconstruction and Development",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT___TECHNICAL_CO_OPERATION_AND_SPECIAL_FUNDS__ODA_ELIGIBLE_COUNTRIES_ONLY_ = (
        46016,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Bank for Reconstruction and Development – technical co-operation and special funds (ODA-eligible countries only)",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT___TECHNICAL_CO_OPERATION_AND_SPECIAL_FUNDS__ALL_EBRD_COUNTRIES_OF_OPERATIONS_ = (
        46017,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Bank for Reconstruction and Development – technical co-operation and special funds (all EBRD countries of operations)",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT_EARLY_TRANSITION_COUNTRIES_FUND = (
        46018,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Bank for Reconstruction and Development - Early Transition Countries Fund",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT_WESTERN_BALKANS_JOINT_TRUST_FUND = (
        46019,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Bank for Reconstruction and Development - Western Balkans Joint Trust Fund",
        ),
    )
    CENTRAL_AFRICAN_STATES_DEVELOPMENT_BANK = (
        46020,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Central African States Development Bank"
        ),
    )
    WEST_AFRICAN_DEVELOPMENT_BANK = (
        46021,
        pgettext_lazy("IATI codelist CRSChannelCode", "West African Development Bank"),
    )
    AFRICAN_EXPORT_IMPORT_BANK = (
        46022,
        pgettext_lazy("IATI codelist CRSChannelCode", "African Export Import Bank"),
    )
    EASTERN_AND_SOUTHERN_AFRICAN_TRADE_AND_DEVELOPMENT_BANK = (
        46023,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Eastern and Southern African Trade and Development Bank",
        ),
    )
    COUNCIL_OF_EUROPE_DEVELOPMENT_BANK = (
        46024,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Council of Europe Development Bank"
        ),
    )
    ISLAMIC_DEVELOPMENT_BANK = (
        46025,
        pgettext_lazy("IATI codelist CRSChannelCode", "Islamic Development Bank"),
    )
    ASIAN_INFRASTRUCTURE_INVESTMENT_BANK = (
        46026,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Asian Infrastructure Investment Bank"
        ),
    )
    FINANCIAL_FUND_FOR_THE_DEVELOPMENT_OF_THE_RIVER_PLATE_BASIN = (
        46027,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Financial Fund for the Development of the River Plate Basin",
        ),
    )
    OTHER_MULTILATERAL_INSTITUTIONS = (
        47000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Other multilateral institutions"
        ),
    )
    AFRICAN_CAPACITY_BUILDING_FOUNDATION = (
        47001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "African Capacity Building Foundation"
        ),
    )
    ASIAN_PRODUCTIVITY_ORGANISATION = (
        47002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Asian Productivity Organisation"
        ),
    )
    ASSOCIATION_OF_SOUTH_EAST_ASIAN_NATIONS__ECONOMIC_CO_OPERATION = (
        47003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Association of South East Asian Nations: Economic Co-operation",
        ),
    )
    ASEAN_CULTURAL_FUND = (
        47004,
        pgettext_lazy("IATI codelist CRSChannelCode", "ASEAN Cultural Fund"),
    )
    AFRICAN_UNION__EXCLUDING_PEACEKEEPING_FACILITIES_ = (
        47005,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "African Union (excluding peacekeeping facilities)",
        ),
    )
    WORLD_VEGETABLE_CENTRE = (
        47008,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Vegetable Centre"),
    )
    AFRICAN_AND_MALAGASY_COUNCIL_FOR_HIGHER_EDUCATION = (
        47009,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "African and Malagasy Council for Higher Education",
        ),
    )
    COMMONWEALTH_AGENCY_FOR_PUBLIC_ADMINISTRATION_AND_MANAGEMENT = (
        47010,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Commonwealth Agency for Public Administration and Management",
        ),
    )
    CARIBBEAN_COMMUNITY_SECRETARIAT = (
        47011,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Caribbean Community Secretariat"
        ),
    )
    CARIBBEAN_EPIDEMIOLOGY_CENTRE = (
        47012,
        pgettext_lazy("IATI codelist CRSChannelCode", "Caribbean Epidemiology Centre"),
    )
    COMMONWEALTH_FOUNDATION = (
        47013,
        pgettext_lazy("IATI codelist CRSChannelCode", "Commonwealth Foundation"),
    )
    COMMONWEALTH_FUND_FOR_TECHNICAL_CO_OPERATION = (
        47014,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Commonwealth Fund for Technical Co-operation",
        ),
    )
    CGIAR_FUND = (
        47015,
        pgettext_lazy("IATI codelist CRSChannelCode", "CGIAR Fund"),
    )
    COMMONWEALTH_INSTITUTE = (
        47016,
        pgettext_lazy("IATI codelist CRSChannelCode", "Commonwealth Institute"),
    )
    INTERNATIONAL_CENTRE_FOR_TROPICAL_AGRICULTURE = (
        47017,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Tropical Agriculture",
        ),
    )
    CENTRE_FOR_INTERNATIONAL_FORESTRY_RESEARCH = (
        47018,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Centre for International Forestry Research"
        ),
    )
    INTERNATIONAL_CENTRE_FOR_ADVANCED_MEDITERRANEAN_AGRONOMIC_STUDIES = (
        47019,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Advanced Mediterranean Agronomic Studies",
        ),
    )
    INTERNATIONAL_MAIZE_AND_WHEAT_IMPROVEMENT_CENTRE = (
        47020,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Maize and Wheat Improvement Centre",
        ),
    )
    INTERNATIONAL_POTATO_CENTRE = (
        47021,
        pgettext_lazy("IATI codelist CRSChannelCode", "International Potato Centre"),
    )
    CONVENTION_ON_INTERNATIONAL_TRADE_IN_ENDANGERED_SPECIES_OF_WILD_FLORA_AND_FAUNA = (
        47022,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Convention on International Trade in Endangered Species of Wild Flora and Fauna",
        ),
    )
    COMMONWEALTH_LEGAL_ADVISORY_SERVICE = (
        47023,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Commonwealth Legal Advisory Service"
        ),
    )
    COMMONWEALTH_MEDIA_DEVELOPMENT_FUND = (
        47024,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Commonwealth Media Development Fund"
        ),
    )
    COMMONWEALTH_OF_LEARNING = (
        47025,
        pgettext_lazy("IATI codelist CRSChannelCode", "Commonwealth of Learning"),
    )
    COMMUNITY_OF_PORTUGUESE_SPEAKING_COUNTRIES = (
        47026,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Community of Portuguese Speaking Countries"
        ),
    )
    COLOMBO_PLAN = (
        47027,
        pgettext_lazy("IATI codelist CRSChannelCode", "Colombo Plan"),
    )
    COMMONWEALTH_PARTNERSHIP_FOR_TECHNICAL_MANAGEMENT = (
        47028,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Commonwealth Partnership for Technical Management",
        ),
    )
    SAHEL_AND_WEST_AFRICA_CLUB = (
        47029,
        pgettext_lazy("IATI codelist CRSChannelCode", "Sahel and West Africa Club"),
    )
    COMMONWEALTH_SCIENTIFIC_COUNCIL = (
        47030,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Commonwealth Scientific Council"
        ),
    )
    COMMONWEALTH_SMALL_STATES_OFFICE = (
        47031,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Commonwealth Small States Office"
        ),
    )
    COMMONWEALTH_TRADE_AND_INVESTMENT_ACCESS_FACILITY = (
        47032,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Commonwealth Trade and Investment Access Facility",
        ),
    )
    COMMONWEALTH_YOUTH_PROGRAMME = (
        47033,
        pgettext_lazy("IATI codelist CRSChannelCode", "Commonwealth Youth Programme"),
    )
    ECONOMIC_COMMUNITY_OF_WEST_AFRICAN_STATES = (
        47034,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Economic Community of West African States"
        ),
    )
    ENVIRONMENTAL_DEVELOPMENT_ACTION_IN_THE_THIRD_WORLD = (
        47035,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Environmental Development Action in the Third World",
        ),
    )
    EUROPEAN_AND_MEDITERRANEAN_PLANT_PROTECTION_ORGANISATION = (
        47036,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European and Mediterranean Plant Protection Organisation",
        ),
    )
    EASTERN_REGIONAL_ORGANISATION_OF_PUBLIC_ADMINISTRATION = (
        47037,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Eastern-Regional Organisation of Public Administration",
        ),
    )
    INTERPOL_FUND_FOR_AID_AND_TECHNICAL_ASSISTANCE_TO_DEVELOPING_COUNTRIES = (
        47038,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "INTERPOL Fund for Aid and Technical Assistance to Developing Countries",
        ),
    )
    FORUM_FISHERIES_AGENCY = (
        47040,
        pgettext_lazy("IATI codelist CRSChannelCode", "Forum Fisheries Agency"),
    )
    FOOD_AND_FERTILIZER_TECHNOLOGY_CENTRE = (
        47041,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Food and Fertilizer Technology Centre"
        ),
    )
    FOUNDATION_FOR_INTERNATIONAL_TRAINING = (
        47042,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Foundation for International Training"
        ),
    )
    GLOBAL_CROP_DIVERSITY_TRUST = (
        47043,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Crop Diversity Trust"),
    )
    GLOBAL_ENVIRONMENT_FACILITY_TRUST_FUND = (
        47044,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Global Environment Facility Trust Fund"
        ),
    )
    GLOBAL_FUND_TO_FIGHT_AIDS__TUBERCULOSIS_AND_MALARIA = (
        47045,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Fund to Fight AIDS, Tuberculosis and Malaria",
        ),
    )
    INTERNATIONAL_ORGANISATION_OF_THE_FRANCOPHONIE = (
        47046,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Organisation of the Francophonie",
        ),
    )
    INTERNATIONAL_AFRICAN_INSTITUTE = (
        47047,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International African Institute"
        ),
    )
    INTER_AMERICAN_INDIAN_INSTITUTE = (
        47048,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Inter-American Indian Institute"
        ),
    )
    INTERNATIONAL_BUREAU_OF_EDUCATION_INTERNATIONAL_EDUCATIONAL_REPORTING_SYSTEM__IERS_ = (
        47049,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Bureau of Education - International Educational Reporting System (IERS)",
        ),
    )
    INTERNATIONAL_COTTON_ADVISORY_COMMITTEE = (
        47050,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Cotton Advisory Committee"
        ),
    )
    INTERNATIONAL_CENTRE_FOR_AGRICULTURAL_RESEARCH_IN_DRY_AREAS = (
        47051,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Agricultural Research in Dry Areas",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_DIARRHOEAL_DISEASE_RESEARCH__BANGLADESH = (
        47053,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Diarrhoeal Disease Research, Bangladesh",
        ),
    )
    INTERNATIONAL_CENTRE_OF_INSECT_PHYSIOLOGY_AND_ECOLOGY = (
        47054,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre of Insect Physiology and Ecology",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_DEVELOPMENT_ORIENTED_RESEARCH_IN_AGRICULTURE = (
        47055,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Centre for Development Oriented Research in Agriculture",
        ),
    )
    WORLD_AGROFORESTRY_CENTRE = (
        47056,
        pgettext_lazy("IATI codelist CRSChannelCode", "World AgroForestry Centre"),
    )
    INTERNATIONAL_CROP_RESEARCH_FOR_SEMI_ARID_TROPICS = (
        47057,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Crop Research for Semi-Arid Tropics",
        ),
    )
    INTERNATIONAL_INSTITUTE_FOR_DEMOCRACY_AND_ELECTORAL_ASSISTANCE = (
        47058,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Institute for Democracy and Electoral Assistance",
        ),
    )
    INTERNATIONAL_DEVELOPMENT_LAW_ORGANISATION = (
        47059,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Development Law Organisation"
        ),
    )
    INTERNATIONAL_INSTITUTE_FOR_COTTON = (
        47060,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Institute for Cotton"
        ),
    )
    INTER_AMERICAN_INSTITUTE_FOR_CO_OPERATION_ON_AGRICULTURE = (
        47061,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Inter-American Institute for Co-operation on Agriculture",
        ),
    )
    INTERNATIONAL_INSTITUTE_OF_TROPICAL_AGRICULTURE = (
        47062,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Institute of Tropical Agriculture",
        ),
    )
    INTERNATIONAL_LIVESTOCK_RESEARCH_INSTITUTE = (
        47063,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Livestock Research Institute"
        ),
    )
    INTERNATIONAL_NETWORK_FOR_BAMBOO_AND_RATTAN = (
        47064,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Network for Bamboo and Rattan",
        ),
    )
    INTERGOVERNMENTAL_OCEANOGRAPHIC_COMMISSION = (
        47065,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Intergovernmental Oceanographic Commission"
        ),
    )
    INTERNATIONAL_ORGANISATION_FOR_MIGRATION = (
        47066,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Organisation for Migration"
        ),
    )
    INTERGOVERNMENTAL_PANEL_ON_CLIMATE_CHANGE = (
        47067,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Intergovernmental Panel on Climate Change"
        ),
    )
    ASIA_PACIFIC_FISHERY_COMMISSION = (
        47068,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Asia-Pacific Fishery Commission"
        ),
    )
    BIOVERSITY_INTERNATIONAL = (
        47069,
        pgettext_lazy("IATI codelist CRSChannelCode", "Bioversity International"),
    )
    INTERNATIONAL_RICE_RESEARCH_INSTITUTE = (
        47070,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Rice Research Institute"
        ),
    )
    INTERNATIONAL_SEED_TESTING_ASSOCIATION = (
        47071,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Seed Testing Association"
        ),
    )
    INTERNATIONAL_TROPICAL_TIMBER_ORGANISATION = (
        47073,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Tropical Timber Organisation"
        ),
    )
    INTERNATIONAL_VACCINE_INSTITUTE = (
        47074,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Vaccine Institute"
        ),
    )
    INTERNATIONAL_WATER_MANAGEMENT_INSTITUTE = (
        47075,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Water Management Institute"
        ),
    )
    JUSTICE_STUDIES_CENTRE_OF_THE_AMERICAS = (
        47076,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Justice Studies Centre of the Americas"
        ),
    )
    MEKONG_RIVER_COMMISSION = (
        47077,
        pgettext_lazy("IATI codelist CRSChannelCode", "Mekong River Commission"),
    )
    MULTILATERAL_FUND_FOR_THE_IMPLEMENTATION_OF_THE_MONTREAL_PROTOCOL = (
        47078,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Multilateral Fund for the Implementation of the Montreal Protocol",
        ),
    )
    ORGANISATION_OF_AMERICAN_STATES = (
        47079,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Organisation of American States"
        ),
    )
    ORGANISATION_FOR_ECONOMIC_CO_OPERATION_AND_DEVELOPMENT__CONTRIBUTIONS_TO_SPECIAL_FUNDS_FOR_TECHNICAL_CO_OPERATION_ACTIVITIES_ONLY_ = (
        47080,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Organisation for Economic Co-operation and Development (Contributions to special funds for Technical Co-operation Activities Only)",
        ),
    )
    OECD_DEVELOPMENT_CENTRE = (
        47081,
        pgettext_lazy("IATI codelist CRSChannelCode", "OECD Development Centre"),
    )
    ORGANISATION_OF_EASTERN_CARIBBEAN_STATES = (
        47082,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Organisation of Eastern Caribbean States"
        ),
    )
    PAN_AMERICAN_HEALTH_ORGANISATION = (
        47083,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Pan-American Health Organisation"
        ),
    )
    PAN_AMERICAN_INSTITUTE_OF_GEOGRAPHY_AND_HISTORY = (
        47084,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Pan-American Institute of Geography and History",
        ),
    )
    PAN_AMERICAN_RAILWAY_CONGRESS_ASSOCIATION = (
        47085,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Pan-American Railway Congress Association"
        ),
    )
    PRIVATE_INFRASTRUCTURE_DEVELOPMENT_GROUP = (
        47086,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Private Infrastructure Development Group"
        ),
    )
    PACIFIC_ISLANDS_FORUM_SECRETARIAT = (
        47087,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Pacific Islands Forum Secretariat"
        ),
    )
    RELIEF_NET = (
        47088,
        pgettext_lazy("IATI codelist CRSChannelCode", "Relief Net"),
    )
    SOUTHERN_AFRICAN_DEVELOPMENT_COMMUNITY = (
        47089,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Southern African Development Community"
        ),
    )
    SOUTHERN_AFRICAN_TRANSPORT_AND_COMMUNICATIONS_COMMISSION = (
        47090,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Southern African Transport and Communications Commission",
        ),
    )
    _COLOMBO_PLAN__SPECIAL_COMMONWEALTH_AFRICAN_ASSISTANCE_PROGRAMME = (
        47091,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "(Colombo Plan) Special Commonwealth African Assistance Programme",
        ),
    )
    SOUTH_EAST_ASIAN_FISHERIES_DEVELOPMENT_CENTRE = (
        47092,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "South East Asian Fisheries Development Centre",
        ),
    )
    SOUTH_EAST_ASIAN_MINISTERS_OF_EDUCATION = (
        47093,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "South East Asian Ministers of Education"
        ),
    )
    SOUTH_PACIFIC_APPLIED_GEOSCIENCE_COMMISSION = (
        47094,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "South Pacific Applied Geoscience Commission",
        ),
    )
    SOUTH_PACIFIC_BOARD_FOR_EDUCATIONAL_ASSESSMENT = (
        47095,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "South Pacific Board for Educational Assessment",
        ),
    )
    SECRETARIAT_OF_THE_PACIFIC_COMMUNITY = (
        47096,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Secretariat of the Pacific Community"
        ),
    )
    PACIFIC_REGIONAL_ENVIRONMENT_PROGRAMME = (
        47097,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Pacific Regional Environment Programme"
        ),
    )
    UNREPRESENTED_NATIONS_AND_PEOPLES__ORGANISATION = (
        47098,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Unrepresented Nations and Peoples’ Organisation",
        ),
    )
    UNIVERSITY_OF_THE_SOUTH_PACIFIC = (
        47099,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "University of the South Pacific"
        ),
    )
    WEST_AFRICAN_MONETARY_UNION = (
        47100,
        pgettext_lazy("IATI codelist CRSChannelCode", "West African Monetary Union"),
    )
    AFRICA_RICE_CENTRE = (
        47101,
        pgettext_lazy("IATI codelist CRSChannelCode", "Africa Rice Centre"),
    )
    WORLD_CUSTOMS_ORGANISATION_FELLOWSHIP_PROGRAMME = (
        47102,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Customs Organisation Fellowship Programme",
        ),
    )
    WORLD_MARITIME_UNIVERSITY = (
        47103,
        pgettext_lazy("IATI codelist CRSChannelCode", "World Maritime University"),
    )
    WORLDFISH_CENTRE = (
        47104,
        pgettext_lazy("IATI codelist CRSChannelCode", "WorldFish Centre"),
    )
    COMMON_FUND_FOR_COMMODITIES = (
        47105,
        pgettext_lazy("IATI codelist CRSChannelCode", "Common Fund for Commodities"),
    )
    GENEVA_CENTRE_FOR_THE_DEMOCRATIC_CONTROL_OF_ARMED_FORCES = (
        47106,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Geneva Centre for the Democratic Control of Armed Forces",
        ),
    )
    INTERNATIONAL_FINANCE_FACILITY_FOR_IMMUNISATION = (
        47107,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Finance Facility for Immunisation",
        ),
    )
    MULTI_COUNTRY_DEMOBILISATION_AND_REINTEGRATION_PROGRAM = (
        47108,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Multi-Country Demobilisation and Reintegration Program",
        ),
    )
    ASIA_PACIFIC_ECONOMIC_COOPERATION_SUPPORT_FUND__EXCEPT_CONTRIBUTIONS_TIED_TO_COUNTER_TERRORISM_ACTIVITIES_ = (
        47109,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Asia-Pacific Economic Cooperation Support Fund (except contributions tied to counter-terrorism activities)",
        ),
    )
    ORGANISATION_OF_THE_BLACK_SEA_ECONOMIC_COOPERATION = (
        47110,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Organisation of the Black Sea Economic Cooperation",
        ),
    )
    ADAPTATION_FUND = (
        47111,
        pgettext_lazy("IATI codelist CRSChannelCode", "Adaptation Fund"),
    )
    CENTRAL_EUROPEAN_INITIATIVE_SPECIAL_FUND_FOR_CLIMATE_AND_ENVIRONMENTAL_PROTECTION = (
        47112,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Central European Initiative - Special Fund for Climate and Environmental Protection",
        ),
    )
    ECONOMIC_AND_MONETARY_COMMUNITY_OF_CENTRAL_AFRICA = (
        47113,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Economic and Monetary Community of Central Africa",
        ),
    )
    INTEGRATED_FRAMEWORK_FOR_TRADE_RELATED_TECHNICAL_ASSISTANCE_TO_LEAST_DEVELOPED_COUNTRIES = (
        47116,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Integrated Framework for Trade-Related Technical Assistance to Least Developed Countries",
        ),
    )
    NEW_PARTNERSHIP_FOR_AFRICA_S_DEVELOPMENT = (
        47117,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "New Partnership for Africa's Development"
        ),
    )
    REGIONAL_ORGANISATION_FOR_THE_STRENGTHENING_OF_SUPREME_AUDIT_INSTITUTIONS_OF_FRANCOPHONE_SUB_SAHARAN_COUNTRIES = (
        47118,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Regional Organisation for the Strengthening of Supreme Audit Institutions of Francophone Sub-Saharan Countries",
        ),
    )
    SAHARA_AND_SAHEL_OBSERVATORY = (
        47119,
        pgettext_lazy("IATI codelist CRSChannelCode", "Sahara and Sahel Observatory"),
    )
    SOUTH_ASIAN_ASSOCIATION_FOR_REGIONAL_COOPERATION = (
        47120,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "South Asian Association for Regional Cooperation",
        ),
    )
    UNITED_CITIES_AND_LOCAL_GOVERNMENTS_OF_AFRICA = (
        47121,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "United Cities and Local Governments of Africa",
        ),
    )
    GLOBAL_ALLIANCE_FOR_VACCINES_AND_IMMUNIZATION = (
        47122,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Alliance for Vaccines and Immunization",
        ),
    )
    GENEVA_INTERNATIONAL_CENTRE_FOR_HUMANITARIAN_DEMINING = (
        47123,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Geneva International Centre for Humanitarian Demining",
        ),
    )
    LATIN_AMERICAN_ENERGY_ORGANISATION = (
        47127,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Latin-American Energy Organisation"
        ),
    )
    NORDIC_DEVELOPMENT_FUND = (
        47128,
        pgettext_lazy("IATI codelist CRSChannelCode", "Nordic Development Fund"),
    )
    GLOBAL_ENVIRONMENT_FACILITY_LEAST_DEVELOPED_COUNTRIES_FUND = (
        47129,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Environment Facility - Least Developed Countries Fund",
        ),
    )
    GLOBAL_ENVIRONMENT_FACILITY_SPECIAL_CLIMATE_CHANGE_FUND = (
        47130,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Environment Facility - Special Climate Change Fund",
        ),
    )
    ORGANIZATION_FOR_SECURITY_AND_CO_OPERATION_IN_EUROPE = (
        47131,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Organization for Security and Co-operation in Europe",
        ),
    )
    COMMONWEALTH_SECRETARIAT__ODA_ELIGIBLE_CONTRIBUTIONS_ONLY_ = (
        47132,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Commonwealth Secretariat (ODA-eligible contributions only)",
        ),
    )
    CLEAN_TECHNOLOGY_FUND = (
        47134,
        pgettext_lazy("IATI codelist CRSChannelCode", "Clean Technology Fund"),
    )
    STRATEGIC_CLIMATE_FUND = (
        47135,
        pgettext_lazy("IATI codelist CRSChannelCode", "Strategic Climate Fund"),
    )
    GLOBAL_GREEN_GROWTH_INSTITUTE = (
        47136,
        pgettext_lazy("IATI codelist CRSChannelCode", "Global Green Growth Institute"),
    )
    AFRICAN_RISK_CAPACITY_GROUP = (
        47137,
        pgettext_lazy("IATI codelist CRSChannelCode", "African Risk Capacity Group"),
    )
    COUNCIL_OF_EUROPE = (
        47138,
        pgettext_lazy("IATI codelist CRSChannelCode", "Council of Europe"),
    )
    WORLD_CUSTOMS_ORGANIZATION_CUSTOMS_CO_OPERATION_FUND = (
        47139,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "World Customs Organization Customs Co-operation Fund",
        ),
    )
    ORGANISATION_OF_IBERO_AMERICAN_STATES_FOR_EDUCATION__SCIENCE_AND_CULTURE = (
        47140,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Organisation of Ibero-American States for Education, Science and Culture",
        ),
    )
    AFRICAN_TAX_ADMINISTRATION_FORUM = (
        47141,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "African Tax Administration Forum"
        ),
    )
    OPEC_FUND_FOR_INTERNATIONAL_DEVELOPMENT = (
        47142,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "OPEC Fund for International Development"
        ),
    )
    GLOBAL_COMMUNITY_ENGAGEMENT_AND_RESILIENCE_FUND = (
        47143,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Community Engagement and Resilience Fund",
        ),
    )
    INTERNATIONAL_RENEWABLE_ENERGY_AGENCY = (
        47144,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "International Renewable Energy Agency"
        ),
    )
    CENTER_OF_EXCELLENCE_IN_FINANCE = (
        47145,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Center of Excellence in Finance"
        ),
    )
    INTERNATIONAL_INVESTMENT_BANK = (
        47146,
        pgettext_lazy("IATI codelist CRSChannelCode", "International Investment Bank"),
    )
    INTERNATIONAL_FINANCE_FACILITY_FOR_EDUCATION = (
        47147,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Finance Facility for Education",
        ),
    )
    WORLD_ORGANISATION_FOR_ANIMAL_HEALTH = (
        47148,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "World Organisation for Animal Health"
        ),
    )
    EUROPEAN_SPACE_AGENCY__ESA__PROGRAMME__SPACE_IN_SUPPORT_OF_INTERNATIONAL_DEVELOPMENT_AID_ = (
        47400,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "European Space Agency (ESA) programme 'Space in support of International Development Aid'",
        ),
    )
    GLOBAL_PARTNERSHIP_FOR_EDUCATION = (
        47501,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Global Partnership for Education"
        ),
    )
    GLOBAL_FUND_FOR_DISASTER_RISK_REDUCTION = (
        47502,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Global Fund for Disaster Risk Reduction"
        ),
    )
    GLOBAL_AGRICULTURE_AND_FOOD_SECURITY_PROGRAM = (
        47503,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Global Agriculture and Food Security Program",
        ),
    )
    FOREST_CARBON_PARTNERSHIP_FACILITY = (
        47504,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Forest Carbon Partnership Facility"
        ),
    )
    OTHERS = (
        50000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Others"),
    )
    UNIVERSITY__COLLEGE_OR_OTHER_TEACHING_INSTITUTION__RESEARCH_INSTITUTE_OR_THINK_TANK = (
        51000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "University, college or other teaching institution, research institute or think-tank",
        ),
    )
    INTERNATIONAL_FOOD_POLICY_RESEARCH_INSTITUTE = (
        51001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "International Food Policy Research Institute",
        ),
    )
    OTHER = (
        52000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Other"),
    )
    PRIVATE_SECTOR_INSTITUTIONS = (
        60000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Private Sector Institutions"),
    )
    PRIVATE_SECTOR_IN_PROVIDER_COUNTRY = (
        61000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Private sector in provider country"
        ),
    )
    BANKS__DEPOSIT_TAKING_CORPORATIONS_ = (
        61001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Banks (deposit taking corporations)"
        ),
    )
    PRIVATE_EXPORTER_IN_PROVIDER_COUNTRY = (
        61002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Private exporter in provider country"
        ),
    )
    INVESTMENT_FUNDS_AND_OTHER_COLLECTIVE_INVESTMENT_INSTITUTIONS = (
        61003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Investment funds and other collective investment institutions",
        ),
    )
    HOLDING_COMPANIES__TRUSTS_AND_SPECIAL_PURPOSE_VEHICLES = (
        61004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Holding companies, trusts and Special Purpose Vehicles",
        ),
    )
    INSURANCE_CORPORATIONS = (
        61005,
        pgettext_lazy("IATI codelist CRSChannelCode", "Insurance Corporations"),
    )
    PENSION_FUNDS = (
        61006,
        pgettext_lazy("IATI codelist CRSChannelCode", "Pension Funds"),
    )
    OTHER_FINANCIAL_CORPORATIONS = (
        61007,
        pgettext_lazy("IATI codelist CRSChannelCode", "Other financial corporations"),
    )
    EXPORTERS = (
        61008,
        pgettext_lazy("IATI codelist CRSChannelCode", "Exporters"),
    )
    OTHER_NON_FINANCIAL_CORPORATIONS = (
        61009,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Other non-financial corporations"
        ),
    )
    RETAIL_INVESTORS = (
        61010,
        pgettext_lazy("IATI codelist CRSChannelCode", "Retail investors"),
    )
    PRIVATE_SECTOR_IN_RECIPIENT_COUNTRY = (
        62000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Private sector in recipient country"
        ),
    )
    BANKS__DEPOSIT_TAKING_CORPORATIONS_EXCEPT_MICRO_FINANCE_INSTITUTIONS_ = (
        62001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Banks (deposit taking corporations except Micro Finance Institutions)",
        ),
    )
    MICRO_FINANCE_INSTITUTIONS__DEPOSIT_AND_NON_DEPOSIT_ = (
        62002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Micro Finance Institutions (deposit and non-deposit)",
        ),
    )
    INVESTMENT_FUNDS_AND_OTHER_COLLECTIVE_INVESTMENT_INSTITUTIONS = (
        62003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Investment funds and other collective investment institutions",
        ),
    )
    HOLDING_COMPANIES__TRUSTS_AND_SPECIAL_PURPOSE_VEHICLES = (
        62004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Holding companies, trusts and Special Purpose Vehicles",
        ),
    )
    INSURANCE_CORPORATIONS = (
        62005,
        pgettext_lazy("IATI codelist CRSChannelCode", "Insurance Corporations"),
    )
    PENSION_FUNDS = (
        62006,
        pgettext_lazy("IATI codelist CRSChannelCode", "Pension Funds"),
    )
    OTHER_FINANCIAL_CORPORATIONS = (
        62007,
        pgettext_lazy("IATI codelist CRSChannelCode", "Other financial corporations"),
    )
    IMPORTERS_EXPORTERS = (
        62008,
        pgettext_lazy("IATI codelist CRSChannelCode", "Importers/Exporters"),
    )
    OTHER_NON_FINANCIAL_CORPORATIONS = (
        62009,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Other non-financial corporations"
        ),
    )
    RETAIL_INVESTORS = (
        62010,
        pgettext_lazy("IATI codelist CRSChannelCode", "Retail investors"),
    )
    PRIVATE_SECTOR_IN_THIRD_COUNTRY = (
        63000,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Private sector in third country"
        ),
    )
    BANKS__DEPOSIT_TAKING_CORPORATIONS_EXCEPT_MICRO_FINANCE_INSTITUTIONS_ = (
        63001,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Banks (deposit taking corporations except Micro Finance Institutions)",
        ),
    )
    MICRO_FINANCE_INSTITUTIONS__DEPOSIT_AND_NON_DEPOSIT_ = (
        63002,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Micro Finance Institutions (deposit and non-deposit)",
        ),
    )
    INVESTMENT_FUNDS_AND_OTHER_COLLECTIVE_INVESTMENT_INSTITUTIONS = (
        63003,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Investment funds and other collective investment institutions",
        ),
    )
    HOLDING_COMPANIES__TRUSTS_AND_SPECIAL_PURPOSE_VEHICLES = (
        63004,
        pgettext_lazy(
            "IATI codelist CRSChannelCode",
            "Holding companies, trusts and Special Purpose Vehicles",
        ),
    )
    INSURANCE_CORPORATIONS = (
        63005,
        pgettext_lazy("IATI codelist CRSChannelCode", "Insurance Corporations"),
    )
    PENSION_FUNDS = (
        63006,
        pgettext_lazy("IATI codelist CRSChannelCode", "Pension Funds"),
    )
    OTHER_FINANCIAL_CORPORATIONS = (
        63007,
        pgettext_lazy("IATI codelist CRSChannelCode", "Other financial corporations"),
    )
    EXPORTERS = (
        63008,
        pgettext_lazy("IATI codelist CRSChannelCode", "Exporters"),
    )
    OTHER_NON_FINANCIAL_CORPORATIONS = (
        63009,
        pgettext_lazy(
            "IATI codelist CRSChannelCode", "Other non-financial corporations"
        ),
    )
    RETAIL_INVESTORS = (
        63010,
        pgettext_lazy("IATI codelist CRSChannelCode", "Retail investors"),
    )
    OTHER = (
        90000,
        pgettext_lazy("IATI codelist CRSChannelCode", "Other"),
    )
