from django.db import models
from django.utils.translation import pgettext_lazy


class UNSDG_Targets(models.TextChoices):
    """
    A value from the second-level list of UN sustainable development goals (SDGs) (e.g. ‘1.1’)
    """

    BY_2030__ERADICATE_EXTREME_POVERTY_FOR_ALL_PEOPLE_EVERYWHERE__CURRENTLY_MEASURED_AS_PEOPLE_LIVING_ON_LESS_THAN__1_25_A_DAY = (
        "1.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, eradicate extreme poverty for all people everywhere, currently measured as people living on less than $1.25 a day",
        ),
    )
    BY_2030__REDUCE_AT_LEAST_BY_HALF_THE_PROPORTION_OF_MEN__WOMEN_AND_CHILDREN_OF_ALL_AGES_LIVING_IN_POVERTY_IN_ALL_ITS_DIMENSIONS_ACCORDING_TO_NATIONAL_DEFINITIONS = (
        "1.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, reduce at least by half the proportion of men, women and children of all ages living in poverty in all its dimensions according to national definitions",
        ),
    )
    IMPLEMENT_NATIONALLY_APPROPRIATE_SOCIAL_PROTECTION_SYSTEMS_AND_MEASURES_FOR_ALL__INCLUDING_FLOORS__AND_BY_2030_ACHIEVE_SUBSTANTIAL_COVERAGE_OF_THE_POOR_AND_THE_VULNERABLE = (
        "1.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Implement nationally appropriate social protection systems and measures for all, including floors, and by 2030 achieve substantial coverage of the poor and the vulnerable",
        ),
    )
    BY_2030__ENSURE_THAT_ALL_MEN_AND_WOMEN__IN_PARTICULAR_THE_POOR_AND_THE_VULNERABLE__HAVE_EQUAL_RIGHTS_TO_ECONOMIC_RESOURCES__AS_WELL_AS_ACCESS_TO_BASIC_SERVICES__OWNERSHIP_AND_CONTROL_OVER_LAND_AND_OTHER_FORMS_OF_PROPERTY__INHERITANCE__NATURAL_RESOURCES__APPROPRIATE_NEW_TECHNOLOGY_AND_FINANCIAL_SERVICES__INCLUDING_MICROFINANCE = (
        "1.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure that all men and women, in particular the poor and the vulnerable, have equal rights to economic resources, as well as access to basic services, ownership and control over land and other forms of property, inheritance, natural resources, appropriate new technology and financial services, including microfinance",
        ),
    )
    BY_2030__BUILD_THE_RESILIENCE_OF_THE_POOR_AND_THOSE_IN_VULNERABLE_SITUATIONS_AND_REDUCE_THEIR_EXPOSURE_AND_VULNERABILITY_TO_CLIMATE_RELATED_EXTREME_EVENTS_AND_OTHER_ECONOMIC__SOCIAL_AND_ENVIRONMENTAL_SHOCKS_AND_DISASTERS = (
        "1.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, build the resilience of the poor and those in vulnerable situations and reduce their exposure and vulnerability to climate-related extreme events and other economic, social and environmental shocks and disasters",
        ),
    )
    ENSURE_SIGNIFICANT_MOBILIZATION_OF_RESOURCES_FROM_A_VARIETY_OF_SOURCES__INCLUDING_THROUGH_ENHANCED_DEVELOPMENT_COOPERATION__IN_ORDER_TO_PROVIDE_ADEQUATE_AND_PREDICTABLE_MEANS_FOR_DEVELOPING_COUNTRIES__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES__TO_IMPLEMENT_PROGRAMMES_AND_POLICIES_TO_END_POVERTY_IN_ALL_ITS_DIMENSIONS = (
        "1.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure significant mobilization of resources from a variety of sources, including through enhanced development cooperation, in order to provide adequate and predictable means for developing countries, in particular least developed countries, to implement programmes and policies to end poverty in all its dimensions",
        ),
    )
    CREATE_SOUND_POLICY_FRAMEWORKS_AT_THE_NATIONAL__REGIONAL_AND_INTERNATIONAL_LEVELS__BASED_ON_PRO_POOR_AND_GENDER_SENSITIVE_DEVELOPMENT_STRATEGIES__TO_SUPPORT_ACCELERATED_INVESTMENT_IN_POVERTY_ERADICATION_ACTIONS = (
        "1.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Create sound policy frameworks at the national, regional and international levels, based on pro-poor and gender-sensitive development strategies, to support accelerated investment in poverty eradication actions",
        ),
    )
    BY_2030__END_HUNGER_AND_ENSURE_ACCESS_BY_ALL_PEOPLE__IN_PARTICULAR_THE_POOR_AND_PEOPLE_IN_VULNERABLE_SITUATIONS__INCLUDING_INFANTS__TO_SAFE__NUTRITIOUS_AND_SUFFICIENT_FOOD_ALL_YEAR_ROUND = (
        "2.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, end hunger and ensure access by all people, in particular the poor and people in vulnerable situations, including infants, to safe, nutritious and sufficient food all year round",
        ),
    )
    BY_2030__END_ALL_FORMS_OF_MALNUTRITION__INCLUDING_ACHIEVING__BY_2025__THE_INTERNATIONALLY_AGREED_TARGETS_ON_STUNTING_AND_WASTING_IN_CHILDREN_UNDER_5_YEARS_OF_AGE__AND_ADDRESS_THE_NUTRITIONAL_NEEDS_OF_ADOLESCENT_GIRLS__PREGNANT_AND_LACTATING_WOMEN_AND_OLDER_PERSONS = (
        "2.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, end all forms of malnutrition, including achieving, by 2025, the internationally agreed targets on stunting and wasting in children under 5 years of age, and address the nutritional needs of adolescent girls, pregnant and lactating women and older persons",
        ),
    )
    BY_2030__DOUBLE_THE_AGRICULTURAL_PRODUCTIVITY_AND_INCOMES_OF_SMALL_SCALE_FOOD_PRODUCERS__IN_PARTICULAR_WOMEN__INDIGENOUS_PEOPLES__FAMILY_FARMERS__PASTORALISTS_AND_FISHERS__INCLUDING_THROUGH_SECURE_AND_EQUAL_ACCESS_TO_LAND__OTHER_PRODUCTIVE_RESOURCES_AND_INPUTS__KNOWLEDGE__FINANCIAL_SERVICES__MARKETS_AND_OPPORTUNITIES_FOR_VALUE_ADDITION_AND_NON_FARM_EMPLOYMENT = (
        "2.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, double the agricultural productivity and incomes of small-scale food producers, in particular women, indigenous peoples, family farmers, pastoralists and fishers, including through secure and equal access to land, other productive resources and inputs, knowledge, financial services, markets and opportunities for value addition and non-farm employment",
        ),
    )
    BY_2030__ENSURE_SUSTAINABLE_FOOD_PRODUCTION_SYSTEMS_AND_IMPLEMENT_RESILIENT_AGRICULTURAL_PRACTICES_THAT_INCREASE_PRODUCTIVITY_AND_PRODUCTION__THAT_HELP_MAINTAIN_ECOSYSTEMS__THAT_STRENGTHEN_CAPACITY_FOR_ADAPTATION_TO_CLIMATE_CHANGE__EXTREME_WEATHER__DROUGHT__FLOODING_AND_OTHER_DISASTERS_AND_THAT_PROGRESSIVELY_IMPROVE_LAND_AND_SOIL_QUALITY = (
        "2.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure sustainable food production systems and implement resilient agricultural practices that increase productivity and production, that help maintain ecosystems, that strengthen capacity for adaptation to climate change, extreme weather, drought, flooding and other disasters and that progressively improve land and soil quality",
        ),
    )
    BY_2020__MAINTAIN_THE_GENETIC_DIVERSITY_OF_SEEDS__CULTIVATED_PLANTS_AND_FARMED_AND_DOMESTICATED_ANIMALS_AND_THEIR_RELATED_WILD_SPECIES__INCLUDING_THROUGH_SOUNDLY_MANAGED_AND_DIVERSIFIED_SEED_AND_PLANT_BANKS_AT_THE_NATIONAL__REGIONAL_AND_INTERNATIONAL_LEVELS__AND_PROMOTE_ACCESS_TO_AND_FAIR_AND_EQUITABLE_SHARING_OF_BENEFITS_ARISING_FROM_THE_UTILIZATION_OF_GENETIC_RESOURCES_AND_ASSOCIATED_TRADITIONAL_KNOWLEDGE__AS_INTERNATIONALLY_AGREED = (
        "2.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, maintain the genetic diversity of seeds, cultivated plants and farmed and domesticated animals and their related wild species, including through soundly managed and diversified seed and plant banks at the national, regional and international levels, and promote access to and fair and equitable sharing of benefits arising from the utilization of genetic resources and associated traditional knowledge, as internationally agreed",
        ),
    )
    INCREASE_INVESTMENT__INCLUDING_THROUGH_ENHANCED_INTERNATIONAL_COOPERATION__IN_RURAL_INFRASTRUCTURE__AGRICULTURAL_RESEARCH_AND_EXTENSION_SERVICES__TECHNOLOGY_DEVELOPMENT_AND_PLANT_AND_LIVESTOCK_GENE_BANKS_IN_ORDER_TO_ENHANCE_AGRICULTURAL_PRODUCTIVE_CAPACITY_IN_DEVELOPING_COUNTRIES__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES = (
        "2.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Increase investment, including through enhanced international cooperation, in rural infrastructure, agricultural research and extension services, technology development and plant and livestock gene banks in order to enhance agricultural productive capacity in developing countries, in particular least developed countries",
        ),
    )
    CORRECT_AND_PREVENT_TRADE_RESTRICTIONS_AND_DISTORTIONS_IN_WORLD_AGRICULTURAL_MARKETS__INCLUDING_THROUGH_THE_PARALLEL_ELIMINATION_OF_ALL_FORMS_OF_AGRICULTURAL_EXPORT_SUBSIDIES_AND_ALL_EXPORT_MEASURES_WITH_EQUIVALENT_EFFECT__IN_ACCORDANCE_WITH_THE_MANDATE_OF_THE_DOHA_DEVELOPMENT_ROUND = (
        "2.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Correct and prevent trade restrictions and distortions in world agricultural markets, including through the parallel elimination of all forms of agricultural export subsidies and all export measures with equivalent effect, in accordance with the mandate of the Doha Development Round",
        ),
    )
    ADOPT_MEASURES_TO_ENSURE_THE_PROPER_FUNCTIONING_OF_FOOD_COMMODITY_MARKETS_AND_THEIR_DERIVATIVES_AND_FACILITATE_TIMELY_ACCESS_TO_MARKET_INFORMATION__INCLUDING_ON_FOOD_RESERVES__IN_ORDER_TO_HELP_LIMIT_EXTREME_FOOD_PRICE_VOLATILITY = (
        "2.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Adopt measures to ensure the proper functioning of food commodity markets and their derivatives and facilitate timely access to market information, including on food reserves, in order to help limit extreme food price volatility",
        ),
    )
    BY_2030__REDUCE_THE_GLOBAL_MATERNAL_MORTALITY_RATIO_TO_LESS_THAN_70_PER_100_000_LIVE_BIRTHS = (
        "3.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, reduce the global maternal mortality ratio to less than 70 per 100,000 live births",
        ),
    )
    BY_2030__END_PREVENTABLE_DEATHS_OF_NEWBORNS_AND_CHILDREN_UNDER_5_YEARS_OF_AGE__WITH_ALL_COUNTRIES_AIMING_TO_REDUCE_NEONATAL_MORTALITY_TO_AT_LEAST_AS_LOW_AS_12_PER_1_000_LIVE_BIRTHS_AND_UNDER_5_MORTALITY_TO_AT_LEAST_AS_LOW_AS_25_PER_1_000_LIVE_BIRTHS = (
        "3.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, end preventable deaths of newborns and children under 5 years of age, with all countries aiming to reduce neonatal mortality to at least as low as 12 per 1,000 live births and under‑5 mortality to at least as low as 25 per 1,000 live births",
        ),
    )
    BY_2030__END_THE_EPIDEMICS_OF_AIDS__TUBERCULOSIS__MALARIA_AND_NEGLECTED_TROPICAL_DISEASES_AND_COMBAT_HEPATITIS__WATER_BORNE_DISEASES_AND_OTHER_COMMUNICABLE_DISEASES = (
        "3.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, end the epidemics of AIDS, tuberculosis, malaria and neglected tropical diseases and combat hepatitis, water-borne diseases and other communicable diseases",
        ),
    )
    BY_2030__REDUCE_BY_ONE_THIRD_PREMATURE_MORTALITY_FROM_NONCOMMUNICABLE_DISEASES_THROUGH_PREVENTION_AND_TREATMENT_AND_PROMOTE_MENTAL_HEALTH_AND_WELL_BEING = (
        "3.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being",
        ),
    )
    STRENGTHEN_THE_PREVENTION_AND_TREATMENT_OF_SUBSTANCE_ABUSE__INCLUDING_NARCOTIC_DRUG_ABUSE_AND_HARMFUL_USE_OF_ALCOHOL = (
        "3.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen the prevention and treatment of substance abuse, including narcotic drug abuse and harmful use of alcohol",
        ),
    )
    BY_2020__HALVE_THE_NUMBER_OF_GLOBAL_DEATHS_AND_INJURIES_FROM_ROAD_TRAFFIC_ACCIDENTS = (
        "3.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, halve the number of global deaths and injuries from road traffic accidents",
        ),
    )
    BY_2030__ENSURE_UNIVERSAL_ACCESS_TO_SEXUAL_AND_REPRODUCTIVE_HEALTHCARE_SERVICES__INCLUDING_FOR_FAMILY_PLANNING__INFORMATION_AND_EDUCATION__AND_THE_INTEGRATION_OF_REPRODUCTIVE_HEALTH_INTO_NATIONAL_STRATEGIES_AND_PROGRAMMES = (
        "3.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure universal access to sexual and reproductive health-care services, including for family planning, information and education, and the integration of reproductive health into national strategies and programmes",
        ),
    )
    ACHIEVE_UNIVERSAL_HEALTH_COVERAGE__INCLUDING_FINANCIAL_RISK_PROTECTION__ACCESS_TO_QUALITY_ESSENTIAL_HEALTHCARE_SERVICES_AND_ACCESS_TO_SAFE__EFFECTIVE__QUALITY_AND_AFFORDABLE_ESSENTIAL_MEDICINES_AND_VACCINES_FOR_ALL = (
        "3.8",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Achieve universal health coverage, including financial risk protection, access to quality essential health-care services and access to safe, effective, quality and affordable essential medicines and vaccines for all",
        ),
    )
    BY_2030__SUBSTANTIALLY_REDUCE_THE_NUMBER_OF_DEATHS_AND_ILLNESSES_FROM_HAZARDOUS_CHEMICALS_AND_AIR__WATER_AND_SOIL_POLLUTION_AND_CONTAMINATION = (
        "3.9",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, substantially reduce the number of deaths and illnesses from hazardous chemicals and air, water and soil pollution and contamination",
        ),
    )
    STRENGTHEN_THE_IMPLEMENTATION_OF_THE_WORLD_HEALTH_ORGANIZATION_FRAMEWORK_CONVENTION_ON_TOBACCO_CONTROL_IN_ALL_COUNTRIES__AS_APPROPRIATE = (
        "3.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen the implementation of the World Health Organization Framework Convention on Tobacco Control in all countries, as appropriate",
        ),
    )
    SUPPORT_THE_RESEARCH_AND_DEVELOPMENT_OF_VACCINES_AND_MEDICINES_FOR_THE_COMMUNICABLE_AND_NON_COMMUNICABLE_DISEASES_THAT_PRIMARILY_AFFECT_DEVELOPING_COUNTRIES__PROVIDE_ACCESS_TO_AFFORDABLE_ESSENTIAL_MEDICINES_AND_VACCINES__IN_ACCORDANCE_WITH_THE_DOHA_DECLARATION_ON_THE_TRIPS_AGREEMENT_AND_PUBLIC_HEALTH__WHICH_AFFIRMS_THE_RIGHT_OF_DEVELOPING_COUNTRIES_TO_USE_TO_THE_FULL_THE_PROVISIONS_IN_THE_AGREEMENT_ON_TRADE_RELATED_ASPECTS_OF_INTELLECTUAL_PROPERTY_RIGHTS_REGARDING_FLEXIBILITIES_TO_PROTECT_PUBLIC_HEALTH__AND__IN_PARTICULAR__PROVIDE_ACCESS_TO_MEDICINES_FOR_ALL = (
        "3.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Support the research and development of vaccines and medicines for the communicable and non‑communicable diseases that primarily affect developing countries, provide access to affordable essential medicines and vaccines, in accordance with the Doha Declaration on the TRIPS Agreement and Public Health, which affirms the right of developing countries to use to the full the provisions in the Agreement on Trade-Related Aspects of Intellectual Property Rights regarding flexibilities to protect public health, and, in particular, provide access to medicines for all",
        ),
    )
    SUBSTANTIALLY_INCREASE_HEALTH_FINANCING_AND_THE_RECRUITMENT__DEVELOPMENT__TRAINING_AND_RETENTION_OF_THE_HEALTH_WORKFORCE_IN_DEVELOPING_COUNTRIES__ESPECIALLY_IN_LEAST_DEVELOPED_COUNTRIES_AND_SMALL_ISLAND_DEVELOPING_STATES = (
        "3.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Substantially increase health financing and the recruitment, development, training and retention of the health workforce in developing countries, especially in least developed countries and small island developing States",
        ),
    )
    STRENGTHEN_THE_CAPACITY_OF_ALL_COUNTRIES__IN_PARTICULAR_DEVELOPING_COUNTRIES__FOR_EARLY_WARNING__RISK_REDUCTION_AND_MANAGEMENT_OF_NATIONAL_AND_GLOBAL_HEALTH_RISKS = (
        "3.d",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen the capacity of all countries, in particular developing countries, for early warning, risk reduction and management of national and global health risks",
        ),
    )
    BY_2030__ENSURE_THAT_ALL_GIRLS_AND_BOYS_COMPLETE_FREE__EQUITABLE_AND_QUALITY_PRIMARY_AND_SECONDARY_EDUCATION_LEADING_TO_RELEVANT_AND_EFFECTIVE_LEARNING_OUTCOMES = (
        "4.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure that all girls and boys complete free, equitable and quality primary and secondary education leading to relevant and effective learning outcomes",
        ),
    )
    BY_2030__ENSURE_THAT_ALL_GIRLS_AND_BOYS_HAVE_ACCESS_TO_QUALITY_EARLY_CHILDHOOD_DEVELOPMENT__CARE_AND_PRE_PRIMARY_EDUCATION_SO_THAT_THEY_ARE_READY_FOR_PRIMARY_EDUCATION = (
        "4.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure that all girls and boys have access to quality early childhood development, care and pre‑primary education so that they are ready for primary education",
        ),
    )
    BY_2030__ENSURE_EQUAL_ACCESS_FOR_ALL_WOMEN_AND_MEN_TO_AFFORDABLE_AND_QUALITY_TECHNICAL__VOCATIONAL_AND_TERTIARY_EDUCATION__INCLUDING_UNIVERSITY = (
        "4.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure equal access for all women and men to affordable and quality technical, vocational and tertiary education, including university",
        ),
    )
    BY_2030__SUBSTANTIALLY_INCREASE_THE_NUMBER_OF_YOUTH_AND_ADULTS_WHO_HAVE_RELEVANT_SKILLS__INCLUDING_TECHNICAL_AND_VOCATIONAL_SKILLS__FOR_EMPLOYMENT__DECENT_JOBS_AND_ENTREPRENEURSHIP = (
        "4.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, substantially increase the number of youth and adults who have relevant skills, including technical and vocational skills, for employment, decent jobs and entrepreneurship",
        ),
    )
    BY_2030__ELIMINATE_GENDER_DISPARITIES_IN_EDUCATION_AND_ENSURE_EQUAL_ACCESS_TO_ALL_LEVELS_OF_EDUCATION_AND_VOCATIONAL_TRAINING_FOR_THE_VULNERABLE__INCLUDING_PERSONS_WITH_DISABILITIES__INDIGENOUS_PEOPLES_AND_CHILDREN_IN_VULNERABLE_SITUATIONS = (
        "4.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, eliminate gender disparities in education and ensure equal access to all levels of education and vocational training for the vulnerable, including persons with disabilities, indigenous peoples and children in vulnerable situations",
        ),
    )
    BY_2030__ENSURE_THAT_ALL_YOUTH_AND_A_SUBSTANTIAL_PROPORTION_OF_ADULTS__BOTH_MEN_AND_WOMEN__ACHIEVE_LITERACY_AND_NUMERACY = (
        "4.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure that all youth and a substantial proportion of adults, both men and women, achieve literacy and numeracy",
        ),
    )
    BY_2030__ENSURE_THAT_ALL_LEARNERS_ACQUIRE_THE_KNOWLEDGE_AND_SKILLS_NEEDED_TO_PROMOTE_SUSTAINABLE_DEVELOPMENT__INCLUDING__AMONG_OTHERS__THROUGH_EDUCATION_FOR_SUSTAINABLE_DEVELOPMENT_AND_SUSTAINABLE_LIFESTYLES__HUMAN_RIGHTS__GENDER_EQUALITY__PROMOTION_OF_A_CULTURE_OF_PEACE_AND_NON_VIOLENCE__GLOBAL_CITIZENSHIP_AND_APPRECIATION_OF_CULTURAL_DIVERSITY_AND_OF_CULTURE_S_CONTRIBUTION_TO_SUSTAINABLE_DEVELOPMENT = (
        "4.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure that all learners acquire the knowledge and skills needed to promote sustainable development, including, among others, through education for sustainable development and sustainable lifestyles, human rights, gender equality, promotion of a culture of peace and non-violence, global citizenship and appreciation of cultural diversity and of culture’s contribution to sustainable development",
        ),
    )
    BUILD_AND_UPGRADE_EDUCATION_FACILITIES_THAT_ARE_CHILD__DISABILITY_AND_GENDER_SENSITIVE_AND_PROVIDE_SAFE__NON_VIOLENT__INCLUSIVE_AND_EFFECTIVE_LEARNING_ENVIRONMENTS_FOR_ALL = (
        "4.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Build and upgrade education facilities that are child, disability and gender sensitive and provide safe, non-violent, inclusive and effective learning environments for all",
        ),
    )
    BY_2020__SUBSTANTIALLY_EXPAND_GLOBALLY_THE_NUMBER_OF_SCHOLARSHIPS_AVAILABLE_TO_DEVELOPING_COUNTRIES__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES__SMALL_ISLAND_DEVELOPING_STATES_AND_AFRICAN_COUNTRIES__FOR_ENROLMENT_IN_HIGHER_EDUCATION__INCLUDING_VOCATIONAL_TRAINING_AND_INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY__TECHNICAL__ENGINEERING_AND_SCIENTIFIC_PROGRAMMES__IN_DEVELOPED_COUNTRIES_AND_OTHER_DEVELOPING_COUNTRIES = (
        "4.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, substantially expand globally the number of scholarships available to developing countries, in particular least developed countries, small island developing States and African countries, for enrolment in higher education, including vocational training and information and communications technology, technical, engineering and scientific programmes, in developed countries and other developing countries",
        ),
    )
    BY_2030__SUBSTANTIALLY_INCREASE_THE_SUPPLY_OF_QUALIFIED_TEACHERS__INCLUDING_THROUGH_INTERNATIONAL_COOPERATION_FOR_TEACHER_TRAINING_IN_DEVELOPING_COUNTRIES__ESPECIALLY_LEAST_DEVELOPED_COUNTRIES_AND_SMALL_ISLAND_DEVELOPING_STATES = (
        "4.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, substantially increase the supply of qualified teachers, including through international cooperation for teacher training in developing countries, especially least developed countries and small island developing States",
        ),
    )
    END_ALL_FORMS_OF_DISCRIMINATION_AGAINST_ALL_WOMEN_AND_GIRLS_EVERYWHERE = (
        "5.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "End all forms of discrimination against all women and girls everywhere",
        ),
    )
    ELIMINATE_ALL_FORMS_OF_VIOLENCE_AGAINST_ALL_WOMEN_AND_GIRLS_IN_THE_PUBLIC_AND_PRIVATE_SPHERES__INCLUDING_TRAFFICKING_AND_SEXUAL_AND_OTHER_TYPES_OF_EXPLOITATION = (
        "5.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Eliminate all forms of violence against all women and girls in the public and private spheres, including trafficking and sexual and other types of exploitation",
        ),
    )
    ELIMINATE_ALL_HARMFUL_PRACTICES__SUCH_AS_CHILD__EARLY_AND_FORCED_MARRIAGE_AND_FEMALE_GENITAL_MUTILATION = (
        "5.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Eliminate all harmful practices, such as child, early and forced marriage and female genital mutilation",
        ),
    )
    RECOGNIZE_AND_VALUE_UNPAID_CARE_AND_DOMESTIC_WORK_THROUGH_THE_PROVISION_OF_PUBLIC_SERVICES__INFRASTRUCTURE_AND_SOCIAL_PROTECTION_POLICIES_AND_THE_PROMOTION_OF_SHARED_RESPONSIBILITY_WITHIN_THE_HOUSEHOLD_AND_THE_FAMILY_AS_NATIONALLY_APPROPRIATE = (
        "5.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Recognize and value unpaid care and domestic work through the provision of public services, infrastructure and social protection policies and the promotion of shared responsibility within the household and the family as nationally appropriate",
        ),
    )
    ENSURE_WOMEN_S_FULL_AND_EFFECTIVE_PARTICIPATION_AND_EQUAL_OPPORTUNITIES_FOR_LEADERSHIP_AT_ALL_LEVELS_OF_DECISION_MAKING_IN_POLITICAL__ECONOMIC_AND_PUBLIC_LIFE = (
        "5.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure women’s full and effective participation and equal opportunities for leadership at all levels of decision-making in political, economic and public life",
        ),
    )
    ENSURE_UNIVERSAL_ACCESS_TO_SEXUAL_AND_REPRODUCTIVE_HEALTH_AND_REPRODUCTIVE_RIGHTS_AS_AGREED_IN_ACCORDANCE_WITH_THE_PROGRAMME_OF_ACTION_OF_THE_INTERNATIONAL_CONFERENCE_ON_POPULATION_AND_DEVELOPMENT_AND_THE_BEIJING_PLATFORM_FOR_ACTION_AND_THE_OUTCOME_DOCUMENTS_OF_THEIR_REVIEW_CONFERENCES = (
        "5.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure universal access to sexual and reproductive health and reproductive rights as agreed in accordance with the Programme of Action of the International Conference on Population and Development and the Beijing Platform for Action and the outcome documents of their review conferences",
        ),
    )
    UNDERTAKE_REFORMS_TO_GIVE_WOMEN_EQUAL_RIGHTS_TO_ECONOMIC_RESOURCES__AS_WELL_AS_ACCESS_TO_OWNERSHIP_AND_CONTROL_OVER_LAND_AND_OTHER_FORMS_OF_PROPERTY__FINANCIAL_SERVICES__INHERITANCE_AND_NATURAL_RESOURCES__IN_ACCORDANCE_WITH_NATIONAL_LAWS = (
        "5.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Undertake reforms to give women equal rights to economic resources, as well as access to ownership and control over land and other forms of property, financial services, inheritance and natural resources, in accordance with national laws",
        ),
    )
    ENHANCE_THE_USE_OF_ENABLING_TECHNOLOGY__IN_PARTICULAR_INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY__TO_PROMOTE_THE_EMPOWERMENT_OF_WOMEN = (
        "5.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance the use of enabling technology, in particular information and communications technology, to promote the empowerment of women",
        ),
    )
    ADOPT_AND_STRENGTHEN_SOUND_POLICIES_AND_ENFORCEABLE_LEGISLATION_FOR_THE_PROMOTION_OF_GENDER_EQUALITY_AND_THE_EMPOWERMENT_OF_ALL_WOMEN_AND_GIRLS_AT_ALL_LEVELS = (
        "5.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Adopt and strengthen sound policies and enforceable legislation for the promotion of gender equality and the empowerment of all women and girls at all levels",
        ),
    )
    BY_2030__ACHIEVE_UNIVERSAL_AND_EQUITABLE_ACCESS_TO_SAFE_AND_AFFORDABLE_DRINKING_WATER_FOR_ALL = (
        "6.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, achieve universal and equitable access to safe and affordable drinking water for all",
        ),
    )
    BY_2030__ACHIEVE_ACCESS_TO_ADEQUATE_AND_EQUITABLE_SANITATION_AND_HYGIENE_FOR_ALL_AND_END_OPEN_DEFECATION__PAYING_SPECIAL_ATTENTION_TO_THE_NEEDS_OF_WOMEN_AND_GIRLS_AND_THOSE_IN_VULNERABLE_SITUATIONS = (
        "6.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, achieve access to adequate and equitable sanitation and hygiene for all and end open defecation, paying special attention to the needs of women and girls and those in vulnerable situations",
        ),
    )
    BY_2030__IMPROVE_WATER_QUALITY_BY_REDUCING_POLLUTION__ELIMINATING_DUMPING_AND_MINIMIZING_RELEASE_OF_HAZARDOUS_CHEMICALS_AND_MATERIALS__HALVING_THE_PROPORTION_OF_UNTREATED_WASTEWATER_AND_SUBSTANTIALLY_INCREASING_RECYCLING_AND_SAFE_REUSE_GLOBALLY = (
        "6.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, improve water quality by reducing pollution, eliminating dumping and minimizing release of hazardous chemicals and materials, halving the proportion of untreated wastewater and substantially increasing recycling and safe reuse globally",
        ),
    )
    BY_2030__SUBSTANTIALLY_INCREASE_WATER_USE_EFFICIENCY_ACROSS_ALL_SECTORS_AND_ENSURE_SUSTAINABLE_WITHDRAWALS_AND_SUPPLY_OF_FRESHWATER_TO_ADDRESS_WATER_SCARCITY_AND_SUBSTANTIALLY_REDUCE_THE_NUMBER_OF_PEOPLE_SUFFERING_FROM_WATER_SCARCITY = (
        "6.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, substantially increase water-use efficiency across all sectors and ensure sustainable withdrawals and supply of freshwater to address water scarcity and substantially reduce the number of people suffering from water scarcity",
        ),
    )
    BY_2030__IMPLEMENT_INTEGRATED_WATER_RESOURCES_MANAGEMENT_AT_ALL_LEVELS__INCLUDING_THROUGH_TRANSBOUNDARY_COOPERATION_AS_APPROPRIATE = (
        "6.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, implement integrated water resources management at all levels, including through transboundary cooperation as appropriate",
        ),
    )
    BY_2020__PROTECT_AND_RESTORE_WATER_RELATED_ECOSYSTEMS__INCLUDING_MOUNTAINS__FORESTS__WETLANDS__RIVERS__AQUIFERS_AND_LAKES = (
        "6.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, protect and restore water-related ecosystems, including mountains, forests, wetlands, rivers, aquifers and lakes",
        ),
    )
    BY_2030__EXPAND_INTERNATIONAL_COOPERATION_AND_CAPACITY_BUILDING_SUPPORT_TO_DEVELOPING_COUNTRIES_IN_WATER_AND_SANITATION_RELATED_ACTIVITIES_AND_PROGRAMMES__INCLUDING_WATER_HARVESTING__DESALINATION__WATER_EFFICIENCY__WASTEWATER_TREATMENT__RECYCLING_AND_REUSE_TECHNOLOGIES = (
        "6.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, expand international cooperation and capacity-building support to developing countries in water- and sanitation-related activities and programmes, including water harvesting, desalination, water efficiency, wastewater treatment, recycling and reuse technologies",
        ),
    )
    SUPPORT_AND_STRENGTHEN_THE_PARTICIPATION_OF_LOCAL_COMMUNITIES_IN_IMPROVING_WATER_AND_SANITATION_MANAGEMENT = (
        "6.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Support and strengthen the participation of local communities in improving water and sanitation management",
        ),
    )
    BY_2030__ENSURE_UNIVERSAL_ACCESS_TO_AFFORDABLE__RELIABLE_AND_MODERN_ENERGY_SERVICES = (
        "7.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure universal access to affordable, reliable and modern energy services",
        ),
    )
    BY_2030__INCREASE_SUBSTANTIALLY_THE_SHARE_OF_RENEWABLE_ENERGY_IN_THE_GLOBAL_ENERGY_MIX = (
        "7.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, increase substantially the share of renewable energy in the global energy mix",
        ),
    )
    BY_2030__DOUBLE_THE_GLOBAL_RATE_OF_IMPROVEMENT_IN_ENERGY_EFFICIENCY = (
        "7.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, double the global rate of improvement in energy efficiency",
        ),
    )
    BY_2030__ENHANCE_INTERNATIONAL_COOPERATION_TO_FACILITATE_ACCESS_TO_CLEAN_ENERGY_RESEARCH_AND_TECHNOLOGY__INCLUDING_RENEWABLE_ENERGY__ENERGY_EFFICIENCY_AND_ADVANCED_AND_CLEANER_FOSSIL_FUEL_TECHNOLOGY__AND_PROMOTE_INVESTMENT_IN_ENERGY_INFRASTRUCTURE_AND_CLEAN_ENERGY_TECHNOLOGY = (
        "7.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, enhance international cooperation to facilitate access to clean energy research and technology, including renewable energy, energy efficiency and advanced and cleaner fossil-fuel technology, and promote investment in energy infrastructure and clean energy technology",
        ),
    )
    BY_2030__EXPAND_INFRASTRUCTURE_AND_UPGRADE_TECHNOLOGY_FOR_SUPPLYING_MODERN_AND_SUSTAINABLE_ENERGY_SERVICES_FOR_ALL_IN_DEVELOPING_COUNTRIES__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES__SMALL_ISLAND_DEVELOPING_STATES_AND_LANDLOCKED_DEVELOPING_COUNTRIES__IN_ACCORDANCE_WITH_THEIR_RESPECTIVE_PROGRAMMES_OF_SUPPORT = (
        "7.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, expand infrastructure and upgrade technology for supplying modern and sustainable energy services for all in developing countries, in particular least developed countries, small island developing States and landlocked developing countries, in accordance with their respective programmes of support",
        ),
    )
    SUSTAIN_PER_CAPITA_ECONOMIC_GROWTH_IN_ACCORDANCE_WITH_NATIONAL_CIRCUMSTANCES_AND__IN_PARTICULAR__AT_LEAST_7_PER_CENT_GROSS_DOMESTIC_PRODUCT_GROWTH_PER_ANNUM_IN_THE_LEAST_DEVELOPED_COUNTRIES = (
        "8.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Sustain per capita economic growth in accordance with national circumstances and, in particular, at least 7 per cent gross domestic product growth per annum in the least developed countries",
        ),
    )
    ACHIEVE_HIGHER_LEVELS_OF_ECONOMIC_PRODUCTIVITY_THROUGH_DIVERSIFICATION__TECHNOLOGICAL_UPGRADING_AND_INNOVATION__INCLUDING_THROUGH_A_FOCUS_ON_HIGH_VALUE_ADDED_AND_LABOUR_INTENSIVE_SECTORS = (
        "8.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Achieve higher levels of economic productivity through diversification, technological upgrading and innovation, including through a focus on high-value added and labour-intensive sectors",
        ),
    )
    PROMOTE_DEVELOPMENT_ORIENTED_POLICIES_THAT_SUPPORT_PRODUCTIVE_ACTIVITIES__DECENT_JOB_CREATION__ENTREPRENEURSHIP__CREATIVITY_AND_INNOVATION__AND_ENCOURAGE_THE_FORMALIZATION_AND_GROWTH_OF_MICRO___SMALL_AND_MEDIUM_SIZED_ENTERPRISES__INCLUDING_THROUGH_ACCESS_TO_FINANCIAL_SERVICES = (
        "8.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote development-oriented policies that support productive activities, decent job creation, entrepreneurship, creativity and innovation, and encourage the formalization and growth of micro-, small- and medium-sized enterprises, including through access to financial services",
        ),
    )
    IMPROVE_PROGRESSIVELY__THROUGH_2030__GLOBAL_RESOURCE_EFFICIENCY_IN_CONSUMPTION_AND_PRODUCTION_AND_ENDEAVOUR_TO_DECOUPLE_ECONOMIC_GROWTH_FROM_ENVIRONMENTAL_DEGRADATION__IN_ACCORDANCE_WITH_THE_10_YEAR_FRAMEWORK_OF_PROGRAMMES_ON_SUSTAINABLE_CONSUMPTION_AND_PRODUCTION__WITH_DEVELOPED_COUNTRIES_TAKING_THE_LEAD = (
        "8.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Improve progressively, through 2030, global resource efficiency in consumption and production and endeavour to decouple economic growth from environmental degradation, in accordance with the 10‑Year Framework of Programmes on Sustainable Consumption and Production, with developed countries taking the lead",
        ),
    )
    BY_2030__ACHIEVE_FULL_AND_PRODUCTIVE_EMPLOYMENT_AND_DECENT_WORK_FOR_ALL_WOMEN_AND_MEN__INCLUDING_FOR_YOUNG_PEOPLE_AND_PERSONS_WITH_DISABILITIES__AND_EQUAL_PAY_FOR_WORK_OF_EQUAL_VALUE = (
        "8.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, achieve full and productive employment and decent work for all women and men, including for young people and persons with disabilities, and equal pay for work of equal value",
        ),
    )
    BY_2020__SUBSTANTIALLY_REDUCE_THE_PROPORTION_OF_YOUTH_NOT_IN_EMPLOYMENT__EDUCATION_OR_TRAINING = (
        "8.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, substantially reduce the proportion of youth not in employment, education or training",
        ),
    )
    TAKE_IMMEDIATE_AND_EFFECTIVE_MEASURES_TO_ERADICATE_FORCED_LABOUR__END_MODERN_SLAVERY_AND_HUMAN_TRAFFICKING_AND_SECURE_THE_PROHIBITION_AND_ELIMINATION_OF_THE_WORST_FORMS_OF_CHILD_LABOUR__INCLUDING_RECRUITMENT_AND_USE_OF_CHILD_SOLDIERS__AND_BY_2025_END_CHILD_LABOUR_IN_ALL_ITS_FORMS = (
        "8.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Take immediate and effective measures to eradicate forced labour, end modern slavery and human trafficking and secure the prohibition and elimination of the worst forms of child labour, including recruitment and use of child soldiers, and by 2025 end child labour in all its forms ",
        ),
    )
    PROTECT_LABOUR_RIGHTS_AND_PROMOTE_SAFE_AND_SECURE_WORKING_ENVIRONMENTS_FOR_ALL_WORKERS__INCLUDING_MIGRANT_WORKERS__IN_PARTICULAR_WOMEN_MIGRANTS__AND_THOSE_IN_PRECARIOUS_EMPLOYMENT = (
        "8.8",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Protect labour rights and promote safe and secure working environments for all workers, including migrant workers, in particular women migrants, and those in precarious employment",
        ),
    )
    BY_2030__DEVISE_AND_IMPLEMENT_POLICIES_TO_PROMOTE_SUSTAINABLE_TOURISM_THAT_CREATES_JOBS_AND_PROMOTES_LOCAL_CULTURE_AND_PRODUCTS = (
        "8.9",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, devise and implement policies to promote sustainable tourism that creates jobs and promotes local culture and products",
        ),
    )
    STRENGTHEN_THE_CAPACITY_OF_DOMESTIC_FINANCIAL_INSTITUTIONS_TO_ENCOURAGE_AND_EXPAND_ACCESS_TO_BANKING__INSURANCE_AND_FINANCIAL_SERVICES_FOR_ALL = (
        "8.10",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen the capacity of domestic financial institutions to encourage and expand access to banking, insurance and financial services for all",
        ),
    )
    INCREASE_AID_FOR_TRADE_SUPPORT_FOR_DEVELOPING_COUNTRIES__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES__INCLUDING_THROUGH_THE_ENHANCED_INTEGRATED_FRAMEWORK_FOR_TRADE_RELATED_TECHNICAL_ASSISTANCE_TO_LEAST_DEVELOPED_COUNTRIES = (
        "8.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Increase Aid for Trade support for developing countries, in particular least developed countries, including through the Enhanced Integrated Framework for Trade-related Technical Assistance to Least Developed Countries",
        ),
    )
    BY_2020__DEVELOP_AND_OPERATIONALIZE_A_GLOBAL_STRATEGY_FOR_YOUTH_EMPLOYMENT_AND_IMPLEMENT_THE_GLOBAL_JOBS_PACT_OF_THE_INTERNATIONAL_LABOUR_ORGANIZATION = (
        "8.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, develop and operationalize a global strategy for youth employment and implement the Global Jobs Pact of the International Labour Organization",
        ),
    )
    DEVELOP_QUALITY__RELIABLE__SUSTAINABLE_AND_RESILIENT_INFRASTRUCTURE__INCLUDING_REGIONAL_AND_TRANSBORDER_INFRASTRUCTURE__TO_SUPPORT_ECONOMIC_DEVELOPMENT_AND_HUMAN_WELL_BEING__WITH_A_FOCUS_ON_AFFORDABLE_AND_EQUITABLE_ACCESS_FOR_ALL = (
        "9.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Develop quality, reliable, sustainable and resilient infrastructure, including regional and transborder infrastructure, to support economic development and human well-being, with a focus on affordable and equitable access for all",
        ),
    )
    PROMOTE_INCLUSIVE_AND_SUSTAINABLE_INDUSTRIALIZATION_AND__BY_2030__SIGNIFICANTLY_RAISE_INDUSTRY_S_SHARE_OF_EMPLOYMENT_AND_GROSS_DOMESTIC_PRODUCT__IN_LINE_WITH_NATIONAL_CIRCUMSTANCES__AND_DOUBLE_ITS_SHARE_IN_LEAST_DEVELOPED_COUNTRIES = (
        "9.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote inclusive and sustainable industrialization and, by 2030, significantly raise industry’s share of employment and gross domestic product, in line with national circumstances, and double its share in least developed countries",
        ),
    )
    INCREASE_THE_ACCESS_OF_SMALL_SCALE_INDUSTRIAL_AND_OTHER_ENTERPRISES__IN_PARTICULAR_IN_DEVELOPING_COUNTRIES__TO_FINANCIAL_SERVICES__INCLUDING_AFFORDABLE_CREDIT__AND_THEIR_INTEGRATION_INTO_VALUE_CHAINS_AND_MARKETS = (
        "9.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Increase the access of small-scale industrial and other enterprises, in particular in developing countries, to financial services, including affordable credit, and their integration into value chains and markets",
        ),
    )
    BY_2030__UPGRADE_INFRASTRUCTURE_AND_RETROFIT_INDUSTRIES_TO_MAKE_THEM_SUSTAINABLE__WITH_INCREASED_RESOURCE_USE_EFFICIENCY_AND_GREATER_ADOPTION_OF_CLEAN_AND_ENVIRONMENTALLY_SOUND_TECHNOLOGIES_AND_INDUSTRIAL_PROCESSES__WITH_ALL_COUNTRIES_TAKING_ACTION_IN_ACCORDANCE_WITH_THEIR_RESPECTIVE_CAPABILITIES = (
        "9.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, upgrade infrastructure and retrofit industries to make them sustainable, with increased resource-use efficiency and greater adoption of clean and environmentally sound technologies and industrial processes, with all countries taking action in accordance with their respective capabilities",
        ),
    )
    ENHANCE_SCIENTIFIC_RESEARCH__UPGRADE_THE_TECHNOLOGICAL_CAPABILITIES_OF_INDUSTRIAL_SECTORS_IN_ALL_COUNTRIES__IN_PARTICULAR_DEVELOPING_COUNTRIES__INCLUDING__BY_2030__ENCOURAGING_INNOVATION_AND_SUBSTANTIALLY_INCREASING_THE_NUMBER_OF_RESEARCH_AND_DEVELOPMENT_WORKERS_PER_1_MILLION_PEOPLE_AND_PUBLIC_AND_PRIVATE_RESEARCH_AND_DEVELOPMENT_SPENDING = (
        "9.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance scientific research, upgrade the technological capabilities of industrial sectors in all countries, in particular developing countries, including, by 2030, encouraging innovation and substantially increasing the number of research and development workers per 1 million people and public and private research and development spending",
        ),
    )
    FACILITATE_SUSTAINABLE_AND_RESILIENT_INFRASTRUCTURE_DEVELOPMENT_IN_DEVELOPING_COUNTRIES_THROUGH_ENHANCED_FINANCIAL__TECHNOLOGICAL_AND_TECHNICAL_SUPPORT_TO_AFRICAN_COUNTRIES__LEAST_DEVELOPED_COUNTRIES__LANDLOCKED_DEVELOPING_COUNTRIES_AND_SMALL_ISLAND_DEVELOPING_STATES = (
        "9.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Facilitate sustainable and resilient infrastructure development in developing countries through enhanced financial, technological and technical support to African countries, least developed countries, landlocked developing countries and small island developing States",
        ),
    )
    SUPPORT_DOMESTIC_TECHNOLOGY_DEVELOPMENT__RESEARCH_AND_INNOVATION_IN_DEVELOPING_COUNTRIES__INCLUDING_BY_ENSURING_A_CONDUCIVE_POLICY_ENVIRONMENT_FOR__INTER_ALIA__INDUSTRIAL_DIVERSIFICATION_AND_VALUE_ADDITION_TO_COMMODITIES = (
        "9.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Support domestic technology development, research and innovation in developing countries, including by ensuring a conducive policy environment for, inter alia, industrial diversification and value addition to commodities",
        ),
    )
    SIGNIFICANTLY_INCREASE_ACCESS_TO_INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY_AND_STRIVE_TO_PROVIDE_UNIVERSAL_AND_AFFORDABLE_ACCESS_TO_THE_INTERNET_IN_LEAST_DEVELOPED_COUNTRIES_BY_2020 = (
        "9.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Significantly increase access to information and communications technology and strive to provide universal and affordable access to the Internet in least developed countries by 2020",
        ),
    )
    BY_2030__PROGRESSIVELY_ACHIEVE_AND_SUSTAIN_INCOME_GROWTH_OF_THE_BOTTOM_40_PER_CENT_OF_THE_POPULATION_AT_A_RATE_HIGHER_THAN_THE_NATIONAL_AVERAGE = (
        "10.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, progressively achieve and sustain income growth of the bottom 40 per cent of the population at a rate higher than the national average",
        ),
    )
    BY_2030__EMPOWER_AND_PROMOTE_THE_SOCIAL__ECONOMIC_AND_POLITICAL_INCLUSION_OF_ALL__IRRESPECTIVE_OF_AGE__SEX__DISABILITY__RACE__ETHNICITY__ORIGIN__RELIGION_OR_ECONOMIC_OR_OTHER_STATUS = (
        "10.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, empower and promote the social, economic and political inclusion of all, irrespective of age, sex, disability, race, ethnicity, origin, religion or economic or other status",
        ),
    )
    ENSURE_EQUAL_OPPORTUNITY_AND_REDUCE_INEQUALITIES_OF_OUTCOME__INCLUDING_BY_ELIMINATING_DISCRIMINATORY_LAWS__POLICIES_AND_PRACTICES_AND_PROMOTING_APPROPRIATE_LEGISLATION__POLICIES_AND_ACTION_IN_THIS_REGARD = (
        "10.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure equal opportunity and reduce inequalities of outcome, including by eliminating discriminatory laws, policies and practices and promoting appropriate legislation, policies and action in this regard",
        ),
    )
    ADOPT_POLICIES__ESPECIALLY_FISCAL__WAGE_AND_SOCIAL_PROTECTION_POLICIES__AND_PROGRESSIVELY_ACHIEVE_GREATER_EQUALITY = (
        "10.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Adopt policies, especially fiscal, wage and social protection policies, and progressively achieve greater equality",
        ),
    )
    IMPROVE_THE_REGULATION_AND_MONITORING_OF_GLOBAL_FINANCIAL_MARKETS_AND_INSTITUTIONS_AND_STRENGTHEN_THE_IMPLEMENTATION_OF_SUCH_REGULATIONS = (
        "10.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Improve the regulation and monitoring of global financial markets and institutions and strengthen the implementation of such regulations",
        ),
    )
    ENSURE_ENHANCED_REPRESENTATION_AND_VOICE_FOR_DEVELOPING_COUNTRIES_IN_DECISION_MAKING_IN_GLOBAL_INTERNATIONAL_ECONOMIC_AND_FINANCIAL_INSTITUTIONS_IN_ORDER_TO_DELIVER_MORE_EFFECTIVE__CREDIBLE__ACCOUNTABLE_AND_LEGITIMATE_INSTITUTIONS = (
        "10.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure enhanced representation and voice for developing countries in decision-making in global international economic and financial institutions in order to deliver more effective, credible, accountable and legitimate institutions",
        ),
    )
    FACILITATE_ORDERLY__SAFE__REGULAR_AND_RESPONSIBLE_MIGRATION_AND_MOBILITY_OF_PEOPLE__INCLUDING_THROUGH_THE_IMPLEMENTATION_OF_PLANNED_AND_WELL_MANAGED_MIGRATION_POLICIES = (
        "10.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Facilitate orderly, safe, regular and responsible migration and mobility of people, including through the implementation of planned and well-managed migration policies",
        ),
    )
    IMPLEMENT_THE_PRINCIPLE_OF_SPECIAL_AND_DIFFERENTIAL_TREATMENT_FOR_DEVELOPING_COUNTRIES__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES__IN_ACCORDANCE_WITH_WORLD_TRADE_ORGANIZATION_AGREEMENTS = (
        "10.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Implement the principle of special and differential treatment for developing countries, in particular least developed countries, in accordance with World Trade Organization agreements",
        ),
    )
    ENCOURAGE_OFFICIAL_DEVELOPMENT_ASSISTANCE_AND_FINANCIAL_FLOWS__INCLUDING_FOREIGN_DIRECT_INVESTMENT__TO_STATES_WHERE_THE_NEED_IS_GREATEST__IN_PARTICULAR_LEAST_DEVELOPED_COUNTRIES__AFRICAN_COUNTRIES__SMALL_ISLAND_DEVELOPING_STATES_AND_LANDLOCKED_DEVELOPING_COUNTRIES__IN_ACCORDANCE_WITH_THEIR_NATIONAL_PLANS_AND_PROGRAMMES = (
        "10.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Encourage official development assistance and financial flows, including foreign direct investment, to States where the need is greatest, in particular least developed countries, African countries, small island developing States and landlocked developing countries, in accordance with their national plans and programmes",
        ),
    )
    BY_2030__REDUCE_TO_LESS_THAN_3_PER_CENT_THE_TRANSACTION_COSTS_OF_MIGRANT_REMITTANCES_AND_ELIMINATE_REMITTANCE_CORRIDORS_WITH_COSTS_HIGHER_THAN_5_PER_CENT = (
        "10.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, reduce to less than 3 per cent the transaction costs of migrant remittances and eliminate remittance corridors with costs higher than 5 per cent",
        ),
    )
    BY_2030__ENSURE_ACCESS_FOR_ALL_TO_ADEQUATE__SAFE_AND_AFFORDABLE_HOUSING_AND_BASIC_SERVICES_AND_UPGRADE_SLUMS = (
        "11.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure access for all to adequate, safe and affordable housing and basic services and upgrade slums",
        ),
    )
    BY_2030__PROVIDE_ACCESS_TO_SAFE__AFFORDABLE__ACCESSIBLE_AND_SUSTAINABLE_TRANSPORT_SYSTEMS_FOR_ALL__IMPROVING_ROAD_SAFETY__NOTABLY_BY_EXPANDING_PUBLIC_TRANSPORT__WITH_SPECIAL_ATTENTION_TO_THE_NEEDS_OF_THOSE_IN_VULNERABLE_SITUATIONS__WOMEN__CHILDREN__PERSONS_WITH_DISABILITIES_AND_OLDER_PERSONS = (
        "11.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, provide access to safe, affordable, accessible and sustainable transport systems for all, improving road safety, notably by expanding public transport, with special attention to the needs of those in vulnerable situations, women, children, persons with disabilities and older persons",
        ),
    )
    BY_2030__ENHANCE_INCLUSIVE_AND_SUSTAINABLE_URBANIZATION_AND_CAPACITY_FOR_PARTICIPATORY__INTEGRATED_AND_SUSTAINABLE_HUMAN_SETTLEMENT_PLANNING_AND_MANAGEMENT_IN_ALL_COUNTRIES = (
        "11.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, enhance inclusive and sustainable urbanization and capacity for participatory, integrated and sustainable human settlement planning and management in all countries",
        ),
    )
    STRENGTHEN_EFFORTS_TO_PROTECT_AND_SAFEGUARD_THE_WORLD_S_CULTURAL_AND_NATURAL_HERITAGE = (
        "11.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen efforts to protect and safeguard the world’s cultural and natural heritage",
        ),
    )
    BY_2030__SIGNIFICANTLY_REDUCE_THE_NUMBER_OF_DEATHS_AND_THE_NUMBER_OF_PEOPLE_AFFECTED_AND_SUBSTANTIALLY_DECREASE_THE_DIRECT_ECONOMIC_LOSSES_RELATIVE_TO_GLOBAL_GROSS_DOMESTIC_PRODUCT_CAUSED_BY_DISASTERS__INCLUDING_WATER_RELATED_DISASTERS__WITH_A_FOCUS_ON_PROTECTING_THE_POOR_AND_PEOPLE_IN_VULNERABLE_SITUATIONS = (
        "11.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, significantly reduce the number of deaths and the number of people affected and substantially decrease the direct economic losses relative to global gross domestic product caused by disasters, including water-related disasters, with a focus on protecting the poor and people in vulnerable situations",
        ),
    )
    BY_2030__REDUCE_THE_ADVERSE_PER_CAPITA_ENVIRONMENTAL_IMPACT_OF_CITIES__INCLUDING_BY_PAYING_SPECIAL_ATTENTION_TO_AIR_QUALITY_AND_MUNICIPAL_AND_OTHER_WASTE_MANAGEMENT = (
        "11.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, reduce the adverse per capita environmental impact of cities, including by paying special attention to air quality and municipal and other waste management",
        ),
    )
    BY_2030__PROVIDE_UNIVERSAL_ACCESS_TO_SAFE__INCLUSIVE_AND_ACCESSIBLE__GREEN_AND_PUBLIC_SPACES__IN_PARTICULAR_FOR_WOMEN_AND_CHILDREN__OLDER_PERSONS_AND_PERSONS_WITH_DISABILITIES = (
        "11.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, provide universal access to safe, inclusive and accessible, green and public spaces, in particular for women and children, older persons and persons with disabilities",
        ),
    )
    SUPPORT_POSITIVE_ECONOMIC__SOCIAL_AND_ENVIRONMENTAL_LINKS_BETWEEN_URBAN__PERI_URBAN_AND_RURAL_AREAS_BY_STRENGTHENING_NATIONAL_AND_REGIONAL_DEVELOPMENT_PLANNING = (
        "11.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Support positive economic, social and environmental links between urban, peri-urban and rural areas by strengthening national and regional development planning",
        ),
    )
    BY_2020__SUBSTANTIALLY_INCREASE_THE_NUMBER_OF_CITIES_AND_HUMAN_SETTLEMENTS_ADOPTING_AND_IMPLEMENTING_INTEGRATED_POLICIES_AND_PLANS_TOWARDS_INCLUSION__RESOURCE_EFFICIENCY__MITIGATION_AND_ADAPTATION_TO_CLIMATE_CHANGE__RESILIENCE_TO_DISASTERS__AND_DEVELOP_AND_IMPLEMENT__IN_LINE_WITH_THE_SENDAI_FRAMEWORK_FOR_DISASTER_RISK_REDUCTION_2015_2030__HOLISTIC_DISASTER_RISK_MANAGEMENT_AT_ALL_LEVELS = (
        "11.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, substantially increase the number of cities and human settlements adopting and implementing integrated policies and plans towards inclusion, resource efficiency, mitigation and adaptation to climate change, resilience to disasters, and develop and implement, in line with the Sendai Framework for Disaster Risk Reduction 2015–2030, holistic disaster risk management at all levels",
        ),
    )
    SUPPORT_LEAST_DEVELOPED_COUNTRIES__INCLUDING_THROUGH_FINANCIAL_AND_TECHNICAL_ASSISTANCE__IN_BUILDING_SUSTAINABLE_AND_RESILIENT_BUILDINGS_UTILIZING_LOCAL_MATERIALS = (
        "11.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Support least developed countries, including through financial and technical assistance, in building sustainable and resilient buildings utilizing local materials",
        ),
    )
    IMPLEMENT_THE_10_YEAR_FRAMEWORK_OF_PROGRAMMES_ON_SUSTAINABLE_CONSUMPTION_AND_PRODUCTION_PATTERNS__ALL_COUNTRIES_TAKING_ACTION__WITH_DEVELOPED_COUNTRIES_TAKING_THE_LEAD__TAKING_INTO_ACCOUNT_THE_DEVELOPMENT_AND_CAPABILITIES_OF_DEVELOPING_COUNTRIES = (
        "12.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Implement the 10‑Year Framework of Programmes on Sustainable Consumption and Production Patterns, all countries taking action, with developed countries taking the lead, taking into account the development and capabilities of developing countries",
        ),
    )
    BY_2030__ACHIEVE_THE_SUSTAINABLE_MANAGEMENT_AND_EFFICIENT_USE_OF_NATURAL_RESOURCES = (
        "12.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, achieve the sustainable management and efficient use of natural resources",
        ),
    )
    BY_2030__HALVE_PER_CAPITA_GLOBAL_FOOD_WASTE_AT_THE_RETAIL_AND_CONSUMER_LEVELS_AND_REDUCE_FOOD_LOSSES_ALONG_PRODUCTION_AND_SUPPLY_CHAINS__INCLUDING_POST_HARVEST_LOSSES = (
        "12.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, halve per capita global food waste at the retail and consumer levels and reduce food losses along production and supply chains, including post-harvest losses",
        ),
    )
    BY_2020__ACHIEVE_THE_ENVIRONMENTALLY_SOUND_MANAGEMENT_OF_CHEMICALS_AND_ALL_WASTES_THROUGHOUT_THEIR_LIFE_CYCLE__IN_ACCORDANCE_WITH_AGREED_INTERNATIONAL_FRAMEWORKS__AND_SIGNIFICANTLY_REDUCE_THEIR_RELEASE_TO_AIR__WATER_AND_SOIL_IN_ORDER_TO_MINIMIZE_THEIR_ADVERSE_IMPACTS_ON_HUMAN_HEALTH_AND_THE_ENVIRONMENT = (
        "12.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, achieve the environmentally sound management of chemicals and all wastes throughout their life cycle, in accordance with agreed international frameworks, and significantly reduce their release to air, water and soil in order to minimize their adverse impacts on human health and the environment",
        ),
    )
    BY_2030__SUBSTANTIALLY_REDUCE_WASTE_GENERATION_THROUGH_PREVENTION__REDUCTION__RECYCLING_AND_REUSE = (
        "12.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, substantially reduce waste generation through prevention, reduction, recycling and reuse",
        ),
    )
    ENCOURAGE_COMPANIES__ESPECIALLY_LARGE_AND_TRANSNATIONAL_COMPANIES__TO_ADOPT_SUSTAINABLE_PRACTICES_AND_TO_INTEGRATE_SUSTAINABILITY_INFORMATION_INTO_THEIR_REPORTING_CYCLE = (
        "12.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Encourage companies, especially large and transnational companies, to adopt sustainable practices and to integrate sustainability information into their reporting cycle",
        ),
    )
    PROMOTE_PUBLIC_PROCUREMENT_PRACTICES_THAT_ARE_SUSTAINABLE__IN_ACCORDANCE_WITH_NATIONAL_POLICIES_AND_PRIORITIES = (
        "12.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote public procurement practices that are sustainable, in accordance with national policies and priorities",
        ),
    )
    BY_2030__ENSURE_THAT_PEOPLE_EVERYWHERE_HAVE_THE_RELEVANT_INFORMATION_AND_AWARENESS_FOR_SUSTAINABLE_DEVELOPMENT_AND_LIFESTYLES_IN_HARMONY_WITH_NATURE = (
        "12.8",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure that people everywhere have the relevant information and awareness for sustainable development and lifestyles in harmony with nature",
        ),
    )
    SUPPORT_DEVELOPING_COUNTRIES_TO_STRENGTHEN_THEIR_SCIENTIFIC_AND_TECHNOLOGICAL_CAPACITY_TO_MOVE_TOWARDS_MORE_SUSTAINABLE_PATTERNS_OF_CONSUMPTION_AND_PRODUCTION = (
        "12.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Support developing countries to strengthen their scientific and technological capacity to move towards more sustainable patterns of consumption and production",
        ),
    )
    DEVELOP_AND_IMPLEMENT_TOOLS_TO_MONITOR_SUSTAINABLE_DEVELOPMENT_IMPACTS_FOR_SUSTAINABLE_TOURISM_THAT_CREATES_JOBS_AND_PROMOTES_LOCAL_CULTURE_AND_PRODUCTS = (
        "12.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Develop and implement tools to monitor sustainable development impacts for sustainable tourism that creates jobs and promotes local culture and products",
        ),
    )
    RATIONALIZE_INEFFICIENT_FOSSIL_FUEL_SUBSIDIES_THAT_ENCOURAGE_WASTEFUL_CONSUMPTION_BY_REMOVING_MARKET_DISTORTIONS__IN_ACCORDANCE_WITH_NATIONAL_CIRCUMSTANCES__INCLUDING_BY_RESTRUCTURING_TAXATION_AND_PHASING_OUT_THOSE_HARMFUL_SUBSIDIES__WHERE_THEY_EXIST__TO_REFLECT_THEIR_ENVIRONMENTAL_IMPACTS__TAKING_FULLY_INTO_ACCOUNT_THE_SPECIFIC_NEEDS_AND_CONDITIONS_OF_DEVELOPING_COUNTRIES_AND_MINIMIZING_THE_POSSIBLE_ADVERSE_IMPACTS_ON_THEIR_DEVELOPMENT_IN_A_MANNER_THAT_PROTECTS_THE_POOR_AND_THE_AFFECTED_COMMUNITIES = (
        "12.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Rationalize inefficient fossil-fuel subsidies that encourage wasteful consumption by removing market distortions, in accordance with national circumstances, including by restructuring taxation and phasing out those harmful subsidies, where they exist, to reflect their environmental impacts, taking fully into account the specific needs and conditions of developing countries and minimizing the possible adverse impacts on their development in a manner that protects the poor and the affected communities",
        ),
    )
    STRENGTHEN_RESILIENCE_AND_ADAPTIVE_CAPACITY_TO_CLIMATE_RELATED_HAZARDS_AND_NATURAL_DISASTERS_IN_ALL_COUNTRIES = (
        "13.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries",
        ),
    )
    INTEGRATE_CLIMATE_CHANGE_MEASURES_INTO_NATIONAL_POLICIES__STRATEGIES_AND_PLANNING = (
        "13.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Integrate climate change measures into national policies, strategies and planning",
        ),
    )
    IMPROVE_EDUCATION__AWARENESS_RAISING_AND_HUMAN_AND_INSTITUTIONAL_CAPACITY_ON_CLIMATE_CHANGE_MITIGATION__ADAPTATION__IMPACT_REDUCTION_AND_EARLY_WARNING = (
        "13.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Improve education, awareness-raising and human and institutional capacity on climate change mitigation, adaptation, impact reduction and early warning",
        ),
    )
    IMPLEMENT_THE_COMMITMENT_UNDERTAKEN_BY_DEVELOPEDCOUNTRY_PARTIES_TO_THE_UNITED_NATIONS_FRAMEWORK_CONVENTION_ON_CLIMATE_CHANGE_TO_A_GOAL_OF_MOBILIZING_JOINTLY__100_BILLION_ANNUALLY_BY_2020_FROM_ALL_SOURCES_TO_ADDRESS_THE_NEEDS_OF_DEVELOPING_COUNTRIES_IN_THE_CONTEXT_OF_MEANINGFUL_MITIGATION_ACTIONS_AND_TRANSPARENCY_ON_IMPLEMENTATION_AND_FULLY_OPERATIONALIZE_THE_GREEN_CLIMATE_FUND_THROUGH_ITS_CAPITALIZATION_AS_SOON_AS_POSSIBLE = (
        "13.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Implement the commitment undertaken by developed-country parties to the United Nations Framework Convention on Climate Change to a goal of mobilizing jointly $100 billion annually by 2020 from all sources to address the needs of developing countries in the context of meaningful mitigation actions and transparency on implementation and fully operationalize the Green Climate Fund through its capitalization as soon as possible",
        ),
    )
    PROMOTE_MECHANISMS_FOR_RAISING_CAPACITY_FOR_EFFECTIVE_CLIMATE_CHANGE_RELATED_PLANNING_AND_MANAGEMENT_IN_LEAST_DEVELOPED_COUNTRIES_AND_SMALL_ISLAND_DEVELOPING_STATES__INCLUDING_FOCUSING_ON_WOMEN__YOUTH_AND_LOCAL_AND_MARGINALIZED_COMMUNITIES = (
        "13.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote mechanisms for raising capacity for effective climate change-related planning and management in least developed countries and small island developing States, including focusing on women, youth and local and marginalized communities",
        ),
    )
    BY_2025__PREVENT_AND_SIGNIFICANTLY_REDUCE_MARINE_POLLUTION_OF_ALL_KINDS__IN_PARTICULAR_FROM_LAND_BASED_ACTIVITIES__INCLUDING_MARINE_DEBRIS_AND_NUTRIENT_POLLUTION = (
        "14.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2025, prevent and significantly reduce marine pollution of all kinds, in particular from land-based activities, including marine debris and nutrient pollution",
        ),
    )
    BY_2020__SUSTAINABLY_MANAGE_AND_PROTECT_MARINE_AND_COASTAL_ECOSYSTEMS_TO_AVOID_SIGNIFICANT_ADVERSE_IMPACTS__INCLUDING_BY_STRENGTHENING_THEIR_RESILIENCE__AND_TAKE_ACTION_FOR_THEIR_RESTORATION_IN_ORDER_TO_ACHIEVE_HEALTHY_AND_PRODUCTIVE_OCEANS = (
        "14.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, sustainably manage and protect marine and coastal ecosystems to avoid significant adverse impacts, including by strengthening their resilience, and take action for their restoration in order to achieve healthy and productive oceans",
        ),
    )
    MINIMIZE_AND_ADDRESS_THE_IMPACTS_OF_OCEAN_ACIDIFICATION__INCLUDING_THROUGH_ENHANCED_SCIENTIFIC_COOPERATION_AT_ALL_LEVELS = (
        "14.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Minimize and address the impacts of ocean acidification, including through enhanced scientific cooperation at all levels",
        ),
    )
    BY_2020__EFFECTIVELY_REGULATE_HARVESTING_AND_END_OVERFISHING__ILLEGAL__UNREPORTED_AND_UNREGULATED_FISHING_AND_DESTRUCTIVE_FISHING_PRACTICES_AND_IMPLEMENT_SCIENCE_BASED_MANAGEMENT_PLANS__IN_ORDER_TO_RESTORE_FISH_STOCKS_IN_THE_SHORTEST_TIME_FEASIBLE__AT_LEAST_TO_LEVELS_THAT_CAN_PRODUCE_MAXIMUM_SUSTAINABLE_YIELD_AS_DETERMINED_BY_THEIR_BIOLOGICAL_CHARACTERISTICS = (
        "14.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, effectively regulate harvesting and end overfishing, illegal, unreported and unregulated fishing and destructive fishing practices and implement science-based management plans, in order to restore fish stocks in the shortest time feasible, at least to levels that can produce maximum sustainable yield as determined by their biological characteristics",
        ),
    )
    BY_2020__CONSERVE_AT_LEAST_10_PER_CENT_OF_COASTAL_AND_MARINE_AREAS__CONSISTENT_WITH_NATIONAL_AND_INTERNATIONAL_LAW_AND_BASED_ON_THE_BEST_AVAILABLE_SCIENTIFIC_INFORMATION = (
        "14.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, conserve at least 10 per cent of coastal and marine areas, consistent with national and international law and based on the best available scientific information",
        ),
    )
    BY_2020__PROHIBIT_CERTAIN_FORMS_OF_FISHERIES_SUBSIDIES_WHICH_CONTRIBUTE_TO_OVERCAPACITY_AND_OVERFISHING__ELIMINATE_SUBSIDIES_THAT_CONTRIBUTE_TO_ILLEGAL__UNREPORTED_AND_UNREGULATED_FISHING_AND_REFRAIN_FROM_INTRODUCING_NEW_SUCH_SUBSIDIES__RECOGNIZING_THAT_APPROPRIATE_AND_EFFECTIVE_SPECIAL_AND_DIFFERENTIAL_TREATMENT_FOR_DEVELOPING_AND_LEAST_DEVELOPED_COUNTRIES_SHOULD_BE_AN_INTEGRAL_PART_OF_THE_WORLD_TRADE_ORGANIZATION_FISHERIES_SUBSIDIES_NEGOTIATION3 = (
        "14.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, prohibit certain forms of fisheries subsidies which contribute to overcapacity and overfishing, eliminate subsidies that contribute to illegal, unreported and unregulated fishing and refrain from introducing new such subsidies, recognizing that appropriate and effective special and differential treatment for developing and least developed countries should be an integral part of the World Trade Organization fisheries subsidies negotiation3",
        ),
    )
    BY_2030__INCREASE_THE_ECONOMIC_BENEFITS_TO_SMALL_ISLAND_DEVELOPING_STATES_AND_LEAST_DEVELOPED_COUNTRIES_FROM_THE_SUSTAINABLE_USE_OF_MARINE_RESOURCES__INCLUDING_THROUGH_SUSTAINABLE_MANAGEMENT_OF_FISHERIES__AQUACULTURE_AND_TOURISM = (
        "14.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, increase the economic benefits to small island developing States and least developed countries from the sustainable use of marine resources, including through sustainable management of fisheries, aquaculture and tourism",
        ),
    )
    INCREASE_SCIENTIFIC_KNOWLEDGE__DEVELOP_RESEARCH_CAPACITY_AND_TRANSFER_MARINE_TECHNOLOGY__TAKING_INTO_ACCOUNT_THE_INTERGOVERNMENTAL_OCEANOGRAPHIC_COMMISSION_CRITERIA_AND_GUIDELINES_ON_THE_TRANSFER_OF_MARINE_TECHNOLOGY__IN_ORDER_TO_IMPROVE_OCEAN_HEALTH_AND_TO_ENHANCE_THE_CONTRIBUTION_OF_MARINE_BIODIVERSITY_TO_THE_DEVELOPMENT_OF_DEVELOPING_COUNTRIES__IN_PARTICULAR_SMALL_ISLAND_DEVELOPING_STATES_AND_LEAST_DEVELOPED_COUNTRIES = (
        "14.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Increase scientific knowledge, develop research capacity and transfer marine technology, taking into account the Intergovernmental Oceanographic Commission Criteria and Guidelines on the Transfer of Marine Technology, in order to improve ocean health and to enhance the contribution of marine biodiversity to the development of developing countries, in particular small island developing States and least developed countries",
        ),
    )
    PROVIDE_ACCESS_FOR_SMALL_SCALE_ARTISANAL_FISHERS_TO_MARINE_RESOURCES_AND_MARKETS = (
        "14.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Provide access for small-scale artisanal fishers to marine resources and markets",
        ),
    )
    ENHANCE_THE_CONSERVATION_AND_SUSTAINABLE_USE_OF_OCEANS_AND_THEIR_RESOURCES_BY_IMPLEMENTING_INTERNATIONAL_LAW_AS_REFLECTED_IN_THE_UNITED_NATIONS_CONVENTION_ON_THE_LAW_OF_THE_SEA__WHICH_PROVIDES_THE_LEGAL_FRAMEWORK_FOR_THE_CONSERVATION_AND_SUSTAINABLE_USE_OF_OCEANS_AND_THEIR_RESOURCES__AS_RECALLED_IN_PARAGRAPH_158_OF__THE_FUTURE_WE_WANT_ = (
        "14.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance the conservation and sustainable use of oceans and their resources by implementing international law as reflected in the United Nations Convention on the Law of the Sea, which provides the legal framework for the conservation and sustainable use of oceans and their resources, as recalled in paragraph 158 of “The future we want”",
        ),
    )
    BY_2020__ENSURE_THE_CONSERVATION__RESTORATION_AND_SUSTAINABLE_USE_OF_TERRESTRIAL_AND_INLAND_FRESHWATER_ECOSYSTEMS_AND_THEIR_SERVICES__IN_PARTICULAR_FORESTS__WETLANDS__MOUNTAINS_AND_DRYLANDS__IN_LINE_WITH_OBLIGATIONS_UNDER_INTERNATIONAL_AGREEMENTS = (
        "15.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, ensure the conservation, restoration and sustainable use of terrestrial and inland freshwater ecosystems and their services, in particular forests, wetlands, mountains and drylands, in line with obligations under international agreements",
        ),
    )
    BY_2020__PROMOTE_THE_IMPLEMENTATION_OF_SUSTAINABLE_MANAGEMENT_OF_ALL_TYPES_OF_FORESTS__HALT_DEFORESTATION__RESTORE_DEGRADED_FORESTS_AND_SUBSTANTIALLY_INCREASE_AFFORESTATION_AND_REFORESTATION_GLOBALLY = (
        "15.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, promote the implementation of sustainable management of all types of forests, halt deforestation, restore degraded forests and substantially increase afforestation and reforestation globally",
        ),
    )
    BY_2030__COMBAT_DESERTIFICATION__RESTORE_DEGRADED_LAND_AND_SOIL__INCLUDING_LAND_AFFECTED_BY_DESERTIFICATION__DROUGHT_AND_FLOODS__AND_STRIVE_TO_ACHIEVE_A_LAND_DEGRADATION_NEUTRAL_WORLD = (
        "15.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, combat desertification, restore degraded land and soil, including land affected by desertification, drought and floods, and strive to achieve a land degradation-neutral world",
        ),
    )
    BY_2030__ENSURE_THE_CONSERVATION_OF_MOUNTAIN_ECOSYSTEMS__INCLUDING_THEIR_BIODIVERSITY__IN_ORDER_TO_ENHANCE_THEIR_CAPACITY_TO_PROVIDE_BENEFITS_THAT_ARE_ESSENTIAL_FOR_SUSTAINABLE_DEVELOPMENT = (
        "15.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, ensure the conservation of mountain ecosystems, including their biodiversity, in order to enhance their capacity to provide benefits that are essential for sustainable development",
        ),
    )
    TAKE_URGENT_AND_SIGNIFICANT_ACTION_TO_REDUCE_THE_DEGRADATION_OF_NATURAL_HABITATS__HALT_THE_LOSS_OF_BIODIVERSITY_AND__BY_2020__PROTECT_AND_PREVENT_THE_EXTINCTION_OF_THREATENED_SPECIES = (
        "15.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Take urgent and significant action to reduce the degradation of natural habitats, halt the loss of biodiversity and, by 2020, protect and prevent the extinction of threatened species",
        ),
    )
    PROMOTE_FAIR_AND_EQUITABLE_SHARING_OF_THE_BENEFITS_ARISING_FROM_THE_UTILIZATION_OF_GENETIC_RESOURCES_AND_PROMOTE_APPROPRIATE_ACCESS_TO_SUCH_RESOURCES__AS_INTERNATIONALLY_AGREED = (
        "15.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote fair and equitable sharing of the benefits arising from the utilization of genetic resources and promote appropriate access to such resources, as internationally agreed",
        ),
    )
    TAKE_URGENT_ACTION_TO_END_POACHING_AND_TRAFFICKING_OF_PROTECTED_SPECIES_OF_FLORA_AND_FAUNA_AND_ADDRESS_BOTH_DEMAND_AND_SUPPLY_OF_ILLEGAL_WILDLIFE_PRODUCTS = (
        "15.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Take urgent action to end poaching and trafficking of protected species of flora and fauna and address both demand and supply of illegal wildlife products",
        ),
    )
    BY_2020__INTRODUCE_MEASURES_TO_PREVENT_THE_INTRODUCTION_AND_SIGNIFICANTLY_REDUCE_THE_IMPACT_OF_INVASIVE_ALIEN_SPECIES_ON_LAND_AND_WATER_ECOSYSTEMS_AND_CONTROL_OR_ERADICATE_THE_PRIORITY_SPECIES = (
        "15.8",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, introduce measures to prevent the introduction and significantly reduce the impact of invasive alien species on land and water ecosystems and control or eradicate the priority species",
        ),
    )
    BY_2020__INTEGRATE_ECOSYSTEM_AND_BIODIVERSITY_VALUES_INTO_NATIONAL_AND_LOCAL_PLANNING__DEVELOPMENT_PROCESSES__POVERTY_REDUCTION_STRATEGIES_AND_ACCOUNTS = (
        "15.9",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, integrate ecosystem and biodiversity values into national and local planning, development processes, poverty reduction strategies and accounts",
        ),
    )
    MOBILIZE_AND_SIGNIFICANTLY_INCREASE_FINANCIAL_RESOURCES_FROM_ALL_SOURCES_TO_CONSERVE_AND_SUSTAINABLY_USE_BIODIVERSITY_AND_ECOSYSTEMS = (
        "15.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Mobilize and significantly increase financial resources from all sources to conserve and sustainably use biodiversity and ecosystems",
        ),
    )
    MOBILIZE_SIGNIFICANT_RESOURCES_FROM_ALL_SOURCES_AND_AT_ALL_LEVELS_TO_FINANCE_SUSTAINABLE_FOREST_MANAGEMENT_AND_PROVIDE_ADEQUATE_INCENTIVES_TO_DEVELOPING_COUNTRIES_TO_ADVANCE_SUCH_MANAGEMENT__INCLUDING_FOR_CONSERVATION_AND_REFORESTATION = (
        "15.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Mobilize significant resources from all sources and at all levels to finance sustainable forest management and provide adequate incentives to developing countries to advance such management, including for conservation and reforestation",
        ),
    )
    ENHANCE_GLOBAL_SUPPORT_FOR_EFFORTS_TO_COMBAT_POACHING_AND_TRAFFICKING_OF_PROTECTED_SPECIES__INCLUDING_BY_INCREASING_THE_CAPACITY_OF_LOCAL_COMMUNITIES_TO_PURSUE_SUSTAINABLE_LIVELIHOOD_OPPORTUNITIES = (
        "15.c",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance global support for efforts to combat poaching and trafficking of protected species, including by increasing the capacity of local communities to pursue sustainable livelihood opportunities",
        ),
    )
    SIGNIFICANTLY_REDUCE_ALL_FORMS_OF_VIOLENCE_AND_RELATED_DEATH_RATES_EVERYWHERE = (
        "16.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Significantly reduce all forms of violence and related death rates everywhere",
        ),
    )
    END_ABUSE__EXPLOITATION__TRAFFICKING_AND_ALL_FORMS_OF_VIOLENCE_AGAINST_AND_TORTURE_OF_CHILDREN = (
        "16.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "End abuse, exploitation, trafficking and all forms of violence against and torture of children",
        ),
    )
    PROMOTE_THE_RULE_OF_LAW_AT_THE_NATIONAL_AND_INTERNATIONAL_LEVELS_AND_ENSURE_EQUAL_ACCESS_TO_JUSTICE_FOR_ALL = (
        "16.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote the rule of law at the national and international levels and ensure equal access to justice for all",
        ),
    )
    BY_2030__SIGNIFICANTLY_REDUCE_ILLICIT_FINANCIAL_AND_ARMS_FLOWS__STRENGTHEN_THE_RECOVERY_AND_RETURN_OF_STOLEN_ASSETS_AND_COMBAT_ALL_FORMS_OF_ORGANIZED_CRIME = (
        "16.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, significantly reduce illicit financial and arms flows, strengthen the recovery and return of stolen assets and combat all forms of organized crime",
        ),
    )
    SUBSTANTIALLY_REDUCE_CORRUPTION_AND_BRIBERY_IN_ALL_THEIR_FORMS = (
        "16.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Substantially reduce corruption and bribery in all their forms",
        ),
    )
    DEVELOP_EFFECTIVE__ACCOUNTABLE_AND_TRANSPARENT_INSTITUTIONS_AT_ALL_LEVELS = (
        "16.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Develop effective, accountable and transparent institutions at all levels",
        ),
    )
    ENSURE_RESPONSIVE__INCLUSIVE__PARTICIPATORY_AND_REPRESENTATIVE_DECISION_MAKING_AT_ALL_LEVELS = (
        "16.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure responsive, inclusive, participatory and representative decision-making at all levels",
        ),
    )
    BROADEN_AND_STRENGTHEN_THE_PARTICIPATION_OF_DEVELOPING_COUNTRIES_IN_THE_INSTITUTIONS_OF_GLOBAL_GOVERNANCE = (
        "16.8",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Broaden and strengthen the participation of developing countries in the institutions of global governance",
        ),
    )
    BY_2030__PROVIDE_LEGAL_IDENTITY_FOR_ALL__INCLUDING_BIRTH_REGISTRATION = (
        "16.9",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, provide legal identity for all, including birth registration",
        ),
    )
    ENSURE_PUBLIC_ACCESS_TO_INFORMATION_AND_PROTECT_FUNDAMENTAL_FREEDOMS__IN_ACCORDANCE_WITH_NATIONAL_LEGISLATION_AND_INTERNATIONAL_AGREEMENTS = (
        "16.10",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Ensure public access to information and protect fundamental freedoms, in accordance with national legislation and international agreements",
        ),
    )
    STRENGTHEN_RELEVANT_NATIONAL_INSTITUTIONS__INCLUDING_THROUGH_INTERNATIONAL_COOPERATION__FOR_BUILDING_CAPACITY_AT_ALL_LEVELS__IN_PARTICULAR_IN_DEVELOPING_COUNTRIES__TO_PREVENT_VIOLENCE_AND_COMBAT_TERRORISM_AND_CRIME = (
        "16.a",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen relevant national institutions, including through international cooperation, for building capacity at all levels, in particular in developing countries, to prevent violence and combat terrorism and crime",
        ),
    )
    PROMOTE_AND_ENFORCE_NON_DISCRIMINATORY_LAWS_AND_POLICIES_FOR_SUSTAINABLE_DEVELOPMENT = (
        "16.b",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote and enforce non-discriminatory laws and policies for sustainable development",
        ),
    )
    STRENGTHEN_DOMESTIC_RESOURCE_MOBILIZATION__INCLUDING_THROUGH_INTERNATIONAL_SUPPORT_TO_DEVELOPING_COUNTRIES__TO_IMPROVE_DOMESTIC_CAPACITY_FOR_TAX_AND_OTHER_REVENUE_COLLECTION = (
        "17.1",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Strengthen domestic resource mobilization, including through international support to developing countries, to improve domestic capacity for tax and other revenue collection",
        ),
    )
    DEVELOPED_COUNTRIES_TO_IMPLEMENT_FULLY_THEIR_OFFICIAL_DEVELOPMENT_ASSISTANCE_COMMITMENTS__INCLUDING_THE_COMMITMENT_BY_MANY_DEVELOPED_COUNTRIES_TO_ACHIEVE_THE_TARGET_OF_0_7_PER_CENT_OF_GROSS_NATIONAL_INCOME_FOR_OFFICIAL_DEVELOPMENT_ASSISTANCE__ODA_GNI__TO_DEVELOPING_COUNTRIES_AND_0_15_TO_0_20_PER_CENT_OF_ODA_GNI_TO_LEAST_DEVELOPED_COUNTRIES__ODA_PROVIDERS_ARE_ENCOURAGED_TO_CONSIDER_SETTING_A_TARGET_TO_PROVIDE_AT_LEAST_0_20_PER_CENT_OF_ODA_GNI_TO_LEAST_DEVELOPED_COUNTRIES = (
        "17.2",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Developed countries to implement fully their official development assistance commitments, including the commitment by many developed countries to achieve the target of 0.7 per cent of gross national income for official development assistance (ODA/GNI) to developing countries and 0.15 to 0.20 per cent of ODA/GNI to least developed countries; ODA providers are encouraged to consider setting a target to provide at least 0.20 per cent of ODA/GNI to least developed countries",
        ),
    )
    MOBILIZE_ADDITIONAL_FINANCIAL_RESOURCES_FOR_DEVELOPING_COUNTRIES_FROM_MULTIPLE_SOURCES = (
        "17.3",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Mobilize additional financial resources for developing countries from multiple sources",
        ),
    )
    ASSIST_DEVELOPING_COUNTRIES_IN_ATTAINING_LONG_TERM_DEBT_SUSTAINABILITY_THROUGH_COORDINATED_POLICIES_AIMED_AT_FOSTERING_DEBT_FINANCING__DEBT_RELIEF_AND_DEBT_RESTRUCTURING__AS_APPROPRIATE__AND_ADDRESS_THE_EXTERNAL_DEBT_OF_HIGHLY_INDEBTED_POOR_COUNTRIES_TO_REDUCE_DEBT_DISTRESS = (
        "17.4",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Assist developing countries in attaining long-term debt sustainability through coordinated policies aimed at fostering debt financing, debt relief and debt restructuring, as appropriate, and address the external debt of highly indebted poor countries to reduce debt distress",
        ),
    )
    ADOPT_AND_IMPLEMENT_INVESTMENT_PROMOTION_REGIMES_FOR_LEAST_DEVELOPED_COUNTRIES = (
        "17.5",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Adopt and implement investment promotion regimes for least developed countries",
        ),
    )
    ENHANCE_NORTH_SOUTH__SOUTH_SOUTH_AND_TRIANGULAR_REGIONAL_AND_INTERNATIONAL_COOPERATION_ON_AND_ACCESS_TO_SCIENCE__TECHNOLOGY_AND_INNOVATION_AND_ENHANCE_KNOWLEDGE_SHARING_ON_MUTUALLY_AGREED_TERMS__INCLUDING_THROUGH_IMPROVED_COORDINATION_AMONG_EXISTING_MECHANISMS__IN_PARTICULAR_AT_THE_UNITED_NATIONS_LEVEL__AND_THROUGH_A_GLOBAL_TECHNOLOGY_FACILITATION_MECHANISM = (
        "17.6",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance North-South, South-South and triangular regional and international cooperation on and access to science, technology and innovation and enhance knowledge-sharing on mutually agreed terms, including through improved coordination among existing mechanisms, in particular at the United Nations level, and through a global technology facilitation mechanism",
        ),
    )
    PROMOTE_THE_DEVELOPMENT__TRANSFER__DISSEMINATION_AND_DIFFUSION_OF_ENVIRONMENTALLY_SOUND_TECHNOLOGIES_TO_DEVELOPING_COUNTRIES_ON_FAVOURABLE_TERMS__INCLUDING_ON_CONCESSIONAL_AND_PREFERENTIAL_TERMS__AS_MUTUALLY_AGREED = (
        "17.7",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote the development, transfer, dissemination and diffusion of environmentally sound technologies to developing countries on favourable terms, including on concessional and preferential terms, as mutually agreed",
        ),
    )
    FULLY_OPERATIONALIZE_THE_TECHNOLOGY_BANK_AND_SCIENCE__TECHNOLOGY_AND_INNOVATION_CAPACITY_BUILDING_MECHANISM_FOR_LEAST_DEVELOPED_COUNTRIES_BY_2017_AND_ENHANCE_THE_USE_OF_ENABLING_TECHNOLOGY__IN_PARTICULAR_INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY = (
        "17.8",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Fully operationalize the technology bank and science, technology and innovation capacity-building mechanism for least developed countries by 2017 and enhance the use of enabling technology, in particular information and communications technology",
        ),
    )
    ENHANCE_INTERNATIONAL_SUPPORT_FOR_IMPLEMENTING_EFFECTIVE_AND_TARGETED_CAPACITY_BUILDING_IN_DEVELOPING_COUNTRIES_TO_SUPPORT_NATIONAL_PLANS_TO_IMPLEMENT_ALL_THE_SUSTAINABLE_DEVELOPMENT_GOALS__INCLUDING_THROUGH_NORTH_SOUTH__SOUTH_SOUTH_AND_TRIANGULAR_COOPERATION = (
        "17.9",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance international support for implementing effective and targeted capacity-building in developing countries to support national plans to implement all the Sustainable Development Goals, including through North-South, South-South and triangular cooperation",
        ),
    )
    PROMOTE_A_UNIVERSAL__RULES_BASED__OPEN__NON_DISCRIMINATORY_AND_EQUITABLE_MULTILATERAL_TRADING_SYSTEM_UNDER_THE_WORLD_TRADE_ORGANIZATION__INCLUDING_THROUGH_THE_CONCLUSION_OF_NEGOTIATIONS_UNDER_ITS_DOHA_DEVELOPMENT_AGENDA = (
        "17.10",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Promote a universal, rules-based, open, non‑discriminatory and equitable multilateral trading system under the World Trade Organization, including through the conclusion of negotiations under its Doha Development Agenda",
        ),
    )
    SIGNIFICANTLY_INCREASE_THE_EXPORTS_OF_DEVELOPING_COUNTRIES__IN_PARTICULAR_WITH_A_VIEW_TO_DOUBLING_THE_LEAST_DEVELOPED_COUNTRIES__SHARE_OF_GLOBAL_EXPORTS_BY_2020 = (
        "17.11",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Significantly increase the exports of developing countries, in particular with a view to doubling the least developed countries’ share of global exports by 2020",
        ),
    )
    REALIZE_TIMELY_IMPLEMENTATION_OF_DUTY_FREE_AND_QUOTA_FREE_MARKET_ACCESS_ON_A_LASTING_BASIS_FOR_ALL_LEAST_DEVELOPED_COUNTRIES__CONSISTENT_WITH_WORLD_TRADE_ORGANIZATION_DECISIONS__INCLUDING_BY_ENSURING_THAT_PREFERENTIAL_RULES_OF_ORIGIN_APPLICABLE_TO_IMPORTS_FROM_LEAST_DEVELOPED_COUNTRIES_ARE_TRANSPARENT_AND_SIMPLE__AND_CONTRIBUTE_TO_FACILITATING_MARKET_ACCESS = (
        "17.12",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Realize timely implementation of duty-free and quota-free market access on a lasting basis for all least developed countries, consistent with World Trade Organization decisions, including by ensuring that preferential rules of origin applicable to imports from least developed countries are transparent and simple, and contribute to facilitating market access",
        ),
    )
    ENHANCE_GLOBAL_MACROECONOMIC_STABILITY__INCLUDING_THROUGH_POLICY_COORDINATION_AND_POLICY_COHERENCE = (
        "17.13",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance global macroeconomic stability, including through policy coordination and policy coherence",
        ),
    )
    ENHANCE_POLICY_COHERENCE_FOR_SUSTAINABLE_DEVELOPMENT = (
        "17.14",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance policy coherence for sustainable development",
        ),
    )
    RESPECT_EACH_COUNTRY_S_POLICY_SPACE_AND_LEADERSHIP_TO_ESTABLISH_AND_IMPLEMENT_POLICIES_FOR_POVERTY_ERADICATION_AND_SUSTAINABLE_DEVELOPMENT = (
        "17.15",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Respect each country’s policy space and leadership to establish and implement policies for poverty eradication and sustainable development",
        ),
    )
    ENHANCE_THE_GLOBAL_PARTNERSHIP_FOR_SUSTAINABLE_DEVELOPMENT__COMPLEMENTED_BY_MULTI_STAKEHOLDER_PARTNERSHIPS_THAT_MOBILIZE_AND_SHARE_KNOWLEDGE__EXPERTISE__TECHNOLOGY_AND_FINANCIAL_RESOURCES__TO_SUPPORT_THE_ACHIEVEMENT_OF_THE_SUSTAINABLE_DEVELOPMENT_GOALS_IN_ALL_COUNTRIES__IN_PARTICULAR_DEVELOPING_COUNTRIES = (
        "17.16",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Enhance the Global Partnership for Sustainable Development, complemented by multi-stakeholder partnerships that mobilize and share knowledge, expertise, technology and financial resources, to support the achievement of the Sustainable Development Goals in all countries, in particular developing countries",
        ),
    )
    ENCOURAGE_AND_PROMOTE_EFFECTIVE_PUBLIC__PUBLIC_PRIVATE_AND_CIVIL_SOCIETY_PARTNERSHIPS__BUILDING_ON_THE_EXPERIENCE_AND_RESOURCING_STRATEGIES_OF_PARTNERSHIPS = (
        "17.17",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "Encourage and promote effective public, public-private and civil society partnerships, building on the experience and resourcing strategies of partnerships",
        ),
    )
    BY_2020__ENHANCE_CAPACITY_BUILDING_SUPPORT_TO_DEVELOPING_COUNTRIES__INCLUDING_FOR_LEAST_DEVELOPED_COUNTRIES_AND_SMALL_ISLAND_DEVELOPING_STATES__TO_INCREASE_SIGNIFICANTLY_THE_AVAILABILITY_OF_HIGH_QUALITY__TIMELY_AND_RELIABLE_DATA_DISAGGREGATED_BY_INCOME__GENDER__AGE__RACE__ETHNICITY__MIGRATORY_STATUS__DISABILITY__GEOGRAPHIC_LOCATION_AND_OTHER_CHARACTERISTICS_RELEVANT_IN_NATIONAL_CONTEXTS = (
        "17.18",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2020, enhance capacity-building support to developing countries, including for least developed countries and small island developing States, to increase significantly the availability of high-quality, timely and reliable data disaggregated by income, gender, age, race, ethnicity, migratory status, disability, geographic location and other characteristics relevant in national contexts",
        ),
    )
    BY_2030__BUILD_ON_EXISTING_INITIATIVES_TO_DEVELOP_MEASUREMENTS_OF_PROGRESS_ON_SUSTAINABLE_DEVELOPMENT_THAT_COMPLEMENT_GROSS_DOMESTIC_PRODUCT__AND_SUPPORT_STATISTICAL_CAPACITY_BUILDING_IN_DEVELOPING_COUNTRIES = (
        "17.19",
        pgettext_lazy(
            "IATI codelist UNSDG-Targets",
            "By 2030, build on existing initiatives to develop measurements of progress on sustainable development that complement gross domestic product, and support statistical capacity-building in developing countries",
        ),
    )
