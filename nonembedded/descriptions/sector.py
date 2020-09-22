from django.db import models
from django.utils.translation import pgettext_lazy


class SectorDescription(models.IntegerChoices):
    EDUCATION_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        11110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Education sector policy, planning and programmes; aid to education ministries, administration and management systems; institution capacity building and advice; school management and governance; curriculum and materials development; unspecified education activities.",
        ),
    )
    EDUCATION_FACILITIES_AND_TRAINING = (
        11120,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Educational buildings, equipment, materials; subsidiary services to education (boarding facilities, staff housing); language training; colloquia, seminars, lectures, etc.",
        ),
    )
    TEACHER_TRAINING = (
        11130,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Teacher education (where the level of education is unspecified); in-service and pre-service training; materials development.",
        ),
    )
    EDUCATIONAL_RESEARCH = (
        11182,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Research and studies on education effectiveness, relevance and quality; systematic evaluation and monitoring.",
        ),
    )
    PRIMARY_EDUCATION = (
        11220,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Formal and non-formal primary education for children; all elementary and first cycle systematic instruction; provision of learning materials.",
        ),
    )
    BASIC_LIFE_SKILLS_FOR_YOUTH_AND_ADULTS = (
        11230,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Formal and non-formal education for basic life skills for young people and adults (adults education); literacy and numeracy training. Excludes health education (12261) and activities related to prevention of noncommunicable diseases. (123xx).",
        ),
    )
    BASIC_LIFE_SKILLS_FOR_YOUTH = (
        11231,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Formal and non-formal education for basic life skills for young people.",
        ),
    )
    PRIMARY_EDUCATION_EQUIVALENT_FOR_ADULTS = (
        11232,
        pgettext_lazy(
            "IATI codelist Sector description", "Formal primary education for adults."
        ),
    )
    EARLY_CHILDHOOD_EDUCATION = (
        11240,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Formal and non-formal pre-school education.",
        ),
    )
    SCHOOL_FEEDING = (
        11250,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Provision of meals or snacks at school; other uses of food for the achievement of educational outcomes including “take-home” food rations provided as economic incentives to families (or foster families, or other child care institutions) in return for a child’s regular attendance at school; food provided to adults or youth who attend literacy or vocational training programmes; food for pre-school activities with an educational component. These activities may help reduce children’s hunger during the school day if provision of food/meals contains bioavailable nutrients to address specific nutrition needs and have nutrition expected outcomes in school children, or if the rationale mainstream nutrition or expected outcome is nutrition-linked.",
        ),
    )
    SECONDARY_EDUCATION = (
        11320,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Second cycle systematic instruction at both junior and senior levels.",
        ),
    )
    LOWER_SECONDARY_EDUCATION = (
        11321,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Second cycle systematic instruction at junior level.",
        ),
    )
    UPPER_SECONDARY_EDUCATION = (
        11322,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Second cycle systematic instruction at senior level.",
        ),
    )
    VOCATIONAL_TRAINING = (
        11330,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Elementary vocational training and secondary level technical education; on-the job training; apprenticeships; including informal vocational training.",
        ),
    )
    HIGHER_EDUCATION = (
        11420,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Degree and diploma programmes at universities, colleges and polytechnics; scholarships.",
        ),
    )
    ADVANCED_TECHNICAL_AND_MANAGERIAL_TRAINING = (
        11430,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Professional-level vocational training programmes and in-service training.",
        ),
    )
    HEALTH_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        12110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Health sector policy, planning and programmes; aid to health ministries, public health administration; institution capacity building and advice; medical insurance programmes; including health system strengthening and health governance; unspecified health activities.",
        ),
    )
    MEDICAL_EDUCATION_TRAINING = (
        12181,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Medical education and training for tertiary level services.",
        ),
    )
    MEDICAL_RESEARCH = (
        12182,
        pgettext_lazy(
            "IATI codelist Sector description",
            "General medical research (excluding basic health research and research for prevention and control of NCDs (12382)).",
        ),
    )
    MEDICAL_SERVICES = (
        12191,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Laboratories, specialised clinics and hospitals (including equipment and supplies); ambulances; dental services; medical rehabilitation. Excludes noncommunicable diseases (123xx).",
        ),
    )
    HEALTH_STATISTICS_AND_DATA = (
        12196,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Collection, production, management and dissemination of statistics and data related to health. Includes health surveys, establishment of health databases, data collection on epidemics, etc.",
        ),
    )
    BASIC_HEALTH_CARE = (
        12220,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Basic and primary health care programmes; paramedical and nursing care programmes; supply of drugs, medicines and vaccines related to basic health care; activities aimed at achieving universal health coverage.",
        ),
    )
    BASIC_HEALTH_INFRASTRUCTURE = (
        12230,
        pgettext_lazy(
            "IATI codelist Sector description",
            "District-level hospitals, clinics and dispensaries and related medical equipment; excluding specialised hospitals and clinics (12191).",
        ),
    )
    BASIC_NUTRITION = (
        12240,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Micronutrient deficiency identification and supplementation; Infant and young child feeding promotion including exclusive breastfeeding; Non-emergency management of acute malnutrition and other targeted feeding programs (including complementary feeding); Staple food fortification including salt iodization; Nutritional status monitoring and national nutrition surveillance; Research, capacity building, policy development, monitoring and evaluation in support of these interventions.  Use code 11250 for school feeding and 43072 for household food security.",
        ),
    )
    INFECTIOUS_DISEASE_CONTROL = (
        12250,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Immunisation; prevention and control of infectious and parasite diseases, except malaria (12262), tuberculosis (12263), HIV/AIDS and other STDs (13040). It includes diarrheal diseases, vector-borne diseases (e.g. river blindness and guinea worm), viral diseases, mycosis, helminthiasis, zoonosis, diseases by other bacteria and viruses, pediculosis, etc.",
        ),
    )
    HEALTH_EDUCATION = (
        12261,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Information, education and training of the population for improving health knowledge and practices; public health and awareness campaigns; promotion of improved personal hygiene practices, including use of sanitation facilities and handwashing with soap.",
        ),
    )
    MALARIA_CONTROL = (
        12262,
        pgettext_lazy(
            "IATI codelist Sector description", "Prevention and control of malaria."
        ),
    )
    TUBERCULOSIS_CONTROL = (
        12263,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Immunisation, prevention and control of tuberculosis.",
        ),
    )
    HEALTH_PERSONNEL_DEVELOPMENT = (
        12281,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Training of health staff for basic health care services.",
        ),
    )
    NCDS_CONTROL__GENERAL = (
        12310,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Programmes for the prevention and control of NCDs which cannot be broken down into the codes below.",
        ),
    )
    TOBACCO_USE_CONTROL = (
        12320,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Population/individual measures and interventions to reduce all forms of tobacco use in any form. Includes activities related to the implementation of the WHO Framework Convention on Tobacco Control, including specific high-impact demand reduction measures for effective tobacco control.",
        ),
    )
    CONTROL_OF_HARMFUL_USE_OF_ALCOHOL_AND_DRUGS = (
        12330,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Prevention and reduction of harmful use of alcohol and psychoactive drugs; development, implementation, monitoring and evaluation of prevention and treatment strategies, programmes and interventions; early identification and management of health conditions caused by use of alcohol and drugs [excluding narcotics traffic control (16063)].",
        ),
    )
    PROMOTION_OF_MENTAL_HEALTH_AND_WELL_BEING = (
        12340,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Promotion of programmes and interventions which support mental health and well-being resiliency; prevention, care and support to individuals vulnerable to suicide. Excluding treatment of addiction to tobacco, alcohol and drugs (included in codes 12320 and 12330).",
        ),
    )
    OTHER_PREVENTION_AND_TREATMENT_OF_NCDS = (
        12350,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Population/individual measures to reduce exposure to unhealthy diets and physical inactivity and to strengthen capacity for prevention, early detection, treatment and sustained management of NCDs including:  Cardiovascular disease control: Prevention, screening and treatment of cardiovascular diseases (including hypertension, hyperlipidaemia, ischaemic heart diseases, stroke, rheumatic heart disease, congenital heart disease, heart failure, etc.).   Diabetes control: Prevention, screening, diagnosis, treatment and management of complications from all types of diabetes.  Exposure to physical inactivity: Promotion of physical activity through supportive built environment (urban design, transport), sports, health care, schools and community programmes and mass media campaign.  Exposure to unhealthy diet: Programmes and interventions that promote healthy diet through reduced consumption of salt, sugar and fats and increased consumption of fruits and vegetables e.g. food reformulation, nutrient labelling, food taxes, marketing restriction on unhealthy foods, nutrition education and counselling, and settings-based interventions (schools, workplaces, villages, communities).  Cancer control: Prevention (including immunisation, HPV and HBV), early diagnosis (including pathology), screening, treatment (e.g. radiotherapy, chemotherapy, surgery) and palliative care for all types of cancers. Implementation, maintenance and improvement of cancer registries are also included.  Chronic respiratory diseases: Prevention, early diagnosis and treatment of chronic respiratory diseases, including asthma. Excludes: Tobacco use control (12320), Control of harmful use of alcohol and drugs (12330), research for the prevention and control of NCDs (12382).",
        ),
    )
    RESEARCH_FOR_PREVENTION_AND_CONTROL_OF_NCDS = (
        12382,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Research to enhance understanding of NCDs, their risk factors, epidemiology, social determinants and economic impact; translational and implementation research to enhance operationalisation of cost-effective strategies to prevent and control NCDs; surveillance and monitoring of NCD mortality, morbidity, risk factor exposures, and national capacity to prevent and control NCDs.",
        ),
    )
    POPULATION_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        13010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Population/development policies; demographic research/analysis; reproductive health research; unspecified population activities. (Use purpose code 15190 for data on migration and refugees. Use code 13096 for census work, vital registration and migration data collection.)",
        ),
    )
    REPRODUCTIVE_HEALTH_CARE = (
        13020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Promotion of reproductive health; prenatal and postnatal care including delivery; prevention and treatment of infertility; prevention and management of consequences of abortion; safe motherhood activities.",
        ),
    )
    FAMILY_PLANNING = (
        13030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Family planning services including counselling; information, education and communication (IEC) activities; delivery of contraceptives; capacity building and training.",
        ),
    )
    STD_CONTROL_INCLUDING_HIV_AIDS = (
        13040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "All activities related to sexually transmitted diseases and HIV/AIDS control e.g. information, education and communication; testing; prevention; treatment, care.",
        ),
    )
    PERSONNEL_DEVELOPMENT_FOR_POPULATION_AND_REPRODUCTIVE_HEALTH = (
        13081,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Education and training of health staff for population and reproductive health care services.",
        ),
    )
    POPULATION_STATISTICS_AND_DATA = (
        13096,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Collection, production, management and dissemination of statistics and data related to Population and Reproductive Health. Includes census work, vital registration, migration data collection, demographic data, etc.",
        ),
    )
    WATER_SECTOR_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        14010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Water sector policy and governance, including legislation, regulation, planning and management as well as transboundary management of water; institutional capacity development; activities supporting the Integrated Water Resource Management approach (IWRM:  see box below).",
        ),
    )
    WATER_RESOURCES_CONSERVATION__INCLUDING_DATA_COLLECTION_ = (
        14015,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Collection and usage of quantitative and qualitative data on water resources; creation and sharing of water knowledge; conservation and rehabilitation of inland surface waters (rivers, lakes etc.), ground water and coastal waters; prevention of water contamination.",
        ),
    )
    WATER_SUPPLY_AND_SANITATION_LARGE_SYSTEMS = (
        14020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Programmes where components according to 14021 and 14022 cannot be identified.  When components are known, they should individually be reported under their respective purpose codes:  water supply [14021], sanitation [14022], and hygiene [12261].",
        ),
    )
    WATER_SUPPLY_LARGE_SYSTEMS = (
        14021,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Potable water treatment plants; intake works; storage; water supply pumping stations; large scale transmission / conveyance and distribution systems.",
        ),
    )
    SANITATION_LARGE_SYSTEMS = (
        14022,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Large scale sewerage including trunk sewers and sewage pumping stations; domestic and industrial waste water treatment plants.",
        ),
    )
    BASIC_DRINKING_WATER_SUPPLY_AND_BASIC_SANITATION = (
        14030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Programmes where components according to 14031 and 14032 cannot be identified.  When components are known, they should individually be reported under their respective purpose codes:  water supply [14031], sanitation [14032], and hygiene [12261].",
        ),
    )
    BASIC_DRINKING_WATER_SUPPLY = (
        14031,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Rural water supply schemes using handpumps, spring catchments, gravity-fed systems, rainwater collection and fog harvesting, storage tanks, small distribution systems typically with shared connections/points of use. Urban schemes using handpumps and local neighbourhood networks including those with shared connections.",
        ),
    )
    BASIC_SANITATION = (
        14032,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Latrines, on-site disposal and alternative sanitation systems, including the promotion of household and community investments in the construction of these facilities. (Use code 12261 for activities promoting improved personal hygiene practices.)",
        ),
    )
    RIVER_BASINS_DEVELOPMENT = (
        14040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Infrastructure-focused integrated river basin projects and related institutional activities; river flow control; dams and reservoirs [excluding dams primarily for irrigation (31140) and hydropower (23220) and activities related to river transport (21040)].",
        ),
    )
    WASTE_MANAGEMENT_DISPOSAL = (
        14050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Municipal and industrial solid waste management, including hazardous and toxic waste; collection, disposal and treatment; landfill areas; composting and reuse.",
        ),
    )
    EDUCATION_AND_TRAINING_IN_WATER_SUPPLY_AND_SANITATION = (
        14081,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Education and training for sector professionals and service providers.",
        ),
    )
    PUBLIC_SECTOR_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        15110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Institution-building assistance to strengthen core public sector management systems and capacities. This includes general public policy management, co-ordination, planning and reform; human resource management; organisational development; civil service reform; e-government; development planning, monitoring and evaluation; support to ministries involved in aid co-ordination; other ministries and government departments when sector cannot be specified. (Use specific sector codes for development of systems and capacities in sector ministries. For macro-economic policy use code 15142. For public procurement use code 15125.)",
        ),
    )
    PUBLIC_FINANCE_MANAGEMENT__PFM_ = (
        15111,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Fiscal policy and planning; support to ministries of finance; strengthening financial and managerial accountability; public expenditure management; improving financial management systems; budget drafting; inter-governmental fiscal relations, public audit, public debt. (Use code 15114 for domestic revenue mobilisation and code 33120 for customs).",
        ),
    )
    DECENTRALISATION_AND_SUPPORT_TO_SUBNATIONAL_GOVERNMENT = (
        15112,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Decentralisation processes (including political, administrative and fiscal dimensions); intergovernmental relations and federalism; strengthening departments of regional and local government, regional and local authorities and their national associations. (Use specific sector codes for decentralisation of sector management and services.)",
        ),
    )
    ANTICORRUPTION_ORGANISATIONS_AND_INSTITUTIONS = (
        15113,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Specialised organisations, institutions and frameworks for the prevention of and combat against corruption, bribery, money-laundering and other aspects of organised crime, with or without law enforcement powers, e.g. anti-corruption commissions and monitoring bodies, special investigation services, institutions and initiatives of integrity and ethics oversight, specialised NGOs, other civil society and citizens’ organisations directly concerned with corruption.",
        ),
    )
    DOMESTIC_REVENUE_MOBILISATION = (
        15114,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to domestic revenue mobilisation/tax policy, analysis and administration as well as non-tax public revenue, which includes work with ministries of finance, line ministries, revenue authorities or other local, regional or national public bodies. (Use code 16010 for social security and other social protection.)",
        ),
    )
    TAX_COLLECTION = (
        15116,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation of the inland revenue authority.",
        ),
    )
    BUDGET_PLANNING = (
        15117,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation of the budget office and planning as part of the budget process.",
        ),
    )
    NATIONAL_AUDIT = (
        15118,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation of the accounting and audit services.",
        ),
    )
    DEBT_AND_AID_MANAGEMENT = (
        15119,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Management of public debt and foreign aid received (in the partner country). For reporting on debt reorganisation, use codes 600xx.",
        ),
    )
    PUBLIC_SECTOR_FINANCIAL_MANAGEMENT = (
        15120,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Strengthening financial and managerial accountability; public expenditure management; improving financial management systems; tax assessment procedures; budget drafting; field auditing; measures against waste, fraud and corruption.",
        ),
    )
    FOREIGN_AFFAIRS = (
        15121,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Administration of external affairs and services.",
        ),
    )
    DIPLOMATIC_MISSIONS = (
        15122,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation of diplomatic and consular missions stationed abroad or at offices of international organisations.",
        ),
    )
    ADMINISTRATION_OF_DEVELOPING_COUNTRIES__FOREIGN_AID = (
        15123,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to administration of developing countries' foreign aid (including triangular and south-south cooperation).",
        ),
    )
    GENERAL_PERSONNEL_SERVICES = (
        15124,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Administration and operation of the civil service including policies, procedures and regulations.",
        ),
    )
    PUBLIC_PROCUREMENT = (
        15125,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to public procurement, including to create and evaluate legal frameworks; advice in establishing strategic orientation of public procurement policies and reforms; advice in designing public procurement systems and processes; support to public procurement institutions (including electronic procurement) as well as structures or initiatives to assess public procurement systems; and development of professional capacity of public procurement bodies and staff.",
        ),
    )
    OTHER_GENERAL_PUBLIC_SERVICES = (
        15126,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Maintenance and storage of government records and archives, operation of government-owned or occupied buildings, central motor vehicle pools, government-operated printing offices, centralised computer and data processing services, etc.",
        ),
    )
    NATIONAL_MONITORING_AND_EVALUATION = (
        15127,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation or support of institutions providing national monitoring and evaluation.",
        ),
    )
    LOCAL_GOVERNMENT_FINANCE = (
        15128,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Financial transfers to local government; support to institutions managing such transfers. (Use specific sector codes for sector-related transfers.)",
        ),
    )
    OTHER_CENTRAL_TRANSFERS_TO_INSTITUTIONS = (
        15129,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Transfers to non sector-specific autonomous bodies or state-owned enterprises outside of local government finance; support to institutions managing such transfers. (Use specific sector codes for sector-related transfers.)",
        ),
    )
    LEGAL_AND_JUDICIAL_DEVELOPMENT = (
        15130,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to institutions, systems and procedures of the justice sector, both formal and informal; support to ministries of justice, the interior and home affairs; judges and courts; legal drafting services; bar and lawyers associations; professional legal education; maintenance of law and order and public safety; border management; law enforcement agencies, police, prisons and their supervision; ombudsmen; alternative dispute resolution, arbitration and mediation; legal aid and counsel; traditional, indigenous and paralegal practices that fall outside the formal legal system. Measures that support the improvement of legal frameworks, constitutions, laws and regulations; legislative and constitutional drafting and review; legal reform; integration of formal and informal systems of law. Public legal education; dissemination of information on entitlements and remedies for injustice; awareness campaigns. (Use codes 152xx for activities that are primarily aimed at supporting security system reform or undertaken in connection with post-conflict and peace building activities. Use code 15190 for capacity building in border management related to migration.)",
        ),
    )
    JUSTICE__LAW_AND_ORDER_POLICY__PLANNING_AND_ADMINISTRATION = (
        15131,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Judicial law and order sectors; policy development within ministries of justice or equivalents.",
        ),
    )
    POLICE = (
        15132,
        pgettext_lazy(
            "IATI codelist Sector description", "Police affairs and services."
        ),
    )
    FIRE_AND_RESCUE_SERVICES = (
        15133,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Fire-prevention and fire-fighting affairs and services.",
        ),
    )
    JUDICIAL_AFFAIRS = (
        15134,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Civil and criminal law courts and the judicial system, including enforcement of fines and legal settlements imposed by the courts and operation of parole and probation systems.",
        ),
    )
    OMBUDSMAN = (
        15135,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Independent service representing the interests of the public by investigating and addressing complaints of unfair treatment or maladministration.",
        ),
    )
    IMMIGRATION = (
        15136,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Immigration affairs and services, including alien registration, issuing work and travel documents to immigrants.",
        ),
    )
    GOVERNMENT_ADMINISTRATION = (
        15140,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Systems of government including parliament, local government, decentralisation; civil service and civil service reform. Including general services by government (or commissioned by government) not elsewhere specified e.g. police, fire protection; cartography, meteorology, legal metrology, aerial surveys and remote sensing; administrative buildings.",
        ),
    )
    MACROECONOMIC_POLICY = (
        15142,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to macroeconomic stability, debt sustainability and structural reforms. Includes technical assistance for strategic formulation of policies, laws and regulation; capacity building to enhance public sector development; policy-based funding. For fiscal policy and domestic revenue mobilisation use codes 15111 and 15114.",
        ),
    )
    METEOROLOGICAL_SERVICES = (
        15143,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation or support of institutions dealing with weather forecasting.",
        ),
    )
    NATIONAL_STANDARDS_DEVELOPMENT = (
        15144,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Operation or support of institutions dealing with national standards development. (Use code 16062 for statistical capacity-building.)",
        ),
    )
    DEMOCRATIC_PARTICIPATION_AND_CIVIL_SOCIETY = (
        15150,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to the exercise of democracy and diverse forms of participation of citizens beyond elections (15151); direct democracy instruments such as referenda and citizens’ initiatives; support to organisations to represent and advocate for their members, to monitor, engage and hold governments to account, and to help citizens learn to act in the public sphere; curricula and teaching for civic education at various levels. (This purpose code is restricted to activities targeting governance issues. When assistance to civil society is for non-governance purposes use other appropriate purpose codes.)",
        ),
    )
    ELECTIONS = (
        15151,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Electoral management bodies and processes, election observation, voters' education. (Use code 15230 when in the context of an international peacekeeping operation.)",
        ),
    )
    LEGISLATURES_AND_POLITICAL_PARTIES = (
        15152,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Assistance to strengthen key functions of legislatures/ parliaments including subnational assemblies and councils (representation; oversight; legislation), such as improving the capacity of legislative bodies, improving legislatures’ committees and administrative procedures,; research and information management systems; providing training programmes for legislators and support personnel. Assistance to political parties and strengthening of party systems.",
        ),
    )
    MEDIA_AND_FREE_FLOW_OF_INFORMATION = (
        15153,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Activities that support free and uncensored flow of information on public issues; activities that increase the editorial and technical skills and the integrity of the print and broadcast media, e.g. training of journalists. (Use codes 22010-22040 for provision of equipment and capital assistance to media.)",
        ),
    )
    EXECUTIVE_OFFICE = (
        15154,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Administration, operation or support of executive office. Includes office of the chief executive at all levels of government (monarch, governor-general, president, prime minister, governor, mayor, etc.).",
        ),
    )
    OTHER_NON_TAX_REVENUE_MOBILISATION = (
        15156,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Non-tax public revenue, which includes line ministries, revenue authorities or other local, regional or national public bodies.",
        ),
    )
    HUMAN_RIGHTS = (
        15160,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Measures to support specialised official human rights institutions and mechanisms at universal, regional, national and local levels in their statutory roles to promote and protect civil and political, economic, social and cultural rights as defined in international conventions and covenants; translation of international human rights commitments into national legislation; reporting and follow-up; human rights dialogue. Human rights defenders and human rights NGOs; human rights advocacy, activism, mobilisation; awareness raising and public human rights education. Human rights programming targeting specific groups, e.g. children, persons with disabilities, migrants, ethnic, religious, linguistic and sexual minorities, indigenous people and those suffering from caste discrimination, victims of trafficking, victims of torture. (Use code 15230 when in the context of a peacekeeping operation and code 15180 for ending violence against women and girls. Use code 15190 for human rights programming for refugees or migrants, including when they are victims of trafficking.Use code 16070 for Fundamental Principles and Rights at Work, i.e. Child Labour, Forced Labour, Non-discrimination in employment and occupation, Freedom of Association and Collective Bargaining.)",
        ),
    )
    ELECTIONS = (
        15161,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Electoral assistance and monitoring, voters' education [other than in connection with UN peace building (15230)].",
        ),
    )
    HUMAN_RIGHTS = (
        15162,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Monitoring of human rights performance; support for national and regional human rights bodies; protection of ethnic, religious and cultural minorities [other than in connection with un peace building (15230)].",
        ),
    )
    FREE_FLOW_OF_INFORMATION = (
        15163,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Uncensored flow of information on public issues, including activities that increase the professionalism, skills and integrity of the print and broadcast media (e.g. training of journalists).",
        ),
    )
    WOMEN_S_EQUALITY_ORGANISATIONS_AND_INSTITUTIONS = (
        15164,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support for institutions and organisations (governmental and non-governmental) working for gender equality and women's empowerment.",
        ),
    )
    WOMEN_S_RIGHTS_ORGANISATIONS_AND_MOVEMENTS__AND_GOVERNMENT_INSTITUTIONS = (
        15170,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support for feminist, women-led and women’s rights organisations and movements, and institutions (governmental and non-govermental) at all levels to enhance their effectiveness, influence and substainability (activities and core-funding). These organisations exist to bring about transformative change for gender equality and/or the rights of women and girls in developing countries. Their activities include agenda-setting, advocacy, policy dialogue, capacity development, awareness raising and prevention, service provision, conflict-prevention and peacebuilding, research, organising, and alliance and network building",
        ),
    )
    ENDING_VIOLENCE_AGAINST_WOMEN_AND_GIRLS = (
        15180,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to programmes designed to prevent and eliminate all forms of violence against women and girls/gender-based violence. This encompasses a broad range of forms of physical, sexual and psychological violence including but not limited to: intimate partner violence (domestic violence); sexual violence; female genital mutilation/cutting (FGM/C); child, early and forced marriage; acid throwing; honour killings; and trafficking of women and girls. Prevention activities may include efforts to empower women and girls; change attitudes, norms and behaviour; adopt and enact legal reforms; and strengthen implementation of laws and policies on ending violence against women and girls, including through strengthening institutional capacity. Interventions to respond to violence against women and girls/gender-based violence may include expanding access to services including legal assistance, psychosocial counselling and health care; training personnel to respond more effectively to the needs of survivors; and ensuring investigation, prosecution and punishment of perpetrators of violence.",
        ),
    )
    LOCAL_GOVERNMENT_ADMINISTRATION = (
        15185,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Decentralisation processes (including political, administrative and fiscal dimensions); intergovernmental relations and federalism; strengthening local authorities.",
        ),
    )
    FACILITATION_OF_ORDERLY__SAFE__REGULAR_AND_RESPONSIBLE_MIGRATION_AND_MOBILITY = (
        15190,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Assistance to developing countries that facilitates the orderly, safe, regular and responsible migration and mobility of people. This includes:• Capacity building in migration and mobility policy, analysis, planning and management. This includes support to facilitate safe and regular migration and address irregular migration, engagement with diaspora and programmes enhancing the development impact of remittances and/or their use for developmental projects in developing countries.• Measures to improve migrant labour recruitment systems in developing countries.• Capacity building for strategy and policy development as well as legal and judicial development (including border management) in developing countries. This includes support to address and reduce vulnerabilities in migration, and strengthen the transnational response to smuggling of migrants and preventing and combating trafficking in human beings.• Support to effective strategies to ensure international protection and the right to asylum.• Support to effective strategies to ensure access to justice and assistance for displaced persons.• Assistance to migrants for their safe, dignified, informed and voluntary return to their country of origin (covers only returns from another developing country; assistance to forced returns is excluded from ODA).• Assistance to migrants for their sustainable reintegration in their country of origin (use code 93010 for pre-departure assistance provided in donor countries in the context of voluntary returns). Activities that pursue first and foremost providers’ interest are excluded from ODA. Activities addressing the root causes of forced displacement and irregular migration should not be coded here, but under their relevant sector of intervention. In addition, use code 15136 for support to countries' authorities for immigration affairs and services (optional), code 24050 for programmes aiming at reducing the sending costs of remittances, code 72010 for humanitarian aspects of assistance to refugees and internally displaced persons (IDPs) such as delivery of emergency services and humanitarian protection. Use code 93010 when expenditure is for the temporary sustenance of refugees in the donor country, including for their voluntary return and for their reintegration when support is provided in a donor country in connection with the return from that donor country (i.e. pre-departure assistance), or voluntary resettlement in a third developed country.",
        ),
    )
    GOVERNMENT_AND_CIVIL_SOCIETY_STATISTICS_AND_DATA = (
        15196,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Collection, production, management and dissemination of statistics and data related to Government & Civil Society. Includes macroeconomic statistics, government finance, fiscal and public sector statistics, support to development of administrative data infrastructure, civil society surveys.",
        ),
    )
    SECURITY_SYSTEM_MANAGEMENT_AND_REFORM = (
        15210,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Technical co-operation provided to parliament, government ministries, law enforcement agencies and the judiciary to assist review and reform of the security system to improve democratic governance and civilian control; technical co-operation provided to government to improve civilian oversight and democratic control of budgeting, management, accountability and auditing of security expenditure, including military budgets, as part of a public expenditure management programme; assistance to civil society to enhance its competence and capacity to scrutinise the security system so that it is managed in accordance with democratic norms and principles of accountability, transparency and good governance. [Other than in the context of an international peacekeeping operation (15230)].",
        ),
    )
    CIVILIAN_PEACE_BUILDING__CONFLICT_PREVENTION_AND_RESOLUTION = (
        15220,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support for civilian activities related to peace building, conflict prevention and resolution, including capacity building, monitoring, dialogue and information exchange. Bilateral participation in international civilian peace missions such as those conducted by the UN Department of Political Affairs (UNDPA) or the European Union (European Security and Defence Policy), and contributions to civilian peace funds or commissions (e.g. Peacebuilding Commission, Peacebuilding thematic window of the MDG achievement fund etc.). The contributions can take the form of financing or provision of equipment or civilian or military personnel (e.g. for training civilians).(Use code 15230 for bilateral participation in international peacekeeping operations).",
        ),
    )
    PARTICIPATION_IN_INTERNATIONAL_PEACEKEEPING_OPERATIONS = (
        15230,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Bilateral participation in peacekeeping operations mandated or authorised by the United Nations (UN) through Security Council resolutions, and conducted by international organisations, e.g. UN, NATO, the European Union (Security and Defence Policy security-related operations), or regional groupings of developing countries. Direct contributions to the UN Department for Peacekeeping Operations (UNDPKO) budget are excluded from bilateral ODA (they are reportable in part as multilateral ODA, see Annex 9). The activities that can be reported as bilateral ODA under this code are limited to: human rights and election monitoring; reintegration of demobilised soldiers; rehabilitation of basic national infrastructure; monitoring or retraining of civil administrators and police forces; security sector reform and other rule of law-related activities; training in customs and border control procedures; advice or training in fiscal or macroeconomic stabilisation policy; repatriation and demobilisation of armed factions, and disposal of their weapons; explosive mine removal. The enforcement aspects of international peacekeeping operations are not reportable as ODA. ODA-eligible bilateral participation in peacekeeping operations can take the form of financing or provision of equipment or military or civilian personnel (e.g. police officers). The reportable cost is calculated as the excess over what the personnel and equipment would have cost to maintain had they not been assigned to take part in a peace operation. Costs for military contingents participating in UNDPKO peacekeeping operations are not reportable as ODA. International peacekeeping operations may include humanitarian-type activities (contributions to the form of equipment or personnel), as described in codes 7xxxx. These should be included under code 15230 if they are an integrated part of the activities above, otherwise they should be reported as humanitarian aid. NB: When using this code, indicate the name of the operation in the short description of the activity reported.",
        ),
    )
    REINTEGRATION_AND_SALW_CONTROL = (
        15240,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Reintegration of demobilised military personnel into the economy; conversion of production facilities from military to civilian outputs; technical co-operation to control, prevent and/or reduce the proliferation of small arms and light weapons (SALW) – see para. 80 of the Directives for definition of SALW activities covered. [Other than in the context of an international peacekeeping operation (15230) or child soldiers (15261)].",
        ),
    )
    REMOVAL_OF_LAND_MINES_AND_EXPLOSIVE_REMNANTS_OF_WAR = (
        15250,
        pgettext_lazy(
            "IATI codelist Sector description",
            "All activities related to land mines and explosive remnants of war which have benefits to developing countries as their main objective, including removal of land mines and explosive remnants of war, and stockpile destruction for developmental purposes [other than in the context of an international peacekeeping operation (15230)]; risk education and awareness raising; rehabilitation, reintegration and assistance to victims, and research and development on demining and clearance. Only activities for civilian purposes are ODA-eligible.",
        ),
    )
    CHILD_SOLDIERS__PREVENTION_AND_DEMOBILISATION_ = (
        15261,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Technical co-operation provided to government – and assistance to civil society organisations – to support and apply legislation designed to prevent the recruitment of child soldiers, and to demobilise, disarm, reintegrate, repatriate and resettle (DDR) child soldiers.",
        ),
    )
    SOCIAL_PROTECTION = (
        16010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Social protection or social security strategies, legislation and administration; institution capacity building and advice; social security and other social schemes; support programmes, cash benefits, pensions and special programmes for older persons, orphans, persons with disabilities, children, mothers with newborns, those living in poverty, without jobs and other vulnerable groups; social dimensions of structural adjustment.",
        ),
    )
    SOCIAL_PROTECTION_AND_WELFARE_SERVICES_POLICY__PLANNING_AND_ADMINISTRATION = (
        16011,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Administration of overall social protection policies, plans, programmes and budgets including legislation, standards and statistics on social protection.",
        ),
    )
    SOCIAL_SECURITY__EXCL_PENSIONS_ = (
        16012,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Social protection shemes in the form of cash or in-kind benefits to people unable to work due to sickness or injury.",
        ),
    )
    GENERAL_PENSIONS = (
        16013,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Social protection schemes in the form of cash or in-kind benefits, including pensions, against the risks linked to old age.",
        ),
    )
    CIVIL_SERVICE_PENSIONS = (
        16014,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Pension schemes for government personnel.",
        ),
    )
    SOCIAL_SERVICES__INCL_YOUTH_DEVELOPMENT_AND_WOMEN__CHILDREN_ = (
        16015,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Social protection schemes in the form of cash or in-kind benefits to households with dependent children, including parental leave benefits.",
        ),
    )
    EMPLOYMENT_CREATION = (
        16020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Employment policy and planning; institution capacity building and advice; employment creation and income generation programmes; including activities specifically designed for the needs of vulnerable groups.",
        ),
    )
    HOUSING_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        16030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Housing sector policy, planning and programmes;  excluding low-cost housing and slum clearance (16040).",
        ),
    )
    LOWCOST_HOUSING = (
        16040,
        pgettext_lazy("IATI codelist Sector description", "Including slum clearance."),
    )
    MULTISECTOR_AID_FOR_BASIC_SOCIAL_SERVICES = (
        16050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Basic social services are defined to include basic education, basic health, basic nutrition, population/reproductive health and basic drinking water supply and basic sanitation.",
        ),
    )
    CULTURE_AND_RECREATION = (
        16061,
        pgettext_lazy(
            "IATI codelist Sector description", "Including libraries and museums."
        ),
    )
    STATISTICAL_CAPACITY_BUILDING = (
        16062,
        pgettext_lazy(
            "IATI codelist Sector description",
            "All statistical activities, such as data collection, processing, dissemination and analysis; support to development and management of official statistics including demographic, social, economic, environmental and multi-sectoral statistics; statistical quality frameworks; development of human and technological resources for statistics, investments in data innovation. Activities related to data and statistics in the sectors 120, 130 or 150 should preferably be coded under the voluntary purpose codes 12196, 13096 and 15196. Activities with the sole purpose of monitoring development co-operation activities, including if performed by third parties, should be coded under 91010 (Administrative costs).",
        ),
    )
    NARCOTICS_CONTROL = (
        16063,
        pgettext_lazy(
            "IATI codelist Sector description",
            "In-country and customs controls including training of the police; educational programmes and awareness campaigns to restrict narcotics traffic and in-country distribution. ODA recording of narcotics control expenditures is limited to activities that focus on economic development and welfare including alternative development programmes and crop substitution (see 31165 and 43050). Activities by the donor country to interdict drug supplies destroy crops or train or finance military personnel in anti-narcotics activities are not reportable.",
        ),
    )
    SOCIAL_MITIGATION_OF_HIV_AIDS = (
        16064,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Special programmes to address the consequences of HIV/AIDS, e.g. social, legal and economic assistance to people living with HIV/AIDS including food security and employment; support to vulnerable groups and children orphaned by HIV/AIDS; human rights of HIV/AIDS affected people.",
        ),
    )
    LABOUR_RIGHTS = (
        16070,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Advocacy for international labour standards, labour law, fundamental principles and rights at work (child labour, forced labour, non-discrimination in the workplace, freedom of association and collective bargaining); formalisation of informal work, occupational safety and health.",
        ),
    )
    SOCIAL_DIALOGUE = (
        16080,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Capacity building and advice in support of social dialogue; support to social dialogue institutions, bodies and mechanisms; capacity building of workers' and employers' organisations.",
        ),
    )
    TRANSPORT_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        21010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Transport sector policy, planning and programmes; aid to transport ministries; institution capacity building and advice; unspecified transport; activities that combine road, rail, water and/or air transport. Includes prevention of road accidents. Whenever possible, report transport of goods under the sector of the good being transported.",
        ),
    )
    TRANSPORT_POLICY__PLANNING_AND_ADMINISTRATION = (
        21011,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Administration of affairs and services concerning transport systems.",
        ),
    )
    PUBLIC_TRANSPORT_SERVICES = (
        21012,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Administration of affairs and services concerning public transport.",
        ),
    )
    TRANSPORT_REGULATION = (
        21013,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Supervision and regulation of users, operations, construction and maintenance of transport systems (registration, licensing, inspection of equipment, operator skills and training; safety standards, franchises, tariffs, levels of service, etc.).",
        ),
    )
    ROAD_TRANSPORT = (
        21020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Road infrastructure, road vehicles; passenger road transport, motor passenger cars.",
        ),
    )
    FEEDER_ROAD_CONSTRUCTION = (
        21021,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Construction or operation of feeder road transport systems and facilities.",
        ),
    )
    FEEDER_ROAD_MAINTENANCE = (
        21022,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Maintenance of feeder road transport systems and facilities.",
        ),
    )
    NATIONAL_ROAD_CONSTRUCTION = (
        21023,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Construction or operation of national road transport systems and facilities.",
        ),
    )
    NATIONAL_ROAD_MAINTENANCE = (
        21024,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Maintenance of national road transport systems and facilities.",
        ),
    )
    RAIL_TRANSPORT = (
        21030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Rail infrastructure, rail equipment, locomotives, other rolling stock; including light rail (tram) and underground systems.",
        ),
    )
    WATER_TRANSPORT = (
        21040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Harbours and docks, harbour guidance systems, ships and boats; river and other inland water transport, inland barges and vessels.",
        ),
    )
    AIR_TRANSPORT = (
        21050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Airports, airport guidance systems, aeroplanes, aeroplane maintenance equipment.",
        ),
    )
    STORAGE = (
        21061,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Whether or not related to transportation. Whenever possible, report storage projects under the sector of the resource being stored.",
        ),
    )
    COMMUNICATIONS_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        22010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Communications sector policy, planning and programmes; institution capacity building and advice; including postal services development; unspecified communications activities.",
        ),
    )
    POSTAL_SERVICES = (
        22012,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Development and operation of postal services.",
        ),
    )
    INFORMATION_SERVICES = (
        22013,
        pgettext_lazy(
            "IATI codelist Sector description", "Provision of information services."
        ),
    )
    TELECOMMUNICATIONS = (
        22020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Telephone networks, telecommunication satellites, earth stations.",
        ),
    )
    RADIO_TELEVISION_PRINT_MEDIA = (
        22030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Radio and TV links, equipment; newspapers; printing and publishing.",
        ),
    )
    INFORMATION_AND_COMMUNICATION_TECHNOLOGY__ICT_ = (
        22040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Computer hardware and software; internet access; IT training.  When sector cannot be specified.",
        ),
    )
    ENERGY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        23010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Energy sector policy, planning and programmes; aid to energy ministries; institution capacity building and advice; unspecified energy activities including energy conservation.",
        ),
    )
    POWER_GENERATION_NON_RENEWABLE_SOURCES = (
        23020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Thermal power plants including when heat source cannot be determined; combined gas-coal power plants.",
        ),
    )
    POWER_GENERATION_RENEWABLE_SOURCES = (
        23030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including policy, planning, development programmes, surveys and incentives. Fuelwood/ charcoal production should be included under forestry (31261).",
        ),
    )
    ELECTRICAL_TRANSMISSION__DISTRIBUTION = (
        23040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Distribution from power source to end user; transmission lines.",
        ),
    )
    GAS_DISTRIBUTION = (
        23050,
        pgettext_lazy(
            "IATI codelist Sector description", "Delivery for use by ultimate consumer."
        ),
    )
    OIL_FIRED_POWER_PLANTS = (
        23061,
        pgettext_lazy(
            "IATI codelist Sector description", "Including diesel power plants."
        ),
    )
    NUCLEAR_POWER_PLANTS = (
        23064,
        pgettext_lazy("IATI codelist Sector description", "Including nuclear safety."),
    )
    HYDRO_ELECTRIC_POWER_PLANTS = (
        23065,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including power-generating river barges.",
        ),
    )
    SOLAR_ENERGY = (
        23067,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including photo-voltaic cells, solar thermal applications and solar heating.",
        ),
    )
    WIND_POWER = (
        23068,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Wind energy for water lifting and electric power generation.",
        ),
    )
    OCEAN_POWER = (
        23069,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including ocean thermal energy conversion, tidal and wave power.",
        ),
    )
    BIOMASS = (
        23070,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Densification technologies and use of biomass for direct power generation including biogas, gas obtained from sugar cane and other plant residues, anaerobic digesters.",
        ),
    )
    ENERGY_EDUCATION_TRAINING = (
        23081,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Applies to all energy sub-sectors; all levels of training.",
        ),
    )
    ENERGY_RESEARCH = (
        23082,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including general inventories, surveys.",
        ),
    )
    ENERGY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        23110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Energy sector policy, planning; aid to energy ministries and other governmental or nongovernmental institutions for activities related to the SDG7; institution capacity building and advice; tariffs, market building, unspecified energy activities; energy activities for which a more specific code cannot be assigned.",
        ),
    )
    ENERGY_REGULATION = (
        23112,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Regulation of the energy sector, including wholesale and retail electricity provision.",
        ),
    )
    ENERGY_EDUCATION_TRAINING = (
        23181,
        pgettext_lazy(
            "IATI codelist Sector description",
            "All levels of training not included elsewhere.",
        ),
    )
    ENERGY_RESEARCH = (
        23182,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including general inventories, surveys.",
        ),
    )
    ENERGY_CONSERVATION_AND_DEMAND_SIDE_EFFICIENCY = (
        23183,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support for energy demand reduction, e.g. building and industry upgrades, smart grids, metering and tariffs. For clean cooking appliances use code 32174.",
        ),
    )
    ENERGY_GENERATION__RENEWABLE_SOURCES_MULTIPLE_TECHNOLOGIES = (
        23210,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Renewable energy generation programmes that cannot be attributed to one single technology (codes 23220 through 23280 below). Fuelwood/charcoal production should be included under forestry 31261.",
        ),
    )
    HYDRO_ELECTRIC_POWER_PLANTS = (
        23220,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including energy generating river barges.",
        ),
    )
    SOLAR_ENERGY_FOR_CENTRALISED_GRIDS = (
        23230,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including photo-voltaic cells, concentrated solar power systems connected to the main grid and net-metered decentralised solutions.",
        ),
    )
    SOLAR_ENERGY_FOR_ISOLATED_GRIDS_AND_STANDALONE_SYSTEMS = (
        23231,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Solar power generation for isolated mini-grids, solar home systems (including integrated wiring and related appliances), solar lanterns distribution and commercialisation. This code refers to the power generation component only.",
        ),
    )
    SOLAR_ENERGY_THERMAL_APPLICATIONS = (
        23232,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Solar solutions for indoor space and water heating (except for solar cook stoves 32174).",
        ),
    )
    WIND_ENERGY = (
        23240,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Wind energy for water lifting and electric power generation.",
        ),
    )
    MARINE_ENERGY = (
        23250,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including ocean thermal energy conversion, tidal and wave power.",
        ),
    )
    GEOTHERMAL_ENERGY = (
        23260,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Use of geothermal energy for generating electric power or directly as heat for agriculture, etc.",
        ),
    )
    BIOFUEL_FIRED_POWER_PLANTS = (
        23270,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Use of solids and liquids produced from biomass for direct power generation. Also includes biogases from anaerobic fermentation (e.g. landfill gas, sewage sludge gas, fermentation of energy crops and manure) and thermal processes (also known as syngas); waste-fired power plants making use of biodegradable municipal waste (household waste and waste from companies and public services that resembles household waste, collected at installations specifically designed for their disposal with recovery of combustible liquids, gases or heat). See code 23360 for non-renewable waste-fired power plants.",
        ),
    )
    ENERGY_GENERATION__NON_RENEWABLE_SOURCES__UNSPECIFIED = (
        23310,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Thermal power plants including when energy source cannot be determined; combined gas-coal power plants.",
        ),
    )
    COAL_FIRED_ELECTRIC_POWER_PLANTS = (
        23320,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Thermal electric power plants that use coal as the energy source.",
        ),
    )
    OIL_FIRED_ELECTRIC_POWER_PLANTS = (
        23330,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Thermal electric power plants that use fuel oil or diesel fuel as the energy source.",
        ),
    )
    NATURAL_GAS_FIRED_ELECTRIC_POWER_PLANTS = (
        23340,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Electric power plants that are fuelled by natural gas; related feed-in infrastructure (LNG terminals, gasifiers, pipelines to feed the plant).",
        ),
    )
    FOSSIL_FUEL_ELECTRIC_POWER_PLANTS_WITH_CARBON_CAPTURE_AND_STORAGE__CCS_ = (
        23350,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Fossil fuel electric power plants employing technologies to capture carbon dioxide emissions. CCS not related to power plants should be included under 41020. CCS activities are not reportable as ODA.",
        ),
    )
    NON_RENEWABLE_WASTE_FIRED_ELECTRIC_POWER_PLANTS = (
        23360,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Electric power plants that use non-biodegradable industrial and municipal waste as the energy source.",
        ),
    )
    HYBRID_ENERGY_ELECTRIC_POWER_PLANTS = (
        23410,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Electric power plants that make use of both non-renewable and renewable energy sources.",
        ),
    )
    NUCLEAR_ENERGY_ELECTRIC_POWER_PLANTS_AND_NUCLEAR_SAFETY = (
        23510,
        pgettext_lazy(
            "IATI codelist Sector description",
            "See note regarding ODA eligibility of nuclear energy.",
        ),
    )
    HEAT_PLANTS = (
        23610,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Power plants which are designed to produce heat only.",
        ),
    )
    DISTRICT_HEATING_AND_COOLING = (
        23620,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Distribution of heat generated in a centralised location, or delivery of chilled water, for residential and commercial heating or cooling purposes.",
        ),
    )
    ELECTRIC_POWER_TRANSMISSION_AND_DISTRIBUTION__CENTRALISED_GRIDS_ = (
        23630,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Grid distribution from power source to end user; transmission lines. Also includes storage of energy to generate power (e.g. pumped hydro, batteries) and the extension of grid access, often to rural areas.",
        ),
    )
    ELECTRIC_POWER_TRANSMISSION_AND_DISTRIBUTION__ISOLATED_MINI_GRIDS_ = (
        23631,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Includes village grids and other electricity distribution technologies to end users that are not connected to the main national grid. Also includes related electricity storage. This code refers to the network infrastructure only regardless of the power generation technologies.",
        ),
    )
    RETAIL_GAS_DISTRIBUTION = (
        23640,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Includes urban infrastructure for the delivery of urban gas and LPG cylinder production, distribution and refill. Excludes gas distribution for purposes of electricity generation (23340) and pipelines (32262).",
        ),
    )
    ELECTRIC_MOBILITY_INFRASTRUCTURES = (
        23642,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Includes electricity or hydrogen recharging stations for private and public transport systems and related infrastructure (except for rail transport 21030).",
        ),
    )
    FINANCIAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        24010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Finance sector policy, planning and programmes; institution capacity building and advice; financial markets and systems.",
        ),
    )
    MONETARY_INSTITUTIONS = (
        24020,
        pgettext_lazy("IATI codelist Sector description", "Central banks."),
    )
    FORMAL_SECTOR_FINANCIAL_INTERMEDIARIES = (
        24030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "All formal sector financial intermediaries; credit lines; insurance, leasing, venture capital, etc. (except when focused on only one sector).",
        ),
    )
    INFORMAL_SEMI_FORMAL_FINANCIAL_INTERMEDIARIES = (
        24040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Micro credit, savings and credit co-operatives etc.",
        ),
    )
    REMITTANCE_FACILITATION__PROMOTION_AND_OPTIMISATION = (
        24050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Includes programmes aiming at reducing the sending costs of remittances.",
        ),
    )
    BUSINESS_POLICY_AND_ADMINISTRATION = (
        25010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Public sector policies and institution support to the business environment and investment climate, including business regulations, property rights, non-discrimination, investment promotion, competition policy, enterprises law, private-public partnerships.",
        ),
    )
    PRIVATISATION = (
        25020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "When sector cannot be specified. Including general state enterprise restructuring or demonopolisation programmes; planning, programming, advice.",
        ),
    )
    BUSINESS_DEVELOPMENT_SERVICES = (
        25030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Public and private provision of business development services, e.g. incubators, business strategies, commercial linkages programmes and matchmaking services. Includes support to private organisations representing businesses, e.g. business associations; chambers of commerce; producer associations; providers of know-how and other business development services. For financial services use CRS codes 24030 or 24040. For SME development and for support to companies in the industrial sector use codes 32130 through 32172. For support to companies in the agricultural sector use code 31120.",
        ),
    )
    RESPONSIBLE_BUSINESS_CONDUCT = (
        25040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to policy reform, implementation and enforcement of responsible business conduct (RBC) principles and standards as well as facilitation of responsible business practices by companies. Includes establishing and enforcing a legal and regulatory framework to protect stakeholder rights and the environment, rewarding best performers; exemplifying RBC in government economic activities, such as state-owned enterprises’ operations or public procurement; support to the implementation of the OECD Guidelines for MNEs, including disclosure, human rights, employment and industrial relations, environment, combating bribery, consumer interests, science and technology, competition and taxation.",
        ),
    )
    AGRICULTURAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        31110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Agricultural sector policy, planning and programmes; aid to agricultural ministries;  institution capacity building and advice; unspecified agriculture.",
        ),
    )
    AGRICULTURAL_DEVELOPMENT = (
        31120,
        pgettext_lazy(
            "IATI codelist Sector description", "Integrated projects; farm development."
        ),
    )
    AGRICULTURAL_LAND_RESOURCES = (
        31130,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including soil degradation control; soil improvement; drainage of water logged areas; soil desalination; agricultural land surveys; land reclamation; erosion control, desertification control.",
        ),
    )
    AGRICULTURAL_WATER_RESOURCES = (
        31140,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Irrigation, reservoirs, hydraulic structures, ground water exploitation for agricultural use.",
        ),
    )
    AGRICULTURAL_INPUTS = (
        31150,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Supply of seeds, fertilizers, agricultural machinery/equipment.",
        ),
    )
    FOOD_CROP_PRODUCTION = (
        31161,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including grains (wheat, rice, barley, maize, rye, oats, millet, sorghum); horticulture; vegetables; fruit and berries; other annual and perennial crops. [Use code 32161 for agro-industries.]",
        ),
    )
    INDUSTRIAL_CROPS_EXPORT_CROPS = (
        31162,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including sugar; coffee, cocoa, tea; oil seeds, nuts, kernels; fibre crops; tobacco; rubber.  [Use code 32161 for agro-industries.]",
        ),
    )
    LIVESTOCK = (
        31163,
        pgettext_lazy(
            "IATI codelist Sector description", "Animal husbandry; animal feed aid."
        ),
    )
    AGRARIAN_REFORM = (
        31164,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including agricultural sector adjustment.",
        ),
    )
    AGRICULTURAL_ALTERNATIVE_DEVELOPMENT = (
        31165,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Projects to reduce illicit drug cultivation through other agricultural marketing and production opportunities (see code 43050 for non-agricultural alternative development).",
        ),
    )
    AGRICULTURAL_EXTENSION = (
        31166,
        pgettext_lazy(
            "IATI codelist Sector description", "Non-formal training in agriculture."
        ),
    )
    AGRICULTURAL_RESEARCH = (
        31182,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Plant breeding, physiology, genetic resources, ecology, taxonomy, disease control, agricultural bio-technology; including livestock research (animal health, breeding and genetics, nutrition, physiology).",
        ),
    )
    AGRICULTURAL_SERVICES = (
        31191,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Marketing policies & organisation; storage and transportation, creation of strategic reserves.",
        ),
    )
    PLANT_AND_POST_HARVEST_PROTECTION_AND_PEST_CONTROL = (
        31192,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including integrated plant protection, biological plant protection activities, supply and management of agrochemicals, supply of pesticides, plant protection policy and legislation.",
        ),
    )
    AGRICULTURAL_FINANCIAL_SERVICES = (
        31193,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Financial intermediaries for the agricultural sector including credit schemes; crop insurance.",
        ),
    )
    AGRICULTURAL_CO_OPERATIVES = (
        31194,
        pgettext_lazy(
            "IATI codelist Sector description", "Including farmers’ organisations."
        ),
    )
    LIVESTOCK_VETERINARY_SERVICES = (
        31195,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Animal health and management, genetic resources, feed resources.",
        ),
    )
    FORESTRY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        31210,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Forestry sector policy, planning and programmes; institution capacity building and advice; forest surveys; unspecified forestry and agro-forestry activities.",
        ),
    )
    FORESTRY_DEVELOPMENT = (
        31220,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Afforestation for industrial and rural consumption; exploitation and utilisation; erosion control, desertification control; integrated forestry projects.",
        ),
    )
    FUELWOOD_CHARCOAL = (
        31261,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Sustainable forestry development whose primary purpose is production of fuelwood and charcoal. Further transformation of biomass in biofuels is coded under 32173.",
        ),
    )
    FORESTRY_RESEARCH = (
        31282,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including artificial regeneration, genetic improvement, production methods, fertilizer, harvesting.",
        ),
    )
    FISHING_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        31310,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Fishing sector policy, planning and programmes; institution capacity building and advice; ocean and coastal fishing; marine and freshwater fish surveys and prospecting; fishing boats/equipment; unspecified fishing activities.",
        ),
    )
    FISHERY_DEVELOPMENT = (
        31320,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Exploitation and utilisation of fisheries; fish stock protection; aquaculture; integrated fishery projects.",
        ),
    )
    FISHERY_RESEARCH = (
        31382,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Pilot fish culture; marine/freshwater biological research.",
        ),
    )
    FISHERY_SERVICES = (
        31391,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Fishing harbours; fish markets; fishery transport and cold storage.",
        ),
    )
    INDUSTRIAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        32110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Industrial sector policy, planning and programmes; institution capacity building and advice; unspecified industrial activities; manufacturing of goods not specified below.",
        ),
    )
    SMALL_AND_MEDIUM_SIZED_ENTERPRISES__SME__DEVELOPMENT = (
        32130,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Direct support to improve the productive capacity and business management of micro, small and medium-sized enterprises in the industrial sector, including accounting, auditing, advisory services, technological transfer and skill upgrading. For business policy and institutional support use code 25010. For business development services through business intermediary organisations (e.g. business associations; chambers of commerce; producer associations; incubators; providers of know-how and other business development services) use CRS code 250xx. For farm and agricultural development use code 31120.",
        ),
    )
    AGRO_INDUSTRIES = (
        32161,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Staple food processing, dairy products, slaughter houses and equipment, meat and fish processing and preserving, oils/fats, sugar refineries, beverages/tobacco, animal feeds production.",
        ),
    )
    FOREST_INDUSTRIES = (
        32162,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Wood production, pulp/paper production.",
        ),
    )
    TEXTILES__LEATHER_AND_SUBSTITUTES = (
        32163,
        pgettext_lazy(
            "IATI codelist Sector description", "Including knitting factories."
        ),
    )
    CHEMICALS = (
        32164,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Industrial and non-industrial production facilities; includes pesticides production.",
        ),
    )
    ENERGY_MANUFACTURING__FOSSIL_FUELS_ = (
        32167,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including gas liquefaction; petroleum refineries, wholesale distribution of fossil fuels. (Use 23640 for retail distribution of gas and 23641 for retail distribution of liquid or solid fossil fuels.)",
        ),
    )
    PHARMACEUTICAL_PRODUCTION = (
        32168,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Medical equipment/supplies; drugs, medicines, vaccines; hygienic products.",
        ),
    )
    BASIC_METAL_INDUSTRIES = (
        32169,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Iron and steel, structural metal production.",
        ),
    )
    ENGINEERING = (
        32171,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Manufacturing of electrical and non-electrical machinery, engines/turbines.",
        ),
    )
    TRANSPORT_EQUIPMENT_INDUSTRY = (
        32172,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Shipbuilding, fishing boats building; railroad equipment; motor vehicles and motor passenger cars; aircraft; navigation/guidance systems.",
        ),
    )
    MODERN_BIOFUELS_MANUFACTURING = (
        32173,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Includes biogas, liquid biofuels and pellets for domestic and non-domestic use. Excludes raw fuelwood and charcoal (31261).",
        ),
    )
    CLEAN_COOKING_APPLIANCES_MANUFACTURING = (
        32174,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Includes manufacturing and distribution of efficient biomass cooking stoves, gasifiers, liquid biofuels stoves, solar stoves, gas and biogas stoves, electric stoves.",
        ),
    )
    TECHNOLOGICAL_RESEARCH_AND_DEVELOPMENT = (
        32182,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including industrial standards; quality management; metrology;  testing;  accreditation;  certification.",
        ),
    )
    MINERAL_MINING_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        32210,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Mineral and mining sector policy, planning and programmes;  mining legislation, mining cadastre, mineral resources inventory, information systems, institution capacity building and advice;  unspecified mineral resources exploitation.",
        ),
    )
    MINERAL_PROSPECTION_AND_EXPLORATION = (
        32220,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Geology, geophysics, geochemistry;  excluding hydrogeology (14010) and environmental geology (41010), mineral extraction and processing, infrastructure, technology, economics, safety and environment management.",
        ),
    )
    COAL = (
        32261,
        pgettext_lazy(
            "IATI codelist Sector description", "Including lignite and peat."
        ),
    )
    OIL_AND_GAS__UPSTREAM_ = (
        32262,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Petroleum, natural gas, condensates, liquefied petroleum gas (LPG), liquefied natural gas (LNG); including drilling and production, oil and gas pipelines.",
        ),
    )
    FERROUS_METALS = (
        32263,
        pgettext_lazy(
            "IATI codelist Sector description", "Iron and ferro-alloy metals."
        ),
    )
    NONFERROUS_METALS = (
        32264,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Aluminium, copper, lead, nickel, tin, zinc.",
        ),
    )
    PRECIOUS_METALS_MATERIALS = (
        32265,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Gold, silver, platinum, diamonds, gemstones.",
        ),
    )
    INDUSTRIAL_MINERALS = (
        32266,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Baryte, limestone, feldspar, kaolin, sand, gypsym, gravel, ornamental stones.",
        ),
    )
    FERTILIZER_MINERALS = (
        32267,
        pgettext_lazy("IATI codelist Sector description", "Phosphates, potash."),
    )
    OFFSHORE_MINERALS = (
        32268,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Polymetallic nodules, phosphorites, marine placer deposits.",
        ),
    )
    CONSTRUCTION_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        32310,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Construction sector policy and planning; excluding construction activities within specific sectors (e.g., hospital or school construction).",
        ),
    )
    TRADE_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        33110,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Trade policy and planning; support to ministries and departments responsible for trade policy; trade-related legislation and regulatory reforms; policy analysis and implementation of multilateral trade agreements e.g. technical barriers to trade and sanitary and phytosanitary measures (TBT/SPS) except at regional level (see 33130); mainstreaming trade in national development strategies (e.g. poverty reduction strategy papers); wholesale/retail trade; unspecified trade and trade promotion activities.",
        ),
    )
    TRADE_FACILITATION = (
        33120,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Simplification and harmonisation of international import and export procedures (e.g. customs valuation, licensing procedures, transport formalities, payments, insurance); support to customs departments  and other border agencies, including in particular implementation of the provisions of the WTO Trade Facilitation Agreement; tariff reforms.",
        ),
    )
    REGIONAL_TRADE_AGREEMENTS__RTAS_ = (
        33130,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support to regional trade arrangements [e.g. Southern African Development Community (SADC), Association of Southeast Asian Nations (ASEAN), Free Trade Area of the Americas (FTAA), African Caribbean Pacific/European Union (ACP/EU)], including work on technical barriers to trade and sanitary and phytosanitary measures (TBT/SPS) at regional level; elaboration of rules of origin and introduction of special and differential treatment in RTAs.",
        ),
    )
    MULTILATERAL_TRADE_NEGOTIATIONS = (
        33140,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support developing countries’ effective participation in multilateral trade negotiations, including training of negotiators, assessing impacts of negotiations; accession to the World Trade Organisation (WTO) and other multilateral trade-related organisations.",
        ),
    )
    TRADE_RELATED_ADJUSTMENT = (
        33150,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Contributions to the government budget to assist the implementation of recipients' own trade reforms and adjustments to trade policy measures by other countries; assistance to manage shortfalls in the balance of payments due to changes in the world trading environment.",
        ),
    )
    TRADE_EDUCATION_TRAINING = (
        33181,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Human resources development in trade not included under any of the above codes.  Includes university programmes in trade.",
        ),
    )
    ENVIRONMENTAL_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        41010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Environmental policy, laws, regulations and economic instruments; administrational institutions and practices; environmental and land use planning and decision-making procedures; seminars, meetings; miscellaneous conservation and protection measures not specified below.",
        ),
    )
    BIOSPHERE_PROTECTION = (
        41020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Air pollution control, ozone layer preservation; marine pollution control.",
        ),
    )
    BIO_DIVERSITY = (
        41030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including natural reserves and actions in the surrounding areas; other measures to protect endangered or vulnerable species and their habitats (e.g. wetlands preservation).",
        ),
    )
    SITE_PRESERVATION = (
        41040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Applies to unique cultural landscape; including sites/objects of historical, archeological, aesthetic, scientific or educational value.",
        ),
    )
    FLOOD_PREVENTION_CONTROL = (
        41050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Floods from rivers or the sea; including sea water intrusion control and sea level rise related activities.",
        ),
    )
    ENVIRONMENTAL_RESEARCH = (
        41082,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Including establishment of databases, inventories/accounts of physical and natural resources; environmental profiles and impact studies if not sector specific.",
        ),
    )
    URBAN_DEVELOPMENT_AND_MANAGEMENT = (
        43030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Integrated urban development projects; local development and urban management; urban infrastructure and services; municipal finances; urban environmental management; urban development and planning; urban renewal and urban housing; land information systems.",
        ),
    )
    URBAN_LAND_POLICY_AND_MANAGEMENT = (
        43031,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Urban development and planning; urban management, land information systems.",
        ),
    )
    URBAN_DEVELOPMENT = (
        43032,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Integrated urban development projects; local development; urban infrastructure and services; municipal finances; urban environment systems; urban renewal and urban housing.",
        ),
    )
    RURAL_DEVELOPMENT = (
        43040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Integrated rural development projects;  e.g. regional development planning;  promotion of decentralised and multi-sectoral competence for planning, co-ordination and management;  implementation of regional development and measures (including natural reserve management);  land management;  land use planning; land settlement and resettlement activities [excluding resettlement of refugees and internally displaced persons (72010)]; functional integration of rural and urban areas;  geographical information systems.",
        ),
    )
    RURAL_LAND_POLICY_AND_MANAGEMENT = (
        43041,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Regional development planning; promotion of decentralised and multi-sectoral competence for planning, co-ordination and management; land management; land use planning; geographical information systems.",
        ),
    )
    RURAL_DEVELOPMENT = (
        43042,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Integrated rural development projects; implementation of regional development and measures (including natural reserve management); land settlement and resettlement activities [excluding resettlement of refugees and internally displaced persons (72010)]; functional integration of rural and urban areas.",
        ),
    )
    NON_AGRICULTURAL_ALTERNATIVE_DEVELOPMENT = (
        43050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Projects to reduce illicit drug cultivation through, for example, non-agricultural income opportunities, social and physical infrastructure (see code 31165 for agricultural alternative development).",
        ),
    )
    DISASTER_RISK_REDUCTION = (
        43060,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Disaster risk reduction activities if not sector specific. Comprises risk assessments, structural prevention measures (e.g. flood prevention infrastructure), preparedness measures (e.g. early warning systems) normative prevention measures (e.g. building codes, land-use planning), and risk transfer systems (e.g. insurance schemes, risk funds). Also includes building local and national capacities and supporting the establishment of efficient and sustainable national structures able to promote disaster risk reduction.",
        ),
    )
    FOOD_SECURITY_POLICY_AND_ADMINISTRATIVE_MANAGEMENT = (
        43071,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Food security policy, programmes and activities; institution capacity strengthening; policies, programmes for the reduction of food loss/waste; food security information systems, data collection, statistics, analysis, tools, methods; coordination and governance mechanisms; other unspecified food security activities.",
        ),
    )
    HOUSEHOLD_FOOD_SECURITY_PROGRAMMES = (
        43072,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Short or longer term household food security programmes and activities that improve the access of households to nutritionally adequate diets (excluding any cash transfers within broader social welfare programmes that do not have a specific food security, food acquisition or nutrition focus which should be reported under code 16010).",
        ),
    )
    FOOD_SAFETY_AND_QUALITY = (
        43073,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Food safety and quality policies, programmes and activities, including food inspection and certification; strengthening food safety/quality capacities and development of standards along the value chain; monitoring/surveillance and laboratory capacities; and delivery of information, communication, education.",
        ),
    )
    MULTISECTOR_EDUCATION_TRAINING = (
        43081,
        pgettext_lazy("IATI codelist Sector description", "Including scholarships."),
    )
    RESEARCH_SCIENTIFIC_INSTITUTIONS = (
        43082,
        pgettext_lazy(
            "IATI codelist Sector description", "When sector cannot be identified."
        ),
    )
    GENERAL_BUDGET_SUPPORT_RELATED_AID = (
        51010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Unearmarked contributions to the government budget; support for the implementation of macroeconomic reforms (structural adjustment programmes, poverty reduction strategies); general programme assistance (when not allocable by sector).",
        ),
    )
    FOOD_ASSISTANCE = (
        52010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Supply of edible human food under national or international programmes including transport costs, cash payments made for food supplies; project food assistance aid and food assistance aid for market sales when benefiting sector not specified. Excludes food security policy and administrative management (43071), household food security programmes (43072) and emergency food assistance aid (72040). Report as multilateral: i) food assistance aid by EU financed out of its budget and allocated pro rata to EU member countries; and ii) core contributions to the World Food Programme.",
        ),
    )
    IMPORT_SUPPORT__CAPITAL_GOODS_ = (
        53030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Capital goods and services; lines of credit.",
        ),
    )
    IMPORT_SUPPORT__COMMODITIES_ = (
        53040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Commodities, general goods and services, oil imports.",
        ),
    )
    ACTION_RELATING_TO_DEBT = (
        60010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Actions falling outside the code headings below.",
        ),
    )
    RELIEF_OF_MULTILATERAL_DEBT = (
        60030,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Grants or credits to cover debt owed to multilateral financial institutions; including contributions to Heavily Indebted Poor Countries (HIPC) Trust Fund.",
        ),
    )
    DEBT_FOR_DEVELOPMENT_SWAP = (
        60061,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Allocation of debt claims to use for development (e.g., debt for education, debt for environment).",
        ),
    )
    OTHER_DEBT_SWAP = (
        60062,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Where the debt swap benefits an external agent i.e. is not specifically for development purposes.",
        ),
    )
    DEBT_BUY_BACK = (
        60063,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Purchase of debt for the purpose of cancellation.",
        ),
    )
    MATERIAL_RELIEF_ASSISTANCE_AND_SERVICES = (
        72010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Shelter, water, sanitation, education, health services including supply of medicines and malnutrition management, including medical nutrition management; supply of other nonfood relief items (including cash and voucher delivery modalities) for the benefit of crisisaffected people, including refugees and internally displaced people in developing countries, Includes assistance delivered by or coordinated by international civil protection units in the immediate aftermath of a disaster (in-kind assistance, deployment of specially-equipped teams, logistics and transportation, or assessment and coordination by experts sent to the field). Also includes measures to promote and protect the safety, well-being, dignity and integrity of crisis-affected people including refugees and internally displaced persons in developing countries. (Activities designed to protect the security of persons or properties through the use or display of force are not reportable as ODA.)",
        ),
    )
    BASIC_HEALTH_CARE_SERVICES_IN_EMERGENCIES = (
        72011,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Provision of health services (basic health services, mental health, sexual and reproductive health), medical nutritional intervention (therapeutic feeding and medical interventions for treating malnutrition) and supply of medicines for the benefit of affected people. Excludes supplemental feeding (72040).",
        ),
    )
    EDUCATION_IN_EMERGENCIES = (
        72012,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Support for education facilities (including restoring pre-existing essential infrastructure and school facilities), teaching, training and learning materials (including digital technologies, as appropriate) and immediate access to quality basic and primary education (including formal and non-formal education), and secondary education (including vocational training and secondary level technical education) in emergencies for the benefit of affected children and youth, particularly targeting girls and women and refugees, life skills for youth and adults, and vocational training for youth and adults",
        ),
    )
    EMERGENCY_FOOD_ASSISTANCE = (
        72040,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Provision and distribution of food; cash and vouchers for the purchase of food; non-medical nutritional interventions for the benefit of crisis-affected people, including refugees and internally displaced people in developing countries in emergency situations. Includes logistical costs. Excludes non-emergency food assistance (52010), food security policy and administrative management (43071), household food programmes (43072) and medical nutrition interventions (therapeutic feeding) (72010 and 72011).",
        ),
    )
    RELIEF_CO_ORDINATION_AND_SUPPORT_SERVICES = (
        72050,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Measures to co-ordinate the assessment and safe delivery of humanitarian aid, including logistic, transport and communication systems; direct financial or technical support to national governments of affected countries to manage a disaster situation; activities to build an evidence base for humanitarian financing and operations, sharing this information and developing standards and guidelines for more effective response; funding for identifying and sharing innovative and scalable solutions to deliver effective humanitarian assistance.",
        ),
    )
    IMMEDIATE_POST_EMERGENCY_RECONSTRUCTION_AND_REHABILITATION = (
        73010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Social and economic rehabilitation in the aftermath of emergencies to facilitate recovery and resilience building and enable populations to restore their livelihoods in the wake of an emergency situation (e.g. trauma counselling and treatment, employment programmes). Includes infrastructure necessary for the delivery of humanitarian aid; restoring pre-existing essential infrastructure and facilities (e.g. water and sanitation, shelter, health care services, education); rehabilitation of basic agricultural inputs and livestock. Excludes longer-term reconstruction (“build back better”) which is reportable against relevant sectors.",
        ),
    )
    DISASTER_PREVENTION_AND_PREPAREDNESS = (
        74010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Disaster risk reduction activities (e.g. developing knowledge, natural risks cartography, legal norms for construction); early warning systems; emergency contingency stocks and contingency planning including preparations for forced displacement.",
        ),
    )
    MULTI_HAZARD_RESPONSE_PREPAREDNESS = (
        74020,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Building the responsiveness, capability and capacity of international, regional and national humanitarian actors to disasters. Support to the institutional capacities of national and local government, specialised humanitarian bodies, and civil society organisations to anticipate, respond and recover from the impact of potential, imminent and current hazardous events and emergency situations that pose humanitarian threats and could call for a humanitarian response. This includes risk analysis and assessment, mitigation, preparedness, such as stockpiling of emergency items and training and capacity building aimed to increase the speed and effectiveness of lifesaving assistance delivered in the occurrence of crisis.",
        ),
    )
    SUPPORT_TO_NATIONAL_NGOS = (
        92010,
        pgettext_lazy("IATI codelist Sector description", "In the donor country."),
    )
    SUPPORT_TO_LOCAL_AND_REGIONAL_NGOS = (
        92030,
        pgettext_lazy(
            "IATI codelist Sector description", "In the recipient country or region."
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES__NON_SECTOR_ALLOCABLE_ = (
        93010,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months, when costs cannot be disaggregated. See section II.6 and Annex 17.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_FOOD_AND_SHELTER = (
        93011,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months – food and shelter: - Food and other essential temporary sustenance provisions such as clothing. - Temporary accommodation facilities (e.g. reception centres, containers, tent camps). In respect of buildings, only the costs of maintenance and upkeep may be reported as ODA. The cost of renting temporary accommodation facilities is eligible. (All construction costs are excluded).",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_TRAINING = (
        93012,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months – training: - Early childhood education, primary and secondary education for children (this includes school costs but excludes vocational training), as part of temporary sustenance. - Language training and other ad-hoc basic training for refugees e.g. basic life skills for youth and adults (literacy and numeracy training).",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_HEALTH = (
        93013,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months: basic health care and psycho-social support for persons with specific needs e.g. unaccompanied minors, persons with disabilities, survivors of violence and torture.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_OTHER_TEMPORARY_SUSTENANCE = (
        93014,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months: temporary sustenance other than food and shelter (code 93011), training (93012) and health (93013), i.e.  cash “pocket money” to cover subsistence costs and assistance in the asylum procedure: translation of documents, legal and administrative counselling, interpretation services.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_VOLUNTARY_REPATRIATION = (
        93015,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months: voluntary repatriation of refugees to a developing country during first twelve months.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_TRANSPORT = (
        93016,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months: transport to the host country in the case of resettlement programmes and transport within the host country.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_RESCUE_AT_SEA = (
        93017,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months: rescue of refugees at sea when it is the main purpose of the operation. Only the additional costs related to the operation may be counted.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES_ADMINISTRATIVE_COSTS = (
        93018,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months: administrative costs. Only overhead costs attached to the direct provision of temporary sustenance to refugees are eligible. This includes costs of personnel assigned to provide eligible services to refugees, but does not include costs of personnel who are not involved in the direct execution of these services, e.g. management, human resources, information technology.",
        ),
    )
    SECTORS_NOT_SPECIFIED = (
        99810,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Contributions to general development of the recipient should be included under programme assistance (51010).",
        ),
    )
    PROMOTION_OF_DEVELOPMENT_AWARENESS__NON_SECTOR_ALLOCABLE_ = (
        99820,
        pgettext_lazy(
            "IATI codelist Sector description",
            "Spending in donor country for heightened awareness/interest in development co-operation (brochures, lectures, special research projects, etc.).",
        ),
    )
