from django.db import models
from django.utils.translation import pgettext_lazy


class PolicyMarker(models.IntegerChoices):
    """
    The Policy Marker codelist is derived from the policy markers declared by the WP-STAT. The codes themselves are created by IATI.
    """

    GENDER_EQUALITY = (
        1,
        pgettext_lazy("PolicyMarker", "Gender Equality"),
    )
    AID_TO_ENVIRONMENT = (
        2,
        pgettext_lazy("PolicyMarker", "Aid to Environment"),
    )
    PARTICIPATORY_DEVELOPMENT_GOOD_GOVERNANCE = (
        3,
        pgettext_lazy("PolicyMarker", "Participatory Development/Good Governance"),
    )
    TRADE_DEVELOPMENT = (
        4,
        pgettext_lazy("PolicyMarker", "Trade Development"),
    )
    AID_TARGETING_THE_OBJECTIVES_OF_THE_CONVENTION_ON_BIOLOGICAL_DIVERSITY = (
        5,
        pgettext_lazy(
            "PolicyMarker",
            "Aid Targeting the Objectives of the Convention on Biological Diversity",
        ),
    )
    AID_TARGETING_THE_OBJECTIVES_OF_THE_FRAMEWORK_CONVENTION_ON_CLIMATE_CHANGE_MITIGATION = (
        6,
        pgettext_lazy(
            "PolicyMarker",
            "Aid Targeting the Objectives of the Framework Convention on Climate Change - Mitigation",
        ),
    )
    AID_TARGETING_THE_OBJECTIVES_OF_THE_FRAMEWORK_CONVENTION_ON_CLIMATE_CHANGE_ADAPTATION = (
        7,
        pgettext_lazy(
            "PolicyMarker",
            "Aid Targeting the Objectives of the Framework Convention on Climate Change - Adaptation",
        ),
    )
    AID_TARGETING_THE_OBJECTIVES_OF_THE_CONVENTION_TO_COMBAT_DESERTIFICATION = (
        8,
        pgettext_lazy(
            "PolicyMarker",
            "Aid Targeting the Objectives of the Convention to Combat Desertification",
        ),
    )
    REPRODUCTIVE__MATERNAL__NEWBORN_AND_CHILD_HEALTH__RMNCH_ = (
        9,
        pgettext_lazy(
            "PolicyMarker",
            "Reproductive, Maternal, Newborn and Child Health (RMNCH)",
        ),
    )
    DISASTER_RISK_REDUCTION_DRR_ = (
        10,
        pgettext_lazy("PolicyMarker", "Disaster Risk Reduction(DRR)"),
    )
    DISABILITY = (
        11,
        pgettext_lazy("PolicyMarker", "Disability"),
    )
    NUTRITION = (
        12,
        pgettext_lazy("PolicyMarker", "Nutrition"),
    )
