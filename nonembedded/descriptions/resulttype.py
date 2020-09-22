from django.db import models
from django.utils.translation import pgettext_lazy


class ResultTypeDescription(models.IntegerChoices):
    OUTPUT = (
        1,
        pgettext_lazy(
            "IATI codelist ResultType description",
            "Results of the activity that came about as a direct effect of your work and specific, what is done, and what communities are reached. For example, X number of individuals.",
        ),
    )
    OUTCOME = (
        2,
        pgettext_lazy(
            "IATI codelist ResultType description",
            "Results of the activity that produce an effect on the overall communities or issues you serve. For example lower rate of infection after a vaccination programme.",
        ),
    )
    IMPACT = (
        3,
        pgettext_lazy(
            "IATI codelist ResultType description",
            "The long term effects of the outcomes, that lead to larger, over arching results, such as improved life-expectancy.",
        ),
    )
    OTHER = (
        9,
        pgettext_lazy(
            "IATI codelist ResultType description",
            "Another type of result, not specified above.",
        ),
    )
