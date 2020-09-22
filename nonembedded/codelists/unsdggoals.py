from django.db import models
from django.utils.translation import pgettext_lazy


class UNSDG_Goals(models.IntegerChoices):
    """
    A value from the top-level list of UN sustainable development goals (SDGs) (e.g. ‘1’)
    """

    GOAL_1__END_POVERTY_IN_ALL_ITS_FORMS_EVERYWHERE = (
        1,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 1. End poverty in all its forms everywhere",
        ),
    )
    GOAL_2__END_HUNGER__ACHIEVE_FOOD_SECURITY_AND_IMPROVED_NUTRITION_AND_PROMOTE_SUSTAINABLE_AGRICULTURE = (
        2,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 2. End hunger, achieve food security and improved nutrition and promote sustainable agriculture",
        ),
    )
    GOAL_3__ENSURE_HEALTHY_LIVES_AND_PROMOTE_WELL_BEING_FOR_ALL_AT_ALL_AGES = (
        3,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 3. Ensure healthy lives and promote well-being for all at all ages",
        ),
    )
    GOAL_4__ENSURE_INCLUSIVE_AND_EQUITABLE_QUALITY_EDUCATION_AND_PROMOTE_LIFELONG_LEARNING_OPPORTUNITIES_FOR_ALL = (
        4,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 4. Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
        ),
    )
    GOAL_5__ACHIEVE_GENDER_EQUALITY_AND_EMPOWER_ALL_WOMEN_AND_GIRLS = (
        5,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 5. Achieve gender equality and empower all women and girls",
        ),
    )
    GOAL_6__ENSURE_AVAILABILITY_AND_SUSTAINABLE_MANAGEMENT_OF_WATER_AND_SANITATION_FOR_ALL = (
        6,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 6. Ensure availability and sustainable management of water and sanitation for all",
        ),
    )
    GOAL_7__ENSURE_ACCESS_TO_AFFORDABLE__RELIABLE__SUSTAINABLE_AND_MODERN_ENERGY_FOR_ALL = (
        7,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 7. Ensure access to affordable, reliable, sustainable and modern energy for all",
        ),
    )
    GOAL_8__PROMOTE_SUSTAINED__INCLUSIVE_AND_SUSTAINABLE_ECONOMIC_GROWTH__FULL_AND_PRODUCTIVE_EMPLOYMENT_AND_DECENT_WORK_FOR_ALL = (
        8,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 8. Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all",
        ),
    )
    GOAL_9__BUILD_RESILIENT_INFRASTRUCTURE__PROMOTE_INCLUSIVE_AND_SUSTAINABLE_INDUSTRIALIZATION_AND_FOSTER_INNOVATION = (
        9,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 9. Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation",
        ),
    )
    GOAL_10__REDUCE_INEQUALITY_WITHIN_AND_AMONG_COUNTRIES = (
        10,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 10. Reduce inequality within and among countries",
        ),
    )
    GOAL_11__MAKE_CITIES_AND_HUMAN_SETTLEMENTS_INCLUSIVE__SAFE__RESILIENT_AND_SUSTAINABLE = (
        11,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 11. Make cities and human settlements inclusive, safe, resilient and sustainable",
        ),
    )
    GOAL_12__ENSURE_SUSTAINABLE_CONSUMPTION_AND_PRODUCTION_PATTERNS = (
        12,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 12. Ensure sustainable consumption and production patterns",
        ),
    )
    GOAL_13__TAKE_URGENT_ACTION_TO_COMBAT_CLIMATE_CHANGE_AND_ITS_IMPACTS = (
        13,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 13. Take urgent action to combat climate change and its impacts",
        ),
    )
    GOAL_14__CONSERVE_AND_SUSTAINABLY_USE_THE_OCEANS__SEAS_AND_MARINE_RESOURCES_FOR_SUSTAINABLE_DEVELOPMENT = (
        14,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 14. Conserve and sustainably use the oceans, seas and marine resources for sustainable development",
        ),
    )
    GOAL_15__PROTECT__RESTORE_AND_PROMOTE_SUSTAINABLE_USE_OF_TERRESTRIAL_ECOSYSTEMS__SUSTAINABLY_MANAGE_FORESTS__COMBAT_DESERTIFICATION__AND_HALT_AND_REVERSE_LAND_DEGRADATION_AND_HALT_BIODIVERSITY_LOSS = (
        15,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 15. Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss",
        ),
    )
    GOAL_16__PROMOTE_PEACEFUL_AND_INCLUSIVE_SOCIETIES_FOR_SUSTAINABLE_DEVELOPMENT__PROVIDE_ACCESS_TO_JUSTICE_FOR_ALL_AND_BUILD_EFFECTIVE__ACCOUNTABLE_AND_INCLUSIVE_INSTITUTIONS_AT_ALL_LEVELS = (
        16,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 16. Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels",
        ),
    )
    GOAL_17__STRENGTHEN_THE_MEANS_OF_IMPLEMENTATION_AND_REVITALIZE_THE_GLOBAL_PARTNERSHIP_FOR_SUSTAINABLE_DEVELOPMENT = (
        17,
        pgettext_lazy(
            "IATI codelist UNSDG-Goals",
            "Goal 17. Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development",
        ),
    )
