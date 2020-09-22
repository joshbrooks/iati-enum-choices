from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationIdentifier(models.TextChoices):
    """
    As of 1.04 this list is no longer maintained. http://support.iatistandard.org/entries/28497976-Retire-the-Organisation-Identifier-codelist#view-post-25368673 For general guidance about constructing Organisation Identifiers, please see http://iatistandard.org/organisation-identifiers/
    """

    FEDERAL_MINISTRY_OF_FINANCE = (
        "AT-1",
        pgettext_lazy("OrganisationIdentifier", "Federal Ministry of Finance"),
    )
    MINISTRY_FOR_AGRICULTURE_AND_ENVIRONMENT = (
        "AT-10",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry for Agriculture and Environment",
        ),
    )
    MINISTRY_OF_DEFENSE = (
        "AT-11",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Defense"),
    )
    MINISTRY_OF_INTERIOR = (
        "AT-12",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Interior"),
    )
    VARIOUS_MINISTRIES = (
        "AT-2",
        pgettext_lazy("OrganisationIdentifier", "Various ministries"),
    )
    FEDERAL_GOVERNMENT_OF_AUSTRIA = (
        "AT-3",
        pgettext_lazy("OrganisationIdentifier", "Federal Government of Austria"),
    )
    OESTERREICHISCHE_KONTROLLBANK_AG = (
        "AT-4",
        pgettext_lazy("OrganisationIdentifier", "Oesterreichische Kontrollbank AG"),
    )
    FEDERAL_MINISTRY_OF_FOREIGN_AFFAIRS = (
        "AT-5",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Federal Ministry of Foreign Affairs",
        ),
    )
    PROVINCIAL_GOVERNMENTS__LOCAL_COMMUNITIES = (
        "AT-6",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Provincial governments, local communities ",
        ),
    )
    AUSTRIAN_DEVELOPMENT_AGENCY = (
        "AT-8",
        pgettext_lazy("OrganisationIdentifier", "Austrian Development Agency"),
    )
    EDUCATION_AND_SCIENCE_MINISTRY = (
        "AT-9",
        pgettext_lazy("OrganisationIdentifier", "Education and Science Ministry"),
    )
    MISCELLANEOUS = (
        "AT-99",
        pgettext_lazy("OrganisationIdentifier", "Miscellaneous"),
    )
    AUSTRALIAN_AGENCY_FOR_INTERNATIONAL_DEVELOPMENT = (
        "AU-5",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Australian Agency for International Development",
        ),
    )
    EXPORT_FINANCE_AND_INSURANCE_CORPORATION = (
        "AU-72",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Export Finance and Insurance Corporation",
        ),
    )
    DIRECTORATE_GENERAL_FOR_CO_OPERATION_AND_DEVELOPMENT = (
        "BE-10",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Directorate General for Co-operation and Development",
        ),
    )
    OFFICIAL_FEDERAL_SERVICE_OF_FOREIGN_AFFAIRS__EXCL__DGCD_ = (
        "BE-20",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Official Federal Service of Foreign Affairs (excl. DGCD)",
        ),
    )
    OFFICIAL_FEDERAL_SERVICE_OF_FINANCE = (
        "BE-30",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Official Federal Service of Finance",
        ),
    )
    DUCROIRE_NATIONAL_OFFICE = (
        "BE-31",
        pgettext_lazy("OrganisationIdentifier", "Ducroire National Office"),
    )
    OTHER_OFFICIAL_FEDERAL_SERVICES = (
        "BE-39",
        pgettext_lazy("OrganisationIdentifier", "Other Official Federal Services"),
    )
    FLANDERS_OFFICIAL_REGIONAL_MINISTRIES = (
        "BE-70",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Flanders Official Regional Ministries",
        ),
    )
    WALLOON_OFFICIAL_REGIONAL_MINISTRIES = (
        "BE-80",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Walloon Official Regional Ministries",
        ),
    )
    BRUSSELS_OFFICIAL_REGIONAL_MINISTRIES = (
        "BE-91",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Brussels Official Regional Ministries",
        ),
    )
    GERMAN_SPEAKING_OFFICIAL_REGIONAL_MINISTRIES = (
        "BE-94",
        pgettext_lazy(
            "OrganisationIdentifier",
            "German speaking Official Regional Ministries",
        ),
    )
    CANADIAN_INTERNATIONAL_DEVELOPMENT_AGENCY = (
        "CA-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Canadian International Development Agency",
        ),
    )
    INTERNATIONAL_DEVELOPMENT_RESEARCH_CENTRE = (
        "CA-2",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Development Research Centre",
        ),
    )
    EXPORT_DEVELOPMENT_CORPORATION = (
        "CA-31",
        pgettext_lazy("OrganisationIdentifier", "Export Development Corporation"),
    )
    DEPARTMENT_OF_FINANCE = (
        "CA-4",
        pgettext_lazy("OrganisationIdentifier", "Department of Finance"),
    )
    FEDERAL_ADMINISTRATION__VARIOUS_DEPARTMENTS_ = (
        "CH-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Federal Administration (various departments)",
        ),
    )
    SWISS_AGENCY_FOR_THE_ENVIRONMENT__FORESTS_AND_LANDSCAPE = (
        "CH-10",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Swiss Agency for the Environment, Forests and Landscape ",
        ),
    )
    MUNICIPALITIES = (
        "CH-11",
        pgettext_lazy("OrganisationIdentifier", "Municipalities"),
    )
    SWISS_AGENCY_FOR_DEVELOPMENT_AND_CO_OPERATION = (
        "CH-4",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Swiss Agency for Development and Co-operation",
        ),
    )
    STATE_SECRETARIAT_FOR_ECONOMIC_AFFAIRS = (
        "CH-5",
        pgettext_lazy(
            "OrganisationIdentifier",
            "State Secretariat for Economic Affairs",
        ),
    )
    FEDERAL_DEPARTMENT_OF_FOREIGN_AFFAIRS = (
        "CH-6",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Federal Department of Foreign Affairs",
        ),
    )
    STATE_SECRETARIAT_FOR_EDUCATION_AND_RESEARCH = (
        "CH-7",
        pgettext_lazy(
            "OrganisationIdentifier",
            "State Secretariat for Education and Research",
        ),
    )
    FEDERAL_OFFICE_FOR_MIGRATION = (
        "CH-8",
        pgettext_lazy("OrganisationIdentifier", "Federal Office for Migration"),
    )
    FEDERAL_DEPARTMENT_FOR_DEFENCE__CIVIL_PROTECTION_AND_SPORTS = (
        "CH-9",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Federal Department for Defence, Civil Protection and Sports ",
        ),
    )
    BUNDESMINISTERIUM_FÜR_WIRTSCHAFTLICHE_ZUSAMMENARBEIT_UND_ENTWICKLUNG = (
        "DE-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Bundesministerium für Wirtschaftliche Zusammenarbeit und Entwicklung",
        ),
    )
    FOREIGN_OFFICE = (
        "DE-11",
        pgettext_lazy("OrganisationIdentifier", "Foreign Office"),
    )
    FEDERAL_STATES___LOCAL_GOVERNMENTS = (
        "DE-12",
        pgettext_lazy("OrganisationIdentifier", "Federal States & Local Governments"),
    )
    FEDERAL_INSTITUTIONS = (
        "DE-14",
        pgettext_lazy("OrganisationIdentifier", "Federal Institutions"),
    )
    FEDERAL_MINISTRIES = (
        "DE-16",
        pgettext_lazy("OrganisationIdentifier", "Federal Ministries"),
    )
    FOUNDATIONS_SOCIETIES_MISC___NON_FEDERAL_ = (
        "DE-17",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Foundations/Societies/Misc. (non federal)",
        ),
    )
    KREDITANSTALT_FÜR_WIEDERAUFBAU = (
        "DE-2",
        pgettext_lazy("OrganisationIdentifier", "Kreditanstalt für Wiederaufbau"),
    )
    HERMES_KREDITVERSICHERUNGS_AG = (
        "DE-34",
        pgettext_lazy("OrganisationIdentifier", "Hermes Kreditversicherungs-AG"),
    )
    GERMAN_INVESTMENT_AND_DEVELOPMENT_COMPANY = (
        "DE-4",
        pgettext_lazy(
            "OrganisationIdentifier",
            "German Investment and Development Company",
        ),
    )
    DEUTSCHE_GESELLSCHAFT_FÜR_TECHNISCHE_ZUSAMMENARBEIT = (
        "DE-52",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Deutsche Gesellschaft für Technische Zusammenarbeit",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "DK-1",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    DANISH_INTERNATIONAL_DEVELOPMENT_AGENCY__NOT_IN_CRS_DIRECTIVES_ = (
        "DK-2",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Danish International Development Agency (Not in CRS Directives)",
        ),
    )
    NOT_IN_CRS_DIRECTIVES = (
        "DK-4",
        pgettext_lazy("OrganisationIdentifier", "Not in CRS Directives"),
    )
    EKR = (
        "DK-72",
        pgettext_lazy("OrganisationIdentifier", "EKR"),
    )
    INSTITUTO_DE_CREDITO_OFICIAL = (
        "ES-1",
        pgettext_lazy("OrganisationIdentifier", "Instituto de Credito Oficial"),
    )
    MINISTRY_OF_ENVIRONMENT = (
        "ES-10",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Environment"),
    )
    MINISTRY_OF_HEALTH = (
        "ES-11",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Health"),
    )
    MINISTRY_OF_LABOUR_AND_SOCIAL_AFFAIRS = (
        "ES-12",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Labour and Social Affairs",
        ),
    )
    MINISTRY_OF_INTERIOR = (
        "ES-13",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Interior"),
    )
    MINISTRY_OF_PUBLIC_ADMINISTRATION = (
        "ES-14",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Public Administration"),
    )
    COMPANIA_ESPANOLA_DE_SEGUROS_DE_CREDITO_A_LA_EXPORTACIÓN = (
        "ES-15",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Compania Espanola de Seguros de Credito a la Exportación",
        ),
    )
    MUNICIPALITIES = (
        "ES-16",
        pgettext_lazy("OrganisationIdentifier", "Municipalities"),
    )
    MISCELLANEOUS = (
        "ES-17",
        pgettext_lazy("OrganisationIdentifier", "Miscellaneous"),
    )
    MINISTRY_OF_SCIENCE_AND_TECHNOLOGY = (
        "ES-18",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Science and Technology"),
    )
    MINISTRY_OF_DEFENSE = (
        "ES-19",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Defense"),
    )
    AUTONOMOUS_GOVERNMENTS = (
        "ES-2",
        pgettext_lazy("OrganisationIdentifier", "Autonomous Governments"),
    )
    MINISTRY_OF_AGRICULTURE__FISHERIES__AND_FOOD = (
        "ES-4",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Agriculture, Fisheries, and Food ",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "ES-5",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    MINISTRY_OF_ECONOMY_AND_FINANCE = (
        "ES-6",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Economy and Finance"),
    )
    MINISTRY_OF_EDUCATION__CULTURE_AND_SPORTS = (
        "ES-7",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Education, Culture and Sports ",
        ),
    )
    MINISTRY_OF_PUBLIC_WORKS = (
        "ES-8",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Public Works"),
    )
    MINISTRY_OF_INDUSTRY_AND_ENERGY = (
        "ES-9",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Industry and Energy"),
    )
    COMMISSION_OF_THE_EUROPEAN_COMMUNITIES = (
        "EU-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commission of the European Communities",
        ),
    )
    EUROPEAN_DEVELOPMENT_FUND = (
        "EU-2",
        pgettext_lazy("OrganisationIdentifier", "European Development Fund"),
    )
    EUROPEAN_INVESTMENT_BANK = (
        "EU-3",
        pgettext_lazy("OrganisationIdentifier", "European Investment Bank"),
    )
    HUMANITARIAN_AID_OFFICE_OF_THE_EUROPEAN_COMMISSION = (
        "EU-4",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Humanitarian Aid Office of the European Commission",
        ),
    )
    FINNISH_GOVERNMENT = (
        "FI-1",
        pgettext_lazy("OrganisationIdentifier", "Finnish Government"),
    )
    FINNFUND = (
        "FI-2",
        pgettext_lazy("OrganisationIdentifier", "FinnFund"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "FI-3",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    FIDE = (
        "FI-4",
        pgettext_lazy("OrganisationIdentifier", "FIDE"),
    )
    FINNVERA = (
        "FI-72",
        pgettext_lazy("OrganisationIdentifier", "FinnVera"),
    )
    MINISTRY_OF_ECONOMY__FINANCE_AND_INDUSTRY = (
        "FR-10",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Economy, Finance and Industry ",
        ),
    )
    MINISTRY_OF_EDUCATION__HIGHER_EDUCATION_AND_RESEARCH = (
        "FR-17",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Education, Higher education and Research ",
        ),
    )
    FRENCH_DEVELOPMENT_AGENCY = (
        "FR-3",
        pgettext_lazy("OrganisationIdentifier", "French Development Agency"),
    )
    COFACE = (
        "FR-43",
        pgettext_lazy("OrganisationIdentifier", "Coface"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "FR-6",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    DEPARTMENT_FOR_INTERNATIONAL_DEVELOPMENT = (
        "GB-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Department for International Development",
        ),
    )
    CDC_CAPITAL_PARTNERS_PLC = (
        "GB-2",
        pgettext_lazy("OrganisationIdentifier", "CDC Capital Partners PLC"),
    )
    EXPORT_CREDIT_GUARANTEE_DEPARTMENT = (
        "GB-5",
        pgettext_lazy("OrganisationIdentifier", "Export Credit Guarantee Department"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "GR-1",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    MINISTRY_OF_NATIONAL_ECONOMY = (
        "GR-2",
        pgettext_lazy("OrganisationIdentifier", "Ministry of National Economy"),
    )
    MISCELLANEOUS = (
        "GR-20",
        pgettext_lazy("OrganisationIdentifier", "Miscellaneous"),
    )
    MINISTRY_OF_THE_INTERIOR__PUBLIC_ADMINISTRATION_AND_DECENTRALISATION = (
        "GR-3",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of the Interior, Public Administration and Decentralisation ",
        ),
    )
    MINISTRY_OF_NATIONAL_DEFENCE = (
        "GR-4",
        pgettext_lazy("OrganisationIdentifier", "Ministry of National Defence"),
    )
    MINISTRY_OF_THE_ENVIRONMENT__LAND_PLANNING_AND_PUBLIC_WORKS = (
        "GR-5",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of the Environment, Land Planning and Public Works ",
        ),
    )
    MINISTRY_OF_NATIONAL_EDUCATION_AND_RELIGIONS = (
        "GR-6",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of National Education and Religions",
        ),
    )
    MINISTRY_OF_AGRICULTURE = (
        "GR-7",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Agriculture"),
    )
    MINISTRY_OF_HEALTH_WELFARE = (
        "GR-8",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Health - Welfare"),
    )
    MINISTRY_OF_MERCHANT_MARINE = (
        "GR-9",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Merchant Marine"),
    )
    DEPARTMENT_OF_FOREIGN_AFFAIRS = (
        "IE-1",
        pgettext_lazy("OrganisationIdentifier", "Department of Foreign Affairs"),
    )
    DEPARTMENT_OF_INDUSTRY_AND_COMMERCE = (
        "IE-71",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Department of Industry and Commerce",
        ),
    )
    AGENZIA_EROGAZIONI_PER_L_AGRICOLTURA = (
        "IT-2",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Agenzia Erogazioni Per l'Agricoltura",
        ),
    )
    DIREZIONE_GENERALE_PER_LA_COOPERAZIONE_ALLO_SVILUPPO = (
        "IT-4",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Direzione Generale per la Cooperazione allo Sviluppo",
        ),
    )
    NOT_IN_CRS_DIRECTIVES = (
        "IT-5",
        pgettext_lazy("OrganisationIdentifier", "Not in CRS Directives"),
    )
    CENTRAL_ADMINISTRATION = (
        "IT-7",
        pgettext_lazy("OrganisationIdentifier", "Central administration"),
    )
    SEZIONE_SPECIALE_PER_L_ASSICURAZIONE_DEL_CREDITO_ALL_ESPORTAZIONE = (
        "IT-74",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Sezione Speciale per l'Assicurazione del Credito all'Esportazione",
        ),
    )
    LOCAL_ADMINISTRATION = (
        "IT-8",
        pgettext_lazy("OrganisationIdentifier", "Local administration"),
    )
    ARTIGIANCASSA = (
        "IT-9",
        pgettext_lazy("OrganisationIdentifier", "Artigiancassa"),
    )
    MINISTRY_OF_AGRICULTURE__FORESTRY_AND_FISHERIES = (
        "JP-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Agriculture, Forestry and Fisheries ",
        ),
    )
    JAPAN_OVERSEAS_DEVELOPMENT_CO_OPERATION = (
        "JP-10",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Japan Overseas Development Co-operation",
        ),
    )
    JAPAN_BANK_FOR_INTERNATIONAL_CO_OPERATION = (
        "JP-11",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Japan Bank for International Co-operation",
        ),
    )
    OTHER_MINISTRIES = (
        "JP-12",
        pgettext_lazy("OrganisationIdentifier", "Other Ministries"),
    )
    PUBLIC_CORPORATIONS = (
        "JP-13",
        pgettext_lazy("OrganisationIdentifier", "Public Corporations"),
    )
    PREFECTURES = (
        "JP-14",
        pgettext_lazy("OrganisationIdentifier", "Prefectures"),
    )
    ORDINANCE_DESIGNED_CITIES = (
        "JP-15",
        pgettext_lazy("OrganisationIdentifier", "Ordinance-designed Cities"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "JP-2",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    OVERSEAS_FISHERY_CO_OPERATION_FOUNDATION = (
        "JP-7",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Overseas Fishery Co-operation Foundation",
        ),
    )
    NIPPON_EXPORT_AND_INVESTMENT_INSURANCE = (
        "JP-71",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Nippon Export and Investment Insurance",
        ),
    )
    JAPANESE_INTERNATIONAL_CO_OPERATION_AGENCY = (
        "JP-8",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Japanese International Co-operation Agency",
        ),
    )
    LUX_DEVELOPMENT = (
        "LU-1",
        pgettext_lazy("OrganisationIdentifier", "Lux-Development"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "LU-2",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    DUCROIRE_OFFICE = (
        "LU-22",
        pgettext_lazy("OrganisationIdentifier", "Ducroire Office"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS__DGIS_ = (
        "NL-1",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs (DGIS)"),
    )
    NCM_CREDIT_MANAGEMENT_WORLDWIDE = (
        "NL-33",
        pgettext_lazy("OrganisationIdentifier", "NCM Credit Management Worldwide"),
    )
    NETHERLANDS_GOV__THROUGH_NETHERLANDS_INVESTMENT_BANK_FOR_DEVELOPING_COUNTRIES = (
        "NL-4",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Netherlands Gov. through Netherlands Investment Bank for Developing Countries",
        ),
    )
    NORWEGIAN_AGENCY_FOR_DEVELOPMENT_CO_OPERATION = (
        "NO-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Norwegian Agency for Development Co-operation",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "NO-4",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    STATENS_NÆRINGS_OG_DISTRIKSUTVIKLINGSFOND = (
        "NO-7",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Statens Nærings og Distriksutviklingsfond",
        ),
    )
    GARANTIINSTITUTTET_FOR_EKSPORTKREDITT = (
        "NO-71",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Garantiinstituttet for Eksportkreditt",
        ),
    )
    EKSPORT_FINANS = (
        "NO-72",
        pgettext_lazy("OrganisationIdentifier", "Eksport Finans"),
    )
    NORFUND = (
        "NO-8",
        pgettext_lazy("OrganisationIdentifier", "NORFUND"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS_AND_TRADE = (
        "NZ-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Ministry of Foreign Affairs and Trade",
        ),
    )
    NEW_ZEALAND_INTERNATIONAL_AID_AND_DEVELOPMENT_AGENCY = (
        "NZ-2",
        pgettext_lazy(
            "OrganisationIdentifier",
            "New Zealand International Aid and Development Agency",
        ),
    )
    PORTUGUESE_GOVERNMENT = (
        "PT-1",
        pgettext_lazy("OrganisationIdentifier", "Portuguese Government"),
    )
    INSTITUTE_FOR_PORTUGUESE_DEVELOPMENT_AID = (
        "PT-2",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Institute for Portuguese Development Aid",
        ),
    )
    OTHER = (
        "PT-3",
        pgettext_lazy("OrganisationIdentifier", "Other"),
    )
    CONSELHO_DE_GARANTIAS_FINANCEIRAS = (
        "PT-71",
        pgettext_lazy("OrganisationIdentifier", "Conselho de garantias financeiras"),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "SE-2",
        pgettext_lazy("OrganisationIdentifier", "Ministry of Foreign Affairs"),
    )
    SWEDISH_INTERNATIONAL_DEVELOPMENT_AUTHORITY = (
        "SE-6",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Swedish International Development Authority",
        ),
    )
    SWEDISH_EXPORT_CREDITS_GUARANTEE_BOARD = (
        "SE-71",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Swedish Export Credits Guarantee Board",
        ),
    )
    AGENCY_FOR_INTERNATIONAL_DEVELOPMENT = (
        "US-1",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Agency for International Development",
        ),
    )
    PEACE_CORPS = (
        "US-10",
        pgettext_lazy("OrganisationIdentifier", "Peace Corps"),
    )
    STATE_DEPARTMENT = (
        "US-11",
        pgettext_lazy("OrganisationIdentifier", "State Department"),
    )
    TRADE_AND_DEVELOPMENT_AGENCY = (
        "US-12",
        pgettext_lazy("OrganisationIdentifier", "Trade and Development Agency"),
    )
    AFRICAN_DEVELOPMENT_FOUNDATION = (
        "US-13",
        pgettext_lazy("OrganisationIdentifier", "African Development Foundation"),
    )
    CENTERS_FOR_DISEASE_CONTROL_AND_PREVENTION = (
        "US-15",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Centers for Disease Control and Prevention",
        ),
    )
    NATIONAL_INSTITUTES_OF_HEALTH = (
        "US-16",
        pgettext_lazy("OrganisationIdentifier", "National Institutes of Health"),
    )
    DEPARTMENT_OF_LABOR = (
        "US-17",
        pgettext_lazy("OrganisationIdentifier", "Department of Labor"),
    )
    DEPARTMENT_OF_AGRICULTURE = (
        "US-2",
        pgettext_lazy("OrganisationIdentifier", "Department of Agriculture"),
    )
    EXPORT_IMPORT_BANK = (
        "US-31",
        pgettext_lazy("OrganisationIdentifier", "Export Import Bank"),
    )
    DEPARTMENT_OF_TRANSPORTATION = (
        "US-5",
        pgettext_lazy("OrganisationIdentifier", "Department of Transportation"),
    )
    DEPARTMENT_OF_TREASURY = (
        "US-6",
        pgettext_lazy("OrganisationIdentifier", "Department of Treasury"),
    )
    DEPARTMENT_OF_DEFENSE = (
        "US-7",
        pgettext_lazy("OrganisationIdentifier", "Department of Defense"),
    )
    MISCELLANEOUS = (
        "US-8",
        pgettext_lazy("OrganisationIdentifier", "Miscellaneous"),
    )
    DEPARTMENT_OF_INTERIOR = (
        "US-9",
        pgettext_lazy("OrganisationIdentifier", "Department of Interior"),
    )
    CONVENTION_TO_COMBAT_DESERTIFICATION = (
        "41101",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Convention to Combat Desertification",
        ),
    )
    DESERT_LOCUST_CONTROL_ORGANISATION_FOR_EASTERN_AFRICA = (
        "41102",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Desert Locust Control Organisation for Eastern Africa",
        ),
    )
    ECONOMIC_COMMISSION_FOR_AFRICA = (
        "41103",
        pgettext_lazy("OrganisationIdentifier", "Economic Commission for Africa"),
    )
    ECONOMIC_COMMISSION_FOR_LATIN_AMERICA_AND_THE_CARIBBEAN = (
        "41104",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Economic Commission for Latin America and the Caribbean",
        ),
    )
    ECONOMIC_AND_SOCIAL_COMMISSION_FOR_WESTERN_ASIA = (
        "41105",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Economic and Social Commission for Western Asia",
        ),
    )
    ECONOMIC_AND_SOCIAL_COMMISSION_FOR_ASIA_AND_THE_PACIFIC = (
        "41106",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Economic and Social Commission for Asia and the Pacific",
        ),
    )
    INTERNATIONAL_ATOMIC_ENERGY_AGENCY__CONTRIBUTIONS_TO_TECHNICAL_COOPERATION_FUND_ONLY_ = (
        "41107",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Atomic Energy Agency (Contributions to Technical Cooperation Fund Only)",
        ),
    )
    INTERNATIONAL_FUND_FOR_AGRICULTURAL_DEVELOPMENT = (
        "41108",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Fund for Agricultural Development",
        ),
    )
    INTERNATIONAL_RESEARCH_AND_TRAINING_INSTITUTE_FOR_THE_ADVANCEMENT_OF_WOMEN = (
        "41109",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Research and Training Institute for the Advancement of Women",
        ),
    )
    JOINT_UNITED_NATIONS_PROGRAMME_ON_HIV_AIDS = (
        "41110",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Joint United Nations Programme on HIV/AIDS",
        ),
    )
    UNITED_NATIONS_CAPITAL_DEVELOPMENT_FUND = (
        "41111",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Capital Development Fund",
        ),
    )
    UNITED_NATIONS_CONFERENCE_ON_TRADE_AND_DEVELOPMENT = (
        "41112",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Conference on Trade and Development",
        ),
    )
    UNITED_NATIONS_DEVELOPMENT_PROGRAMME = (
        "41114",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Development Programme",
        ),
    )
    UNITED_NATIONS_ENVIRONMENT_PROGRAMME = (
        "41116",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Environment Programme",
        ),
    )
    UNITED_NATIONS_FRAMEWORK_CONVENTION_ON_CLIMATE_CHANGE = (
        "41118",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Framework Convention on Climate Change",
        ),
    )
    UNITED_NATIONS_POPULATION_FUND = (
        "41119",
        pgettext_lazy("OrganisationIdentifier", "United Nations Population Fund"),
    )
    UNITED_NATIONS_HUMAN_SETTLEMENT_PROGRAMME = (
        "41120",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Human Settlement Programme",
        ),
    )
    UNITED_NATIONS_OFFICE_OF_THE_UNITED_NATIONS_HIGH_COMMISSIONER_FOR_REFUGEES = (
        "41121",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Office of the United Nations High Commissioner for Refugees",
        ),
    )
    UNITED_NATIONS_CHILDREN_S_FUND = (
        "41122",
        pgettext_lazy("OrganisationIdentifier", "United Nations Children's Fund"),
    )
    UNITED_NATIONS_INDUSTRIAL_DEVELOPMENT_ORGANISATION = (
        "41123",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Industrial Development Organisation",
        ),
    )
    UNITED_NATIONS_DEVELOPMENT_FUND_FOR_WOMEN = (
        "41124",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Development Fund for Women",
        ),
    )
    UNITED_NATIONS_INSTITUTE_FOR_TRAINING_AND_RESEARCH = (
        "41125",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Institute for Training and Research",
        ),
    )
    UNITED_NATIONS_MINE_ACTION_SERVICE = (
        "41126",
        pgettext_lazy("OrganisationIdentifier", "United Nations Mine Action Service"),
    )
    UNITED_NATIONS_OFFICE_OF_CO_ORDINATION_OF_HUMANITARIAN_AFFAIRS = (
        "41127",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Office of Co-ordination of Humanitarian Affairs",
        ),
    )
    UNITED_NATIONS_OFFICE_ON_DRUGS_AND_CRIME = (
        "41128",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Office on Drugs and Crime",
        ),
    )
    UNITED_NATIONS_RESEARCH_INSTITUTE_FOR_SOCIAL_DEVELOPMENT = (
        "41129",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Research Institute for Social Development",
        ),
    )
    UNITED_NATIONS_RELIEF_AND_WORKS_AGENCY_FOR_PALESTINE_REFUGEES_IN_THE_NEAR_EAST = (
        "41130",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Relief and Works Agency for Palestine Refugees in the Near East",
        ),
    )
    UNITED_NATIONS_SYSTEM_STAFF_COLLEGE = (
        "41131",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations System Staff College",
        ),
    )
    UNITED_NATIONS_SYSTEM_STANDING_COMMITTEE_ON_NUTRITION = (
        "41132",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations System Standing Committee on Nutrition",
        ),
    )
    UNITED_NATIONS_SPECIAL_INITIATIVE_ON_AFRICA = (
        "41133",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Special Initiative on Africa",
        ),
    )
    UNITED_NATIONS_UNIVERSITY__INCLUDING_ENDOWMENT_FUND_ = (
        "41134",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations University (including Endowment Fund)",
        ),
    )
    UNITED_NATIONS_VOLUNTEERS = (
        "41135",
        pgettext_lazy("OrganisationIdentifier", "United Nations Volunteers"),
    )
    UNITED_NATIONS_VOLUNTARY_FUND_ON_DISABILITY = (
        "41136",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Voluntary Fund on Disability",
        ),
    )
    UNITED_NATIONS_VOLUNTARY_FUND_FOR_TECHNICAL_CO_OPERATION_IN_THE_FIELD_OF_HUMAN_RIGHTS = (
        "41137",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Voluntary Fund for Technical Co-operation in the Field of Human Rights",
        ),
    )
    UNITED_NATIONS_VOLUNTARY_FUND_FOR_VICTIMS_OF_TORTURE = (
        "41138",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Voluntary Fund for Victims of Torture",
        ),
    )
    WORLD_FOOD_PROGRAMME = (
        "41140",
        pgettext_lazy("OrganisationIdentifier", "World Food Programme"),
    )
    UNITED_NATIONS_PEACEBUILDING_FUND__WINDOW_TWO__RESTRICTED_CONTRIBUTIONS_ONLY_ = (
        "41141",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Peacebuilding Fund (Window Two: Restricted Contributions Only)",
        ),
    )
    UNITED_NATIONS_DEMOCRACY_FUND = (
        "41142",
        pgettext_lazy("OrganisationIdentifier", "United Nations Democracy Fund"),
    )
    WORLD_HEALTH_ORGANISATION_CORE_VOLUNTARY_CONTRIBUTIONS_ACCOUNT = (
        "41143",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Health Organisation - core voluntary contributions account",
        ),
    )
    FOOD_AND_AGRICULTURAL_ORGANISATION = (
        "41301",
        pgettext_lazy("OrganisationIdentifier", "Food and Agricultural Organisation"),
    )
    INTERNATIONAL_LABOUR_ORGANISATION = (
        "41302",
        pgettext_lazy("OrganisationIdentifier", "International Labour Organisation"),
    )
    INTERNATIONAL_TELECOMMUNICATIONS_UNION = (
        "41303",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Telecommunications Union",
        ),
    )
    UNITED_NATIONS_EDUCATIONAL__SCIENTIFIC_AND_CULTURAL_ORGANISATION = (
        "41304",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Educational, Scientific and Cultural Organisation ",
        ),
    )
    UNITED_NATIONS = (
        "41305",
        pgettext_lazy("OrganisationIdentifier", "United Nations"),
    )
    UNIVERSAL_POSTAL_UNION = (
        "41306",
        pgettext_lazy("OrganisationIdentifier", "Universal Postal Union"),
    )
    WORLD_HEALTH_ORGANISATION_ASSESSED_CONTRIBUTIONS = (
        "41307",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Health Organisation - assessed contributions",
        ),
    )
    WORLD_INTELLECTUAL_PROPERTY_ORGANISATION = (
        "41308",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Intellectual Property Organisation",
        ),
    )
    WORLD_METEOROLOGICAL_ORGANISATION = (
        "41309",
        pgettext_lazy("OrganisationIdentifier", "World Meteorological Organisation"),
    )
    UNITED_NATIONS_DEPARTMENT_OF_PEACEKEEPING_OPERATIONS__EXCLUDING_UNTSO__UNMOGIP__UNFICYP__UNDOF_ = (
        "41310",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Department of Peacekeeping Operations (excluding UNTSO, UNMOGIP, UNFICYP, UNDOF) ",
        ),
    )
    UNITED_NATIONS_PEACEBUILDING_FUND__WINDOW_ONE__FLEXIBLE_CONTRIBUTIONS_ONLY_ = (
        "41311",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Peacebuilding Fund (Window One: Flexible Contributions Only)",
        ),
    )
    INTERNATIONAL_ATOMIC_ENERGY_AGENCY_ASSESSED_CONTRIBUTIONS = (
        "41312",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Atomic Energy Agency - assessed contributions",
        ),
    )
    UNITED_NATIONS_HIGH_COMMISSIONER_FOR_HUMAN_RIGHTS__EXTRABUDGETARY_CONTRIBUTIONS_ONLY_ = (
        "41313",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations High Commissioner for Human Rights (extrabudgetary contributions only)",
        ),
    )
    UNITED_NATIONS_ECONOMIC_COMMISSION_FOR_EUROPE__EXTRABUDGETARY_CONTRIBUTIONS_ONLY_ = (
        "41314",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Nations Economic Commission for Europe (extrabudgetary contributions only)",
        ),
    )
    EUROPEAN_COMMISSION_DEVELOPMENT_SHARE_OF_BUDGET = (
        "42001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Commission - Development Share of Budget",
        ),
    )
    EUROPEAN_COMMISSION_EUROPEAN_DEVELOPMENT_FUND = (
        "42003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Commission - European Development Fund",
        ),
    )
    EUROPEAN_INVESTMENT_BANK__INTEREST_SUBSIDIES_ONLY_ = (
        "42004",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Investment Bank (interest subsidies only)",
        ),
    )
    FACILITY_FOR_EURO_MEDITERRANEAN_INVESTMENT_AND_PARTNERSHIP_TRUST_FUND = (
        "42005",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Facility for Euro-Mediterranean Investment and Partnership Trust Fund",
        ),
    )
    GLOBAL_ENERGY_EFFICIENCY_AND_RENEWABLE_ENERGY_FUND = (
        "42006",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Global Energy Efficiency and Renewable Energy Fund",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_POVERTY_REDUCTION_AND_GROWTH_FACILITY_TRUST = (
        "43001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Monetary Fund - Poverty Reduction and Growth Facility Trust",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_POVERTY_REDUCTION_AND_GROWTH_FACILITY_HEAVILY_INDEBTED_POOR_COUNTRIES_INITIATIVE_TRUST__INCLUDES_HIPC__PRGF_AND_PRGF_HIPC_SUB_ACCOUNTS_ = (
        "43002",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Monetary Fund - Poverty Reduction and Growth Facility - Heavily Indebted Poor Countries Initiative Trust (includes HIPC, PRGF and PRGF-HIPC sub-accounts) ",
        ),
    )
    INTERNATIONAL_MONETARY_FUND_SUBSIDIZATION_OF_IMF_EMERGENCY_ASSISTANCE_FOR_NATURAL_DISASTERS = (
        "43003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Monetary Fund - Subsidization of IMF Emergency Assistance for Natural Disasters",
        ),
    )
    INTERNATIONAL_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT = (
        "44001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Bank for Reconstruction and Development",
        ),
    )
    INTERNATIONAL_DEVELOPMENT_ASSOCIATION = (
        "44002",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Development Association",
        ),
    )
    INTERNATIONAL_DEVELOPMENT_ASSOCIATION_HEAVILY_INDEBTED_POOR_COUNTRIES_DEBT_INITIATIVE_TRUST_FUND = (
        "44003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Development Association - Heavily Indebted Poor Countries Debt Initiative Trust Fund",
        ),
    )
    INTERNATIONAL_FINANCE_CORPORATION = (
        "44004",
        pgettext_lazy("OrganisationIdentifier", "International Finance Corporation"),
    )
    MULTILATERAL_INVESTMENT_GUARANTEE_AGENCY = (
        "44005",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Multilateral Investment Guarantee Agency",
        ),
    )
    ADVANCE_MARKET_COMMITMENTS = (
        "44006",
        pgettext_lazy("OrganisationIdentifier", "Advance Market Commitments"),
    )
    INTERNATIONAL_DEVELOPMENT_ASSOCIATION_MULTILATERAL_DEBT_RELIEF_INITIATIVE = (
        "44007",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Development Association - Multilateral Debt Relief Initiative",
        ),
    )
    WORLD_TRADE_ORGANISATION_INTERNATIONAL_TRADE_CENTRE = (
        "45001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Trade Organisation - International Trade Centre",
        ),
    )
    WORLD_TRADE_ORGANISATION_ADVISORY_CENTRE_ON_WTO_LAW = (
        "45002",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Trade Organisation - Advisory Centre on WTO Law",
        ),
    )
    WORLD_TRADE_ORGANISATION_DOHA_DEVELOPMENT_AGENDA_GLOBAL_TRUST_FUND = (
        "45003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Trade Organisation - Doha Development Agenda Global Trust Fund",
        ),
    )
    AFRICAN_SOLIDARITY_FUND = (
        "46001",
        pgettext_lazy("OrganisationIdentifier", "African Solidarity Fund"),
    )
    AFRICAN_DEVELOPMENT_BANK = (
        "46002",
        pgettext_lazy("OrganisationIdentifier", "African Development Bank"),
    )
    AFRICAN_DEVELOPMENT_FUND = (
        "46003",
        pgettext_lazy("OrganisationIdentifier", "African Development Fund"),
    )
    ASIAN_DEVELOPMENT_BANK = (
        "46004",
        pgettext_lazy("OrganisationIdentifier", "Asian Development Bank"),
    )
    ASIAN_DEVELOPMENT_FUND = (
        "46005",
        pgettext_lazy("OrganisationIdentifier", "Asian Development Fund"),
    )
    BLACK_SEA_TRADE_AND_DEVELOPMENT_BANK = (
        "46006",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Black Sea Trade and Development Bank",
        ),
    )
    CENTRAL_AMERICAN_BANK_FOR_ECONOMIC_INTEGRATION = (
        "46007",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Central American Bank for Economic Integration",
        ),
    )
    ANDEAN_DEVELOPMENT_CORPORATION = (
        "46008",
        pgettext_lazy("OrganisationIdentifier", "Andean Development Corporation"),
    )
    CARIBBEAN_DEVELOPMENT_BANK = (
        "46009",
        pgettext_lazy("OrganisationIdentifier", "Caribbean Development Bank"),
    )
    INTER_AMERICAN_DEVELOPMENT_BANK__INTER_AMERICAN_INVESTMENT_CORPORATION_AND_MULTILATERAL_INVESTMENT_FUND = (
        "46012",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Inter-American Development Bank, Inter-American Investment Corporation and Multilateral Investment Fund ",
        ),
    )
    INTER_AMERICAN_DEVELOPMENT_FUND_FOR_SPECIAL_OPERATIONS = (
        "46013",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Inter-American Development Fund for Special Operations",
        ),
    )
    AFRICAN_CAPACITY_BUILDING_FOUNDATION = (
        "47001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "African Capacity Building Foundation",
        ),
    )
    ASIAN_PRODUCTIVITY_ORGANISATION = (
        "47002",
        pgettext_lazy("OrganisationIdentifier", "Asian Productivity Organisation"),
    )
    ASSOCIATION_OF_SOUTH_EAST_ASIAN_NATIONS__ECONOMIC_CO_OPERATION = (
        "47003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Association of South East Asian Nations: Economic Co-operation",
        ),
    )
    ASEAN_CULTURAL_FUND = (
        "47004",
        pgettext_lazy("OrganisationIdentifier", "ASEAN Cultural Fund"),
    )
    AFRICAN_UNION__EXCLUDING_PEACEKEEPING_FACILITIES_ = (
        "47005",
        pgettext_lazy(
            "OrganisationIdentifier",
            "African Union (excluding peacekeeping facilities)",
        ),
    )
    WORLD_VEGETABLE_CENTRE = (
        "47008",
        pgettext_lazy("OrganisationIdentifier", "World Vegetable Centre"),
    )
    AFRICAN_AND_MALAGASY_COUNCIL_FOR_HIGHER_EDUCATION = (
        "47009",
        pgettext_lazy(
            "OrganisationIdentifier",
            "African and Malagasy Council for Higher Education",
        ),
    )
    COMMONWEALTH_AGENCY_FOR_PUBLIC_ADMINISTRATION_AND_MANAGEMENT = (
        "47010",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commonwealth Agency for Public Administration and Management",
        ),
    )
    CARIBBEAN_COMMUNITY_SECRETARIAT = (
        "47011",
        pgettext_lazy("OrganisationIdentifier", "Caribbean Community Secretariat"),
    )
    CARIBBEAN_EPIDEMIOLOGY_CENTRE = (
        "47012",
        pgettext_lazy("OrganisationIdentifier", "Caribbean Epidemiology Centre"),
    )
    COMMONWEALTH_FOUNDATION = (
        "47013",
        pgettext_lazy("OrganisationIdentifier", "Commonwealth Foundation"),
    )
    COMMONWEALTH_FUND_FOR_TECHNICAL_CO_OPERATION = (
        "47014",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commonwealth Fund for Technical Co-operation",
        ),
    )
    CONSULTATIVE_GROUP_ON_INTERNATIONAL_AGRICULTURAL_RESEARCH = (
        "47015",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Consultative Group on International Agricultural Research",
        ),
    )
    COMMONWEALTH_INSTITUTE = (
        "47016",
        pgettext_lazy("OrganisationIdentifier", "Commonwealth Institute"),
    )
    INTERNATIONAL_CENTRE_FOR_TROPICAL_AGRICULTURE = (
        "47017",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre for Tropical Agriculture",
        ),
    )
    CENTRE_FOR_INTERNATIONAL_FORESTRY_RESEARCH = (
        "47018",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Centre for International Forestry Research",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_ADVANCED_MEDITERRANEAN_AGRONOMIC_STUDIES = (
        "47019",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre for Advanced Mediterranean Agronomic Studies",
        ),
    )
    INTERNATIONAL_MAIZE_AND_WHEAT_IMPROVEMENT_CENTRE = (
        "47020",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Maize and Wheat Improvement Centre",
        ),
    )
    INTERNATIONAL_POTATO_CENTRE = (
        "47021",
        pgettext_lazy("OrganisationIdentifier", "International Potato Centre"),
    )
    CONVENTION_ON_INTERNATIONAL_TRADE_IN_ENDANGERED_SPECIES_OF_WILD_FLORA_AND_FAUNA = (
        "47022",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Convention on International Trade in Endangered Species of Wild Flora and Fauna",
        ),
    )
    COMMONWEALTH_LEGAL_ADVISORY_SERVICE = (
        "47023",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commonwealth Legal Advisory Service",
        ),
    )
    COMMONWEALTH_MEDIA_DEVELOPMENT_FUND = (
        "47024",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commonwealth Media Development Fund",
        ),
    )
    COMMONWEALTH_OF_LEARNING = (
        "47025",
        pgettext_lazy("OrganisationIdentifier", "Commonwealth of Learning"),
    )
    COMMUNITY_OF_PORTUGUESE_SPEAKING_COUNTRIES = (
        "47026",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Community of Portuguese Speaking Countries",
        ),
    )
    COLOMBO_PLAN = (
        "47027",
        pgettext_lazy("OrganisationIdentifier", "Colombo Plan"),
    )
    COMMONWEALTH_PARTNERSHIP_FOR_TECHNICAL_MANAGEMENT = (
        "47028",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commonwealth Partnership for Technical Management",
        ),
    )
    SAHEL_AND_WEST_AFRICA_CLUB = (
        "47029",
        pgettext_lazy("OrganisationIdentifier", "Sahel and West Africa Club"),
    )
    COMMONWEALTH_SCIENTIFIC_COUNCIL = (
        "47030",
        pgettext_lazy("OrganisationIdentifier", "Commonwealth Scientific Council"),
    )
    COMMONWEALTH_SMALL_STATES_OFFICE = (
        "47031",
        pgettext_lazy("OrganisationIdentifier", "Commonwealth Small States Office"),
    )
    COMMONWEALTH_TRADE_AND_INVESTMENT_ACCESS_FACILITY = (
        "47032",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Commonwealth Trade and Investment Access Facility",
        ),
    )
    COMMONWEALTH_YOUTH_PROGRAMME = (
        "47033",
        pgettext_lazy("OrganisationIdentifier", "Commonwealth Youth Programme"),
    )
    ECONOMIC_COMMUNITY_OF_WEST_AFRICAN_STATES = (
        "47034",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Economic Community of West African States",
        ),
    )
    ENVIRONMENTAL_DEVELOPMENT_ACTION_IN_THE_THIRD_WORLD = (
        "47035",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Environmental Development Action in the Third World",
        ),
    )
    EUROPEAN_AND_MEDITERRANEAN_PLANT_PROTECTION_ORGANISATION = (
        "47036",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European and Mediterranean Plant Protection Organisation",
        ),
    )
    EASTERN_REGIONAL_ORGANISATION_OF_PUBLIC_ADMINISTRATION = (
        "47037",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Eastern-Regional Organisation of Public Administration",
        ),
    )
    INTERPOL_FUND_FOR_AID_AND_TECHNICAL_ASSISTANCE_TO_DEVELOPING_COUNTRIES = (
        "47038",
        pgettext_lazy(
            "OrganisationIdentifier",
            "INTERPOL Fund for Aid and Technical Assistance to Developing Countries",
        ),
    )
    FORUM_FISHERIES_AGENCY = (
        "47040",
        pgettext_lazy("OrganisationIdentifier", "Forum Fisheries Agency"),
    )
    FOOD_AND_FERTILIZER_TECHNOLOGY_CENTRE = (
        "47041",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Food and Fertilizer Technology Centre",
        ),
    )
    FOUNDATION_FOR_INTERNATIONAL_TRAINING = (
        "47042",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Foundation for International Training",
        ),
    )
    GLOBAL_CROP_DIVERSITY_TRUST = (
        "47043",
        pgettext_lazy("OrganisationIdentifier", "Global Crop Diversity Trust"),
    )
    GLOBAL_ENVIRONMENT_FACILITY = (
        "47044",
        pgettext_lazy("OrganisationIdentifier", "Global Environment Facility"),
    )
    GLOBAL_FUND_TO_FIGHT_AIDS__TUBERCULOSIS_AND_MALARIA = (
        "47045",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Global Fund to Fight AIDS, Tuberculosis and Malaria ",
        ),
    )
    INTERNATIONAL_ORGANISATION_OF_THE_FRANCOPHONIC = (
        "47046",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Organisation of the Francophonic",
        ),
    )
    INTERNATIONAL_AFRICAN_INSTITUTE = (
        "47047",
        pgettext_lazy("OrganisationIdentifier", "International African Institute"),
    )
    INTER_AMERICAN_INDIAN_INSTITUTE = (
        "47048",
        pgettext_lazy("OrganisationIdentifier", "Inter-American Indian Institute"),
    )
    INTERNATIONAL_BUREAU_OF_EDUCATION_INTERNATIONAL_EDUCATIONAL_REPORTING_SYSTEM__IERS_ = (
        "47049",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Bureau of Education - International Educational Reporting System (IERS)",
        ),
    )
    INTERNATIONAL_COTTON_ADVISORY_COMMITTEE = (
        "47050",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Cotton Advisory Committee",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_AGRICULTURAL_RESEARCH_IN_DRY_AREAS = (
        "47051",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre for Agricultural Research in Dry Areas",
        ),
    )
    CENTRE_FOR_HEALTH_AND_POPULATION_RESEARCH = (
        "47053",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Centre for Health and Population Research",
        ),
    )
    INTERNATIONAL_CENTRE_OF_INSECT_PHYSIOLOGY_AND_ECOLOGY = (
        "47054",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre of Insect Physiology and Ecology",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_DEVELOPMENT_ORIENTED_RESEARCH_IN_AGRICULTURE = (
        "47055",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre for Development Oriented Research in Agriculture",
        ),
    )
    WORLD_AGROFORESTRY_CENTRE = (
        "47056",
        pgettext_lazy("OrganisationIdentifier", "World AgroForestry Centre"),
    )
    INTERNATIONAL_CROP_RESEARCH_FOR_SEMI_ARID_TROPICS = (
        "47057",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Crop Research for Semi-Arid Tropics",
        ),
    )
    INTERNATIONAL_INSTITUTE_FOR_DEMOCRACY_AND_ELECTORAL_ASSISTANCE = (
        "47058",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Institute for Democracy and Electoral Assistance",
        ),
    )
    INTERNATIONAL_DEVELOPMENT_LAW_ORGANISATION = (
        "47059",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Development Law Organisation",
        ),
    )
    INTERNATIONAL_INSTITUTE_FOR_COTTON = (
        "47060",
        pgettext_lazy("OrganisationIdentifier", "International Institute for Cotton"),
    )
    INTER_AMERICAN_INSTITUTE_FOR_CO_OPERATION_ON_AGRICULTURE = (
        "47061",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Inter-American Institute for Co-operation on Agriculture",
        ),
    )
    INTERNATIONAL_INSTITUTE_OF_TROPICAL_AGRICULTURE = (
        "47062",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Institute of Tropical Agriculture",
        ),
    )
    INTERNATIONAL_LIVESTOCK_RESEARCH_INSTITUTE = (
        "47063",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Livestock Research Institute",
        ),
    )
    INTERNATIONAL_NETWORK_FOR_BAMBOO_AND_RATTAN = (
        "47064",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Network for Bamboo and Rattan",
        ),
    )
    INTERGOVERNMENTAL_OCEANOGRAPHIC_COMMISSION = (
        "47065",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Intergovernmental Oceanographic Commission",
        ),
    )
    INTERNATIONAL_ORGANISATION_FOR_MIGRATION = (
        "47066",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Organisation for Migration",
        ),
    )
    INTERGOVERNMENTAL_PANEL_ON_CLIMATE_CHANGE = (
        "47067",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Intergovernmental Panel on Climate Change",
        ),
    )
    ASIA_PACIFIC_FISHERY_COMMISSION = (
        "47068",
        pgettext_lazy("OrganisationIdentifier", "Asia-Pacific Fishery Commission"),
    )
    BIODIVERSITY_INTERNATIONAL = (
        "47069",
        pgettext_lazy("OrganisationIdentifier", "Biodiversity International"),
    )
    INTERNATIONAL_RICE_RESEARCH_INSTITUTE = (
        "47070",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Rice Research Institute",
        ),
    )
    INTERNATIONAL_SEED_TESTING_ASSOCIATION = (
        "47071",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Seed Testing Association",
        ),
    )
    INTERNATIONAL_TROPICAL_TIMBER_ORGANISATION = (
        "47073",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Tropical Timber Organisation",
        ),
    )
    INTERNATIONAL_VACCINE_INSTITUTE = (
        "47074",
        pgettext_lazy("OrganisationIdentifier", "International Vaccine Institute"),
    )
    INTERNATIONAL_WATER_MANAGEMENT_INSTITUTE = (
        "47075",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Water Management Institute",
        ),
    )
    JUSTICE_STUDIES_CENTRE_OF_THE_AMERICAS = (
        "47076",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Justice Studies Centre of the Americas",
        ),
    )
    MEKONG_RIVER_COMMISSION = (
        "47077",
        pgettext_lazy("OrganisationIdentifier", "Mekong River Commission"),
    )
    MULTILATERAL_FUND_FOR_THE_IMPLEMENTATION_OF_THE_MONTREAL_PROTOCOL = (
        "47078",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Multilateral Fund for the Implementation of the Montreal Protocol",
        ),
    )
    ORGANISATION_OF_AMERICAN_STATES = (
        "47079",
        pgettext_lazy("OrganisationIdentifier", "Organisation of American States"),
    )
    ORGANISATION_FOR_ECONOMIC_CO_OPERATION_AND_DEVELOPMENT__CONTRIBUTIONS_TO_SPECIAL_FUNDS_FOR_TECHNICAL_CO_OPERATION_ACTIVITIES_ONLY_ = (
        "47080",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Organisation for Economic Co-operation and Development (Contributions to special funds for Technical Co-operation Activities Only)",
        ),
    )
    OECD_DEVELOPMENT_CENTRE = (
        "47081",
        pgettext_lazy("OrganisationIdentifier", "OECD Development Centre"),
    )
    ORGANISATION_OF_EASTERN_CARIBBEAN_STATES = (
        "47082",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Organisation of Eastern Caribbean States",
        ),
    )
    PAN_AMERICAN_HEALTH_ORGANISATION = (
        "47083",
        pgettext_lazy("OrganisationIdentifier", "Pan-American Health Organisation"),
    )
    PAN_AMERICAN_INSTITUTE_OF_GEOGRAPHY_AND_HISTORY = (
        "47084",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Pan-American Institute of Geography and History",
        ),
    )
    PAN_AMERICAN_RAILWAY_CONGRESS_ASSOCIATION = (
        "47085",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Pan-American Railway Congress Association",
        ),
    )
    PRIVATE_INFRASTRUCTURE_DEVELOPMENT_GROUP = (
        "47086",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Private Infrastructure Development Group",
        ),
    )
    PACIFIC_ISLANDS_FORUM_SECRETARIAT = (
        "47087",
        pgettext_lazy("OrganisationIdentifier", "Pacific Islands Forum Secretariat"),
    )
    RELIEF_NET = (
        "47088",
        pgettext_lazy("OrganisationIdentifier", "Relief Net"),
    )
    SOUTHERN_AFRICAN_DEVELOPMENT_COMMUNITY = (
        "47089",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Southern African Development Community",
        ),
    )
    SOUTHERN_AFRICAN_TRANSPORT_AND_COMMUNICATIONS_COMMISSION = (
        "47090",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Southern African Transport and Communications Commission",
        ),
    )
    _COLOMBO_PLAN__SPECIAL_COMMONWEALTH_AFRICAN_ASSISTANCE_PROGRAMME = (
        "47091",
        pgettext_lazy(
            "OrganisationIdentifier",
            "(Colombo Plan) Special Commonwealth African Assistance Programme",
        ),
    )
    SOUTH_EAST_ASIAN_FISHERIES_DEVELOPMENT_CENTRE = (
        "47092",
        pgettext_lazy(
            "OrganisationIdentifier",
            "South East Asian Fisheries Development Centre",
        ),
    )
    SOUTH_EAST_ASIAN_MINISTERS_OF_EDUCATION = (
        "47093",
        pgettext_lazy(
            "OrganisationIdentifier",
            "South East Asian Ministers of Education",
        ),
    )
    SOUTH_PACIFIC_APPLIED_GEOSCIENCE_COMMISSION = (
        "47094",
        pgettext_lazy(
            "OrganisationIdentifier",
            "South Pacific Applied Geoscience Commission",
        ),
    )
    SOUTH_PACIFIC_BOARD_FOR_EDUCATIONAL_ASSESSMENT = (
        "47095",
        pgettext_lazy(
            "OrganisationIdentifier",
            "South Pacific Board for Educational Assessment",
        ),
    )
    SECRETARIAT_OF_THE_PACIFIC_COMMUNITY = (
        "47096",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Secretariat of the Pacific Community",
        ),
    )
    PACIFIC_REGIONAL_ENVIRONMENT_PROGRAMME = (
        "47097",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Pacific Regional Environment Programme",
        ),
    )
    UNREPRESENTED_NATIONS_AND_PEOPLES__ORGANISATION = (
        "47098",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Unrepresented Nations and Peoples' Organisation",
        ),
    )
    UNIVERSITY_OF_THE_SOUTH_PACIFIC = (
        "47099",
        pgettext_lazy("OrganisationIdentifier", "University of the South Pacific"),
    )
    WEST_AFRICAN_MONETARY_UNION = (
        "47100",
        pgettext_lazy("OrganisationIdentifier", "West African Monetary Union"),
    )
    AFRICA_RICE_CENTRE = (
        "47101",
        pgettext_lazy("OrganisationIdentifier", "Africa Rice Centre"),
    )
    WORLD_CUSTOMS_ORGANISATION_FELLOWSHIP_PROGRAMME = (
        "47102",
        pgettext_lazy(
            "OrganisationIdentifier",
            "World Customs Organisation Fellowship Programme",
        ),
    )
    WORLD_MARITIME_UNIVERSITY = (
        "47103",
        pgettext_lazy("OrganisationIdentifier", "World Maritime University"),
    )
    WORLDFISH_CENTRE = (
        "47104",
        pgettext_lazy("OrganisationIdentifier", "WorldFish Centre"),
    )
    COMMON_FUND_FOR_COMMODITIES = (
        "47105",
        pgettext_lazy("OrganisationIdentifier", "Common Fund for Commodities"),
    )
    GENEVA_CENTRE_FOR_THE_DEMOCRATIC_CONTROL_OF_ARMED_FORCES = (
        "47106",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Geneva Centre for the Democratic Control of Armed Forces",
        ),
    )
    INTERNATIONAL_FINANCE_FACILITY_FOR_IMMUNISATION = (
        "47107",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Finance Facility for Immunisation",
        ),
    )
    MULTI_COUNTRY_DEMOBILISATION_AND_REINTEGRATION_PROGRAM = (
        "47108",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Multi-Country Demobilisation and Reintegration Program",
        ),
    )
    ASIA_PACIFIC_ECONOMIC_COOPERATION_SUPPORT_FUND__EXCEPT_CONTRIBUTIONS_TIED_TO_COUNTER_TERRORISM_ACTIVITIES_ = (
        "47109",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Asia-Pacific Economic Cooperation Support Fund (except contributions tied to counter-terrorism activities)",
        ),
    )
    ORGANISATION_OF_THE_BLACK_SEA_ECONOMIC_COOPERATION = (
        "47110",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Organisation of the Black Sea Economic Cooperation",
        ),
    )
    ADAPTATION_FUND = (
        "47111",
        pgettext_lazy("OrganisationIdentifier", "Adaptation Fund"),
    )
    CENTRAL_EUROPEAN_INITIATIVE_SPECIAL_FUND_FOR_CLIMATE_AND_ENVIRONMENTAL_PROTECTION = (
        "47112",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Central European Initiative - Special Fund for Climate and Environmental Protection",
        ),
    )
    ECONOMIC_AND_MONETARY_COMMUNITY_OF_CENTRAL_AFRICA = (
        "47113",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Economic and Monetary Community of Central Africa",
        ),
    )
    INTEGRATED_FRAMEWORK_FOR_TRADE_RELATED_TECHNICAL_ASSISTANCE_TO_LEAST_DEVELOPED_COUNTRIES = (
        "47116",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Integrated Framework for Trade-Related Technical Assistance to Least Developed Countries",
        ),
    )
    NEW_PARTNERSHIP_FOR_AFRICA_S_DEVELOPMENT = (
        "47117",
        pgettext_lazy(
            "OrganisationIdentifier",
            "New Partnership for Africa's Development",
        ),
    )
    REGIONAL_ORGANISATION_FOR_THE_STRENGTHENING_OF_SUPREME_AUDIT_INSTITUTIONS_OF_FRANCOPHONE_SUB_SAHARAN_COUNTRIES = (
        "47118",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Regional Organisation for the Strengthening of Supreme Audit Institutions of Francophone Sub-Saharan Countries",
        ),
    )
    SAHARA_AND_SAHEL_OBSERVATORY = (
        "47119",
        pgettext_lazy("OrganisationIdentifier", "Sahara and Sahel Observatory"),
    )
    SOUTH_ASIAN_ASSOCIATION_FOR_REGIONAL_COOPERATION = (
        "47120",
        pgettext_lazy(
            "OrganisationIdentifier",
            "South Asian Association for Regional Cooperation",
        ),
    )
    UNITED_CITIES_AND_LOCAL_GOVERNMENTS_OF_AFRICA = (
        "47121",
        pgettext_lazy(
            "OrganisationIdentifier",
            "United Cities and Local Governments of Africa",
        ),
    )
    GLOBAL_ALLIANCE_FOR_VACCINES_AND_IMMUNIZATION = (
        "47122",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Global Alliance for Vaccines and Immunization",
        ),
    )
    GENEVA_INTERNATIONAL_CENTRE_FOR_HUMANITARIAN_DEMINING = (
        "47123",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Geneva International Centre for Humanitarian Demining",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT_EARLY_TRANSITION_COUNTRIES_INITIATIVE = (
        "47125",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Bank for Reconstruction and Development - Early Transition Countries Initiative",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT_WESTERN_BALKANS_TRUST_FUND = (
        "47126",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Bank for Reconstruction and Development - Western Balkans Trust Fund",
        ),
    )
    LATIN_AMERICAN_ENERGY_ORGANISATION = (
        "47127",
        pgettext_lazy("OrganisationIdentifier", "Latin-American Energy Organisation"),
    )
    ASSOCIATION_OF_GEOSCIENTISTS_FOR_INTERNATIONAL_DEVELOPMENT = (
        "21001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Association of Geoscientists for International Development",
        ),
    )
    AGENCY_FOR_INTERNATIONAL_TRADE_INFORMATION_AND_CO_OPERATION = (
        "21002",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Agency for International Trade Information and Co-operation",
        ),
    )
    LATIN_AMERICAN_COUNCIL_FOR_SOCIAL_SCIENCES = (
        "21003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Latin American Council for Social Sciences",
        ),
    )
    COUNCIL_FOR_THE_DEVELOPMENT_OF_ECONOMIC_AND_SOCIAL_RESEARCH_IN_AFRICA = (
        "21004",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Council for the Development of Economic and Social Research in Africa",
        ),
    )
    CONSUMER_UNITY_AND_TRUST_SOCIETY_INTERNATIONAL = (
        "21005",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Consumer Unity and Trust Society International",
        ),
    )
    DEVELOPMENT_GATEWAY_FOUNDATION = (
        "21006",
        pgettext_lazy("OrganisationIdentifier", "Development Gateway Foundation"),
    )
    ENVIRONMENTAL_LIAISON_CENTRE_INTERNATIONAL = (
        "21007",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Environmental Liaison Centre International",
        ),
    )
    EUROSTEP = (
        "21008",
        pgettext_lazy("OrganisationIdentifier", "Eurostep"),
    )
    FORUM_FOR_AGRICULTURAL_RESEARCH_IN_AFRICA = (
        "21009",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Forum for Agricultural Research in Africa",
        ),
    )
    FORUM_FOR_AFRICAN_WOMEN_EDUCATIONALISTS = (
        "21010",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Forum for African Women Educationalists",
        ),
    )
    GLOBAL_CAMPAIGN_FOR_EDUCATION = (
        "21011",
        pgettext_lazy("OrganisationIdentifier", "Global Campaign for Education"),
    )
    HEALTH_ACTION_INTERNATIONAL = (
        "21013",
        pgettext_lazy("OrganisationIdentifier", "Health Action International"),
    )
    HUMAN_RIGHTS_INFORMATION_AND_DOCUMENTATION_SYSTEMS = (
        "21014",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Human Rights Information and Documentation Systems",
        ),
    )
    INTERNATIONAL_CATHOLIC_RURAL_ASSOCIATION = (
        "21015",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Catholic Rural Association",
        ),
    )
    INTERNATIONAL_COMMITTEE_OF_THE_RED_CROSS = (
        "21016",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Committee of the Red Cross",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_TRADE_AND_SUSTAINABLE_DEVELOPMENT = (
        "21017",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre for Trade and Sustainable Development",
        ),
    )
    INTERNATIONAL_FEDERATION_OF_RED_CROSS_AND_RED_CRESCENT_SOCIETIES = (
        "21018",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Federation of Red Cross and Red Crescent Societies",
        ),
    )
    INTERNATIONAL_FEDERATION_OF_SETTLEMENTS_AND_NEIGHBOURHOOD_CENTRES = (
        "21019",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Federation of Settlements and Neighbourhood Centres",
        ),
    )
    INTERNATIONAL_HIV_AIDS_ALLIANCE = (
        "21020",
        pgettext_lazy("OrganisationIdentifier", "International HIV/AIDS Alliance"),
    )
    INTERNATIONAL_INSTITUTE_FOR_ENVIRONMENT_AND_DEVELOPMENT = (
        "21021",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Institute for Environment and Development",
        ),
    )
    INTERNATIONAL_NETWORK_FOR_ALTERNATIVE_FINANCIAL_INSTITUTIONS = (
        "21022",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Network for Alternative Financial Institutions",
        ),
    )
    INTERNATIONAL_PLANNED_PARENTHOOD_FEDERATION = (
        "21023",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Planned Parenthood Federation",
        ),
    )
    INTER_PRESS_SERVICE__INTERNATIONAL_ASSOCIATION = (
        "21024",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Inter Press Service, International Association ",
        ),
    )
    INTERNATIONAL_SEISMOLOGICAL_CENTRE = (
        "21025",
        pgettext_lazy("OrganisationIdentifier", "International Seismological Centre"),
    )
    INTERNATIONAL_SERVICE_FOR_HUMAN_RIGHTS = (
        "21026",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Service for Human Rights",
        ),
    )
    INTERNATIONAL_TRUST_FUND_FOR_DEMINING_AND_MINE_VICTIMS_ASSISTANCE = (
        "21027",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Trust Fund for Demining and Mine Victims Assistance",
        ),
    )
    INTERNATIONAL_UNIVERSITY_EXCHANGE_FUND_IUEF_STIP__IN_AFRICA_AND_LATIN_AMERICA = (
        "21028",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International University Exchange Fund - IUEF Stip. in Africa and Latin America",
        ),
    )
    DOCTORS_WITHOUT_BORDERS = (
        "21029",
        pgettext_lazy("OrganisationIdentifier", "Doctors Without Borders"),
    )
    PAN_AFRICAN_INSTITUTE_FOR_DEVELOPMENT = (
        "21030",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Pan African Institute for Development",
        ),
    )
    PANOS_INSTITUTE = (
        "21031",
        pgettext_lazy("OrganisationIdentifier", "PANOS Institute"),
    )
    POPULATION_SERVICES_INTERNATIONAL = (
        "21032",
        pgettext_lazy("OrganisationIdentifier", "Population Services International"),
    )
    TRANSPARENCY_INTERNATIONAL = (
        "21033",
        pgettext_lazy("OrganisationIdentifier", "Transparency International"),
    )
    INTERNATIONAL_UNION_AGAINST_TUBERCULOSIS_AND_LUNG_DISEASE = (
        "21034",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Union Against Tuberculosis and Lung Disease",
        ),
    )
    WORLD_ORGANISATION_AGAINST_TORTURE = (
        "21035",
        pgettext_lazy("OrganisationIdentifier", "World Organisation Against Torture"),
    )
    WORLD_UNIVERSITY_SERVICE = (
        "21036",
        pgettext_lazy("OrganisationIdentifier", "World University Service"),
    )
    WOMEN_S_WORLD_BANKING = (
        "21037",
        pgettext_lazy("OrganisationIdentifier", "Women's World Banking"),
    )
    INTERNATIONAL_ALERT = (
        "21038",
        pgettext_lazy("OrganisationIdentifier", "International Alert"),
    )
    INTERNATIONAL_INSTITUTE_FOR_SUSTAINABLE_DEVELOPMENT = (
        "21039",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Institute for Sustainable Development",
        ),
    )
    INTERNATIONAL_WOMEN_S_TRIBUNE_CENTRE = (
        "21040",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Women's Tribune Centre",
        ),
    )
    SOCIETY_FOR_INTERNATIONAL_DEVELOPMENT = (
        "21041",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Society for International Development",
        ),
    )
    INTERNATIONAL_PEACEBUILDING_ALLIANCE = (
        "21042",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Peacebuilding Alliance",
        ),
    )
    EUROPEAN_PARLIAMENTARIANS_FOR_AFRICA = (
        "21043",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Parliamentarians for Africa",
        ),
    )
    INTERNATIONAL_COUNCIL_FOR_THE_CONTROL_OF_IODINE_DEFICIENCY_DISORDERS = (
        "21044",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Council for the Control of Iodine Deficiency Disorders",
        ),
    )
    AFRICAN_MEDICAL_AND_RESEARCH_FOUNDATION = (
        "21045",
        pgettext_lazy(
            "OrganisationIdentifier",
            "African Medical and Research Foundation",
        ),
    )
    AGENCY_FOR_COOPERATION_AND_RESEARCH_IN_DEVELOPMENT = (
        "21046",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Agency for Cooperation and Research in Development",
        ),
    )
    AGRICORD = (
        "21047",
        pgettext_lazy("OrganisationIdentifier", "AgriCord"),
    )
    ASSOCIATION_OF_AFRICAN_UNIVERSITIES = (
        "21048",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Association of African Universities",
        ),
    )
    EUROPEAN_CENTRE_FOR_DEVELOPMENT_POLICY_MANAGEMENT = (
        "21049",
        pgettext_lazy(
            "OrganisationIdentifier",
            "European Centre for Development Policy Management",
        ),
    )
    GENEVA_CALL = (
        "21050",
        pgettext_lazy("OrganisationIdentifier", "Geneva Call"),
    )
    INSTITUT_SUPÉRIEUR_PANAFRICAINE_D_ECONOMIE_COOPÉRATIVE = (
        "21051",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Institut Supérieur Panafricaine d'Economie Coopérative",
        ),
    )
    IPAS_PROTECTING_WOMEN_S_HEALTH__ADVANCING_WOMEN_S_REPRODUCTIVE_RIGHTS = (
        "21053",
        pgettext_lazy(
            "OrganisationIdentifier",
            "IPAS-Protecting Women's Health, Advancing Women's Reproductive Rights ",
        ),
    )
    LIFE_AND_PEACE_INSTITUTE = (
        "21054",
        pgettext_lazy("OrganisationIdentifier", "Life and Peace Institute"),
    )
    REGIONAL_AIDS_TRAINING_NETWORK = (
        "21055",
        pgettext_lazy("OrganisationIdentifier", "Regional AIDS Training Network"),
    )
    RENEWABLE_ENERGY_AND_ENERGY_EFFICIENCY_PARTNERSHIP = (
        "21056",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Renewable Energy and Energy Efficiency Partnership",
        ),
    )
    INTERNATIONAL_CENTRE_FOR_TRANSITIONAL_JUSTICE = (
        "21057",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Centre for Transitional Justice",
        ),
    )
    GLOBAL_ALLIANCE_FOR_IMPROVED_NUTRITION = (
        "30001",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Global Alliance for Improved Nutrition",
        ),
    )
    GLOBAL_E_SCHOOLS_AND_COMMUNITIES_INITIATIVE = (
        "30003",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Global e-Schools and Communities Initiative",
        ),
    )
    GLOBAL_WATER_PARTNERSHIP = (
        "30004",
        pgettext_lazy("OrganisationIdentifier", "Global Water Partnership"),
    )
    INTERNATIONAL_AIDS_VACCINE_INITIATIVE = (
        "30005",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International AIDS Vaccine Initiative",
        ),
    )
    INTERNATIONAL_PARTNERSHIP_ON_MICROBICIDES = (
        "30006",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Partnership on Microbicides",
        ),
    )
    GLOBAL_ALLIANCE_FOR_ICT_AND_DEVELOPMENT = (
        "30007",
        pgettext_lazy(
            "OrganisationIdentifier",
            "Global Alliance for ICT and Development",
        ),
    )
    CITIES_ALLIANCE = (
        "30008",
        pgettext_lazy("OrganisationIdentifier", "Cities Alliance"),
    )
    SMALL_ARMS_SURVEY = (
        "30009",
        pgettext_lazy("OrganisationIdentifier", "Small Arms Survey"),
    )
    INTERNATIONAL_DRUG_PURCHASE_FACILITY = (
        "30010",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International drug purchase facility",
        ),
    )
    INTERNATIONAL_UNION_FOR_THE_CONSERVATION_OF_NATURE = (
        "30011",
        pgettext_lazy(
            "OrganisationIdentifier",
            "International Union for the Conservation of Nature",
        ),
    )
    GLOBAL_DEVELOPMENT_NETWORK = (
        "31001",
        pgettext_lazy("OrganisationIdentifier", "Global Development Network"),
    )
    GLOBAL_KNOWLEDGE_PARTNERSHIP = (
        "31002",
        pgettext_lazy("OrganisationIdentifier", "Global Knowledge Partnership"),
    )
