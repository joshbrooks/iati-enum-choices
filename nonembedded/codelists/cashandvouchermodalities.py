from django.db import models
from django.utils.translation import pgettext_lazy


class CashandVoucherModalities(models.IntegerChoices):
    """
    This codelist has been created by IATI following agreements and recommendations of the Tracking Cash and Voucher Assistance (CVA) Working Group. Definitions of the codes have been aligned with the CaLP Glossary:http://www.cashlearning.org/resources/glossary.
    """

    CASH_TRANSFER = (
        1,
        pgettext_lazy("CashandVoucherModalities", "Cash Transfer"),
    )
    VOUCHER = (
        2,
        pgettext_lazy("CashandVoucherModalities", "Voucher"),
    )
