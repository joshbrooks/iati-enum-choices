from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationRegistrationAgency(models.TextChoices):
    """
    The values from this codelist are used to identify the particular list that an organisation identifier was drawn from. The codelist provides a register of known identifier lists, including national company registers, NGO directories and international and multilateral organisation lists - along with guidance and online resources to help locate the identifiers assigned to a specific organisation. As of 17 July 2017 this list is maintained by the org-id.guide project. Data publishers can now search for and locate the relevant list for a particular organisation identifier using the `org-id.guide website <http://org-id.guide/>`__. The full register of identifier sources is also available to download in `XML <http://org-id.guide/download.xml>`__, `JSON <http://org-id.guide/download.json>`__ and `CSV <http://org-id.guide/download.csv>`__ formats. IATI periodically replicates the codelist of identifier sources from org-id.guide, to assist those accessing IATI documentation. However, it is advised that the most up-to-date source is the `org-id.guide project <http://org-id.guide/>`__. If org-id.guide does not contain an entry for the kind of organisation you need to identify, you can make a request a new list is included in the register following the `guidance <http://docs.org-id.guide/en/latest/contribute/>`__ or by getting in touch with org-id.guide at: contact@org-id.guide.
    """

    AJMAN_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-ACCI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ajman Chamber of Commerce and Industry",
        ),
    )
    ABU_DHABI_COMMERCIAL_DIRECTORY = (
        "AE-ADCD",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Abu Dhabi Commercial Directory",
        ),
    )
    AJMAN_FREE_ZONE_AUTHORITY = (
        "AE-AFZ",
        pgettext_lazy("OrganisationRegistrationAgency", "Ajman Free Zone Authority"),
    )
    DUBAI_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-DCCI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Dubai Chamber of Commerce and Industry ",
        ),
    )
    DUBAI_FINANCIAL_SERVICES_AUTHORITY = (
        "AE-DFSA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Dubai Financial Services Authority ",
        ),
    )
    DUBAI_INTERNATIONAL_FINANCIAL_CENTRE = (
        "AE-DIFC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Dubai International Financial Centre",
        ),
    )
    DUBAI_MULTI_COMMODITIES_CENTRE = (
        "AE-DMCC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Dubai Multi Commodities Centre",
        ),
    )
    FUJAIRAH_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-FCCI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Fujairah Chamber of Commerce and Industry",
        ),
    )
    FUJAIRAH_FREE_ZONE_COMPANY_LISTING = (
        "AE-FFZ",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Fujairah Free Zone Company Listing",
        ),
    )
    HAMRIYAH_FREE_ZONE_AUTHORITY = (
        "AE-HFZA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Hamriyah Free Zone Authority",
        ),
    )
    RAS_AL_KHAIMAH_INVESTMENT_AUTHORITY = (
        "AE-RAKIA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ras al-Khaimah Investment Authority",
        ),
    )
    RAS_AL_KHAIMAH_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-RK_CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ras al-Khaimah Chamber of Commerce and Industry",
        ),
    )
    SHARJAH_AIRPORT_INTERNATIONAL_FREE_ZONE = (
        "AE-SAIF",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Sharjah Airport International Free Zone",
        ),
    )
    SHARJAH_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-SCCI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Sharjah Chamber of Commerce and Industry",
        ),
    )
    UMM_AL_QUWAIN_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-UQCCI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Umm al-Quwain Chamber of Commerce and Industry",
        ),
    )
    AFGHANISTAN_CENTRAL_BUSINESS_REGISTRY = (
        "AF-CBR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Afghanistan Central Business Registry",
        ),
    )
    MINISTRY_OF_ECONOMY_NGO_DEPARTMENT = (
        "AF-MOE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Economy NGO Department ",
        ),
    )
    THE_NATIONAL_CENTRE_OF_COMMUNITY_ORGANISATIONS__ARGENTINA_ = (
        "AR-CENOC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The National Centre of Community Organisations (Argentina)",
        ),
    )
    UNIQUE_TAX_IDENTIFICATION_CODE__ARGENTINA_ = (
        "AR-CUIT",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Unique Tax Identification Code (Argentina)",
        ),
    )
    AUSTRIA_COMPANY_REGISTER = (
        "AT-FB",
        pgettext_lazy("OrganisationRegistrationAgency", "Austria Company Register"),
    )
    VAT_NUMBER__AUSTRIA_COMPANY_REGISTER_ = (
        "AT-UID",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "VAT number (Austria Company Register)",
        ),
    )
    AUSTRALIAN_BUSINESS_REGISTER = (
        "AU-ABN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Australian Business Register",
        ),
    )
    AUSTRALIAN_CHARITIES_AND_NOT_FOR_PROFITS_COMMISSION = (
        "AU-ACNC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Australian Charities and Not-for-profits Commission",
        ),
    )
    STATE_REGISTER_OF_COMMERCIAL_ENTITIES__MINISTRY_OF_TAXES_OF_AZERBAIJAN_REPUBLIC_ = (
        "AZ-IVI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "State Register of Commercial Entities (Ministry of Taxes of Azerbaijan Republic)",
        ),
    )
    BANGLADESH_NGO_AFFAIRS_BUREAU = (
        "BD-NAB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Bangladesh NGO Affairs Bureau ",
        ),
    )
    CROSSROADS_BANK_FOR_ENTERPRISES = (
        "BE-BCE_KBO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Crossroads Bank for Enterprises ",
        ),
    )
    AU_GREFFE_DU_TRIBUNAL_DE_COMMERCE_FRANCOPHONE_DE_BRUXELLES = (
        "BE-GTCF",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Au Greffe du Tribunal de Commerce Francophone de Bruxelles",
        ),
    )
    COMMERCIAL_REGISTER = (
        "BG-EIK",
        pgettext_lazy("OrganisationRegistrationAgency", "Commercial Register"),
    )
    UNIQUE_TAX_IDENTIFIER = (
        "BJ-IFU",
        pgettext_lazy("OrganisationRegistrationAgency", "Unique Tax Identifier"),
    )
    COMPANIES_AND_INTELLECTUAL_PROPERTY_AUTHORITY__BOTSWANA_ = (
        "BW-CIPA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Companies and Intellectual Property Authority (Botswana)",
        ),
    )
    UNIFIED_STATE_REGISTER_OF_LEGAL_ENTITIES_AND_INDIVIDUAL_ENTREPRENEURS__MINISTRY_OF_JUSTICE_OF_THE_REPUBLIC_OF_BELARUS_ = (
        "BY-ADR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Unified State Register of Legal Entities and Individual Entrepreneurs (Ministry of Justice of the Republic of Belarus)",
        ),
    )
    CORPORATIONS_CANADA = (
        "CA-CC",
        pgettext_lazy("OrganisationRegistrationAgency", "Corporations Canada"),
    )
    CANADIAN_REVENUE_AGENCY = (
        "CA-CRA_ACR",
        pgettext_lazy("OrganisationRegistrationAgency", "Canadian Revenue Agency "),
    )
    LIST_OF_LEGAL_DEPARTMENT_NAMES__GOVERNMENT_OF_CANADA_ = (
        "CA-GOV",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "List of legal department names (Government of Canada)",
        ),
    )
    CORPORATE_REGISTRY_OFFICE = (
        "CA_AB-ABT",
        pgettext_lazy("OrganisationRegistrationAgency", "Corporate Registry Office "),
    )
    BRITISH_COLUMBIA_CORPORATE_REGISTRY = (
        "CA_BC-BRC_CBR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "British Columbia Corporate Registry ",
        ),
    )
    MANITOBA_COMPANIES_OFFICE__DEPARTMENT_OF_ENTREPRENEURSHIP__TRAINING_AND_TRADE = (
        "CA_MB-MTB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Manitoba Companies Office, Department of Entrepreneurship, Training and Trade ",
        ),
    )
    CORPORATE_REGISTRY = (
        "CA_NB-NWB_NOB",
        pgettext_lazy("OrganisationRegistrationAgency", "Corporate Registry "),
    )
    REGISTRY_OF_COMPANIES__DEPARTMENT_OF_GOVERNMENT_SERVICES = (
        "CA_NL-NFL_TNL",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Registry of Companies, Department of Government Services",
        ),
    )
    NOVA_SCOTIA_REGISTRY_OF_JOINT_STOCK_COMPANIES = (
        "CA_NS-NVS_NVE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Nova Scotia Registry of Joint Stock Companies ",
        ),
    )
    CANADIAN_PROVINCIAL_CORPORATE_REGISTRATION_NORTHWEST_TERRITORIES = (
        "CA_NT-NWT_TNO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Canadian Provincial Corporate Registration - Northwest Territories ",
        ),
    )
    NUNAVUT_DEPARTMENT_OF_JUSTICE_CORPORATE_REGISTRIES = (
        "CA_NU-NNV",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Nunavut Department of Justice - Corporate Registries",
        ),
    )
    SERVICEONTARIO__MINISTRY_OF_GOVERNMENT_SERVICES = (
        "CA_ON-ONT",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "ServiceOntario, Ministry of Government Services ",
        ),
    )
    PRINCE_EDWARD_ISLAND_CORPORATE = (
        "CA_PE-PEI_IPE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Prince Edward Island Corporate",
        ),
    )
    QUEBEC_BUSINESS_REGISTRAR = (
        "CA_QC-QBC",
        pgettext_lazy("OrganisationRegistrationAgency", "Quebec Business Registrar "),
    )
    SASKATCHEWAN_CORPORATE_REGISTRY = (
        "CA_SK-SKN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Saskatchewan Corporate Registry ",
        ),
    )
    YUKON_CORPORATE_AFFAIRS = (
        "CA_YT-YKT",
        pgettext_lazy("OrganisationRegistrationAgency", "Yukon Corporate Affairs "),
    )
    COMMERCIAL_REGISTRY__FEDERAL_OFFICE_OF_JUSTICE__SWITZERLAND_ = (
        "CH-FDJP",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Commercial Registry, Federal Office of Justice (Switzerland)",
        ),
    )
    STATE_ADMINISTRATION_FOR_INDUSTRY_AND_COMMERCE__SAIC_ = (
        "CN-SAIC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "State Administration for Industry and Commerce (SAIC)",
        ),
    )
    BOGOTA_CHAMBER_OF_COMMERCE = (
        "CO-CCB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Bogota Chamber of Commerce ",
        ),
    )
    UNIFIED_COMMERCIAL_AND_SOCIAL_REGISTRY__RUES_ = (
        "CO-RUE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Unified Commercial and Social Registry (RUES) ",
        ),
    )
    CYPRUS_DEPARTMENT_OF_REGISTRAR_OF_COMPANIES_AND_OFFICIAL_RECEIVER__DRCOR_ = (
        "CY-DRCOR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Cyprus Department of Registrar of Companies and Official Receiver (DRCOR)",
        ),
    )
    TAX_ID__DIČ__CZECH_REPUBLIC = (
        "CZ-DIC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Tax ID (DIČ) Czech Republic",
        ),
    )
    ACCESS_TO_REGISTERS_OF_ECONOMIC_SUBJECTS = (
        "CZ-ICO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Access to Registers of Economic Subjects ",
        ),
    )
    COMMON_REGISTER_PORTAL_OF_THE_GERMAN_FEDERAL_STATES__CRP_ = (
        "DE-CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Common Register Portal of the German Federal States (CRP)",
        ),
    )
    DANISH_CENTRAL_BUSINESS_REGISTER = (
        "DK-CVR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Danish Central Business Register",
        ),
    )
    E_BUSINESS_REGISTER__ESTONIA_ = (
        "EE-KMKR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "e-Business Register (Estonia)",
        ),
    )
    CENTRE_OF_REGISTERS_AND_INFORMATION_SYSTEMS__RIK_ = (
        "EE-RIK",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Centre of Registers and Information Systems (RIK)",
        ),
    )
    MINISTRY_OF_SOCIAL_SOLIDARITY_AND_JUSTICE__EGYPT_ = (
        "EG-MOSS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Social Solidarity and Justice (Egypt)",
        ),
    )
    COMMON_DIRECTORY_OF_ORGANIZATIONAL_UNITS_AND_OFFICES_DIR3 = (
        "ES-DIR3",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Common Directory of Organizational Units and Offices - DIR3",
        ),
    )
    CENTRAL_COMMERCIAL_REGISTER_OF_THE_KINGDOM_OF_SPAIN = (
        "ES-RMC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Central Commercial Register of the Kingdom of Spain",
        ),
    )
    CHARITIES_AND_SOCIETIES_AGENCY__ETHIOPIA_ = (
        "ET-CSA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Charities and Societies Agency (Ethiopia)",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "ET-MFA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Foreign Affairs",
        ),
    )
    MINISTRY_OF_TRADE__ETHIOPIA_ = (
        "ET-MOT",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Trade (Ethiopia)",
        ),
    )
    FINNISH_PATENT_AND_REGISTRATION_OFFICE = (
        "FI-PRO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Finnish Patent and Registration Office ",
        ),
    )
    THE_NATIONAL_INSTITUTE_OF_STATISTICS_AND_ECONOMIC_STUDIES = (
        "FR-INSEE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The National Institute of Statistics and Economic Studies ",
        ),
    )
    TRADE_AND_COMPANIES_REGISTER = (
        "FR-RCS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Trade and Companies Register ",
        ),
    )
    CHARITY_COMMISSION = (
        "GB-CHC",
        pgettext_lazy("OrganisationRegistrationAgency", "Charity Commission"),
    )
    COMPANIES_HOUSE = (
        "GB-COH",
        pgettext_lazy("OrganisationRegistrationAgency", "Companies House"),
    )
    REGISTER_OF_SCHOOLS__ENGLAND_AND_WALES_ = (
        "GB-EDU",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Register of Schools (England and Wales)",
        ),
    )
    GOVERNMENT_ORGANISATION_REGISTER = (
        "GB-GOR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Government Organisation Register",
        ),
    )
    UK_GOVERNMENT_DEPARTMENTS_REFERENCE_NUMBERS__IATI_STANDARD_ = (
        "GB-GOV",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "UK Government Departments Reference Numbers (IATI Standard)",
        ),
    )
    GOV_UK_UK_GOVERNMENT_DEPARTMENTS__AGENCIES___PUBLIC_BODIES = (
        "GB-GOVUK",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "GOV.UK - UK Government Departments, Agencies & Public Bodies",
        ),
    )
    SCHOOLS_PLUS__DEPARTMENT_OF_EDUCATION__NORTHERN_IRELAND_ = (
        "GB-IRN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Schools Plus, Department of Education (Northern Ireland)",
        ),
    )
    LOCAL_AUTHORITIES_FOR_ENGLAND_REGISTER = (
        "GB-LAE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Local Authorities for England Register",
        ),
    )
    SCOTTISH_LOCAL_AUTHORITY_REGISTER = (
        "GB-LAS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Scottish Local Authority Register",
        ),
    )
    MUTUALS_PUBLIC_REGISTER = (
        "GB-MPR",
        pgettext_lazy("OrganisationRegistrationAgency", "Mutuals Public Register"),
    )
    NHS_DIGITAL_ORGANISATION_DATA_SERVICE = (
        "GB-NHS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "NHS Digital - Organisation Data Service",
        ),
    )
    THE_CHARITY_COMMISSION_FOR_NORTHERN_IRELAND = (
        "GB-NIC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The Charity Commission for Northern Ireland",
        ),
    )
    PRINCIPAL_LOCAL_AUTHORITY_REGISTER_FOR_WALES = (
        "GB-PLA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Principal Local Authority Register for Wales",
        ),
    )
    HM_REVENUE_AND_CUSTOMS = (
        "GB-REV",
        pgettext_lazy("OrganisationRegistrationAgency", "HM Revenue and Customs"),
    )
    SCOTTISH_CHARITY_REGISTER = (
        "GB-SC",
        pgettext_lazy("OrganisationRegistrationAgency", "Scottish Charity Register"),
    )
    REGISTERED_SOCIAL_HOUSING_PROVIDERS__ENGLAND_ = (
        "GB-SHPE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Registered Social Housing Providers (England)",
        ),
    )
    UK_REGISTER_OF_LEARNING_PROVIDERS = (
        "GB-UKPRN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "UK Register of Learning Providers",
        ),
    )
    REGISTER_OF_ENTREPRENEURIAL_AND_NON_ENTREPRENEURIAL_LEGAL_ENTITIES__GEORGIA = (
        "GE-NAPR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Register of Entrepreneurial and Non-Entrepreneurial Legal Entities, Georgia",
        ),
    )
    GUERNSEY_REGISTRY = (
        "GG-RCE",
        pgettext_lazy("OrganisationRegistrationAgency", "Guernsey Registry"),
    )
    DEPARTMENT_OF_SOCIAL_DEVELOPMENTS = (
        "GH-DSW",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Department of Social Developments",
        ),
    )
    HONG_KONG_COMPANIES_REGISTER = (
        "HK-CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Hong Kong Companies Register",
        ),
    )
    CROATIAN_COURT_BUSINESS_REGISTER = (
        "HR-MBS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Croatian Court Business Register",
        ),
    )
    CROATIA_COURT_REGISTER = (
        "HR-OIB",
        pgettext_lazy("OrganisationRegistrationAgency", "Croatia Court Register"),
    )
    INFORMATION_AND_ELECTRONIC_COMPANY_REGISTRATION_SERVICE = (
        "HU-AFA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Information and Electronic Company Registration Service",
        ),
    )
    MINISTRY_OF_HOME_AFFAIRS = (
        "ID-KDN",
        pgettext_lazy("OrganisationRegistrationAgency", "Ministry of Home Affairs "),
    )
    MINISTRY_OF_JUSTICE___HUMAN_RIGHTS = (
        "ID-KHH",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Justice & Human Rights",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "ID-KLN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Foreign affairs",
        ),
    )
    INDONESIA_NGOS_REGISTERED_AT_PROVINICIAL_LEVEL = (
        "ID-PRO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Indonesia - NGOs registered at Provinicial Level",
        ),
    )
    THE_SMERU_RESEARCH_INSTITUTE = (
        "ID-SMR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The SMERU Research Institute",
        ),
    )
    CHARITIES_REGULATORY_AUTHORITY_OF_IRELAND = (
        "IE-CHY",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Charities Regulatory Authority of Ireland",
        ),
    )
    IRISH_COMPANIESREGISTRATION_OFFICE = (
        "IE-CRO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Irish CompaniesRegistration Office",
        ),
    )
    REGISTRAR_OF_COMPANIES__ISRAEL_ = (
        "IL-ROC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Registrar of Companies (Israel)",
        ),
    )
    ISLE_OF_MAN_COMPANIES_REGISTRY = (
        "IM-CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Isle of Man Companies Registry",
        ),
    )
    ISLE_OF_MAN_INDEX_OF_REGISTERED_CHARITIES = (
        "IM-GR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Isle of Man Index of Registered Charities ",
        ),
    )
    GOVERNMENT_OF_INDIA__MINISTRY_OF_CORPORATE_AFFAIRS = (
        "IN-MCA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Government of India, Ministry of Corporate Affairs",
        ),
    )
    MINISTRY_OF_HOME_AFFAIRS__INDIA__FOREIGN_CONTRIBUTIONS__REGULATION__ACT_REGISTER = (
        "IN-MHA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Home Affairs (India) Foreign Contributions (Regulation) Act Register",
        ),
    )
    ITALIAN_TAX_CODE___VAT_NUMBER = (
        "IT-CF",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Italian Tax Code / VAT Number",
        ),
    )
    BUSINESS_REGISTER_OF_THE_ITALIAN_CHAMBERS_OF_COMMERCE = (
        "IT-RI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Business Register of the Italian Chambers of Commerce",
        ),
    )
    JERSEY_FINANCIAL_SERVICES_COMMISSION__JFSC_ = (
        "JE-FSC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Jersey Financial Services Commission (JFSC)",
        ),
    )
    JERSEY_OVERSEAS_AID_COMMISSION = (
        "JE-OAC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Jersey Overseas Aid Commission",
        ),
    )
    COMPANIES_CONTROL_DEPARTMENT__JORDAN_ = (
        "JO-CCD",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Companies Control Department (Jordan)",
        ),
    )
    REGISTER_OF_ASSOCIATIONS__JORDAN = (
        "JO-MSD",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Register of Associations, Jordan",
        ),
    )
    NATIONAL_TAX_AGENCY_CORPORATE_NUMBER_PUBLICATION_SITE = (
        "JP-JCN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "National Tax Agency Corporate Number Publication Site",
        ),
    )
    NGO_S_COORDINATION_BOARD = (
        "KE-NCB",
        pgettext_lazy("OrganisationRegistrationAgency", "NGO's Coordination Board"),
    )
    REGISTAR_OF_COMPANIES = (
        "KE-RCO",
        pgettext_lazy("OrganisationRegistrationAgency", "Registar of Companies"),
    )
    REGISTRAR_OF_SOCIETIES = (
        "KE-RSO",
        pgettext_lazy("OrganisationRegistrationAgency", "Registrar of Societies"),
    )
    ELECTRONIC_DATABASE_OF_LEGAL_ENTITIES_AND_BRANCHES__KRYGYZSTAN_ = (
        "KG-ID",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Electronic database of legal entities and branches (Krygyzstan)",
        ),
    )
    KYRGYZ_REPUBLIC_REGISTER_OF_LEGAL_ENTITIES = (
        "KG-INN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Kyrgyz Republic Register of Legal Entities",
        ),
    )
    BUSINESS_IDENTIFICATION_NUMBER__BIN_ = (
        "KZ-BIN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Business Identification Number (BIN)",
        ),
    )
    LEBANESE_MINISTRY_OF_JUSTICE__COMMERCIAL_REGISTER = (
        "LB-CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Lebanese Ministry of Justice, Commercial Register",
        ),
    )
    MINISTRY_OF_INTERIOR__LEBANON_ = (
        "LB-MOI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Interior (Lebanon)",
        ),
    )
    LESOTHO_COUNCIL_OF_NON_GOVERNMENTAL_ORGANISATIONS = (
        "LS-LCN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Lesotho Council of Non Governmental Organisations",
        ),
    )
    LITHUANIA_REGISTER_OF_LEGAL_ENTITIES = (
        "LT-PVM",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Lithuania Register of Legal Entities",
        ),
    )
    INFORMATION_PLATFORM_OF_LEGAL_ENTITIES__LITHUANIA_ = (
        "LT-RC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Information Platform of Legal Entities (Lithuania)",
        ),
    )
    REGISTER_OF_ENTERPRISES_OF_THE_REPUBLIC_OF_LATVIA = (
        "LV-RE",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Register of Enterprises of the Republic of Latvia",
        ),
    )
    LEGAL_ENTITY_REGISTRATION_NUMBER__IDNO__MOLDOVA = (
        "MD-IDNO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Legal entity registration number (IDNO) Moldova",
        ),
    )
    THE_CHAMBER_OF_COMMERCE_AND_INDUSTRY_OF_MALI = (
        "ML-CCIM",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The Chamber of Commerce and Industry of Mali",
        ),
    )
    TAX_IDENTIFICATION_NUMBER = (
        "ML-NIF",
        pgettext_lazy("OrganisationRegistrationAgency", "Tax Identification Number"),
    )
    MINISTRY_OF_HOME_AFFAIRS_CENTRAL_COMMITTEE_FOR_THE_REGISTRATION_AND_SUPERVISION_OF_ORGANISATIONS = (
        "MM-MHA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Home Affairs - Central Committee for the Registration and Supervision of Organisations",
        ),
    )
    COMPANIES_AND_BUSINESSES_REGISTRATION_INTEGRATED_SYSTEM__MAURITIUS = (
        "MU-CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Companies and Businesses Registration Integrated System, Mauritius",
        ),
    )
    THE_COUNCIL_FOR_NON_GOVERNMENTAL_ORGANISATIONS_IN_MALAWI = (
        "MW-CNM",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The Council for Non Governmental Organisations in Malawi",
        ),
    )
    MALAWI_REVENUE_AUTHORITY = (
        "MW-MRA",
        pgettext_lazy("OrganisationRegistrationAgency", "Malawi Revenue Authority"),
    )
    NGO_BOARD_OF_MALAWI = (
        "MW-NBM",
        pgettext_lazy("OrganisationRegistrationAgency", "NGO Board of Malawi"),
    )
    REGISTRAR_GENERAL__DEPARTMENT_OF_JUSTICE = (
        "MW-RG",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Registrar General, Department of Justice",
        ),
    )
    BUDGET_CLASSIFICATION_OF_PUBLIC_ENTITIES__MEXICO_ = (
        "MX-CPA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Budget Classification of Public Entities (Mexico)",
        ),
    )
    FEDERAL_TAXPAYERS_REGISTRY = (
        "MX-RFC",
        pgettext_lazy("OrganisationRegistrationAgency", "Federal Taxpayers Registry"),
    )
    COMPANIES_COMMISSION_OF_MALAYSIA = (
        "MY-SSM",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Companies Commission of Malaysia",
        ),
    )
    MOZAMBIQUE_COMMERCIAL_REGISTRY = (
        "MZ-CR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Mozambique Commercial Registry",
        ),
    )
    MOZAMBIQUE_MINISTRY_OF_JUSTICE = (
        "MZ-MOJ",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Mozambique Ministry of Justice",
        ),
    )
    TAXPAYER_SINGLE_IDENTIFICATION_NUMBER__MOZAMBIQUE_ = (
        "MZ-NUIT",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Taxpayer Single Identification Number (Mozambique)",
        ),
    )
    BUREAU_OF_PUBLIC_PROCUREMENT__BPP__CONTRACTOR_REGISTRATION_SYSTEM__NIGERIA_ = (
        "NG-BPP",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Bureau of Public Procurement (BPP) Contractor Registration System (Nigeria)",
        ),
    )
    NIGERIAN_CORPORATE_AFFAIRS_COMMISSION = (
        "NG-CAC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Nigerian Corporate Affairs Commission",
        ),
    )
    CHAMBER_OF_COMMERCE__NETHERLANDS_ = (
        "NL-KVK",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Chamber of Commerce (Netherlands)",
        ),
    )
    OVERHEID_NL_WEB_METADATA_STANDARD = (
        "NL-OWMS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Overheid.nl Web Metadata Standard ",
        ),
    )
    BRØNNØYSUNDREGISTRENE = (
        "NO-BRC",
        pgettext_lazy("OrganisationRegistrationAgency", "Brønnøysundregistrene"),
    )
    COMPANY_REGISTRAR_OFFICE = (
        "NP-CRO",
        pgettext_lazy("OrganisationRegistrationAgency", "Company Registrar Office"),
    )
    SOCIAL_WELFARE_COUNCIL_NEPAL = (
        "NP-SWC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Social Welfare Council Nepal",
        ),
    )
    PERUVIAN_NATIONAL_SUPERINTENDENCY_OF_PUBLIC_REGISTRIES_REGISTERED_LEGAL_ENTITIES = (
        "PE-SUNARP",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Peruvian National Superintendency of Public Registries - Registered Legal Entities ",
        ),
    )
    SECURITIES_AND_EXCHANGE_COMMISSION__PHILIPPINES_ = (
        "PH-SEC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Securities and Exchange Commission (Philippines)",
        ),
    )
    PAKISTAN_CENTRE_FOR_PHILANTHROPY = (
        "PK-PCP",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Pakistan Centre for Philanthropy",
        ),
    )
    PAKISTAN_VOLUNTARY_SOCIAL_WELFARE_AGENCY = (
        "PK-VSWA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Pakistan Voluntary Social Welfare Agency",
        ),
    )
    THE_NATIONAL_COURT_REGISTER__POLAND_ = (
        "PL-KRS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "The National Court Register (Poland)",
        ),
    )
    TAX_IDENTIFICATION_NUMBER__POLAND_ = (
        "PL-NIP",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Tax Identification Number (Poland)",
        ),
    )
    REGON_STATISTICAL_NUMBER_OF_AN_ECONOMY_ENTITY = (
        "PL-REGON",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "REGON - Statistical number of an economy entity",
        ),
    )
    MINISTRY_OF_INTERIOR__PALESTINE_ = (
        "PS-MOI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Interior (Palestine)",
        ),
    )
    PORTAL_OF_PUBLIC_SERVICES = (
        "PT-NIPPC",
        pgettext_lazy("OrganisationRegistrationAgency", "Portal of Public Services"),
    )
    CLASSIFICATION_OF_ENTITIES_IN_THE_NATIONAL_BUDGET_FOR_PARAGUAY = (
        "PY-PGN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Classification of Entities in the National Budget for Paraguay",
        ),
    )
    UNIQUE_TAXPAYER_REGISTRY__PARAGUAY = (
        "PY-RUC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Unique Taxpayer Registry, Paraguay",
        ),
    )
    NATIONAL_TRADE_REGISTER__ROMANIA_ = (
        "RO-CUI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "National Trade Register (Romania)",
        ),
    )
    SERBIAN_BUSINESS_REGISTRATIONS_AGENCY = (
        "RS-APR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Serbian Business Registrations Agency ",
        ),
    )
    TAX_IDENTIFICATION_NUMBER_REGISTER = (
        "RS-PIB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Tax identification number register",
        ),
    )
    UNIFORM_STATE_REGISTER_OF_LEGAL_ENTITIES_OF_RUSSIAN_FEDERATION = (
        "RU-INN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Uniform State Register of Legal Entities of Russian Federation",
        ),
    )
    UNIFIED_STATE_REGISTER_OF_LEGAL_ENTITIES__USRLE___RUSSIAN_FEDERATION = (
        "RU-OGRN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Unified State Register of Legal Entities (USRLE), Russian Federation",
        ),
    )
    BOLAGSVERKET = (
        "SE-BLV",
        pgettext_lazy("OrganisationRegistrationAgency", "Bolagsverket "),
    )
    LEGAL__FINANCIAL_AND_ADMINISTRATIVE_SERVICES_AGENCY__SWEDEN_ = (
        "SE-KK",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Legal, Financial and Administrative Services Agency (Sweden)",
        ),
    )
    BUSINESS_REGISTRATION_NUMBER__ORGANISATIONSNUMMER___SWEDEN = (
        "SE-ON",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Business Registration Number (Organisationsnummer), Sweden",
        ),
    )
    ACCOUNTING_AND_CORPORATE_REGULATORY_AUTHORITY__ACRA_ = (
        "SG-ACRA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Accounting and Corporate Regulatory Authority (ACRA)",
        ),
    )
    SLOVENIAN_BUSINESS_REGISTER = (
        "SI-PRS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Slovenian Business Register",
        ),
    )
    TAX_IDENTIFICATION_NUMBER__SLOVENIA_ = (
        "SI-TIN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Tax Identification Number (Slovenia)",
        ),
    )
    MINISTRY_OF_JUSTICE_BUSINESS_REGISTER = (
        "SK-ORSR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Ministry of Justice Business Register",
        ),
    )
    SLOVAKIA_MINISTRY_OF_INTERIOR_TRADE_REGISTER = (
        "SK-ZRSR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Slovakia Ministry Of Interior Trade Register",
        ),
    )
    NATIONAL_IDENTIFICATION_NUMBER_OF_COMPANIES_AND_ASSOCIATIONS__NINEA___SENEGAL = (
        "SN-NINEA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "National Identification Number of Companies and Associations (NINEA), Senegal",
        ),
    )
    SOUTH_SUDAN_RELIEF_AND_REHABILITATION_COMMISSION = (
        "SS-RRC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "South Sudan Relief and Rehabilitation Commission",
        ),
    )
    MERSIS_CENTRAL_TRADE_REGISTRY_SYSTEM = (
        "TR-MERSIS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "MERSIS - Central Trade Registry System",
        ),
    )
    DEPARTMENT_OF_ASSOCIATIONS__MINISTRY_OF_INTERIOR__TURKEY_ = (
        "TR-MOI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Department of Associations (Ministry of Interior, Turkey)",
        ),
    )
    TANZANIA_BUSINESS_REGISTRATIONS_AND_LICENSING_AGENCY = (
        "TZ-BRLA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Tanzania Business Registrations and Licensing Agency",
        ),
    )
    TANZANIA_REVENUE_AGENCY = (
        "TZ-TRA",
        pgettext_lazy("OrganisationRegistrationAgency", "Tanzania Revenue Agency"),
    )
    UNITED_STATE_REGISTER = (
        "UA-EDR",
        pgettext_lazy("OrganisationRegistrationAgency", "United State Register "),
    )
    NGO_BOARD__MINISTRY_OF_INTERNAL_AFFAIRS = (
        "UG-NGB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "NGO Board, Ministry of Internal Affairs",
        ),
    )
    REGISTRATION_SERVICES_BUREAU = (
        "UG-RSB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Registration Services Bureau",
        ),
    )
    CORPORATION_REGISTRATION_IS_THE_RESPONSIBILITY_OF_EACH_STATE__SEE_LINK_ = (
        "US-DOS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Corporation registration is the responsibility of each state (see link)",
        ),
    )
    EMPLOYER_IDENTIFICATION_NUMBER_INTERNAL_REVENUE_SERVICE = (
        "US-EIN",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Employer Identification Number - Internal Revenue Service",
        ),
    )
    INDEX_OF_U_S__GOVERNMENT_DEPARTMENTS_AND_AGENCIES = (
        "US-USAGOV",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Index of U.S. Government Departments and Agencies",
        ),
    )
    UNITED_STATE_REGISTER_OF_CORPORATE_ENTITES = (
        "UZ-KTUT",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "United State Register of Corporate Entites",
        ),
    )
    EXAMPLE_DATA_PREFIX = (
        "XE-EXAMPLE",
        pgettext_lazy("OrganisationRegistrationAgency", "Example Data Prefix"),
    )
    ECONOMIC_OPERATORS_IDENTIFICATION_AND_REGISTRATION_SYSTEM = (
        "XI-EORI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Economic Operators Identification and Registration system",
        ),
    )
    GLOBAL_RESEARCH_IDENTIFIERS_DATABASE = (
        "XI-GRID",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Global Research Identifiers Database",
        ),
    )
    INTERNATIONAL_AID_TRANSPARENCY_INITIATIVE_ORGANISATION_IDENTIFIER = (
        "XI-IATI",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "International Aid Transparency Initiative Organisation Identifier",
        ),
    )
    PUBLIC_BODIES_OPEN_KNOWLEDGE_FOUNDATION = (
        "XI-PB",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Public Bodies - Open Knowledge Foundation ",
        ),
    )
    PERMID__THOMPSON_REUTERS_PERMANENT_IDENTIFIER = (
        "XI-PID",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "PermID: Thompson Reuters Permanent Identifier",
        ),
    )
    WIKIDATA = (
        "XI-WIKIDATA",
        pgettext_lazy("OrganisationRegistrationAgency", "Wikidata"),
    )
    OECD_DEVELOPMENT_ASSISTANCE_COMMITTEE = (
        "XM-DAC",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "OECD Development Assistance Committee",
        ),
    )
    UNITED_NATIONS_OFFICE_FOR_THE_COORDINATION_OF_HUMANITARIAN_AFFAIRS_FINANCIAL_TRACKING_SERVICES_IDENTIFIERS = (
        "XM-OCHA",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "United Nations Office for the Coordination of Humanitarian Affairs - Financial Tracking Services Identifiers",
        ),
    )
    NUTS_EUROPEAN_UNION_NOMENCLATURE_OF_TERRITORIAL_UNITS_FOR_STATISTICS = (
        "XR-NUTS",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "NUTS - European Union Nomenclature of Territorial Units for Statistics",
        ),
    )
    COMPANIES_AND_INTELLECTUAL_PROPERTY_COMMISSION__CIPC_ = (
        "ZA-CIP",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Companies and Intellectual Property Commission (CIPC)",
        ),
    )
    NONPROFIT_ORGANISATION_DIRECTORATE_SOUTH_AFRICAN_DEPARTMENT_OF_SOCIAL_DEVELOPMENT = (
        "ZA-NPO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Nonprofit Organisation Directorate - South African Department of Social Development",
        ),
    )
    SA_REVENUE_SERVICE_TAX_EXEMPTION_UNIT = (
        "ZA-PBO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "SA Revenue Service Tax Exemption Unit ",
        ),
    )
    PATENTS_AND_COMPANIES_REGISTRATION_AGENCY = (
        "ZM-PCR",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Patents and Companies Registration Agency",
        ),
    )
    PRIVATE_VOLUNTARY_ORGANISATIONS_COUNCIL__ZIMBABWE_ = (
        "ZW-PVO",
        pgettext_lazy(
            "OrganisationRegistrationAgency",
            "Private Voluntary Organisations Council (Zimbabwe)",
        ),
    )
    REGISTRAR_OF_DEEDS = (
        "ZW-ROD",
        pgettext_lazy("OrganisationRegistrationAgency", "Registrar of Deeds"),
    )
