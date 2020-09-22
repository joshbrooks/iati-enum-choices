from django.db import models
from django.utils.translation import pgettext_lazy


class IATIOrganisationIdentifier(models.TextChoices):
    """
    This is a list of organisation identifiers that is maintained by the IATI Secretariat. The prefix for organisations on this list is XI-IATI If a bona fide organisation is not registered with any recognised or appropriate registration agency (http://iatistandard.org/202/codelists/OrganisationRegistrationAgency/) they should contact the IATI Technical Team who will exceptionally allocate an organisation identifier using the XI-IATI prefix. While some of these identifiers have been derived from DAC codes, this 'meaning' is not carried forward. i.e. IATI generated identifiers have no intrinsic meaning. For general guidance about constructing Organisation Identifiers, please see http://iatistandard.org/organisation-identifiers/
    """

    THE_COCA_COLA_EXPORT_CORPORATION = (
        "XI-IATI-1001",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "The Coca-Cola Export Corporation",
        ),
    )
    UNITED_MISSION_TO_NEPAL = (
        "XI-IATI-1002",
        pgettext_lazy("IATIOrganisationIdentifier", "United Mission to Nepal"),
    )
    ASSOCIATION_CENTRAFRICAINE_DE_TRADUCTION_DE_LA_BIBLE_ET_ALPHABETISATION = (
        "XI-IATI-ACATBA",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Association Centrafricaine de Traduction de la Bible et Alphabetisation",
        ),
    )
    AGÊNCIA_DE_DESENVOLVIMENTO_DO_VALE_DO_ZAMBEZE = (
        "XI-IATI-ADVZ",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Agência de Desenvolvimento do Vale do Zambeze",
        ),
    )
    AGRESULTS = (
        "XI-IATI-AGR",
        pgettext_lazy("IATIOrganisationIdentifier", "AgResults"),
    )
    ADMINISTRAÇÃO_DE_INFRA_ESTRUTURAS_DE_ÁGUAS_E_SANEAMENTO = (
        "XI-IATI-AIAS",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Administração de Infra-Estruturas de Águas e Saneamento",
        ),
    )
    ASSOCIATIONS_DES_JURISTES_SÉNÉGALAISES__AJS_ = (
        "XI-IATI-AJS",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Associations des Juristes Sénégalaises (AJS)",
        ),
    )
    ASSOCIATION_OF_TECHNICIANS_IN_INFORMATION_TECHNOLOGY_AND_COMMUNICATION__ATTIC_ = (
        "XI-IATI-ATTIC",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Association of Technicians in Information Technology and Communication (ATTIC)",
        ),
    )
    BANGLADESH_BUSINESS___DISABILITY_NETWORK = (
        "XI-IATI-BBDN",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Bangladesh Business & Disability Network",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT = (
        "XI-IATI-EBRD",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "European Bank for Reconstruction and Development",
        ),
    )
    BENEDICTINE_EYE_HOSPITAL__TORORO = (
        "XI-IATI-BEH",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Benedictine Eye Hospital, Tororo",
        ),
    )
    CABI = (
        "XI-IATI-CABI",
        pgettext_lazy("IATIOrganisationIdentifier", "CABI"),
    )
    THE_COMMONWEALTH_SECRETARIAT = (
        "XI-IATI-CWSEC",
        pgettext_lazy("IATIOrganisationIdentifier", "The Commonwealth Secretariat"),
    )
    DEMOCRATIC_GOVERNANCE_FACILITY = (
        "XI-IATI-DGF",
        pgettext_lazy("IATIOrganisationIdentifier", "Democratic Governance Facility"),
    )
    EUROPEAN_COMMISSION___DEVELOPMENT_AND_COOPERATION = (
        "XI-IATI-EC_DEVCO",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "European Commission – Development and Cooperation",
        ),
    )
    EUROPEAN_COMMISSION_HUMANITARIAN_AID___CIVIL_PROTECTION = (
        "XI-IATI-EC_ECHO",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "European Commission - Humanitarian Aid & Civil Protection",
        ),
    )
    ECONOMIC_AND_SOCIAL_FUND_FOR_DEVELOPMENT = (
        "XI-IATI-ESFD",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Economic and Social Fund for Development",
        ),
    )
    EUROPEAN_COMMISSION___SERVICE_FOR_FOREIGN_POLICY_INSTRUMENTS = (
        "XI-IATI-EC_FPI",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "European Commission – Service for Foreign Policy Instruments",
        ),
    )
    EUROPEAN_COMMISSION_NEIGHBOURHOOD_AND_ENLARGEMENT_NEGOTIATIONS = (
        "XI-IATI-EC_NEAR",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "European Commission - Neighbourhood and Enlargement Negotiations",
        ),
    )
    ENGAGE_FOUNDATION_FOR_RESEARCH_AND_DIALOGUE = (
        "XI-IATI-EFRD",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Engage Foundation for Research and Dialogue",
        ),
    )
    FEDERATION_OF_INSTITUTIONAL_ACTORS_BELGIUM__FIABEL_ = (
        "XI-IATI-FIABEL",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Federation of Institutional Actors Belgium (FIABEL)",
        ),
    )
    GARGAAR_RELIEF_AND_DEVELOPMENT_ORGANIZATION = (
        "XI-IATI-GREDO",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Gargaar Relief and Development Organization",
        ),
    )
    INTER_AMERICAN_DEVELOPMENT_BANK = (
        "XI-IATI-IADB",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Inter-American Development Bank",
        ),
    )
    INTERNATIONAL_FERTILIZER_DEVELOPMENT_CENTER = (
        "XI-IATI-IFDC",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "International Fertilizer Development Center",
        ),
    )
    INTERNATIONAL_CLIMATE_INITIATIVE__IKI_ = (
        "XI-IATI-IKI",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "International Climate Initiative (IKI)",
        ),
    )
    THE_KING_HUSSEIN_FOUNDATION__KHF_ = (
        "XI-IATI-KHF",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "The King Hussein Foundation (KHF)",
        ),
    )
    LIVING_PEACE_INSTITUTE = (
        "XI-IATI-LPI",
        pgettext_lazy("IATIOrganisationIdentifier", "Living Peace Institute"),
    )
    MULTILATERAL_INVESTMENT_FUND__MIF_ = (
        "XI-IATI-MIF",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Multilateral Investment Fund (MIF)",
        ),
    )
    NETHERLANDS_SPACE_OFFICE = (
        "XI-IATI-NSO",
        pgettext_lazy("IATIOrganisationIdentifier", "Netherlands Space Office"),
    )
    UNITED_NATIONS_OFFICE_FOR_THE_COORDINATION_OF_HUMANITARIAN_AFFAIRS_SPECIALLY_DESIGNATED_CONTRIBUTIONS = (
        "XI-IATI-OCHASDC",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "United Nations Office for the Coordination of Humanitarian Affairs - Specially-Designated Contributions",
        ),
    )
    SOMALI_GENDER_JUSTICE = (
        "XI-IATI-SGJ",
        pgettext_lazy("IATIOrganisationIdentifier", "Somali Gender Justice"),
    )
    SOMALI_WOMEN_STUDY_CENTRE = (
        "XI-IATI-SWSC",
        pgettext_lazy("IATIOrganisationIdentifier", "Somali Women Study Centre"),
    )
    UMBRELLA_FOR_COMMUNITY_EDUCATION_IN_SOMALIA = (
        "XI-IATI-UCES",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Umbrella for Community Education in Somalia",
        ),
    )
    UNITED_DARFUR_COMMITTEES = (
        "XI-IATI-UDC",
        pgettext_lazy("IATIOrganisationIdentifier", "United Darfur Committees"),
    )
    UN_POOLED_FUNDS = (
        "XI-IATI-UNPF",
        pgettext_lazy("IATIOrganisationIdentifier", "UN Pooled funds"),
    )
    WARDI_RELIEF_AND_DEVELOPMENT_INITIATIVE = (
        "XI-IATI-WARDI",
        pgettext_lazy(
            "IATIOrganisationIdentifier",
            "Wardi Relief and Development Initiative",
        ),
    )
    WASH_ALLIANCE_INTERNATIONAL = (
        "XI-IATI-WAI",
        pgettext_lazy("IATIOrganisationIdentifier", "WASH Alliance International"),
    )
    WORLD_BANK_TRUST_FUNDS__WBTF_ = (
        "XI-IATI-WBTF",
        pgettext_lazy("IATIOrganisationIdentifier", "World Bank Trust Funds (WBTF)"),
    )
    WORLD_VISION_DRC = (
        "XI-IATI-WVDRC",
        pgettext_lazy("IATIOrganisationIdentifier", "World Vision DRC"),
    )
