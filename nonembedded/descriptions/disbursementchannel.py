from django.db import models
from django.utils.translation import pgettext_lazy


class DisbursementChannelDescription(models.IntegerChoices):
    """
    Categories of information included in published documents
    """

    MONEY_IS_DISBURSED_THROUGH_CENTRAL_MINISTRY_OF_FINANCE_OR_TREASURY = (
        1,
        pgettext_lazy(
            "IATI codelist DisbursementChannel description",
            "Money is disbursed through central Ministry of Finance or Treasury",
        ),
    )
    MONEY_IS_DISBURSED_DIRECTLY_TO_THE_IMPLEMENTING_INSTITUTION_AND_MANAGED_THROUGH_A_SEPARATE_BANK_ACCOUNT = (
        2,
        pgettext_lazy(
            "IATI codelist DisbursementChannel description",
            "Money is disbursed directly to the implementing institution and managed through a separate bank account",
        ),
    )
    AID_IN_KIND__DONORS_UTILISE_THIRD_PARTY_AGENCIES__E_G__NGOS_OR_MANAGEMENT_COMPANIES = (
        3,
        pgettext_lazy(
            "IATI codelist DisbursementChannel description",
            "Aid in kind: Donors utilise third party agencies, e.g. NGOs or management companies",
        ),
    )
    AID_IN_KIND__DONORS_MANAGE_FUNDS_THEMSELVES = (
        4,
        pgettext_lazy(
            "IATI codelist DisbursementChannel description",
            "Aid in kind: Donors manage funds themselves",
        ),
    )
