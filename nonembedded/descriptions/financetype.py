from django.db import models
from django.utils.translation import pgettext_lazy


class FinanceTypeDescription(models.IntegerChoices):
    """
    DAC/CRS transaction classification used to distinguish financial instruments, e.g. grants or loans.
    """

    STANDARD_GRANT = (
        110,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Grants are transfers in cash or in kind for which no legal debt is incurred by the recipient.",
        ),
    )
    INTEREST_SUBSIDY = (
        210,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "A payment to soften the terms of private export credits, or loans or credits by the banking sector.",
        ),
    )
    CAPITAL_SUBSCRIPTION_ON_DEPOSIT_BASIS = (
        310,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Payments to multilateral agencies in the form of notes and similar instruments, unconditionally encashable at sight by the recipient institutions.",
        ),
    )
    CAPITAL_SUBSCRIPTION_ON_ENCASHMENT_BASIS = (
        311,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Payments to multilateral agencies in the form of notes and similar instruments, unconditionally encashable at sight by the recipient institutions.",
        ),
    )
    STANDARD_LOAN = (
        421,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Transfers in cash or in kind for which the recipient incurs legal debt (and the resulting claim is not intended to be traded).  Since payment obligations on standard loan are senior obligations, i.e. creditors are entitled to receive payments against their claims before anyone else, they are also referred to as senior loans.",
        ),
    )
    REIMBURSABLE_GRANT = (
        422,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "A contribution provided to a recipient institution for investment purposes, with the expectation of long-term reflows at conditions specified in the financing agreement. The provider assumes the risk of total or partial failure of the investment; it can also decide if and when to reclaim its investment.",
        ),
    )
    BONDS = (
        423,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Fixed-interest debt instruments, issued by governments, public utilities, banks or companies, tradable in financial markets.",
        ),
    )
    ASSET_BACKED_SECURITIES = (
        424,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Securities whose value and income payments are derived from and backed by a specific pool of underlying assets.",
        ),
    )
    SUBORDINATED_LOAN = (
        431,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "A loan that, in the event of default, will only be repaid after all senior obligations have been satisfied.  In compensation for the increased risk, mezzanine debt holders require a higher return for their investment than secured or more senior lenders.",
        ),
    )
    PREFERRED_EQUITY = (
        432,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Equity that, in the event of default, will be repaid after all senior obligations and subordinated loans have been satisfied; and will be paid before common equity holders. It is a more expensive source of finance than senior debt, a less expensive source than equity.",
        ),
    )
    OTHER_HYBRID_INSTRUMENTS = (
        433,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Including convertible debt or equity.",
        ),
    )
    COMMON_EQUITY = (
        510,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "A share in the ownership of a corporation that gives the owner claims on the residual value of the corporation after creditors’ claims have been met.",
        ),
    )
    SHARES_IN_COLLECTIVE_INVESTMENT_VEHICLES = (
        520,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "Collective undertakings through which investors pool funds for investment in financial or nonfinancial assets or both. These vehicles issue shares (if a corporate structure is used) or units (if a trust structure is used).",
        ),
    )
    REINVESTED_EARNINGS = (
        530,
        pgettext_lazy(
            "IATI codelist FinanceType description",
            "This item is only applicable to Foreign Direct Investment (FDI). Reinvested earnings on FDI consist of the retained earnings of a direct foreign investment enterprise which are treated as if they were distributed and remitted to foreign direct investors in proportion to their ownership of the equity of the enterprise and then reinvested by them in the enterprise.",
        ),
    )
