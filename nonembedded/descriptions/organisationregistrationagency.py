from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationRegistrationAgencyDescription(models.TextChoices):
    """
    The values from this codelist are used to identify the particular list that an organisation identifier was drawn from. The codelist provides a register of known identifier lists, including national company registers, NGO directories and international and multilateral organisation lists - along with guidance and online resources to help locate the identifiers assigned to a specific organisation. As of 17 July 2017 this list is maintained by the org-id.guide project. Data publishers can now search for and locate the relevant list for a particular organisation identifier using the `org-id.guide website <http://org-id.guide/>`__. The full register of identifier sources is also available to download in `XML <http://org-id.guide/download.xml>`__, `JSON <http://org-id.guide/download.json>`__ and `CSV <http://org-id.guide/download.csv>`__ formats. IATI periodically replicates the codelist of identifier sources from org-id.guide, to assist those accessing IATI documentation. However, it is advised that the most up-to-date source is the `org-id.guide project <http://org-id.guide/>`__. If org-id.guide does not contain an entry for the kind of organisation you need to identify, you can make a request a new list is included in the register following the `guidance <http://docs.org-id.guide/en/latest/contribute/>`__ or by getting in touch with org-id.guide at: contact@org-id.guide.
    """

    AJMAN_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-ACCI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "There are 2 types of search available: Commercial search and Industrial search. You can also use an online enquiry form to find the required information. The contact details of Ajman Chamber and the heads of its sectors are also available.",
        ),
    )
    ABU_DHABI_COMMERCIAL_DIRECTORY = (
        "AE-ADCD",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register includes information on companies' Unified no., Membership no., name, address, phone number, email, activity etc.",
        ),
    )
    AJMAN_FREE_ZONE_AUTHORITY = (
        "AE-AFZ",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The authority's website can be used to find its address, email and call center contacts. No clear search functionality directly on the website.",
        ),
    )
    DUBAI_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-DCCI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register includes information on companies name, address, phone number, website, activity and branches.",
        ),
    )
    DUBAI_FINANCIAL_SERVICES_AUTHORITY = (
        "AE-DFSA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register includes information on companies' name, DFSA reference number, address, phone number, legal status, services.",
        ),
    )
    DUBAI_INTERNATIONAL_FINANCIAL_CENTRE = (
        "AE-DIFC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register includes information on companies' name, registration number, activity, phone number, address, etc.",
        ),
    )
    DUBAI_MULTI_COMMODITIES_CENTRE = (
        "AE-DMCC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Dubai Multi Commodities Centre is a Free Zone Authority established by the government of Dubai in 2002. The DMCC authority registers and licenses companies to operate in the DMCC Free Zone.

N.B There is a 'Business Directory', however, this does not provide registration numbers[1]

[1]: https://www.dmcc.ae/business-search""",
        ),
    )
    FUJAIRAH_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-FCCI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "There is no company information available directly from this registry, but Chamber of Commerce and Industry can be contacted via the form on the website, phone or email to request more information.",
        ),
    )
    FUJAIRAH_FREE_ZONE_COMPANY_LISTING = (
        "AE-FFZ",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "There is no search available in this registry, but there is a list of companies with corresponding phone and fax numbers.",
        ),
    )
    HAMRIYAH_FREE_ZONE_AUTHORITY = (
        "AE-HFZA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "A register that contains company names, addresses, phone numbers, emails, license numbers, activities, etc.",
        ),
    )
    RAS_AL_KHAIMAH_INVESTMENT_AUTHORITY = (
        "AE-RAKIA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Ras al-Khaimah Investment Authority is the registering body for companies in the (RAK) free trade zone.

 There is no open registry but you can request more information via the contact form on the website or a phone call.""",
        ),
    )
    RAS_AL_KHAIMAH_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-RK_CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    SHARJAH_AIRPORT_INTERNATIONAL_FREE_ZONE = (
        "AE-SAIF",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register contains information on company name, business type, phone number, email, PO box.",
        ),
    )
    SHARJAH_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-SCCI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This business directory allows you to search for company names and provides information on their address, email, phone number, activity.",
        ),
    )
    UMM_AL_QUWAIN_CHAMBER_OF_COMMERCE_AND_INDUSTRY = (
        "AE-UQCCI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register includes information about company name, PO box, address, activity, registration date.",
        ),
    )
    AFGHANISTAN_CENTRAL_BUSINESS_REGISTRY = (
        "AF-CBR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Afghan Central Business Registry is a service which allows a single place to register a business in Afghanistan. All companies, groups and individuals are required to register at the ACBR, where they receive confirmation of their registration, become published in the ACBR Gazette and receive the Tax Identification Number.

\"The new Central Registry is a one stop shop to register your business. It brings together all of the functions previously done by the commercial courts, the Ministry of Justice and the Ministry of Finance.\" [1]

\"ACBR exists to provide services to businesses in Afghanistan intending to register their names and protect their intellectual property rights.\" [2]

\"All corporations, partnerships, limited liability companies and sole proprietorships doing Trade are required to register with ACBR, which facilitates the registration process, including assistance for completing the application form, paying fees, publishing key business information in the Official Gazette and reporting specification of businesses to the Revenue Department of MoF. Registration is required only one time unless a business makes major changes (i.e., change in ownership, executive management, or location or if the initial capital increases or decreases).

Businesses are referred to ACBR from either the Trader License office located in the Ministry of Commerce and Industry, from AISA, or from any other license departments after they acquire a business license.\" [3]

[1] http://acbr.gov.af/FAQ.html
[2] http://acbr.gov.af/index.html
[3] http://acbr.gov.af/registration.html""",
        ),
    )
    MINISTRY_OF_ECONOMY_NGO_DEPARTMENT = (
        "AF-MOE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "NGOs wishing to operate in Afghanistan must register with the NGOs Department of the Ministry of Economy. The register contains government departments, national NGOs and international NGOs.",
        ),
    )
    THE_NATIONAL_CENTRE_OF_COMMUNITY_ORGANISATIONS__ARGENTINA_ = (
        "AR-CENOC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Law Nº 25.855, de Voluntariado Social (Social Volunteering) established in 2004 a role for  El Centro Nacional de Organizaciones de la Comunidad to maintain a database of civil society organisations (CSOs).

\"The CSOs that receive or intend to receive public funds must be included in the database, to carry out projects financed in whole or in part with state resources, whatever the subject matter.\"

Registration for the database requests detailed information, including capturing a CUIT number for the organisation (where known), address and contact information. However, only a basic list of identifiers and names is currently published. """,
        ),
    )
    UNIQUE_TAX_IDENTIFICATION_CODE__ARGENTINA_ = (
        "AR-CUIT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Any citizen or company starting an economic activity in Argentina must register with the AFIP (Federal Administration of Public Revenues) and receive a Unique Tax Identification Code (CUIT).

This is an 11 digit number, consisting two digits, hyphen, nine digits, and a one digit checksum.
""",
        ),
    )
    AUSTRIA_COMPANY_REGISTER = (
        "AT-FB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Available only in German. Access can be obtained by using services of special companies like http://www.advokat.at/Advokat-Online/Module/Firmenbuch.aspx that are entitled to provide it (for full list see https://www.justiz.gv.at/web2013/html/default/2c9484852308c2a601240b693e1c0860.de.html)",
        ),
    )
    VAT_NUMBER__AUSTRIA_COMPANY_REGISTER_ = (
        "AT-UID",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"Since July 11, 2005, the records of all commercial register courts are kept electronically. The general ledger is kept by storing the entries in a central database, the so-called \"Firmenbuchdatenbank\" in the Federal Computing Center in Vienna.\"[1]

Clearing houses commissioned by the Federal Ministry of Justice (Die Österreichische Justiz) provide the only access to the database.[2] Interfaces are mostly available only in German, and access/fees vary between the different operators.

Consider using the Business Register number with the prefix AT-FB (see list AT-FB) - which is a primary rather than secondary list - instead of the VAT number.

[1] https://www.justiz.gv.at/web2013/html/default/2c9484852308c2a601240b693e1c0860.de.html
[2] A full list of authorized clearing houses is available at https://www.justiz.gv.at/web2013/home/e-justice/firmenbuch/die_firmenbuchdatenbank~2c9484852308c2a601240b693e1c0860.de.html""",
        ),
    )
    AUSTRALIAN_BUSINESS_REGISTER = (
        "AU-ABN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The Australian Business Number (ABN) enables businesses in Australia to deal with a range of government departments and agencies using a single identification number. The ABN is a public number which does not replace an organisations tax file number.\"

\"ABN registration details become part of the Australian Business Register (ABR)\"

Each ABN should equate to a single 'business structure', although that structure may be used to carry out a range of business activities.  A range of kinds of entity are issued ABNs, including individuals, corporations, partnerships, unincorporated associations, trusts and superannuation funds. Entities must be carrying on a business in or connection to Australia to receive an ABN.""",
        ),
    )
    AUSTRALIAN_CHARITIES_AND_NOT_FOR_PROFITS_COMMISSION = (
        "AU-ACNC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"In Australia, charities must register with the Australian Charities and Not-for-profits Commission (ACNC) before they can receive charity tax concessions from the Australian Taxation Office (ATO).\"

Charity Status can be applied to organisations that have an Australian Business Number (ABN) and that take a range of legal forms [1] including Australian Private Company, Australian Public Company, State level registered 'Other Incorporated Entity', Discretionary Investment Trust, Fixed Trusts, Co-operatives and Other Unincorporated Identities.

[1]: http://www.acnc.gov.au/ACNC/Register_my_charity/Who_can_register/Legal_structure/ACNC/Reg/Legal_structure.aspx""",
        ),
    )
    STATE_REGISTER_OF_COMMERCIAL_ENTITIES__MINISTRY_OF_TAXES_OF_AZERBAIJAN_REPUBLIC_ = (
        "AZ-IVI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Available only in Azerbaijani",
        ),
    )
    BANGLADESH_NGO_AFFAIRS_BUREAU = (
        "BD-NAB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All NGOs wishing to carry out programmes in Bangladesh must gain permission from the Bangladesh NGO Affairs Bureau. The Bureau keeps a list of NGOs, monitors funding and ensures the accountability of NGO projects.

\"Its prime objective is to provide one-stop service to the NGOs operating with foreign assistance and registered under the Foreign Donations (Voluntary Activities) Regulation Ordinance, 1978. In addition, it facilitates the activities of the NGOs in the country, and ensures their accountability to the state and thereby to the people of the country\" [1]

\"Bureau approves the project proposals submitted by NGOs\" [2]

\"NGOs much certify in the project proposal that they receive foreign donation or contribution from legal sources.\" [3]

\"Bureau has the responsibility to make sure that money being channelized by NGOs is from legal sources. Bureau also realizes government revenue-both tax (income tax, VAT etc) and non-tax (registration fee). Bureau always coordinates with NGOs, line ministries, different state agencies and development partners in discharging its duty as the regulatory authority. Here the spirit is to facilitate the NGO activities, not to regulate them\" [4]

[1][2][3][4] http://www.ngoab.gov.bd/site/page/092eab90-ba5f-4cba-933f-d9f28863d170/NGO-Bureau-at-a-glance""",
        ),
    )
    CROSSROADS_BANK_FOR_ENTERPRISES = (
        "BE-BCE_KBO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Crossroads Bank for Enterprises (BCE, ECB, CBE) is the registration office for companies in Belgium. The ECB compiles a list of business identification numbers, maintains the database and provides the list in an available format.

\"The following companies must register with the ECB:

1. legal persons under Belgian law
2. institutions, organizations and Belgian law services which perform tasks of general interest or related to public order and that have a distinct financial and accounting autonomy from that of the legal person under Belgian public law governing them;
3. legal persons of foreign or international law which have a seat in Belgium or who are required to register pursuant to an obligation imposed by Belgian law;
4. to any individual as an autonomous entity:
a) carries on an economic and professional activity in Belgium, as usual, the main or supplementary basis;
b) or must register in fulfillment of an obligation imposed by legislation Belgium other than that covered by this Act;
5. associations without legal personality must be registered pursuant to an obligation imposed by Belgian legislation other than that covered by this Act;
6. the establishment of units of the above mentioned companies.\" [3]

\"The Crossroads Bank for Enterprises (BCE) is a register of the Ministry of Economy which includes all the companies basic identification data and their business units. The ECB's management department is responsible for recording, backup, manage and make available data from the ECB. The ECB is one of the authority for initiatives, application of the principle of single data collection, to simplify administrative procedures for businesses and improve the efficiency of public services.\" [1]

\"It centralises the basic identification data of enterprises and establishment units and communicate them to the various authorities. The ECB gives each company and business unit a unique identification number that allows the authorities to exchange information about them.\" [2]

[1][2] http://economie.fgov.be/fr/entreprises/BCE/#.WC9BdqIrL8o
[3] http://economie.fgov.be/fr/entreprises/BCE/inscription/#.WC9BAqIrL8o""",
        ),
    )
    AU_GREFFE_DU_TRIBUNAL_DE_COMMERCE_FRANCOPHONE_DE_BRUXELLES = (
        "BE-GTCF",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """'The Registry of the Francophone Brussels Commercial Court' does not appear to be an organisation registration agency.

The one identifier we have found in use for this list appears to be derived instead from the BE-BCE_KBO register. """,
        ),
    )
    COMMERCIAL_REGISTER = (
        "BG-EIK",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This register uses Unified identification Codes (UIC) which certify the legality of one's business and under which one's company is signed in the National Statistics Agency.",
        ),
    )
    UNIQUE_TAX_IDENTIFIER = (
        "BJ-IFU",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Benin 'Unique Fiscal Identifier' was created by Decree No 2006-201 of 8 May 2006, and is linked to a national directory of persons, institutions and associations.

\"The IFU's main objective is:

* To uniquely register natural or legal persons throughout the national territory;
* To avoid assigning several identifiers (INSAE number, taxpayer number, declaring code, etc.) to the same person;
* Consolidate and secure information about any identified person;
* To establish a reliable database for information, cross-checking and management purposes;
* Improve and modernize the management of public finances with the introduction of a development tax system;\"[1]

Identifiers are assigned to: \"

* Enterprises engaged in commercial or non-commercial activity in the territory of Benin, regardless of their form, legal status or nationality;
* Employees in the public or private sector;
* Corporate officers;
* Embassies, international organizations and non-governmental organizations;
* Landowners;
* Individuals over eighteen (18) years of age engaged in self-employed or non-commercial activities;
* Central government, public institutions and local authorities;
* Trade unions and political parties, any natural or legal person governed by private law\"[1].

An IFU is 13 characters long. The first digit indicate the type of entity identified:

* 1- Individual / male
* 2- Individual / female
* 3- Legal entity / company
* 4- Legal person / state structure
* 5- Legal person / international organization and mission diplomatic
* 6- Legal person / non-governmental organization

The subsequent 4 digits give the year.

The next six digits are a unique identifier within that year.

The next digit indicates either (1) a parent company; (2-9) subsidiary or agencies; (0) other types of person or taxpayer.

The final digit is a checksum.


[1]: http://www.impots.finances.gouv.bj/tout-savoir-sur-lifu/



EXAMPLE: 3200901353510, """,
        ),
    )
    COMPANIES_AND_INTELLECTUAL_PROPERTY_AUTHORITY__BOTSWANA_ = (
        "BW-CIPA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Companies and Intellectual Property Authority (CIPA) is the official register of businesses in Botwana under the Companies Act (CAP 42:01), which provides for the incorporation of companies and the Registration of Business Names Act (CAP 42:05), which provides for registration of business names and post registration notices such as change of ownership and cessation of businesses.

Both domestic and foreign companies may be registered with the Registrar of Companies.

[1]: http://www.cipa.co.bw/
[2]: http://www.gov.bw/en/Business/Sub-audiences/Small--Medium-Businesses/Company--Business-Name-Registration/""",
        ),
    )
    UNIFIED_STATE_REGISTER_OF_LEGAL_ENTITIES_AND_INDIVIDUAL_ENTREPRENEURS__MINISTRY_OF_JUSTICE_OF_THE_REPUBLIC_OF_BELARUS_ = (
        "BY-ADR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The Unified State Register of Legal Entities and Individual Entrepreneurs (hereinafter referred to as the USR) has been operating since 2003.
In accordance with the Resolution of the Council of Ministers of the Republic of Belarus of February 23, 2009 No. 229 \"On the Unified State Register of Legal Entities and Individual Entrepreneurs\", information on legal entities, state bodies and state legal entities, provisions on which are approved by legislative acts, and also about individual entrepreneurs.\"[1]

\"A legal entity is considered established from the moment of its state registration, unless otherwise established by the President of the Republic of Belarus.\"[2]

[1] http://egr.gov.by/egrn/index.jsp?content=AboutEGR
[2] http://egr.gov.by/egrn/index.jsp?content=eJurReorgCreate
""",
        ),
    )
    CORPORATIONS_CANADA = (
        "CA-CC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Corporations Canada are the federal company register.

CA-CC should be used for the Canada Corporation Number

Companies in Canada register with their provincial authority, e.g. British Columbia. While there is currently no complete national database for companies in Canada, Corporations Canada are piloting a Business Search Registry, which allows for the search of multiple jurisdictions at once, but not all - https://www.ic.gc.ca/app/scr/ccbr/search-chercher?lang=eng

Corporations Canada also provides a Federal Corporation search - https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html?locale=en_CA

This entry was imported from the Open Corporates Jurisdiction List.""",
        ),
    )
    CANADIAN_REVENUE_AGENCY = (
        "CA-CRA_ACR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies in Canada register with their provincial authority, e.g. British Columbia, and then they register with the Canadian Revenue Agency in order to pay corporate income tax and receive a Business Number.

The code CA-CRA_ACR is used for Canadian Business Numbers.

Non-profits and other kinds of legal entities may also have a Canadian Business Number.

The business number is sometimes reported with a Program Account code (e.g. RP0001 to indicate a payroll program account, leading a number such as 123456789RP0001). In constructing an organisation identifier, only the first nine digits should be used.

Companies can be searched by using the Business Number, as assigned by the CRA, on this incomplete registry hosted by the Canadian govt - https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html?locale=en_CA

## More detail:

Not all companies need a Canadian Business Number. Detailed information can be found here - http://www.cra-arc.gc.ca/tx/bsnss/tpcs/bn-ne/wrks-eng.html

Not all charities need to register with the Canadian Revenue Agency. Detailed information can be found here - http://www.cra-arc.gc.ca/chrts-gvng/chrts/pplyng/rgstrtn/mnd-eng.html

Not all non-profit organisations must register to become a charity. Detailed information can be found here - http://www.cra-arc.gc.ca/chrts-gvng/dnrs/rgltn/dffrnc-rc-np-eng.html

\"Your Business Number is a nine-digit account number that identifies your business to federal, provincial, and municipal governments.\"[1]

[1] http://www.canadabusiness.ca/programs/business-number-bn-1/""",
        ),
    )
    LIST_OF_LEGAL_DEPARTMENT_NAMES__GOVERNMENT_OF_CANADA_ = (
        "CA-GOV",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The dataset includes a list of legal department names and their respective numbers. The department number is assigned by the Receiver General to an organization listed in Schedules I, 1.1 and II of the Financial Administration Act authorized to use the Consolidated Revenue Fund and interface with the central systems operated by Public Works and Government Services Canada.\"""",
        ),
    )
    CORPORATE_REGISTRY_OFFICE = (
        "CA_AB-ABT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    BRITISH_COLUMBIA_CORPORATE_REGISTRY = (
        "CA_BC-BRC_CBR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    MANITOBA_COMPANIES_OFFICE__DEPARTMENT_OF_ENTREPRENEURSHIP__TRAINING_AND_TRADE = (
        "CA_MB-MTB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    CORPORATE_REGISTRY = (
        "CA_NB-NWB_NOB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    REGISTRY_OF_COMPANIES__DEPARTMENT_OF_GOVERNMENT_SERVICES = (
        "CA_NL-NFL_TNL",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    NOVA_SCOTIA_REGISTRY_OF_JOINT_STOCK_COMPANIES = (
        "CA_NS-NVS_NVE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    CANADIAN_PROVINCIAL_CORPORATE_REGISTRATION_NORTHWEST_TERRITORIES = (
        "CA_NT-NWT_TNO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    NUNAVUT_DEPARTMENT_OF_JUSTICE_CORPORATE_REGISTRIES = (
        "CA_NU-NNV",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    SERVICEONTARIO__MINISTRY_OF_GOVERNMENT_SERVICES = (
        "CA_ON-ONT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    PRINCE_EDWARD_ISLAND_CORPORATE = (
        "CA_PE-PEI_IPE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    QUEBEC_BUSINESS_REGISTRAR = (
        "CA_QC-QBC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    SASKATCHEWAN_CORPORATE_REGISTRY = (
        "CA_SK-SKN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    YUKON_CORPORATE_AFFAIRS = (
        "CA_YT-YKT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This entry was imported from the Open Corporates Jurisdiction List.",
        ),
    )
    COMMERCIAL_REGISTRY__FEDERAL_OFFICE_OF_JUSTICE__SWITZERLAND_ = (
        "CH-FDJP",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Swiss Commercial Register is administered by the cantons under the supervision of the Swiss Confederation. All the commercial register entries made by the cantonal register offices are published in the Swiss Official Gazette of Commerce (SOGC) after having been checked and approved by the Federal Commercial Registry Office.

Since January 2011, all companies, foreign branches and associations / foundations registered in the various Swiss Commerce Registries are assigned a unique federal Company Identification Number, locally known as IDE (French), UID (German), IDI (Italian).

Previously, identifiers were of the format CH-RRR.X.XXX.XXX-P, where RRR is the canton number, X.XXX.XXX is the company number, and P is a check-digit. Some older or inactive companies may still have identifiers of this form.

[1]: https://opencorporates.com/registers/250
""",
        ),
    )
    STATE_ADMINISTRATION_FOR_INDUSTRY_AND_COMMERCE__SAIC_ = (
        "CN-SAIC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The SAIC is the national body which ensures business rights in China, for both domestic and foreign enterprises. Businesses must register with the SAIC. The Enterprise Registration Bureau is the department responsible for enterprise registration.

For further details on the procedure for starting a business entity, see this WikiProcedure - https://www.wikiprocedure.com/index.php/China_-_Start_a_Business_Entity

The database is only available in Chinese language

\"The State Administration for Industry & Commerce (SAIC) of the People’s Republic of China is the competent authority of ministerial level directly under the State Council in charge of market supervision/regulation and related law enforcement through administrative means.

With creating a regulated and harmonized market environment of fairness, justice and faithfulness for the coordinated socioeconomic development as its objective, SAIC functions in maintaining market order and protecting the legitimate rights and interests of businesses and consumers by carrying out regulations in the fields of enterprise registration, competition, consumer protection, trademark protection and combating economic illegalities.\" [1]

\"Our responsibilities:
2.     Carry out and administer registration of enterprises (including foreign-invested enterprises), agricultural cooperatives, entities or individuals engaged in business operation and resident representative offices of foreign companies; and take charge of the investigation and ban on unlicensed business operation according to law.\" [2]

\"Enterprise Registration Bureau
-        Draft measures and practice directions regarding enterprise registration;
-        Coordinate and guide enterprise registration nationwide;
-        Take charge of registration of certain enterprises and supervises the registrants’ registration practices;
-        Organize and guide credit rating of businesses;
-        Establish and maintain the national database of enterprise registration information, and analyze and publish registration information of domestic enterprises.\" [3]

[1][2] http://www.saic.gov.cn/english/aboutus/Mission/index.html
[3] http://www.saic.gov.cn/english/aboutus/Departments/""",
        ),
    )
    BOGOTA_CHAMBER_OF_COMMERCE = (
        "CO-CCB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Each region of Colombia has a Chamber of Commerce to which all corporate entities must register. Bogota Chamber of Commerce (CCB) is responsible for Bogota.

Users should refer to CO-RUE for unique identifiers for Colombia. CO-CCB has ben deprecated in favour of CO-RUE.

\"We are a private, non-for-profit organization whose goal is to foster a sustainable Bogota-Region in the long term, by promoting its residents' prosperity, through services which enhance and strengthen the enterprise capabilities present in the region, and which improve the business environment with an impact over public policies.\" [1]

[1] http://www.ccb.org.co/en/Clusters/20th-TCI-Global-Conference-Bogota-Colombia/Bogota-Chamber-of-Commerce""",
        ),
    )
    UNIFIED_COMMERCIAL_AND_SOCIAL_REGISTRY__RUES_ = (
        "CO-RUE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Unified Commercial and Social Registry (RUES) integrates multiple commercial registries, including the NIT (Número de Identificación Tributaria) which can be used as the unique identifier.

This database can be searched online for free.

\"The CCB hereby informs that, in accordance with Resolution 71029 issued by the Superintendence of Industry and Commerce, starting as of November 13, 2013, entrepreneurs must fill out the new Unified Commercial and Social Registry (RUES), a form that integrates the information from the following forms and records:

* Merchant's Certificate.
* Unified Offeror Registry.
* Non-For-Profit Organizations Registry.
* Common Regime (Associations, Foundations and Corporations) and * Solidary Economy Institutions (Cooperatives, Precooperatives, Employee Funds and Mutual Associations).
* Activity, games and gambling Registry.
* Citizen Oversight Associations Registry (applicable only when registering or signing-up).
* Solidarity Economy Registry.\" [1]

[1] http://www.ccb.org.co/en/Registrations-and-renewals/Merchant-s-certificate/Unified-Commercial-and-Social-Registry-RUES""",
        ),
    )
    CYPRUS_DEPARTMENT_OF_REGISTRAR_OF_COMPANIES_AND_OFFICIAL_RECEIVER__DRCOR_ = (
        "CY-DRCOR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Department of Registrar of Companies and Official Receiver maintains the register of companies, partnerships, business names, and overseas companies.",
        ),
    )
    TAX_ID__DIČ__CZECH_REPUBLIC = (
        "CZ-DIC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """A VAT registration number (DIČ) is a unique and unambiguous identification of each tax entity, a legal or natural person who is a taxpayer (taxpayer). The tax identification number is assigned only after the entity, natural or legal person, obtains its IČO - its unique identification number. Note that the list [CZ-ICO](/list/CZ-ICO) might therefore provide a better set of identifiers for legal entities.

You can search by VAT (DIČ) number for a of the VAT payer registered in the Czech Republic. You can also use your company ID or company name or your business name and surname if you want to verify your VAT payer details.""",
        ),
    )
    ACCESS_TO_REGISTERS_OF_ECONOMIC_SUBJECTS = (
        "CZ-ICO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The ARES is an information system which collates data from several public registers in the Czech Republic. These include:

Public registers comprising: the Commercial Register Federal Register, the Register of Foundations Register’s Institute, Register of Public Service Companies, Trade Register, and the Register of Economic Entities.

Enterprises do not register with the ARES. They must be register with the relevant registration authority.

\"The purpose of the ARES web sites of the Ministry of Finance is to provide a single-point access to all data concerning economic entities kept in particular registers or maintained in files of the state administration. ARES provides an easy access to the data transferred from the source registers to the ARES database. It allows also to switch directly to www applications of the state administration bodies provided that such applications already exist.\" [1]

\"It is not possible to make a registration in the Information System ARES directly. It is necessary to proceed in accordance with applicable laws and to make a registration at the registration points of the public administration authorities. Likewise, data changes or termination of the registration must be reported to the institution that maintains the source registry. List of source registers and responsible institutions is presented in the tab REGISTRATION AUTHORITIES.\" [2]

 Information on companies is searchable in English and is free-of-charge.

[1] http://wwwinfo.mfcr.cz/ares/ares_es.html.en
[2] http://wwwinfo.mfcr.cz/ares/ares.html.en""",
        ),
    )
    COMMON_REGISTER_PORTAL_OF_THE_GERMAN_FEDERAL_STATES__CRP_ = (
        "DE-CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Common register portal of the German federal states provides  the registers of companies, cooperatives and partnerships and, to some extent, also of associations registered in all federal states in Germany as well as announcements for the register (publications).",
        ),
    )
    DANISH_CENTRAL_BUSINESS_REGISTER = (
        "DK-CVR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The CBR is the national body for registering companies and maintaining this information in Denmark. The Central Business Register at Virk is available with English headings and categories. It can be used to search for information on all Danish businesses.

\"The Danish Central Business Register (aka CVR — Det Centrale Virksomhedsregister) is the central government register containing primary data on all businesses in Denmark, regardless of economic and organizational structure, except personally owned companies with an annual turnover of less than 50,000 Danish krones.\" [1]

[1] https://en.wikipedia.org/wiki/Central_Business_Register_(Denmark)""",
        ),
    )
    E_BUSINESS_REGISTER__ESTONIA_ = (
        "EE-KMKR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"Central Commercial Register is an online service based on the central database of Estonian registration department of the court. The central database includes digital data from the commercial register, the commercial pledge register, the register of state agencies and local government institutions, the register of non-profit associations and foundations. \"[1]

Records contain information about the legal entity including e.g. annual reports, address, registration status, tax debt information and legal form. It also includes a Registry Code (\"Registrikood\").

[1] http://www.rik.ee/en/e-business-register""",
        ),
    )
    CENTRE_OF_REGISTERS_AND_INFORMATION_SYSTEMS__RIK_ = (
        "EE-RIK",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Centre of Registers and Information Systems (RIK) provides a number of services for Estonian individuals and business, in particular electronic services. These include the maintenance of the land registry database, criminal records database, company registry database and more. They also have a portal for the online registration of companies.

\"COMPANY REGISTRATION PORTAL

This environment allows companies to submit electronic documents to the Business Register without using the services of a notary. The portal allows submitting applications for registering a new company, for amending the registry data, for liquidating and for deleting a company from the registry.

You can view the data related to you free-of-charge by logging in with your ID-card.\" [1]

[1] http://www.rik.ee/en""",
        ),
    )
    MINISTRY_OF_SOCIAL_SOLIDARITY_AND_JUSTICE__EGYPT_ = (
        "EG-MOSS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Ministry of Social Solidarity and Justice is the main registration body for associations and foundations in Egypt.",
        ),
    )
    COMMON_DIRECTORY_OF_ORGANIZATIONAL_UNITS_AND_OFFICES_DIR3 = (
        "ES-DIR3",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Common Directory of Organizational Units and Offices (DIR3) is a project to improve interoperability between public administration units in Spain. As a part of this, a list of all the public bodies is maintained by the Centro de Transferencia de Tecnología (Technology Transfer Centre).

\"The Common Directory is conceived as a Inventory information on the organizational structure of the public administration, and its citizens care offices. That is, a catalogue of functional units, public agencies and registry offices and attention to the citizen of the administration\" [1]

[1] http://administracionelectronica.gob.es/pae_Home/pae_Estrategias/Racionaliza_y_Comparte/sistemas_informacion_transversales/DIR3.html?idioma=en#.WDTAPaIrL8o

EXCEL Tables: http://administracionelectronica.gob.es/ctt/resources/Soluciones/238/Area%20descargas/Listado%20Oficinas%20AGE.xlsx?idIniciativa=238&idElemento=2745""",
        ),
    )
    CENTRAL_COMMERCIAL_REGISTER_OF_THE_KINGDOM_OF_SPAIN = (
        "ES-RMC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Central Mercantile Register (1) provides the access to the companies information supplied by the Regional Mercantile Registers after the 1 January 1990, once the data has been organized and processed in accordance with Section 379 of the Mercantile Register Regulations currently in effect.

(1) Central Commercial Register - Central Corporate Register - Central Business Register""",
        ),
    )
    CHARITIES_AND_SOCIETIES_AGENCY__ETHIOPIA_ = (
        "ET-CSA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Most Charities and Societies which operate in Ethiopia are required to register with the Charities and Societies Agency, an institution of the Federal Government, which issues certificates of legal personality to those registered.",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "ET-MFA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All charities wishing to operate in Ethiopia must register with the Ministry of Foreign Affairs (MFA). Details for how they register can be found in this document - http://mfa.gov.et/documents/10184/70245/NGO_Rule_English%5B1%5D%281%29.pdf/d20c730a-591e-4d3a-b9d8-a25aeb664904

Charities are registered but no openly searchable database yet available.""",
        ),
    )
    MINISTRY_OF_TRADE__ETHIOPIA_ = (
        "ET-MOT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Ministry of Trade is the official ministry for business registration in Ethiopia.

\"The Ministry of Trade was re-established in August1995 under -- proclamation No 4/1995 issued to provide for the definition of powers and duties of the executive organs of the Federal Democratic Republic ofEthiopia (FDRE).

The Ministry was again reorganized with a proclamation No 619/2003 issued to amend the reorganization of the executive organs of the Federal Democratic Republic Ethiopia Proclamation No 256/2001. With this proclamation and by other laws, the Ministry has been given the power to supervise and coordinate five government institutions that are involved in the promotion & development of trade, industry and investment activities.

The Ministry of Trade shall have the powers and duties to:

Encourage and register the establishment of chambers of commerce and sectorial associations including consumers associations and strengthen those already established(Chambers of Commerce and Sectorial Association Establishment Proclamation No.341/2003).\" [1]

[1]: http://www.mot.gov.et/documents/27281/0/Proc+No.+341-2003+Chamber+of+commerce+and+sectorial+Associa.pdf/50798768-2b9d-4f20-990f-1d4298f16f08?version=1.1""",
        ),
    )
    FINNISH_PATENT_AND_REGISTRATION_OFFICE = (
        "FI-PRO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All business operating in Finland must be registered with the Finnish Trade Register. The Finnish Trade Register is maintained by the Finnish Patent and Registration Office (PRO), whom are also responsible for maintaining the Business Information System, which can be used to search for all companies in Finland, and the API which allows users to download company information in bulk.

\"The Finnish Trade Register (Finnish: Kaupparekisteri, Swedish: Handelsregistret) is a company register in Finland. It provides official information on businesses in the whole country, including data from current and old register entries, articles of association, partnership agreements or rules.\" [1]

\"The Finnish Trade Register is a public register that contains information about businesses and companies. As a rule, all businesses have to be registered at the Trade Register. Businesses also have to notify the register of any changes in their registered details. Most businesses must also submit their financial statements (annual accounts) to the register. \" [2]

\"The Business Information System BIS (\"YTJ\" in Finnish) is a service jointly maintained by the Finnish Patent and Registration Office (PRH) and the Finnish Tax Administration, enabling you to file information to both authorities using one single notification.

You can use the BIS to:

start a business or an organization
report changes
close down a business or an organization
search for basic details of companies and organizations using the company search\" [3]

[1] https://en.wikipedia.org/wiki/Finnish_Trade_Register
[2] https://www.prh.fi/en/kaupparekisteri/rekisterointipalvelut.html
[3] https://www.ytj.fi/en/index/whatisbis.html""",
        ),
    )
    THE_NATIONAL_INSTITUTE_OF_STATISTICS_AND_ECONOMIC_STUDIES = (
        "FR-INSEE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The National Institute of Statistics and Economic Studies provide a registration service for companies and associations with details being held on the SIRENE database.

Information from INSEE is also contained in the RCS dataset, and so this organisation list is deprecated in favour of FR-RCS. """,
        ),
    )
    TRADE_AND_COMPANIES_REGISTER = (
        "FR-RCS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """In France, companies register through a number of institutions, predominantly the local centres de formalités des entreprises, but all companies must eventually be registered with the Trade and Companies Register. Once registered, companies receive a SIREN or SIRET number, which is a unique business identifier.

This information is maintained by Infogreffe. Infogreffe provide a basic overview of company information for free, and bulk download of data for a fee.

A note on identifiers:

- A SIRET number is constituted by the SIREN number, plus the NIC code.

- The SIREN number relates to a business, whereas a SIRET number relates to a specific geographically located establishment which will be owned by a business.

- \"A SIREN number is your unique French business identification number. This 9 digit number will be requested by all French administration when dealing with you.. It is a proof that you are a fully registered French business\" [1]

\"The SIRET code/number is an INSEE code which allows the geographic identification of any French establishment or business.

The 14-digit number consists of three parts:

- first, the SIREN code of the business (or legal unit or person) that owns the unit represented by the SIRET code,
- second, the NIC (French: Numéro interne de classement), is a sequential four-digit number unique to the establishment,
- and finally, a check digit that verifies the entire SIRET number.

For example, 732 829 320 00074 would refer to the seventh establishment of the business with SIREN number 732 829 320.\" [2]

\"Registration is administered by local centres de formalités des entreprises ( CFE), which checks your application and submits details to the relevant agencies (for a small fee). The CFE will provide you with a form M0, which is for the creation of a company.\" [3]

\"Creating a company requires that it is registered with the Trade and Companies Register (RCS).\" [4]

\"WHAT SOURCE IS USED FOR INFORMATION AVAILABLE ON THE INFOGREFFE WEBSITE?

Information concerning companies entered on the Trade and Companies Register with Registries of the Commercial Courts is taken directly from public registers held by said registries.

Information concerning companies entered on the Trade and Companies Register with other jurisdictions (district courts with commercial jurisdiction, mixed commercial courts in the overseas departments and territories) is provided by the National Industrial Property Institute (INPI).

Information concerning companies not entered on the Trade and Companies Register is taken from data on the SIRENE listing held by INSEE.\" [5]

\"WHAT DOCUMENTS ARE AVAILABLE ON THE INFOGREFFE WEBSITE?
Infogreffe makes the following information available to the general public:

Free information
•    Company search and information form
•    Key figures concerning a company
•    Implementing tracking (free alert, paid consultation).
•    Lists of articles of association and company deeds available.
•    Your formalities with online help to be incorporated on the Trade and Companies Register.

Paid information
View, download, order\" [6]

[1] http://www.startbusinessinfrance.com/blog/post/tip-what-is-a-siren-or-siret-number
[2] https://en.wikipedia.org/wiki/SIRET_code
[3] https://www.justlanded.com/english/France/France-Guide/Business/Paperwork
[4][5] https://www.infogreffe.com/societes/formalites-entreprise/immatriculation-entreprise.html
[6] https://www.infogreffe.com/societes/informations-et-dossiers-entreprises/aide-faq.html#1""",
        ),
    )
    CHARITY_COMMISSION = (
        "GB-CHC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """There are four main types of charity structure in the UK:

(1) Charitable incorporated organisation (CIO)
(2) charitable company (limited by guarantee)
(3) unincorporated association
(4) trust


""",
        ),
    )
    COMPANIES_HOUSE = (
        "GB-COH",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies House is the United Kingdom's register of companies.

It contains entries for many kinds of companies, including:

* Public limited company (PLC)
* Private company limited by shares (Ltd, Limited)
* Private company limited by guarantee, typically a non-commercial membership body such as a charity
* Private unlimited company (either with or without a share capital)
* Limited liability partnership (LLP)
* Limited partnership (LP)
* Societas Europaea (SE): European Union-wide company structure
* Companies incorporated by Royal Charter (RC)
* Community interest company""",
        ),
    )
    REGISTER_OF_SCHOOLS__ENGLAND_AND_WALES_ = (
        "GB-EDU",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Schools and Colleges in England must be registered with the Department of Education, and in Wales with the Welsh Government.[1]

The Register of Schools is maintained by the Department of Education and provides a URN for each school, university and other educational establishment in England and Wales.

The full Register of Schools in England is available (Alpha version) on https://registers.cloudapps.digital/registers?phase=in+progress. **The register for Welsh Schools is not yet launched and so all schools in Wales may not yet be present on this list.**

[1] This includes independent schools which meet the criteria on https://www.gov.uk/independent-school-registration""",
        ),
    )
    GOVERNMENT_ORGANISATION_REGISTER = (
        "GB-GOR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The UK Government Organisation Register contains an identifier for every government body with a presence on the gov.uk single domain.

This covers government departments, agencies and Arms Length Bodies (ALBs).

Each organisation is assigned an alphanumeric identifier, and the register also includes website addresses, that can be mapped to entries in the GB-GOVUK identifier list.

Due to the stable identifiers given in the Government Organisation Register, it should be preferred over codes from the GB-GOVUK list. """,
        ),
    )
    UK_GOVERNMENT_DEPARTMENTS_REFERENCE_NUMBERS__IATI_STANDARD_ = (
        "GB-GOV",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """IATI Version 2.x codes for use by IATI for UK Government Departments.

Users looking for non-IATI codes for government organsiations should use the UK Government Organsiation Register GB-GOR""",
        ),
    )
    GOV_UK_UK_GOVERNMENT_DEPARTMENTS__AGENCIES___PUBLIC_BODIES = (
        "GB-GOVUK",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """This list is deprecated in favour of GB-GOR, the Government Organisation Registry which assigns a unique code to each agency with a page at www.gov.uk.

To construct a legacy GB-GOVUK identifier, use the final segment of the url of a body at http://www.gov.uk (below /organisations) as the \"registration number\", converting all \"-\" to \"_\". Keep \"registration number\" portion all lowercase.

It should be possible to map form GB-GOVUK to GB-GOR identifiers. """,
        ),
    )
    SCHOOLS_PLUS__DEPARTMENT_OF_EDUCATION__NORTHERN_IRELAND_ = (
        "GB-IRN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Schools Plus is a directory of institutions, including schools, youth clubs, containing contact information and relevant statistics. Only Open schools seem to be on the list currently.",
        ),
    )
    LOCAL_AUTHORITIES_FOR_ENGLAND_REGISTER = (
        "GB-LAE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Local Authorities for England Register has been developed with the UK Department for Communities and Local Government (DCLG), and contains identifiers for 350+ local authorities. It also includes the 'local authority type' (e.g. Unitary Authority, London Borough) for each.

It uses the second portion of [ISO_3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:GB) codes where these are available, and creates new codes where they are not. For more information on GOV.UK Registers, visit https://registers.cloudapps.digital/""",
        ),
    )
    SCOTTISH_LOCAL_AUTHORITY_REGISTER = (
        "GB-LAS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Local Authority SCT Register has been developed with the Scottish Government and Government Digital Service (GDS), and contains identifiers for 32 local authorities.

It uses the second portion of [ISO_3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:GB) codes and includes all codes listed for Scotland (SCT). """,
        ),
    )
    MUTUALS_PUBLIC_REGISTER = (
        "GB-MPR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Mutuals Public Register is the public record of registered mutual societies:

* building societies
* credit unions
* friendly societies
* registered societies

It contains:

* details of societies’ registered offices and contact information
the services they offer
* public documents such as yearly returns and accounts""",
        ),
    )
    NHS_DIGITAL_ORGANISATION_DATA_SERVICE = (
        "GB-NHS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The Organisation Data Service (ODS) is responsible for publishing organisation and practitioner codes, along with related national policies and standards. We're also responsible for the ongoing maintenance of the organisation and person nodes of the Spine Directory Service, the central data repository used within various NHS systems and services.

Find out more about Organisation Reference data by reading the fundamental standard.\"[1][2]

Codes are allocated for:[3]

* Independent Sector Healthcare Providers (ISHP)
* NHS organisations
* Non-NHS organisations
* optical organisations
* private dental practices
* system suppliers

[1]: https://digital.nhs.uk/organisation-data-service
[2]: Information standard SCCI0090 (Health and Social Care Organisation Reference Data): http://content.digital.nhs.uk/isce/publication/scci0090
[3]: List from https://digital.nhs.uk/organisation-data-service/our-services#code allocation""",
        ),
    )
    THE_CHARITY_COMMISSION_FOR_NORTHERN_IRELAND = (
        "GB-NIC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Register of Charities is an accurate and up-to-date list of all organisations in Northern Ireland considered by law to be charitable. Currently, registration is a managed process and only organisations called forward by the Commission are considered eligible to register. For more information on the Register please visit http://www.charitycommissionni.org.uk/manage-your-charity/register-your-charity/charity-registration-faqs/.",
        ),
    )
    PRINCIPAL_LOCAL_AUTHORITY_REGISTER_FOR_WALES = (
        "GB-PLA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Principal Local Authority Register has been developed with the Welsh Government and Government Digital Service (GDS), and contains identifiers for 22 county and county borough councils. The register may not cover all local authorities as it focuses on bodies providing mainstream local government services.

It uses the second portion of [ISO_3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:GB) codes and includes all codes listed for Wales (WLS). """,
        ),
    )
    HM_REVENUE_AND_CUSTOMS = (
        "GB-REV",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Some UK charitable organisations are exempt or excepted from registering with the Charity Commission. This may be due to the nature of the organisation, it's historical status, or income threshold.

However, these organisations can register for tax purposes with HM Revenue and Customs, and receive a registration number.

This may be reported prefixed with XC (for eXempt Charity).""",
        ),
    )
    SCOTTISH_CHARITY_REGISTER = (
        "GB-SC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Office of the Scottish Charity Register (OSCR) regulates charities in Scotland and maintains a public registry of these charities.

\"The OSCR perform a range of functions which includes:[5]

Determining whether bodies are charities.
Keeping a public Register of charities.
Facilitating compliance by charities with the legislation.
Investigating any apparent misconduct in the administration of charities.
Giving information or advice to Scottish Ministers.\" [1]

[1] https://en.wikipedia.org/wiki/Office_of_the_Scottish_Charity_Regulator""",
        ),
    )
    REGISTERED_SOCIAL_HOUSING_PROVIDERS__ENGLAND_ = (
        "GB-SHPE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """A statutory register of not-for-profit (housing associations), for-profit private, and local authority social housing providers, who are registered to operate in England. The Homes and Communities Agency (HCA)[1] is the regulator for social housing providers in England and maintains the list.

Fields indicate the designation of the social housing provider (e.g. private, non-profit, local authority) and the legal entity type (by their inclusion on the FCA Mutual Register, the Charity Register and Companies House).

A *monthly* published list also appears on the HCA website, which includes new registrations and deregistrations https://www.gov.uk/government/publications/current-registered-providers-of-social-housing

[1]: https://www.gov.uk/government/organisations/homes-and-communities-agency""",
        ),
    )
    UK_REGISTER_OF_LEARNING_PROVIDERS = (
        "GB-UKPRN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "A UKPRN is a unique number allocated to a provider on successful registration on the UK Register of Learning Providers. ",
        ),
    )
    REGISTER_OF_ENTREPRENEURIAL_AND_NON_ENTREPRENEURIAL_LEGAL_ENTITIES__GEORGIA = (
        "GE-NAPR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The National Agency of Public Registry (NAPR) of Georgia registers all legal entities in Georgia. This includes government and non-government bodies (including the private sector). The Identification Code assigned by NAPR is the same as the VAT number in Georgia. NAPR assigns codes for government bodies in addition to all non-governmental organisations (private and non-profit).",
        ),
    )
    GUERNSEY_REGISTRY = (
        "GG-RCE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All companies in Guernsey must register with the Guernsey Registry. This also applies to most charities and NPOs. The Guernsey Registry maintain a registry of all companies, charities and all NPOs in Guernsey. These are recorded in a publicly searchable webpage database for companies and also two separate lists for charities and NPOs.

Please Note: According to OpenCorporates, the identifiers are not unique across the Guernsey Registry, as there a five separate registries that can be assigned to organisation information and up to five companies my have the same identifier. OC have thus added their own identifier number based on each registry type. Further details available here - qa_public/register_problems/guernsey

\"All Guernsey companies must file an Annual Validation submission with the Registry during January 2017 (unless incorporated in December 2016). Submissions received after 31 January 2017 will be subject to a £100 late filing fee.\" [1]

\"The Charities and Non Profit Organisation (Registration) (Guernsey) Law, 2008 requires all Non Profit organisations based in the Islands of Guernsey, Alderney, Herm and Jethou to register with the Office of the Registrar. A failure to do so is an offence.

However there is an exemption from this requirement. This applies to Non Profit organisations based in the Islands of Guernsey, Alderney, Herm and Jethou with gross assets and funds of less than £10,000, or gross annual income of less than £5,000.\" [2]

[1] http://www.guernseyregistry.com/
[2] http://www.guernseyregistry.com/article/112911/Do-I-need-to-register-a-Charity-or-Non-Profit-organisation-""",
        ),
    )
    DEPARTMENT_OF_SOCIAL_DEVELOPMENTS = (
        "GH-DSW",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All NGOs wishing to operate in Ghana must first register with the General Registrar's Office, and then apply for NGO status from the Department of Social Welfare (DSW). NGOs are then issued with a certificate that contains their registration number.

There is no database available for search.

\"The Social Welfare Department is the regulator of NGOs in Ghana and is therefore mandated to issue certificates of recognition to organizations to operate as NGOs. \" [1]

[1] http://g-lishfoundation.org/wp-content/uploads/2011/02/HOW-TO-START-AN-NGO-IN-GHANA.pdf""",
        ),
    )
    HONG_KONG_COMPANIES_REGISTER = (
        "HK-CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All businesses operating in Hong Kong, including non-Hong Kong businesses with a place of business in Hong Kong must register with the Companies Register.

This includes Sole-proprietorship, Partnership and Unincorporated body of persons, Non-Hong Kong company, and Branch business, as well as companies incorporated under the Companies Ordinance.

Businesses are issued with a registration certificate that is valid for three years, and which can be renewed. """,
        ),
    )
    CROATIAN_COURT_BUSINESS_REGISTER = (
        "HR-MBS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The court business register is maintained by the Croatian Ministry of Justice (Ministarstvo Pravosuda Republike Hrvatske).

Registered corporations each have a court-assigned company registration number (matični broj poslovnog subjekta - MBS)""",
        ),
    )
    CROATIA_COURT_REGISTER = (
        "HR-OIB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Maintained by the Ministry of Justice of the Republic of Croatia.",
        ),
    )
    INFORMATION_AND_ELECTRONIC_COMPANY_REGISTRATION_SERVICE = (
        "HU-AFA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Ministry of Justice Information and Electronic Company Registration Service website provides free accesss to individual company data online from 1 January 2008. Only available in Hungarian.",
        ),
    )
    MINISTRY_OF_HOME_AFFAIRS = (
        "ID-KDN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Ministry of Home Affairs conducts a series of tasks in relation to legal practice and administration within Indonesia. However, no link has been found between the Ministry of Home Affairs and NGO/company registration.

As a result, this code has been deprecated.

Users can refer to ID-KLN (Ministry of Foreign Affairs) and ID-PRO for the registration of NGOs.

Users can refer to ID-SMR (SMERU) for an independent body that maintains a database of NGOs.

\"The Ministry of Home Affairs has the task of conducting government affairs in the country to assist the President in running the state government.

The Ministry of Interior has the functions:

1. formulation, determination and implementation of policies in the field of politics and public governance, decentralization, development of the regional administration, coaching village government, formation of government affairs and regional development, development of local finance, as well as the population and civil registration, in accordance with the provisions of the legislation;
2. coordinating the implementation of tasks, coaching, and providing administrative support to all elements of the organization within the Ministry of the Interior;
3. management of property / wealth of the country is the responsibility of the Ministry of the Interior;
4. supervise the execution of duties in the Ministry of the Interior;
5. implementation of the technical guidance and supervision over the implementation of the affairs of the Interior Ministry in the area;
6. coordinating, coaching and general supervision, facilitation, and evaluation of the regional administration in accordance with the provisions of the legislation;
7. implementation of research and development in the field of governance in the country;
8. implementation of human resource development in the field of governance in the country;
9. implementation of the technical activities of the center to the regions; and
10. the implementation of a substantial support to all elements of the organization within the Ministry of Interior.\" [1]

[1] http://www.kemendagri.go.id/profil/tugas-dan-fungsi

NGO registration can also be done through Ministry Home affairs/ Kementerian Dalam Negeri""",
        ),
    )
    MINISTRY_OF_JUSTICE___HUMAN_RIGHTS = (
        "ID-KHH",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Company registration is done through Ministry of Justice & Human Rights. ",
        ),
    )
    MINISTRY_OF_FOREIGN_AFFAIRS = (
        "ID-KLN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All NGOs foreign to Indonesia who wish to operate in the country must register through the Ministry of Foreign affairs/ Kementerian Luar Negeri.

\"Registration Process:

1.    INGO submit complete application documents to the Government of the Republic of Indonesia through the Ministry of Foreign Affairs\" [1]

[1] http://www.kemlu.go.id/en/berita/informasi-penting/Pages/Registration-Guidelines-for-International-Non-Governmental-Organizations-in-Indonesia.aspx""",
        ),
    )
    INDONESIA_NGOS_REGISTERED_AT_PROVINICIAL_LEVEL = (
        "ID-PRO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Registration for NGO in Indonesia can be done at the provincial level. Because there is regional autonomy, each provincial has different requirements.

This list was in the original IATI list, but current research has not been able to identify any publicly accessible registries nor lists of unique identifiers. A search of the IATI database finds no instances of use of ID-PRO as part of an identifier. For these reasons the list has been deprecated.""",
        ),
    )
    THE_SMERU_RESEARCH_INSTITUTE = (
        "ID-SMR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The SMERU Research Institute is an independent body which conducts research on social issues in Indonesia. They also maintains a database of NGOs working in Indonesia.

\"The SMERU Research Institute is an independent institution for research and public policy studies. We professionally and proactively provide accurate and timely information, as well as objective analyses, on various socioeconomic and poverty issues considered most urgent and relevant for the people of Indonesia.\" [1]

\"SMERU manages Indonesia's most comprehensive online database of national and regional non-governmental organizations (NGOs). Currently, there are almost 3,000 NGOs in the database, which provides information on the NGOs’ name, address, contact person, vision, mission, legal form, activities, and sector.\" [2]

[1] http://www.smeru.or.id/en/about
[2] http://www.smeru.or.id/en/content/ngo-database""",
        ),
    )
    CHARITIES_REGULATORY_AUTHORITY_OF_IRELAND = (
        "IE-CHY",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All charities operating in Ireland must register with the Charities Regulatory Authority. The Charities Regulator maintains a publicly searchable database of these organisations, in webpage and Excel form.

\"Our work as a Regulator is to increase public trust and confidence in the management and administration of charitable organisations and to ensure the accountability of charitable organisations to donors, beneficiaries and the public.  All charitable organisations carrying out activities in the state are required to be registered with the Charities Regulator.  All registered charities are required to report on their activities and finances to the Regulator on an annual basis. \" [1]

[1] https://www.charitiesregulatoryauthority.ie/en/CRA/Pages/WP16000071""",
        ),
    )
    IRISH_COMPANIESREGISTRATION_OFFICE = (
        "IE-CRO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Companies Registration Office of Ireland is responsible for the incorporation of business operating in Ireland and maintaining an online database of the information. Data is provided for free and also for a fee, depending on the amount/type requested.

\"The CRO has a number of core functions:

* The incorporation of companies and the registration of business names.
* The receipt and registration of post incorporation documents.
* The enforcement of the Companies Act 2014  in relation to the filing obligations of companies.
* Making information available to the public.\" [1]

[1] https://www.cro.ie/About-CRO/Functions-of-the-CRO""",
        ),
    )
    REGISTRAR_OF_COMPANIES__ISRAEL_ = (
        "IL-ROC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Register of Companies is maintained by the Israeli Corporations Authority and can be searched using part or all of a company name in English or Hebrew, or by entering the company number. The search interface and the results are in Hebrew.

Free information on a company includes type of company, address, legal status and purpose of the company.

Additional information such as details of directors, total authorized capital, division of share capital, shareholders, charges and liabilities is priced.""",
        ),
    )
    ISLE_OF_MAN_COMPANIES_REGISTRY = (
        "IM-CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Isle of Man Companies Registry provides registration for domestic and foreign companies registered or operating on the Isle of Man. ",
        ),
    )
    ISLE_OF_MAN_INDEX_OF_REGISTERED_CHARITIES = (
        "IM-GR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All charities in the Isle of Man must be registered with the General Registry. The General Registry maintain information about charities in the Index of Registered Isle of Man Charities

\"The General Registry has specific statutory roles in relation to the registration of charities and the receipt of statutory statements, accounts and other documents in relation to charities.\" [1]

\"The General Registry is the department which administers –

the civil and criminal Courts of the Isle of Man
the High Court of Justice of the Isle of Man
Courts of General Gaol Delivery
courts of summary jurisdiction
the Registries
Deeds and Probate Registry
Land Registry
Civil Registry, responsible for registration of births, deaths and marriages
registration of charities
Legal Aid
the Public Record Office
criminal injuries compensation
registration of legal practitioners (other than advocates)\" [2]

[1] https://www.gov.im/registries/courts/charities/
[2] https://en.wikipedia.org/wiki/General_Registry_(Isle_of_Man)""",
        ),
    )
    GOVERNMENT_OF_INDIA__MINISTRY_OF_CORPORATE_AFFAIRS = (
        "IN-MCA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies in India register with the Registrar of Companies in their state. While each Registrar of Companies maintains their own database, the Ministry of Corporate Affairs regulates the corporate sector and maintains a database of national company information.

This information is accessible in data.gov.in

\"The Registrar of Companies (ROC) is an office under the Indian Ministry of Corporate Affairs that deals with administration of the Companies Act 1956 and Companies Act, 2013. There are currently 22 Registrars of Companies (ROC) operating from offices in all major states of India. Some states, such as Maharashtra and Tamil Nadu, have two ROCs each. Section 609 of the Companies Act, 1956 tasks the ROCs with the primary duty of registering companies and LLPs floated in the respective states and the union territories under their administration.

The Registrar of Company takes care of company registration (also known as incorporation) in India, completes reporting and regulation of companies and their directors and shareholders, and also oversees government reporting of various matters including the annual filling of various documents.\" [1]

[1] https://en.wikipedia.org/wiki/Registrar_of_Companies,_India
""",
        ),
    )
    MINISTRY_OF_HOME_AFFAIRS__INDIA__FOREIGN_CONTRIBUTIONS__REGULATION__ACT_REGISTER = (
        "IN-MHA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Foreign Contributions (Regulation) Act required NGOs in receipt of foreign funding in India to register with the government. They are assigned an FRCA Registration Number.

""",
        ),
    )
    ITALIAN_TAX_CODE___VAT_NUMBER = (
        "IT-CF",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies (and some other entities) in Italy must register with the Business Register of the Chambers of Commerce.

They are assigned a Codice Fiscale (CF) or Tax Code which also acts as their Partitia IVA (P.IVA) or VAT Number.

Entities may also be assigned an Economic and Administrative Directory (REA) identifier.""",
        ),
    )
    BUSINESS_REGISTER_OF_THE_ITALIAN_CHAMBERS_OF_COMMERCE = (
        "IT-RI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies (and some other entities) in Italy must register with the Business Register of the Chambers of Commerce.

They are assigned a Codice Fiscale (CF) or Tax Code.

Entities may also be assigned an Economic and Administrative Directory (REA) identifier. """,
        ),
    )
    JERSEY_FINANCIAL_SERVICES_COMMISSION__JFSC_ = (
        "JE-FSC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies and Non Profit Organisations operating in Jersey register with the Financial Services Commission (JFSC). A search of company information is freely available on the Commission website. There was no search available for NPOs at the time of last checks.

Users should be aware that the identifier numbers are not unique, as there are multiple types of companies and identifiers can be repeated. For example, there are two companies with the number '1381' - an LP (limited partnership) and an RC (Registered Private Company)

It is recommended that those creating identifiers for JSFC use the business codes as part of the identifier. For example, the limited partnership company described above should have the identifier:

JE-FSC-LP_1381


\"The Non-Profit Organizations (Jersey) Law 2008 (the “NPO Law”) was registered by the Royal Court on 25 July 2008 and came into effect on 8 August 2008.  This legislation requires NPOs to register with the Commission in certain circumstances.  The definition of an NPO, as provided by Article 1 of the NPO Law, is given below:

“An organization is a non-profit organization for the purposes of this Law if –
(a) it is established solely or primarily for charitable, religious, cultural, educational, social,
        or fraternal purposes with the intention of benefiting the public or a section of the public; and
(b) it raises or disburses funds in pursuance of those purposes.” \" [1]

[1] http://www.jerseyfsc.org/anti-money_laundering/forms/NPO/index.asp""",
        ),
    )
    JERSEY_OVERSEAS_AID_COMMISSION = (
        "JE-OAC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Jersey Overseas Aid Commission is responsible for distributing international development funds from Jersey. But they are not responsible for registration of NGOs. No database for organisation identifiers has been found.

\"Jersey has been funding international aid and development since 1968, but the current ‘Jersey Overseas Aid Commission’ was established by law in 2005. It is an independent body within the responsibilities of the Chief Minister. It is governed by three States Commissioners and three non-States Commissioners, all of whom are appointed by the States of Jersey.\" [1]

\"The Non-Profit Organizations (Jersey) Law 2008 (the “NPO Law”) was registered by the Royal Court on 25 July 2008 and came into effect on 8 August 2008. This legislation requires NPOs to register with the Commission in certain circumstances. \" [2]

[1] https://www.joa.je/the-commission/
[2] http://www.jerseyfsc.org/anti-money_laundering/forms/NPO/index.asp""",
        ),
    )
    COMPANIES_CONTROL_DEPARTMENT__JORDAN_ = (
        "JO-CCD",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Companies Control Department is an independent national financial and administrative institution affiliated to the Minister of Industry and Trade in Jordan under the provisions of the amended Companies Law No. (40) of 2002. The work of the department is governed by the 1997 Companies Law No.

The Department is responsible for registration of various types of companies within the Hashemite Kingdom of Jordan, including non-profit companies.

It maintains a number of online services for searching company information at http://www.ccd.gov.jo/e-services/home/db available in Arabic only.""",
        ),
    )
    REGISTER_OF_ASSOCIATIONS__JORDAN = (
        "JO-MSD",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The register of associations was established in the Ministry of Social Development in the Hashemite Kingdom of Jordan by virtue of the Associations Law No. (51) of 2008 and its amendments which abolished the Law of Associations and Voluntary Organizations No. 33 of 1966 and its amendments. The register of associations is the regulator of the associations sector in the Kingdom and in line with the legislation in force.\"[1]

[1]: http://www.societies.gov.jo/SitePage.aspx?PageId=107 (translated from Arabic)""",
        ),
    )
    NATIONAL_TAX_AGENCY_CORPORATE_NUMBER_PUBLICATION_SITE = (
        "JP-JCN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """On this website, the Corporate Number of each organization that has such number designated, and the name and the address of the head office or principal place of business of each organization that has registered its indications in English are made public.
The registry is open and searchable by Japanese Corporate Number (JCN) (in Japanese only), but only limited information is available. More information on the corporate number (JCN) can be found here - http://www.nta.go.jp/foreign_language/corporate_number/ (National Tax Agency website). """,
        ),
    )
    NGO_S_COORDINATION_BOARD = (
        "KE-NCB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The NGO Coordination Board of Kenya registers NGOs and maintains a registry of organisation information. This information can be accessed by through request and after paying a fee.

\"The Board has the responsibility of regulating and enabling the NGO sector in Kenya.

Our Mandate:

To maintain the register of National and International NGOs operating in Kenya, with the precise sectors, affiliations and locations of their activities.\" [1]

\"Under section 31 of the NGOs Regulations 1992, any member of the public is allowed to inspect the files and the documents therein of any registered organization during normal working hours. They can also obtain copies of documents in the files.

To conduct a records search a letter should be written to the ED of the NGOB stating the name of the applicant as well as the organization whose details they wish to search and the information they seek.

The applicant can decide whether to carry out the records search themselves or have the Board conduct it on their behalf. This will be upon a requisite payment of Kenya Shillings Three Thousand (KES 3000)\" [2]

[1] http://www.ngobureau.or.ke/
[2] http://www.ngobureau.or.ke/?page_id=408""",
        ),
    )
    REGISTAR_OF_COMPANIES = (
        "KE-RCO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Registrar of Companies is under the remit of the Registrar General, which is a part of the Office of the Attorney General and Department of Justice. This Registrar is responsible for the registration of companies within Kenya, and maintains a database, the records of which can be accessed on request for a fee.",
        ),
    )
    REGISTRAR_OF_SOCIETIES = (
        "KE-RSO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Registrar of Societies is held under the Office of the Attorney General and Department of Justice. Interest groups in Kenya apply to the Registrar of Societies for both registration and exemption from registration of being a 'society'. But there is no indication that societies have legal/corporate foundation. There is also no publicly available database of the Registrar of Societies.

For Kenya's NGO registry list, users should look to KE-NCB. Please note there is currently no publicly available dataset for this registry.

\"In summary, State Law Office and Department of Justice is mandated to promote the rule of law and public participation; support Government’s investment in socio-economic development; promote transparency, accountability, ethics and integrity; spearhead policy, legal and institutional reforms; promote economic governance and empowerment; promotion, fulfillment and protection of human rights; undertake administrative management; capacity building; and enhance access to justice.\" [1]

[1] http://www.statelaw.go.ke/about-office-of-the-attorney-general-and-department-of-justice/""",
        ),
    )
    ELECTRONIC_DATABASE_OF_LEGAL_ENTITIES_AND_BRANCHES__KRYGYZSTAN_ = (
        "KG-ID",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Ministry of Justice of the Republic of Kyrgyz maintains the register of legal entities.",
        ),
    )
    KYRGYZ_REPUBLIC_REGISTER_OF_LEGAL_ENTITIES = (
        "KG-INN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Ministry of Justice of the Kyrgyz Republic maintains the register of legal entities. Only Russian and Kyrgyz interfaces are available.",
        ),
    )
    BUSINESS_IDENTIFICATION_NUMBER__BIN_ = (
        "KZ-BIN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"Business Identification Number (BIN) is a unique number consisting of 12 digits created for legal person (branch and agency) and individual entrepreneur operating in form of joint entrepreneurship.

[...] as from January 1, 2013 [...] BIN (Business Identification Number) will be implemented in the Republic of Kazakhstan instead of Taxpayer’s Registration Number (TRN).\"[1]

The Ministry of Finance of the Republic of Kazakhstan maintains the business register.

[1] https://www.norvik.eu/en/iin-and-bin-implementation-in-the-republic-of-kazakhstan/?print=1""",
        ),
    )
    LEBANESE_MINISTRY_OF_JUSTICE__COMMERCIAL_REGISTER = (
        "LB-CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """'Article 23 of the Lebanese Trade Law stipulates that 'every court of first instance shall have a record carefully recorded by the author under the supervision of the President or a judge appointed by the President specifically in each year'. The Clerk of the Court is limited to the recording of data submitted by stakeholders without examination or scrutiny and without verifying their validity.

The Commercial Register is divided into two types:
- a general register in which traders and companies register.
- A special register in which commercial establishments and contracts are registered'[1]

[1]: http://cr.justice.gov.lb/desc/desc.aspx (translated)""",
        ),
    )
    MINISTRY_OF_INTERIOR__LEBANON_ = (
        "LB-MOI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Ministry of Interior is the main registration body in Lebanon. All NGOs are required to register with the Ministry of Interior.",
        ),
    )
    LESOTHO_COUNCIL_OF_NON_GOVERNMENTAL_ORGANISATIONS = (
        "LS-LCN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Lesotho Council of NGOs provides a range of support services and advocacy to civil society organisations  in Lesotho. They do not appear to have the responsibility of either registering NGOs or maintaining a database of identifiers.

\"The Lesotho Council of Non-Governmental Organisations (LCN) is an umbrella organizations for NGOs in Lesotho. It was established in May 1990 with an objective of providing supportive services to the NGO Community. The Council implements this through networking and leadership training and development, information dissemination, capacity building, coordination, advocacy and representation when dealing with the government and the international community.\" [1]

[1] http://www.lcn.org.ls/about/default.php""",
        ),
    )
    LITHUANIA_REGISTER_OF_LEGAL_ENTITIES = (
        "LT-PVM",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Register of Legal Entities registers businesses, institutions and NGOs and collects detailed data about Lithuanian legal entities as well as branches and representative offices of foreign companies and organizations. The Register contains complete information (and historical data) about legal form and status of legal entities, fields of its activity, size and structure of the authorized capital, members of sole and collective management bodies, licenses acquired, etc. It is obligatory for the most of business companies to submit annual financial statements to the Register of Legal Entities since 2004. Starting from March 2010 private limited liability companies are obliged to declare current list of shareholders to the Register. ",
        ),
    )
    INFORMATION_PLATFORM_OF_LEGAL_ENTITIES__LITHUANIA_ = (
        "LT-RC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The Register of Legal Entities registers businesses, institutions and NGOs and collects detailed data about Lithuanian legal entities as well as branches and representative offices of foreign companies and organizations.

The Register contains complete information (and historical data) about legal form and status of legal entities, fields of its activity, size and structure of the authorized capital, members of sole and collective management bodies, licenses acquired, etc. It is obligatory for the most of business companies to submit annual financial statements to the Register of Legal Entities since 2004. Starting from March 2010 private limited liability companies are obliged to declare current list of shareholders to the Register. \"[1]

Government agencies are also included in the register.

[1] http://www.registrucentras.lt/jar/index_en.php""",
        ),
    )
    REGISTER_OF_ENTERPRISES_OF_THE_REPUBLIC_OF_LATVIA = (
        "LV-RE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Register of Enterprises registers companies and maintains a database of organisation information. This information is searchable on the website and can be found in CSV form.

\"Register of Enterprises is the central institution which keeps all data and records up to date. It is mandatory to submit incorporation documents with the registry at the moment of company establishment, as well as to file all amendments in the company board (directors) or shareholder registry.

The unified register is also available electronically.

The Register of Enterprises has the following functions:
to register undertakings and their branches, representative offices and representatives of foreign undertakings and organisations, co-operative companies,\" [1]

[1] http://www.baltic-legal.com/commercial-register-of-latvia-eng.htm

Free of charge information includes type of legal entity; registered office; new or current name or trade name and previously registered or historical name or trade name; registration number; Single Euro Payment Area beneficiary identification code (if allocated); registration date; date of deletion of the legal entity from the register (or the date of reorganisation if the reason for the deletion is a reorganisation); deadline for registration of religious organisations that are subject to re-registration.""",
        ),
    )
    LEGAL_ENTITY_REGISTRATION_NUMBER__IDNO__MOLDOVA = (
        "MD-IDNO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"General information about the legal entities incorporated on the Republic of Moldova’s territory, except political parties, non-governmental organizations and press agencies. Data from the State Chamber of Registration is published once per month on the Government Portal of Open Data (http://www.date.gov.md/en) and can be searched in a convenient way via dedicated platform http://www.idno.md/.\"[1]

The unique state identification number (IDNO) assigned to the legal entity also constitutes its fiscal code.

\"The idno.md platform has been developed to facilitate access to open government data and to help citizens gain added value by using them. The project is based on the reuse of public data about registered companies in the Republic of Moldova, presenting them in a user-friendly way so that everyone can easily analyze and process them.

The platform allows users to search through data, track company history, and generate infotainment based on available data. At present, information is available about over 215,000 companies that have been registered in Moldova since 1991.

The data on idno.md is updated monthly, automatically. The idno.md team has long envisioned to integrate other information that will be available to the public, including information on public procurement connected with companies that have won tenders over the years.\"[1]

More information about companies and their administrators / founders can be requested at the State Registration Chamber.

[1] http://www.idno.md/page?id=2 (Nov, 2017)
[2] http://www.idno.md/page?id=5 (Nov, 2017)""",
        ),
    )
    THE_CHAMBER_OF_COMMERCE_AND_INDUSTRY_OF_MALI = (
        "ML-CCIM",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Chamber of Commerce and Industry of Mali (CCIM) is responsible for the organization and professional representation of organisations and legal persons working in the various branches of commercial, industrial and service activities in Mali.",
        ),
    )
    TAX_IDENTIFICATION_NUMBER = (
        "ML-NIF",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Tax Identification Number (Numero d’Identification Fiscale) is issued to registered companies, and to branches of foreign organisations operating in Mali.

There is publicly available register of assigned Tax Identification Numbers.
""",
        ),
    )
    MINISTRY_OF_HOME_AFFAIRS_CENTRAL_COMMITTEE_FOR_THE_REGISTRATION_AND_SUPERVISION_OF_ORGANISATIONS = (
        "MM-MHA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The MHA assigns a registration number to each NGO - this number is time limited, for example 4 years, after which the registration is reviewed.

There is no URL for the Ministry, nor is there a publicly available database of NGO information.""",
        ),
    )
    COMPANIES_AND_BUSINESSES_REGISTRATION_INTEGRATED_SYSTEM__MAURITIUS = (
        "MU-CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Corporate and Business Registration Department has the following main functions:
- The incorporation, registration and striking-off of companies
- The registration of documents that must be filed under the Companies Act 2001
- The provision of company information to the  public
- The enforcement of compliance with the legal requirements
- Registration of Businesses
- The Insolvency Service
- Registration of Limited Partnerships and Foundations""",
        ),
    )
    THE_COUNCIL_FOR_NON_GOVERNMENTAL_ORGANISATIONS_IN_MALAWI = (
        "MW-CNM",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Council for NGOs in Malawi provides a range of support services and advocacy initiatives to NGOs working in Malawi. They do not appear to have the responsibility of registering organisations or maintaining a database with information.

\"Objectives:

1. To represent the collective interests of NGOs in Malawi.
2. To enhance and improve the operational environment within which NGOs function.
3. To promote and facilitate networking, coordination and collaboration within the NGO community, and between the NGOs and government, donor community and private sector.
4. To further the standing of NGOs as competent, professional and suitable agents of development.
5. To support member NGOs to build and strengthen their institutional capacity.
6. To support NGOs carry out their functions under the NGO Act 2000.\" [1]

[1] http://www.congoma.mw/about-us/objectives/""",
        ),
    )
    MALAWI_REVENUE_AUTHORITY = (
        "MW-MRA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Malawi Revenue Authority is responsible for processing tax payments and investigating cases of tax evasion in Malawi. They do not appear to be responsible for the registration of companies or maintaining a database of organisations.

Company registration in Malawi is done through the Department of Registrar General, under the Ministry of Justice and Constitutional Affairs.

\"The Ministry of Industry and Trade is responsible for providing application forms for Registration of Business Name.
Applications may be submitted to the Department of Registrar General’s Head Office in Blantyre and its Regional Office in Lilongwe.\" [1]

[1] https://www.wikiprocedure.com/index.php/Malawi_-_Register_Business_Name""",
        ),
    )
    NGO_BOARD_OF_MALAWI = (
        "MW-NBM",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All NGOs operating in Malawi must register with the NGO Board of Malawi. All NPOs must also register with the Registrar General. There is a pdf file with a list of registered NGOs, but they do not have registration numbers. New database is planned.

\"In line with Section 20 of the NGO Act, every organization that wishes to operate or is operating in Malawi as an NGO must register with the NGO Board of Malawi. The Board is a regulatory Body for NGOs in Malawi and failure to register with it means the NGO will be operating illegally.\" [1]

\"We are currently improving our directory which will not only show a list of registered NGOs when this process is completed, but will also provide an overview of each registered NGO, contacts, and will be searchable by sector and/or location (District).\" [2]

\"The Registrar General is responsible for the registration and the administration non-profit entities under the Trustees Incorporation Act Cap. 5:03. \" [3]

[1][2] http://ngoboardmalawi.mw/directory.php
[3] https://www.registrargeneral.gov.mw/services/registration-of-businesses.html""",
        ),
    )
    REGISTRAR_GENERAL__DEPARTMENT_OF_JUSTICE = (
        "MW-RG",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Department of Registrar General under the Department of Justice and Constitutional Affairs is where companies and NPOs register in Malawi. They do not have a database of company information available online.

\"We are a government department under the Ministry of Justice and Constitutional Affairs responsible for the registration and administration of business entities, Non Profit Organizations and Industrial Property Rights\" [1]

[1] https://www.registrargeneral.gov.mw/index.html""",
        ),
    )
    BUDGET_CLASSIFICATION_OF_PUBLIC_ENTITIES__MEXICO_ = (
        "MX-CPA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """This list provides Mexico's administrative classification, which includes the following concepts:

* Ramo: a concept that groups all the specific organizations from Mexico's Public Administration.
* Unidad Responsable: the specific organizations from Mexico's Public Administration

By combining the Ramo, and Unidad Responsable codes, a unique identifier can be created for government entities.

For example:

4-121 for Dirección General de Protección Civil""",
        ),
    )
    FEDERAL_TAXPAYERS_REGISTRY = (
        "MX-RFC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Registro Federal de Contribuyentes de México assigns an RFC identifier to both individual and corporate taxpayers.

Registration takes place through Servicio de Administración Tributaria (SAT) and registrants are provided with their RFC.

Whilst there is no public database of RFCs available, a web service to validate RFCs is available at https://portalsat.plataforma.sat.gob.mx/ConsultaRFC/

The structure of an RFC encodes information about the initials and date of registration of a company

""",
        ),
    )
    COMPANIES_COMMISSION_OF_MALAYSIA = (
        "MY-SSM",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Companies Commission of Malaysia (SSM) is a statutory body formed as a result of a merger between the Registrar of Companies (ROC) and the Registrar of Businesses (ROB) in Malaysia which regulates companies and businesses. SSM came into operation on 16 April 2002.
""",
        ),
    )
    MOZAMBIQUE_COMMERCIAL_REGISTRY = (
        "MZ-CR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The purpose of the Commercial Registry is to make known the status of merchant of natural and legal persons, being defined as mandatory for the formation of companies. ",
        ),
    )
    MOZAMBIQUE_MINISTRY_OF_JUSTICE = (
        "MZ-MOJ",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """'Domestic NGOs are required to register with the Ministry of Justice.'[1]

[1] http://www.commonwealthofnations.org/sectors-mozambique/civil_society/national_ngos_civil_society/
""",
        ),
    )
    TAXPAYER_SINGLE_IDENTIFICATION_NUMBER__MOZAMBIQUE_ = (
        "MZ-NUIT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """NUIT is the Mozambique Taxpayer Single Identification Number.

It is made up of 9 digits split into 3 parts: the first digit stands for the type of entity, the middle part is a sequential number, and the last digit provides a checksum.

Both individuals and corporate entities are assigned an NUIT. """,
        ),
    )
    BUREAU_OF_PUBLIC_PROCUREMENT__BPP__CONTRACTOR_REGISTRATION_SYSTEM__NIGERIA_ = (
        "NG-BPP",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Nigerian Bureau of Public Procurement are responsible for monitoring and oversight of public procurement in Nigeria.

The Contractor and Service Provider Database System is a government vendor registration database system that assigns a unique contractor identification number, categories, and classification of firms who have applied for, or been involved in, government contracts.


""",
        ),
    )
    NIGERIAN_CORPORATE_AFFAIRS_COMMISSION = (
        "NG-CAC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All companies operating in Nigeria must register with the Corporate Affairs Commission. NGOs also register with the Commission. This database is available through a searchable webpage.

\"The Corporate Affairs Commission (CAC) of Nigeria was established in 1990 vide Companies and Allied Matters Decree no 1 (CAMD) 1990 as amended, now on Act cap C20 Laws of federation of Nigeria. It is an autonomous body charged with the responsibility to regulate the formation and management of companies in Nigeria.\" [1]

\"In Nigeria NGOs may be registered as a company limited by guarantee or as incorporated trustees (by which trustees of the NGO, rather than the NGO itself, obtains the status of a body corporate)... The duly completed application is then submitted to the Corporate Affairs Commission.\" [2]

[1] https://en.wikipedia.org/wiki/Corporate_Affairs_Commission,_Nigeria
[2] http://www.nigeriaformations.com/charities-and-NGOs.php""",
        ),
    )
    CHAMBER_OF_COMMERCE__NETHERLANDS_ = (
        "NL-KVK",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All companies and entities (including most NGOs) in the Netherlands must enrol with the Commercial Register, which is hosted by the Dutch Chamber of Commerce. Each entity receives a Chamber of Commerce number upon registration, which is the appropriate identifier Dutch companies and NPOs.

Basic company information is available for free, detailed info can be downloaded for a fee.

\"All companies and entities in the Netherlands must enroll in the Commercial Register. By law, you have a business if you provide common goods or services to others with the intent to make a profit.\" [1]

\"Recipient companies can consult www.kvk.nl/waadi to check if agencies are registered on the Chamber of Commerce website. They can do this simply by entering their Chamber or Commerce number, which is assigned to all companies and legal entities upon registration in the Business Register.\" [2]

\"The major forms of Dutch non-profit organization are the associations, the foundations and the churches... Associations registered in The Netherlands are unions between two or more individuals, physical persons or corporate bodies that pursue certain goals stated in the Articles of Association and that cannot divide profit among its members... There are two types of associations that can be set up in the Netherlands: with complete authority under the law (in this case the articles of associations are drawn by a civil notary and it’s mandatory in this case that the association is registered at the Dutch Chamber of Commerce trade register) and with limited authority under the law (when the articles are not drawn up by a notary and the registration is not mandatory).\" [3]

[1] https://www.kvk.nl/inschrijven-en-wijzigen/inschrijven/?block=420250
[2] https://www.kvk.nl/english/how-to-register-deregister-and-report-changes/registering-with-the-chamber-of-commerce/hiring-or-provision-of-workers-in-the-netherlands/
[3] http://www.bridgewest.eu/article/register-non-profit-organization-netherlands""",
        ),
    )
    OVERHEID_NL_WEB_METADATA_STANDARD = (
        "NL-OWMS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Overheid.nl is the central access point to all information about government organisations of the Netherlands.

The Overheid.nl Web Metadata Standard ( OWMS ) is the metadata standard for information from the Dutch government on the Internet.

It contains URIs for a wide range of government bodies, including national, local and regional government and water boards.

It provides a linked open dataset which contains ontological information about the relationship between those organisations (e.g. listing parent agencies, or noting organisations that succeed previous organisations).

A management plan is in place for updating of the information [1].


[1]: http://standaarden.overheid.nl/owms/beheer """,
        ),
    )
    BRØNNØYSUNDREGISTRENE = (
        "NO-BRC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies in Norway must be Registered with the Register of Business Enterprises. Non-profits are eligible for registry with the Register of Non-Profit Organizations.

These registries are maintained by the Brønnøysundregistrene.  Businesses can be incorporated by applying to the online 'coordinated register notification' - Altinn, which is also maintained by Brønnøysundregistrene.

This database can be searched by the public for free from the organisation homepage, and can be downloaded in various data format.

\"The Register of Business Enterprises registers all Norwegian and foreign businesses in Norway, ensuring legal protection and financial overview.\" [1]

\"Non-profit organizations that run voluntary activities not motivated by profit are eligible to register. Examples of such organizations are:

- associations
- non-commercial foundations that do not distribute funds, or that only - distribute funds to non-profit activities
- commercial foundations that only distribute funds to non-profit activities
- limited liability companies that only distribute funds to non-profit activities.\" [2]

\"Brønnøysund Register Centre (Norwegian Bokmål: Brønnøysundregistrene, Norwegian Nynorsk: Brønnøysundregistra) is a Norwegian government agency that is responsible for the management of numerous public registers for Norway, and governmental systems for digital exchange of information.\" [3]

[1][2] https://www.brreg.no/home/about-us/the-registers-and-their-timeline/
[3] https://en.wikipedia.org/wiki/Br%C3%B8nn%C3%B8ysund_Register_Centre""",
        ),
    )
    COMPANY_REGISTRAR_OFFICE = (
        "NP-CRO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All companies operating in Nepal must register with the Office of the Company Registrar Office. This database is available for search on the Office homepage.

\"To register a company, the promoter must submit an application as prescribed by the Ministry of Industry, Commerce, and Supplies. Online filing of the required documents has been introduced and made mandatory. After the online filing, entrepreneurs are required to visit the Office of Company Registrar and submit all the original documents for further verification.\" [1]

[1] http://www.doingbusiness.org/data/exploreeconomies/nepal#starting-a-business""",
        ),
    )
    SOCIAL_WELFARE_COUNCIL_NEPAL = (
        "NP-SWC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """International NGOs wishing to operate in Nepal must register with the Social Welfare Council. Upon registration, these INGOs receive an Affiliation Certificate and an SWC Affiliation Number. This database can be searched on the website.

Local NGOs do not need to be associated with the SWC, but may register with their local District Administration Office (DAO). The SWC list is thus not a complete list of all NGOs working in Nepal.

\"1. As laid down in article 12, Section 1, of the Social Welfare Act 2049, the international non-governmental organizations (INGOs) seeking to work in the Kingdom of Nepal must apply to the Social Welfare Council and seek permission prior to starting work.\" [1]

[1] Document available for download at - http://www.swc.org.np/?page_id=47""",
        ),
    )
    PERUVIAN_NATIONAL_SUPERINTENDENCY_OF_PUBLIC_REGISTRIES_REGISTERED_LEGAL_ENTITIES = (
        "PE-SUNARP",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The SUNARP is an autonomous decentralized body of the Justice Sector in Peru and the governing body of the National System of Public Registries. It maintains the register of Legal Entities (\"Registro De Personas Juridicas\") which covers corporate and non-corporate bodies including:

* Non Corporate
    * Associations
    * Foundations
    * Committees
    * Peasant and native communities
    * Cooperatives
    * Grassroots social organizations
* Corporate
    * Public Limited Companies (open and closed)
    * Collective Societies
    * Limited Partnerships
    * Limited Liability Company
    * Civil Companies

""",
        ),
    )
    SECURITIES_AND_EXCHANGE_COMMISSION__PHILIPPINES_ = (
        "PH-SEC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Securities and Exchange Commission in the Philippines provides licenses so that corporations, partnerships or associations can transact business in the Philippines.

For domestic companies, this may come in the form of a 'Certificate of Incorporation'. For foreign firms or organisations, branches may obtain a 'License to transact business'. """,
        ),
    )
    PAKISTAN_CENTRE_FOR_PHILANTHROPY = (
        "PK-PCP",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Pakistan Centre for Philanthropy provides certification for NGOs working in Pakistan. Registration with the PCP is not obligatory for working in Pakistan and therefore not all NGOs will be recorded on the 'PCP Certified CSO List'. However, this list can be searched online.

All NGOs are required to register with their local Voluntary Social Welfare department.

\"This voluntary assessment aims to enhance a CSOs' credibility and resultantly its access to funding. Through the allied activities of this programme, PCP promotes certified CSOs in an annual directory and on its website and also builds capacities of civil society organisations for greater effectiveness.\" [1]

[1] http://pcp.org.pk/page.php?pid=19""",
        ),
    )
    PAKISTAN_VOLUNTARY_SOCIAL_WELFARE_AGENCY = (
        "PK-VSWA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All NGOs are required to register with their local Voluntary Social Welfare (VSWA) department. The VSWA assigns each organisation with an organisation identifier that is made up of a number and the year of registration. There is no searchable database.

The VSWA number should be used as a unique identifier, but users should be aware that the entire sequence is needed (number and year), as it is possible that the number is unique to the year of registration, but is repeated for other years, i.e, 511-2007 is ASFP, but there may be another org with 511-1998.

\"Any person intending to establish an agency, and any person
intending that an agency already in existence should be
continued as such, shall, in the prescribed form, and on payment
of the prescribed fee, make an application to the Registration
Authority\" [1]

\"9.Registration, professional guidance and financial assistance to voluntary Social Welfare agencies for strengthening, improving and promoting their activities, coordination amongst NGOs / Donors and concerned government departments.\" [2]

[1] http://www.ilo.org/dyn/natlex/docs/ELECTRONIC/81785/88956/F1282834913/PAK81785.pdf
[2] http://www.swkpk.gov.pk/""",
        ),
    )
    THE_NATIONAL_COURT_REGISTER__POLAND_ = (
        "PL-KRS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The National Court Register (KRS standing for Krajowy Rejestr Sądowy) number is required to be acquired by several types of organizations: companies (without Sole Proprietorships that register in CEiDG), non-profits (associations, foundations, charities), unions and public health institutions.

An organization has to apply for a KRS number and pay a fee (around 25$). """,
        ),
    )
    TAX_IDENTIFICATION_NUMBER__POLAND_ = (
        "PL-NIP",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Tax Identification Number (NIP) is used for tax purposes and can be assigned to any organization: companies including sole proprietorships, non-profits, government agencies.

NIP is assigned to organizations in process of their registration.

Till 2011 NIP number was also assigned to natural people (tax payers).""",
        ),
    )
    REGON_STATISTICAL_NUMBER_OF_AN_ECONOMY_ENTITY = (
        "PL-REGON",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """A unique number assigned to national economic entities, and to the local units of these entities in the national official register of national economy entities,  REGON. The identifier provides no implicit or explicit information on the features of an entity.

Every organization receives REGON number during the registration phase.

Looking at REGON/NIP relations: most often all organizations having NIP (PL-NIP) will have REGON (PL-REGON) and vice-versa.

One of a few exceptions are, for example, schools that will have REGON numbers (for statistical purposes), but they are not required to have NIP tax id number (because they are executing municipalities' budgets).""",
        ),
    )
    MINISTRY_OF_INTERIOR__PALESTINE_ = (
        "PS-MOI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Palestine Ministry of Interior provide a registration list of NGOs, divided by province and responsible ministry.
""",
        ),
    )
    PORTAL_OF_PUBLIC_SERVICES = (
        "PT-NIPPC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The business register is governed by the Business Registry Code, adopted by Decree-Law No 403/86 of 3 December 1986, and is the responsibility of the business registry offices throughout the country; these offices are external services of the Institute of Registrars and Notaries (IRN), a public body supported by the Ministry of Justice.
""",
        ),
    )
    CLASSIFICATION_OF_ENTITIES_IN_THE_NATIONAL_BUDGET_FOR_PARAGUAY = (
        "PY-PGN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Provides identifiers for organizations and institutions from the Paraguayan State, including national public bodies, administrative departments, and municipalities.

From the National Budget Law (Presupuesto General de la Nación (PGN)) of 2016 from Paraguay:

“The objective of the classification by entities is to organize information related income, spending and budgetary credits from the different state organisms and entities at various institutional levels according to their functions, nature, characteristics and dependencies.”[1]

The list is yearly updated given each the yearly national budget law.

N.B. Please note, many government organisations also have an 'RUC' code (list [PY-RUC](/list/PY-RUC)), which is preferred to this list.

[1]: http://bit.ly/PGNPY2016""",
        ),
    )
    UNIQUE_TAXPAYER_REGISTRY__PARAGUAY = (
        "PY-RUC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Registro Único del Contribuyente (RUC) is the unique taxpayer registry that maintains the personal, non-transferable, identification number for all those physical persons (national or foreign) and legal entities (for-profit and non-profit) that carry out economic activities in the Paraguayan territory.

The identification number is created primarily for tax purposes.""",
        ),
    )
    NATIONAL_TRADE_REGISTER__ROMANIA_ = (
        "RO-CUI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The National Trade Register Office (NTRO) is a public institution with legal personality, subordinated to the Ministry of Justice, entirely financed from the state budget, whose activity is regulated by the Law no. 26/1990 on trade register, as republished and subsequently amended and supplemented.

The National Trade Register Office carries out the following activities:

* keeping the trade register;
* providing documents and information;
* archiving documents based on which the registrations in the trade register are made;
* assisting legal and natural persons subject to registration in the trade register;
* editing and publishing the Insolvency Proceedings Bulletin.""",
        ),
    )
    SERBIAN_BUSINESS_REGISTRATIONS_AGENCY = (
        "RS-APR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Serbian Business Registrations Agency (APR) provides a single place of registration for all companies and individuals - domestic and foreign - operating in Serbia. Each entity is given an identification number and a tax number in the Business Entities Register.

The Матични број / identification number should be used for identifiers.

A searchable database of the Business Entities Register is available online.

\"The SBRA runs business registers as single, centralized, public electronic databases:

The Business Register, in accordance with the Law on Business Entities Registration (operative as of 1/1/2005):

 *Register of Companies (in effect as of 1 January 2005)
* Register of Entrepreneurs (in effect as of 1 January 2006)
* Register of foreign parties (in effect as of 1 January 2006)\" [1]

\"Serbian term or phrase:    matični broj / identification number
This is the identification number contained in the Company Register \" [2]

[1] http://www.apr.gov.rs/eng/AboutAgency/AllRegistersatOnePlace.aspx
[2] http://www.proz.com/kudoz/serbian_to_english/law_contracts/2614508-maticni_broj.html""",
        ),
    )
    TAX_IDENTIFICATION_NUMBER_REGISTER = (
        "RS-PIB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Ordinary taxpayer registration numbers start from the number 10000001 and end with the number 99999999. The PIB is determined so that the first eight digits are the regular registration number of the taxpayer, and the last digit is the control number. ",
        ),
    )
    UNIFORM_STATE_REGISTER_OF_LEGAL_ENTITIES_OF_RUSSIAN_FEDERATION = (
        "RU-INN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """This register offers information reports on any legal entity registered on the territory of the Russian Federation in the on-line mode directly from the respective registers.

 There are following types of products available at this moment:
* Extract from USRLE - price 1 credit (1 credit is equal to 10.8 Euro, discounts available, see Rates/Prices)
* Annual Accounts - price 2 credits
* Extended Report - price 2 credits
* Extended Report + Finances - price 4 credits
* Court records + Enforcement proceedings - price 4 credits""",
        ),
    )
    UNIFIED_STATE_REGISTER_OF_LEGAL_ENTITIES__USRLE___RUSSIAN_FEDERATION = (
        "RU-OGRN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The USRLE (Uniform State Register of Legal Entities) (also EGRUL) is a federal information resource. The USRLE recording is performed by the registering authorities according to the procedure established by the Government of the Russian Federation.

Here you can get information about any legal entity registered in the territory of the Russian Federation in the form of an information extract from the Unified State Register of Legal Entities.

In addition, access to foreign state registers of more than 200 countries of the world is open, including to most European countries.

Information is provided from the Unified State Register of Legal Entities in the form of an electronic document.\"""",
        ),
    )
    BOLAGSVERKET = (
        "SE-BLV",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Swedish Companies Registration Office (Bolagsverket) registers all business operating in Sweden, except for sole traders. This registry is available to search online. All entities are given an organisation number that can be used as an identifer.

\"All forms of business enterprise except for sole traders have to be registered with the Swedish Companies Registration Office before starting to operate.\" [1]

[1] https://www.verksamt.se/en/web/international/starting/get-started-business-registration-and-tax""",
        ),
    )
    LEGAL__FINANCIAL_AND_ADMINISTRATIVE_SERVICES_AGENCY__SWEDEN_ = (
        "SE-KK",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "A Swedish administrative authority under the Ministry of Finance, which is responsible for the registration of religious communities and organisational units of religious communities. ",
        ),
    )
    BUSINESS_REGISTRATION_NUMBER__ORGANISATIONSNUMMER___SWEDEN = (
        "SE-ON",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The organization number is a unique identifier assigned to legal entities, such as companies and associations.

The authority that registers the company or association when it is to be started assigns the organizational number. Most companies and associations have their organization number from the Swedish Companies Registration Office [Bolagsverket](http://www.bolagsverket.se). But also, for example, the Swedish Tax Agency and Land Survey allocate organizational numbers.

From the Swedish Companies Registration Office, the company or association has its organization number when we have decided to register. The organization number is on the registration certificate that we send out.\"[1]

\"The first digit of the organization number is called \"Group Number\" and specifies the company form or other legal form to which the legal entity is grouped. The following group numbers may occur.

1 - Death certificate
2 - State, county council, municipalities, parishes
3 - Foreign companies engaged in business activities or own real estate in Sweden
5 - Aktiebolag
6 - Single company
7 - Economic associations , tenant-owner associations
8 - Ideal associations and foundations
9 - Trading companies , limited companies and simple companies\"[2]

Non-commerical organsiation are searchable through other third-party applications, e.g. https://www.allabolag.se/

[1] http://www.bolagsverket.se/ff/foretagsformer/organisationsnummer-1.7902
[2] https://sv.wikipedia.org/wiki/Organisationsnummer#Organisationsnummer""",
        ),
    )
    ACCOUNTING_AND_CORPORATE_REGULATORY_AUTHORITY__ACRA_ = (
        "SG-ACRA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Accounting and Corporate Regulatory Authority (ACRA) is the national regulator of business entities, public accountants and corporate service providers in Singapore. Each corporate entity receives a Unique Entity Number (UEN), which should be used as the identifier.

\"Registering or setting up a company in Singapore is accomplished through contacting Accounting and Corporate Regulatory Authority (ACRA).\" [1]

\"From 1 January 2009, all entities that are registered in Singapore, such as
businesses, local companies, limited liability partnerships (LLPs), societies,
representative offices, healthcare institutions and trade unions, will have a
Unique Entity Number (UEN) as its identification number. \" [2]

[1] https://www.wikiprocedure.com/index.php/Singapore_-_Registering_or_Setting_up_Local_Company
[2] https://www.ipos.gov.sg/Portals/0/about%20IP/copyrights/UENFAQs2.pdf""",
        ),
    )
    SLOVENIAN_BUSINESS_REGISTER = (
        "SI-PRS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The Slovenian Business Register (PRS) is a central database containing information about all business entities involved in a profit or non-profit activity having their principal place of business located on the territory of the Republic of Slovenia, as well as information on their subsidiaries and other divisions of business entities performing business activities in the territory of the Republic of Slovenia.",
        ),
    )
    TAX_IDENTIFICATION_NUMBER__SLOVENIA_ = (
        "SI-TIN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """A unique tax identifier code (Davčna številka) which every legal entity or an individual entrepreneur must obtain.

These are entered on to the Slovenian Business Register (Poslovni register Slovenije)""",
        ),
    )
    MINISTRY_OF_JUSTICE_BUSINESS_REGISTER = (
        "SK-ORSR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The companies register is administered by the Ministry of Justice. Entry to the register is obligatory for companies, cooperatives and for some specific physical entities stated by law. Information in the register is searchable by trade name, identification number, registered office, registration number and name of a person.\" [1]

\"The Obchodný register (commercial register) is a public list containing statutory data concerning entrepreneurs, companies and other legal entities, where this is laid down by separate legislation.
The list is administered by the Ministry of Justice of the Slovak Republic.\" [2]

[1] http://www.company-registers.info/en/european-union/slovakia.html
[2] https://e-justice.europa.eu/content_business_registers_in_member_states-106-sk-en.do?member=1""",
        ),
    )
    SLOVAKIA_MINISTRY_OF_INTERIOR_TRADE_REGISTER = (
        "SK-ZRSR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Ministry of Interior Trade Register does have a database of companies, but users should refer to the Ministry of Justice Business Register in SK-ORSR for the unique identifier list for Slovakia.

The Ministry of Justice has been shown to be the organisation responsible for company registration, and thus SK-ZRSR has been deprecated in favour of SK-ORSR.""",
        ),
    )
    NATIONAL_IDENTIFICATION_NUMBER_OF_COMPANIES_AND_ASSOCIATIONS__NINEA___SENEGAL = (
        "SN-NINEA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Any organization (company, association, NGO) operating in Senegal must be included in a directory of legal entities ([Source](http://www.impotsetdomaines.gouv.sn/fr/demander-un-ninea)).

Registration takes place through several agencies, and a Numéro d’Identification National des Entreprises et des Associations (NINEA) (National Identification Number for Companies and Associations) is provided to incorporated bodies.

A directory or lookup of companies and numbers is not available online, however most legal entities will have an NINEA which can be used as an identifier.""",
        ),
    )
    SOUTH_SUDAN_RELIEF_AND_REHABILITATION_COMMISSION = (
        "SS-RRC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The South Sudan Relief and Rehabilitation Commission (SSRRC) is an agency of the Government of South Sudan. It is the operational arm of the Ministry of Humanitarian Affairs and Disaster Management. The NGO Act 2016 added additional powers to the agency to register any NGO interested in operating in South Sudan. ",
        ),
    )
    MERSIS_CENTRAL_TRADE_REGISTRY_SYSTEM = (
        "TR-MERSIS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Central Trade Registry System (MERSIS) is a centralized information system allowing for the implementation of the commercial registry processes and storing them and commercial registry data electronically. MERSIS can be accessed by registered users or using the e-signature from the website of the Ministry of Customs and Trade. It contains titles of companies, addresses, contact information, capital information, companies' partners, joint capital information, field of business, executive bodies of companies. Some information can also be found at http://www.ticaretsicil.gov.tr/english/index.php",
        ),
    )
    DEPARTMENT_OF_ASSOCIATIONS__MINISTRY_OF_INTERIOR__TURKEY_ = (
        "TR-MOI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All non-profit associations operating in Turkey should register with the Department of Associations.

During registration, they will be given a registration number. """,
        ),
    )
    TANZANIA_BUSINESS_REGISTRATIONS_AND_LICENSING_AGENCY = (
        "TZ-BRLA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Business Registrations and Licensing Agency (BRELA)[ (http://www.brela.go.tz/] registers companies in Tanzania. Based on the data available on Open Corporates, it appears that BRELA assigns each organisation with a unique identifier .

\"The Business Registrations and Licensing Agency (BRELA) is an Executive Agency under the Ministry of Industry and Trade responsible for business administration and regulation of the laws; namely Companies Registration, Business Names Registration, Trade and Service Marks Registration, granting of Patents and issuing of Industrial License.\" [1]

The Business Registrations and Licencing Agency (BRELA) has started to list registered companies in Tanzania through the Online Registration System (ORS) which can be searched for business and company names by the general public. Please note, however, that not all businesses may yet be present on the ORS as updated data or annual returns are required in order to populate the database.[2]

[1] http://www.brela.go.tz/index.php/about/introduction
[2] https://ors.brela.go.tz/orsreg/searchbusinesspublic#""",
        ),
    )
    TANZANIA_REVENUE_AGENCY = (
        "TZ-TRA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"The Tanzania Revenue Authority (TRA) was established by Act of Parliament No. 11 of 1995, and started its operations on 1st July 1996.  In carrying out its statutory functions, TRA is regulated by law, and is responsible for administering impartially various taxes of the Central Government.\"[1]

The Tanzanian Revenue Authority provides Taxpayer Identification Numbers (TIN) for organisations registered in Tanzania. This is issued under section 3A(4) of the Income Tax Act no. 33 of 1973. As amended by the financial laws (miscellaneous amendments) 2000.

There is no searchable database for TIN. It's possible that a company with a TIN could be on the Tanzanian Business Registrations and Licensing Agency (BRELA) Online Registration System, which can be searched free of charge. It is worth checking list TZ-BRLA before deciding to use this list.

[1]: https://www.tra.go.tz/index.php/about-tra/corporate-news

""",
        ),
    )
    UNITED_STATE_REGISTER = (
        "UA-EDR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Ministry of Justice hosts the United State Register for all corporate entities, individuals and community groups who are registered in Ukraine. Each corporate entity is assigned an identification code which can be used as a unique identifier.

The is a free search and a paid search of the database, and there is a third party search in Russian.

\"The Ministry of Justice of Ukraine introduced online service to obtain information from the Unified State Register of Legal Entities, individual entrepreneurs and community groups\" [1]

[1] https://usr.minjust.gov.ua/ua/home""",
        ),
    )
    NGO_BOARD__MINISTRY_OF_INTERNAL_AFFAIRS = (
        "UG-NGB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """All NGOs wishing to operate in Uganda must register with the NGO Board of the Ministry of Internal Affairs.

\"The National NGO Board under the Ministry of Internal Affairs, which is the lead Ministry, is legally mandated to register, regulate, coordinate and monitor NGOs in Uganda.\"""",
        ),
    )
    REGISTRATION_SERVICES_BUREAU = (
        "UG-RSB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Businesses and NGOs register with the Registration Services Bureau and receive an identification number. This number can be used as an identifier. A publicly available database can be search on the Bureau website.",
        ),
    )
    CORPORATION_REGISTRATION_IS_THE_RESPONSIBILITY_OF_EACH_STATE__SEE_LINK_ = (
        "US-DOS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This code was present in the IATI Organization Registration Agency codelist. It should no longer be used. ",
        ),
    )
    EMPLOYER_IDENTIFICATION_NUMBER_INTERNAL_REVENUE_SERVICE = (
        "US-EIN",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Internal Revenue Service (IRS) assigns companies an Employer Identification Number (EIN) upon application. However, not all corporate entities are required to have an EIN. For tax-exempt entities (non-profits, charities etc.) the IRS maintains a list of EINs. Public listed company EINs are available via the Securities and Exchange Commission (SEC).

Other EINs may be available by asking the organisation concerned, and are sometimes published on their websites.

\"An Employer Identification Number (EIN) is also known as a Federal Tax Identification Number, and is used to identify a business entity. Generally, businesses need an EIN. \" [1]

\"An employer identification number (EIN), also called a tax ID number or taxpayer ID, is required for most business entities... A tax ID number is not required if you operate a sole proprietorship or an LLC with no employees, in which case you would simply use your own Social Security Number as a tax ID.\" [2]

\"In the US, corporate registration happens at the state level. The timeliness, availability, and licensing of this data varies among all 50 states. There is no federal dataset that contains all corporate registrations. It would be possible to create a unified open registry for all US corporations (even if only via aggregation from state ones) but this does not exist at this time.

Across those states performance varies widely and in many cases data is not available in bulk, is not machine readable, is not openly licensed etc. For more detail, see the per state summary on Open Corporates.\" [3]

\"The Employer Identification Number (EIN), also known as the Federal Employer Identification Number (FEIN) or the Federal Tax Identification Number, is a unique nine-digit number assigned by the Internal Revenue Service (IRS) to business entities operating in the United States for the purposes of identification. When the number is used for identification rather than employment tax reporting, it is usually referred to as a Taxpayer Identification Number (TIN), and when used for the purposes of reporting employment taxes, it is usually referred to as an EIN. [4]

[1] https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers-eins
[2] http://tax.findlaw.com/federal-taxes/is-a-tax-id-required-for-my-business-.html
[3] https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers-eins
[4] https://en.wikipedia.org/wiki/Employer_Identification_Number""",
        ),
    )
    INDEX_OF_U_S__GOVERNMENT_DEPARTMENTS_AND_AGENCIES = (
        "US-USAGOV",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The U.S. Government website has an index of departments and agencies. This index can be searched, and the URL paths for agencies used to construct government agency identifiers.

""",
        ),
    )
    UNITED_STATE_REGISTER_OF_CORPORATE_ENTITES = (
        "UZ-KTUT",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "The State Statistics Committee of the Republic of Uzbekistan maintans the United State Register of Corporate Entites and organizations (Корхоналар ва ташкилотларнинг ягона давлат)",
        ),
    )
    EXAMPLE_DATA_PREFIX = (
        "XE-EXAMPLE",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "List code prefix reserved for use in example data which require a valid org-id.guide prefix (e.g. for use in data validator testing).",
        ),
    )
    ECONOMIC_OPERATORS_IDENTIFICATION_AND_REGISTRATION_SYSTEM = (
        "XI-EORI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "This site allows to validate EORI numbers and provides access to the information related to Authorised Economic Operators (AEO). An EORI number is unique throughout the EU, assigned by a customs authority in a member state to economic operators (businesses) or persons. ",
        ),
    )
    GLOBAL_RESEARCH_IDENTIFIERS_DATABASE = (
        "XI-GRID",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Global Research Identifiers Database collects information on research institutions and assigns them a unique identifier.

It draws on information from funding datasets, and claims over 90% coverage of institutions.

It records information on the nature of the research organisation, covering companies, education establishments, healthcare, non-profits, government and other entity types.

GRID also records parent-child relationships between entities, and 'related relationships' for cross-linkages.

It includes cross-linkages to a range of other identifier sources. """,
        ),
    )
    INTERNATIONAL_AID_TRANSPARENCY_INITIATIVE_ORGANISATION_IDENTIFIER = (
        "XI-IATI",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """XI-IATI is a list of organisation identifiers that is maintained by the IATI Secretariat. Any publisher may apply to the IATI Technical Team for an identifier to be generated.

\"If a bona fide organisation is not registered with any recognised or appropriate registration agency (http://iatistandard.org/202/codelists/OrganisationRegistrationAgency/) they should contact the IATI Technical Team who will exceptionally allocate an organisation identifier using the XI-IATI prefix.

While some of these identifiers have been derived from DAC codes, this ‘meaning’ is not carried forward. i.e. IATI generated identifiers have no intrinsic meaning.

For general guidance about constructing Organisation Identifiers, please see http://iatistandard.org/organisation-identifiers/\" [1]

[1] http://iatistandard.org/202/codelists/IATIOrganisationIdentifier/""",
        ),
    )
    PUBLIC_BODIES_OPEN_KNOWLEDGE_FOUNDATION = (
        "XI-PB",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Public Bodies is an Open Knowledge Foundation (OKF) project that aims to provide a unique ID for every part of every government. The main website is a portal for linking to profile pages for countries whose public bodies OKF has recorded. There are also links to directly download CSVs of this information.

Data available on the following countries/regions - Brazil, European Union, Germany, Greece, New Zealand, Switzerland, United Kingdom, United States """,
        ),
    )
    PERMID__THOMPSON_REUTERS_PERMANENT_IDENTIFIER = (
        "XI-PID",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Thomson Reuters Permanent Identifier (PermID) is a machine readable identifier that provides a unique reference for data item. PermID provides comprehensive identification across a wide variety of entity types including organizations, instruments, funds, issuers and people. PermID never changes and is unambiguous, making it ideal as a reference identifier.",
        ),
    )
    WIKIDATA = (
        "XI-WIKIDATA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            "Wikidata is a free knowledge base that anyone can edit. It holds linked open data about tens of millions of entities and more than one million of them are organizations. Each instition item can hold a wide range of statements, names in hundreds of languages and identifiers in other databases.",
        ),
    )
    OECD_DEVELOPMENT_ASSISTANCE_COMMITTEE = (
        "XM-DAC",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Organisation for Economic Co-operation and Development (OECD) Development Assistance Committee (DAC) has created a list of organisations whom are involved in the transfer of financial flows within the work of the OECD DAC. A list of all the Donors, Agencies and Recipients can be downloaded from the OECD website. This list is updated every three years.

See Donor, Agency and Delivery Channel codes.

\"The overarching objective of the DAC for 2011-2015  is to promote development co-operation and other policies so as to contribute to sustainable development, including pro-poor economic growth, poverty reduction, improvement of living standards in developing countries, and to a future in which no country will depend on aid.\" [1]

\"The DAC revises the list every three years. Countries that have exceeded the high-income threshold for three consecutive years at the time of the review are removed.\" [2]

[1] http://www.oecd.org/dac/thedevelopmentassistancecommitteesmandate.htm
[2] http://www.oecd.org/dac/stats/daclist.htm""",
        ),
    )
    UNITED_NATIONS_OFFICE_FOR_THE_COORDINATION_OF_HUMANITARIAN_AFFAIRS_FINANCIAL_TRACKING_SERVICES_IDENTIFIERS = (
        "XM-OCHA",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """OCHA (Office for the Coordination of Humanitarian Affairs) is the part of the United Nations Secretariat responsible for bringing together humanitarian actors to ensure a coherent response to emergencies.

The Financial Tracking Service assigns it's own organisation identifiers to parties involved in funding or delivery of humanitarian work, which are used in UN OCHA data, and may be used by some third-parties.

""",
        ),
    )
    NUTS_EUROPEAN_UNION_NOMENCLATURE_OF_TERRITORIAL_UNITS_FOR_STATISTICS = (
        "XR-NUTS",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The European Union's Nomenclature of Territorial Units for Statistics (NUTS) provides codes for territorial areas at a number of different levels.

Where no primary identifiers for regional and local government entities are available, then NUTS level 2 and 3 codes, and Local Administrative Unit (LAU 1 and LAU 2 level) codes could be used as a proxy for the primary local government body responsible for that area.

EuroStat currently maintain a cross-walk between different levels, codes and area names for each jurisdiction.

To construct an identifier:

For NUTS 2 and 3 codes, use the prefix (XR-NUTS-) and then the NUTS code provided.

For LAU1 and 2 codes (Local authority/ward), use the prefix (XR-NUTS-), the country prefix and underscore (e.g. UK_) , and then the LAU_NAT_Code provided (e.g. E05004874)

For example: XR-NUTS-UK_E07000105


""",
        ),
    )
    COMPANIES_AND_INTELLECTUAL_PROPERTY_COMMISSION__CIPC_ = (
        "ZA-CIP",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Companies and Intellectual Property Commission (CIPC) is responsible for company registration in South Africa. There is a basic free database search, or users can subscribe to the CIPC website.

\"Functions of the Commission

Registration of Companies, Co-operatives and Intellectual Property Rights (trade marks, patents, designs and copyright) and maintenance thereof
Disclosure of Information on its business registers\" [1]

[1] http://www.cipc.co.za/index.php/about/our-functions/""",
        ),
    )
    NONPROFIT_ORGANISATION_DIRECTORATE_SOUTH_AFRICAN_DEPARTMENT_OF_SOCIAL_DEVELOPMENT = (
        "ZA-NPO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Nonprofit Organisation Directorate is held under the South African Department of Social Development. NPOs register with the Nonprofit Organisation Directorate and are assigned a registration number. Users can refer to ZA-NPO for unique identifiers for NGOs in South Africa. The database can be searched for free.

Users should note that they should not include \"NPO\" to the end of the identifier.

\"The Nonprofit Organisations Directorate was established in terms of the Nonprofit Organisations Act 71 of 1997 to essentially administer the Register of Nonprofit Organisations in South Africa.

The Register of Nonprofit Organisations (NPOs) is a voluntary registration facility that enhances the credibility of the registered NPO as it reports to a public office. The NPO Directorate, as a public office, holds information about registered NPOs for the public to access. \" [1]

[1] http://www.dsd.gov.za/npo/""",
        ),
    )
    SA_REVENUE_SERVICE_TAX_EXEMPTION_UNIT = (
        "ZA-PBO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Non-profit organisations (NPOs) can apply for Public Benefit Organisation (PBO) status from the South Africa Revenue Service in order to become tax exempt. However, not all NPOs will be awarded this status, therefore the ZA-PBO should not be referred to as the Primary list of unique identifiers for NPOs in South Africa.

No searchable database of PBOs has been found.

\"The mere fact that an organisation has a non-profit motive or is established or registered as an NPO registered under the NPO Act, or is established as an NPC, does not mean that it automatically qualifies for preferential tax treatment or approval as a PBO.

An organisation will enjoy preferential tax treatment only after it has applied for and been granted approval as a PBO by the Commissioner, and continues to comply with the relevant prescribed requirements. \" [1]

[1] http://www.sars.gov.za/AllDocs/OpsDocs/Guides/LAPD-IT-G16%20-%20Basic%20Guide%20to%20Income%20Tax%20for%20Public%20Benefit%20Organisations%20-%20External%20Guide.pdf""",
        ),
    )
    PATENTS_AND_COMPANIES_REGISTRATION_AGENCY = (
        "ZM-PCR",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """The Patents and Companies Registration Agency (PACRA) is responsible for company registration in Zambia.

\"The Patents and Companies Registration Agency (PACRA) is a semi-autonomous executive agency of the Zambian Ministry of Commerce, Trade and Industry. Its principal functions are to operate a legal system for registration and protection of commercial and industrial property and to serve as a legal depository of the information tendered for registration..\" [1]

[1] https://www.pacra.org.zm/#/html/About/""",
        ),
    )
    PRIVATE_VOLUNTARY_ORGANISATIONS_COUNCIL__ZIMBABWE_ = (
        "ZW-PVO",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """\"NGOs in Zimbabwe are mainly registered under the Private Voluntary Organization Act (PVO Act). Registration is done through the Department of Social Welfare under the Ministry of Public Service Labour and Social Welfare.\" [1]

[1] http://www.kanokangalawfirm.net/setting-ngo-zimbabwe/""",
        ),
    )
    REGISTRAR_OF_DEEDS = (
        "ZW-ROD",
        pgettext_lazy(
            "IATI codelist OrganisationRegistrationAgency description",
            """Companies in Zimbabwe must register with the Registrar of Deeds.

Currently, all Zimbabwe government websites appear not to be working.

\"Reserve the company name with the Chief Registrar of Companies

Agency: Chief Registrar of Companies

Forms are available online but all documents must be physically lodged at Companies and Deeds Registry. The reservation is valid for 30 days and can be extended for another 30 days for an additional fee.\" [1]

[1] http://www.doingbusiness.org/data/exploreeconomies/zimbabwe#starting-a-business""",
        ),
    )
