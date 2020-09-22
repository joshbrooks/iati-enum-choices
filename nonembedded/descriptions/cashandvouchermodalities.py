from django.db import models
from django.utils.translation import pgettext_lazy


class CashandVoucherModalitiesDescription(models.IntegerChoices):
    """
    This codelist has been created by IATI following agreements and recommendations of the Tracking Cash and Voucher Assistance (CVA) Working Group. Definitions of the codes have been aligned with the CaLP Glossary:http://www.cashlearning.org/resources/glossary.
    """

    CASH_TRANSFER = (
        1,
        pgettext_lazy(
            "CashandVoucherModalities description",
            "The provision of assistance in the form of money - either physical currency or e-cash - to recipients (individuals, households or communities). Cash transfers are by definition unrestricted in terms of use and distinct from restricted modalities including vouchers and in-kind assistance.",
        ),
    )
    VOUCHER = (
        2,
        pgettext_lazy(
            "CashandVoucherModalities description",
            "A paper, token or e-voucher that can be exchanged for a set quantity or value of goods or services, denominated either as a cash value (e.g. $15) or predetermined commodities (e.g. 5 kg maize) or specific services (e.g. milling of 5 kg of maize), or a combination of value and commodities. Vouchers are restricted by default, although the degree of restriction will vary based on the programme design and type of voucher. They are redeemable with preselected vendors or in ‘fairs’ created by the implementing agency. The terms vouchers, stamps, or coupons might be used interchangeably.",
        ),
    )
