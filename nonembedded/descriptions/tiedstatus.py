from django.db import models
from django.utils.translation import pgettext_lazy


class TiedStatusDescription(models.IntegerChoices):
    PARTIALLY_TIED = (
        3,
        pgettext_lazy(
            "TiedStatus description",
            "Official Development Assistance for which the associated goods and services must be procured from a restricted number of countries, which must however include substantially all aid recipient countries and can include the donor country.",
        ),
    )
    TIED = (
        4,
        pgettext_lazy(
            "TiedStatus description",
            "Official grants or loans where procurement of the goods or services involved is limited to the donor country or to a group of countries which does not include substantially all aid recipient countries.",
        ),
    )
    UNTIED = (
        5,
        pgettext_lazy(
            "TiedStatus description",
            "Untied aid is defined as loans and grants whose proceeds are fully and freely available to finance procurement from all OECD countries and substantially all developing countries.",
        ),
    )
