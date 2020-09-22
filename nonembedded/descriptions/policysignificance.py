from django.db import models
from django.utils.translation import pgettext_lazy


class PolicySignificanceDescription(models.IntegerChoices):
    NOT_TARGETED = (
        0,
        pgettext_lazy(
            "IATI codelist PolicySignificance description",
            'The score "not targeted" means that the activity was examined but found not to target the policy objective.',
        ),
    )
    SIGNIFICANT_OBJECTIVE = (
        1,
        pgettext_lazy(
            "IATI codelist PolicySignificance description",
            "Significant (secondary) policy objectives are those which, although important, were not the prime motivation for undertaking the activity.",
        ),
    )
    PRINCIPAL_OBJECTIVE = (
        2,
        pgettext_lazy(
            "IATI codelist PolicySignificance description",
            """Principal (primary) policy objectives are those which can be identified as being fundamental in the design and impact of the activity and which are an explicit objective of the activity. They may be selected by answering the question \"Would the activity have been undertaken without this objective?\"""",
        ),
    )
    PRINCIPAL_OBJECTIVE_AND_IN_SUPPORT_OF_AN_ACTION_PROGRAMME = (
        3,
        pgettext_lazy(
            "IATI codelist PolicySignificance description",
            "For desertification-related aid only",
        ),
    )
