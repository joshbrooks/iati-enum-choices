from django.db import models
from django.utils.translation import pgettext_lazy


class IATIOrganisationIdentifierDescription(models.TextChoices):
    """
    This is a list of organisation identifiers that is maintained by the IATI Secretariat. The prefix for organisations on this list is XI-IATI If a bona fide organisation is not registered with any recognised or appropriate registration agency (http://iatistandard.org/202/codelists/OrganisationRegistrationAgency/) they should contact the IATI Technical Team who will exceptionally allocate an organisation identifier using the XI-IATI prefix. While some of these identifiers have been derived from DAC codes, this 'meaning' is not carried forward. i.e. IATI generated identifiers have no intrinsic meaning. For general guidance about constructing Organisation Identifiers, please see http://iatistandard.org/organisation-identifiers/
    """

    THE_COCA_COLA_EXPORT_CORPORATION = (
        "XI-IATI-1001",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Subsidiary of The Coca-Cola Company responsible for marketing and export of soft drinks, bottled water, and other beverages and with links to the various charitable initiatives of The Coca-Cola Company, its subsidiaries and affiliates Coca-Cola charitable foundation. Based in Atlanta Georgia USA",
        ),
    )
    UNITED_MISSION_TO_NEPAL = (
        "XI-IATI-1002",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The United Mission to Nepal (UMN) is a faith based INGO based in Kathmandu, and has worked in Nepal without interruption since 1954. UMN works through local partners in order to serve the people of Nepal, especially the poorest of those living in poverty, to pursue peace and justice for all and to address the root causes of their poverty. We do this by supporting communities in a transformation process focusing on health, education, sustainable livelihoods, peace-building and good governance.",
        ),
    )
    ASSOCIATION_CENTRAFRICAINE_DE_TRADUCTION_DE_LA_BIBLE_ET_ALPHABETISATION = (
        "XI-IATI-ACATBA",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "ACATBA is a charity that exists to promote local language development, Bible translation, literacy and community development in the Central African Republic. They also provide training in basic business skills; this allows beneficiaries to begin income-generating activities and small businesses.",
        ),
    )
    AGÊNCIA_DE_DESENVOLVIMENTO_DO_VALE_DO_ZAMBEZE = (
        "XI-IATI-ADVZ",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            """Description:
                The Agência do Zambeze is a public-sector agency under the Ministry of Economics and Finance in Mozambique. The mission of the Agência do Zambeze is to promote the socio-economic and sustainable development of the Lower Zambezi River Basin.""",
        ),
    )
    AGRESULTS = (
        "XI-IATI-AGR",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "AgResults is a $122 million collaborative initiative between the governments of Australia, Canada, the United Kingdom, the United States, and the Bill and Melinda Gates Foundation to incentivize the private sector to overcome market barriers and develop solutions to food security and agricultural challenges that disproportionately affect people living in poverty. The initiative designs and implements agriculture-focused prize competitions, also referred to as pay-for-results or pull mechanisms, which are innovative development finance programs that engage the private sector to work towards a defined goal to receive a monetary award.",
        ),
    )
    ADMINISTRAÇÃO_DE_INFRA_ESTRUTURAS_DE_ÁGUAS_E_SANEAMENTO = (
        "XI-IATI-AIAS",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            """Description:
                AIAS manages the property of the secondary public systems for water supply and for the residual water drainage public systems in Mozambique promoting their autonomous efficient and financially feasible operational management through assignment to private operators or other third party entities.""",
        ),
    )
    ASSOCIATIONS_DES_JURISTES_SÉNÉGALAISES__AJS_ = (
        "XI-IATI-AJS",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Association des Juristes Sénégalaises (AJS) is an association of women lawyers who promote and contribute to the protection of the rights of individuals, particularly women and children.",
        ),
    )
    ASSOCIATION_OF_TECHNICIANS_IN_INFORMATION_TECHNOLOGY_AND_COMMUNICATION__ATTIC_ = (
        "XI-IATI-ATTIC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "ATTIC, a non-political non-profit association in Republic of Chad, aims to help develop and integrate the promotion of information and communication technologies in the development policy of the formal and non-formal sectors, to fight against food insecurity and poverty, by strengthening the means of vulnerable households, refugees, returnees and internally displaced persons, and by providing socio-professional training and integration for vulnerable groups.",
        ),
    )
    BANGLADESH_BUSINESS___DISABILITY_NETWORK = (
        "XI-IATI-BBDN",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Bangladesh Business and Disability Network (BBDN) is a voluntary group of representatives from business, industry, employers’ organizations and selected non-governmental and disabled peoples’ organizations. BBDN has a primary purpose of facilitating disability and work place diversity in Bangladesh from the perspective of the business and human rights cases.",
        ),
    )
    EUROPEAN_BANK_FOR_RECONSTRUCTION_AND_DEVELOPMENT = (
        "XI-IATI-EBRD",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            """Description:
                Who we are - The EBRD is investing in changing peoples' lives and environments from central Europe to Central Asia, the Western Balkans and the southern and eastern Mediterranean region. With an emphasis on working with the private sector, we invest in projects, engage in policy dialogue and provide  technical advice that fosters innovation and builds sustainable and open-market economies.
                What we do - The EBRD provides direct financing for well structured, financially robust projects of all sizes (including many small businesses), both directly and through financial intermediaries such as local banks and investment funds. The Bank works mainly with private sector clients, but also finances municipal entities and publicly owned companies. Our principal financing instruments are loans, equity investments and guarantees.""",
        ),
    )
    BENEDICTINE_EYE_HOSPITAL__TORORO = (
        "XI-IATI-BEH",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Benedictine Eye Hospital (BEH) is a Private Not-For-Profit specialised hospital established by the Benedictine Fathers of Uganda for providing Eye Care and Community Based Rehabilitation (CBR) services to Persons with Disabilities (PWDs), with special emphasis on children. The hospital is registered by the Ministry of Health and serves the people of Eastern Uganda but is increasingly receiving clients from the rest of the country and neighbouring countries.",
        ),
    )
    CABI = (
        "XI-IATI-CABI",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "CABI (Centre for Agriculture and Biosciences International) is an international not-for-profit organization that improves people’s lives worldwide by providing information and applying scientific expertise to solve problems in agriculture and the environment. It's approach involves putting information, skills and tools into people’s hands. CABI’s member countries guide and influence our work which is delivered by scientific staff based in our global network of centres.",
        ),
    )
    THE_COMMONWEALTH_SECRETARIAT = (
        "XI-IATI-CWSEC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Commonwealth is a voluntary association of 52 independent and equal sovereign states. Its guiding principles are contained in their Commonwealth Charter.",
        ),
    )
    DEMOCRATIC_GOVERNANCE_FACILITY = (
        "XI-IATI-DGF",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "DGF supports state and non state partners to strengthen democratisation, protect human rights, improve access to justice and enhance accountability in Uganda. DGF’s work is built upon the principles and values enshrined in Uganda’s 1995 Constitution and reiterated in its current National Development Plan.",
        ),
    )
    EUROPEAN_COMMISSION___DEVELOPMENT_AND_COOPERATION = (
        "XI-IATI-EC_DEVCO",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "DG DEVCO is in charge of development cooperation policy in a wider framework of international cooperation with developing countries at different stages of development. DG DEVCO is responsible for formulating European Union development policy and thematic policies in order to reduce poverty in the world, to ensure sustainable economic, social and environmental development and to promote democracy, the rule of law, good governance and the respect of human rights; the work is carried out closely with Member States, other Commission services, and with the European External Action Service.",
        ),
    )
    EUROPEAN_COMMISSION_HUMANITARIAN_AID___CIVIL_PROTECTION = (
        "XI-IATI-EC_ECHO",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Directorate General for Humanitarian aid and Civil Protection (ECHO) is responsible for formulating EU humanitarian aid policy, for programming and implementing the EU’s humanitarian aid budget and for supporting the central and overall coordinating role of the United Nations in promoting a coherent international response; ECHO also works closely with Member States' civil protection authorities to improve disaster prevention, preparedness and response and facilitates the cooperation between the 32 States participating in the Civil Protection Mechanism.",
        ),
    )
    ECONOMIC_AND_SOCIAL_FUND_FOR_DEVELOPMENT = (
        "XI-IATI-ESFD",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Economic and Social Fund for Development (ESFD) is a governmental body dedicated to alleviate poverty in Lebanon through the creation of employment opportunities and through the improvement of living conditions in disadvantaged communities.",
        ),
    )
    EUROPEAN_COMMISSION___SERVICE_FOR_FOREIGN_POLICY_INSTRUMENTS = (
        "XI-IATI-EC_FPI",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The core task of the Service for Foreign Policy Instruments (FPI) is to run a number of EU foreign policy actions, managing operations and their financing.  Such areas include crisis response and prevention measures financed under the Instrument contributing to Stability and Peace (IcSP); the Common Foreign and Security Policy (CFSP) budget; and the Partnership Instrument (PI), designed to promote the Union's strategic interests worldwide.",
        ),
    )
    EUROPEAN_COMMISSION_NEIGHBOURHOOD_AND_ENLARGEMENT_NEGOTIATIONS = (
        "XI-IATI-EC_NEAR",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The mission of DG NEAR is to take forward the EU's neighbourhood and enlargement policies, as well as coordinating relations with EEA-EFTA countries. By implementing assistance in Europe's eastern and southern neighbourhood, DG NEAR supports reform and democratic consolidation, and strengthens the prosperity, stability and security around Europe. In the enlargement area, DG NEAR assists those countries with a perspective to join the EU in meeting the criteria defined by the Treaty of European Union and the European Council.",
        ),
    )
    ENGAGE_FOUNDATION_FOR_RESEARCH_AND_DIALOGUE = (
        "XI-IATI-EFRD",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Engage Foundation for Research and Dialogue is a research and discourse generation collective that was established in 2015 and seeks to approach issues of human rights, citizenship and democratization in an interdisciplinary and inter-sectional manner with the hope that a nuanced and sensitive exploration of relevant issues will lead to engagement with an audience beyond the privileged English speaking minority of Pakistan. Engage attempts to present dense or overlooked subjects of public importance in captivating audio and visual formats with the hope that exposure to such subjects will lead to a broader public understanding of life in a modern democratic state.",
        ),
    )
    FEDERATION_OF_INSTITUTIONAL_ACTORS_BELGIUM__FIABEL_ = (
        "XI-IATI-FIABEL",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Fiabel is a federal association that connects Institutional Actors (IA) in Belgium. Fiabel supports her members by a) fulfilling a bridging function between the Belgian Development Cooperation and the Institutional Actors, to ensure that they are fully aware of the government legal framework, procedures and initiatives; b) representing the IA in various consultative committees with government bodies; c) setting up working groups to exchange knowledge and experiences; d) organizing trainings to strengthen the capacities of IA on strategic and operational level.",
        ),
    )
    GARGAAR_RELIEF_AND_DEVELOPMENT_ORGANIZATION = (
        "XI-IATI-GREDO",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "GREDO is a national NGO that is based in Baidoa which is the capital city of South West Administration of Somalia. It exists to support and reach the most affected grass-root communities in those regions and in Somalia at large. Our support focuses on Emergency and Development programs with a key thematic sectors of Integrated Health, Nutrition and Wash, Education and FSL.",
        ),
    )
    INTER_AMERICAN_DEVELOPMENT_BANK = (
        "XI-IATI-IADB",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Inter-American Development Bank works to improve lives in Latin America and the Caribbean. Through financial and technical support for countries working to reduce poverty and inequality, we help improve health and education, and advance infrastructure. Our aim is to achieve development in a sustainable, climate-friendly way.",
        ),
    )
    INTERNATIONAL_FERTILIZER_DEVELOPMENT_CENTER = (
        "XI-IATI-IFDC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Since 1974, IFDC has focused on increasing and sustaining food security and agricultural productivity in over 100 developing countries through the development and transfer of effective and environmentally sound crop nutrient technology and agribusiness expertise.",
        ),
    )
    INTERNATIONAL_CLIMATE_INITIATIVE__IKI_ = (
        "XI-IATI-IKI",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Since 2008, the International Climate Initiative (IKI) of the Federal Ministry for the Environment, Nature Conservation, Building and Nuclear Safety (BMUB) has been financing climate and biodiversity projects in developing and newly industrialising countries, as well as in countries in transition.",
        ),
    )
    THE_KING_HUSSEIN_FOUNDATION__KHF_ = (
        "XI-IATI-KHF",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Their mission is to build upon King Hussein’s lifelong commitment to peace, sustainable community development and cross-cultural understanding through national and regional programs that promote education and leadership, economic empowerment and participatory decision-making.",
        ),
    )
    LIVING_PEACE_INSTITUTE = (
        "XI-IATI-LPI",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Living Peace Institute (LPI) is a local NGO, based in Goma, Democratic Republic of Congo (DRC), and organized around the goal of achieving sustainable, gender-equitable peace at all levels of society in North and South Kivu regions of Eastern DRC.",
        ),
    )
    MULTILATERAL_INVESTMENT_FUND__MIF_ = (
        "XI-IATI-MIF",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Multilateral Investment Fund serves as an innovation laboratory to promote development through the private sector by identifying, supporting, testing and piloting new solutions to development challenges and seeking to create opportunities for the poor and vulnerable populations in the LAC region.",
        ),
    )
    NETHERLANDS_SPACE_OFFICE = (
        "XI-IATI-NSO",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The Netherlands Space Office (NSO) is the governmental space agency of the Netherlands. Its primary task is to develop and execute the national space policy. NSO is the main point of contact for national and international space affairs.",
        ),
    )
    UNITED_NATIONS_OFFICE_FOR_THE_COORDINATION_OF_HUMANITARIAN_AFFAIRS_SPECIALLY_DESIGNATED_CONTRIBUTIONS = (
        "XI-IATI-OCHASDC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The United Nations Office for the Coordination of Humanitarian Affairs (OCHA) is the part of the United Nations Secretariat responsible for bringing together humanitarian actors to ensure a coherent response to emergencies. OCHA’s activities are funded mostly through voluntary contributions from UN Member States, these contributions are reported under the IATI organisation ID XM-DAC-41127. OCHA also administers several Specially-Designated Contributions (SDCs) for projects implemented by third parties. Activities funded through SDCs will be reported under the IATI organisation ID XI-IATI-OCHASDC.",
        ),
    )
    SOMALI_GENDER_JUSTICE = (
        "XI-IATI-SGJ",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Somali Gender Justice is a small NGO based in Garowe, Puntland, Somalia whose goal is to support gender equality, women’s rights, and community transformation.",
        ),
    )
    SOMALI_WOMEN_STUDY_CENTRE = (
        "XI-IATI-SWSC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "SWSC is a women led NGO, founded in 2011 and based in Mogadishu and Kismayo, Somalia. SWSC seeks to achieve gender equality and social inclusion by empowering Somali women to exert their agency and improve their socio- economic status through strengthening their leadership, mentoring, capacity building, advocacy, and research to enable them articulate their specific needs in post- conflict Somalia.",
        ),
    )
    UMBRELLA_FOR_COMMUNITY_EDUCATION_IN_SOMALIA = (
        "XI-IATI-UCES",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "UCES is a national NGO that exists to work for advancement of Somalia Education by delivering formal and non-formal, alternative Education system to improve the knowledge of the Community through active advocacy and networking to deliver quality Education.",
        ),
    )
    UNITED_DARFUR_COMMITTEES = (
        "XI-IATI-UDC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "United Darfur Committees is a non-governmental and non-profit organization established by committees of seven villages in East Dafur State, Sudan, to solve community conflict and assist the people in need.",
        ),
    )
    UN_POOLED_FUNDS = (
        "XI-IATI-UNPF",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The UN pooled funds are a UN inter-agency financing mechanism with three characteristics. First, UN pooled funds are designed to support a clearly defined programmatic purpose and results framework through contributions that are co-mingled, not earmarked to a specific UN entity and held by a UN fund administrator. Second, decisions on project / programmatic allocations are made by a UN-led governance mechanism, taking into account the programmatic purpose and results framework of the fund. Third, fund implementation is (fully or largely) entrusted to UN entities that assume the programmatic and financial accountability for the resources received.",
        ),
    )
    WARDI_RELIEF_AND_DEVELOPMENT_INITIATIVE = (
        "XI-IATI-WARDI",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "WARDI is a national NGO that exists to collaborate and provide assistance in all relevant sectors to the Somali communities. The key thematic intervention areas are Emergency relief, Food security and livelihood, Wash, Health and Nutrition, Education and Peace building and governance.",
        ),
    )
    WASH_ALLIANCE_INTERNATIONAL = (
        "XI-IATI-WAI",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "The WASH Alliance International is a consortium of member organisations in the Netherlands and partner organisations worldwide, working on sustainable WASH for everyone.",
        ),
    )
    WORLD_BANK_TRUST_FUNDS__WBTF_ = (
        "XI-IATI-WBTF",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "A trust fund (TF) is a financing arrangement established with contributions from one or more external development partner(s)/partners, and in some cases, from the World Bank Group, to support development-related activities. The World Bank acts as a trustee/administrator for development partners (donors) funds and implements the activities financed through trust funds in accordance with the signed agreements with donors. As part of fiduciary obligations, the World Bank as Trustee/administrator of trust funds maintains the records for trust funds activities distinct and separate from the activities of IBRD and IDA. The Bank also provides periodic report on the financial situation and results of the individual trust funds to donors.",
        ),
    )
    WORLD_VISION_DRC = (
        "XI-IATI-WVDRC",
        pgettext_lazy(
            "IATIOrganisationIdentifier description",
            "Our teams have been working in the DRC since 1984. Today, we are working to contribute to the measurable and sustainable improvement of well-being for 5,311,208 children and their communities through transformational development and humanitarian relief programmes focused on: health and nutrition, education, water and sanitation, protecting children, livelihoods and resilience, food aid, psychosocial support and the reintegration if displaced people.",
        ),
    )
