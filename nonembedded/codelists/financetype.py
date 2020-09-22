from django.db import models
from django.utils.translation import pgettext_lazy


class FinanceType(models.IntegerChoices):
    """
    DAC/CRS transaction classification used to distinguish financial instruments, e.g. grants or loans.
    """

    GNI__GROSS_NATIONAL_INCOME = (
        1,
        pgettext_lazy("IATI codelist FinanceType", "GNI: Gross National Income"),
    )
    STANDARD_GRANT = (
        110,
        pgettext_lazy("IATI codelist FinanceType", "Standard grant"),
    )
    GUARANTEES_INSURANCE = (
        1100,
        pgettext_lazy("IATI codelist FinanceType", "Guarantees/insurance"),
    )
    SUBSIDIES_TO_NATIONAL_PRIVATE_INVESTORS = (
        111,
        pgettext_lazy(
            "IATI codelist FinanceType", "Subsidies to national private investors"
        ),
    )
    ODA___GNI = (
        2,
        pgettext_lazy("IATI codelist FinanceType", "ODA % GNI"),
    )
    INTEREST_SUBSIDY = (
        210,
        pgettext_lazy("IATI codelist FinanceType", "Interest subsidy"),
    )
    INTEREST_SUBSIDY_TO_NATIONAL_PRIVATE_EXPORTERS = (
        211,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Interest subsidy to national private exporters",
        ),
    )
    TOTAL_FLOWS___GNI = (
        3,
        pgettext_lazy("IATI codelist FinanceType", "Total Flows % GNI"),
    )
    CAPITAL_SUBSCRIPTION_ON_DEPOSIT_BASIS = (
        310,
        pgettext_lazy(
            "IATI codelist FinanceType", "Capital subscription on deposit basis"
        ),
    )
    CAPITAL_SUBSCRIPTION_ON_ENCASHMENT_BASIS = (
        311,
        pgettext_lazy(
            "IATI codelist FinanceType", "Capital subscription on encashment basis"
        ),
    )
    POPULATION = (
        4,
        pgettext_lazy("IATI codelist FinanceType", "Population"),
    )
    AID_LOAN_EXCLUDING_DEBT_REORGANISATION = (
        410,
        pgettext_lazy(
            "IATI codelist FinanceType", "Aid loan excluding debt reorganisation"
        ),
    )
    INVESTMENT_RELATED_LOAN_TO_DEVELOPING_COUNTRIES = (
        411,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Investment-related loan to developing countries",
        ),
    )
    LOAN_IN_A_JOINT_VENTURE_WITH_THE_RECIPIENT = (
        412,
        pgettext_lazy(
            "IATI codelist FinanceType", "Loan in a joint venture with the recipient"
        ),
    )
    LOAN_TO_NATIONAL_PRIVATE_INVESTOR = (
        413,
        pgettext_lazy("IATI codelist FinanceType", "Loan to national private investor"),
    )
    LOAN_TO_NATIONAL_PRIVATE_EXPORTER = (
        414,
        pgettext_lazy("IATI codelist FinanceType", "Loan to national private exporter"),
    )
    STANDARD_LOAN = (
        421,
        pgettext_lazy("IATI codelist FinanceType", "Standard loan"),
    )
    REIMBURSABLE_GRANT = (
        422,
        pgettext_lazy("IATI codelist FinanceType", "Reimbursable grant"),
    )
    BONDS = (
        423,
        pgettext_lazy("IATI codelist FinanceType", "Bonds"),
    )
    ASSET_BACKED_SECURITIES = (
        424,
        pgettext_lazy("IATI codelist FinanceType", "Asset-backed securities"),
    )
    OTHER_DEBT_SECURITIES = (
        425,
        pgettext_lazy("IATI codelist FinanceType", "Other debt securities"),
    )
    SUBORDINATED_LOAN = (
        431,
        pgettext_lazy("IATI codelist FinanceType", "Subordinated loan"),
    )
    PREFERRED_EQUITY = (
        432,
        pgettext_lazy("IATI codelist FinanceType", "Preferred equity"),
    )
    OTHER_HYBRID_INSTRUMENTS = (
        433,
        pgettext_lazy("IATI codelist FinanceType", "Other hybrid instruments"),
    )
    NON_BANKS_GUARANTEED_EXPORT_CREDITS = (
        451,
        pgettext_lazy(
            "IATI codelist FinanceType", "Non-banks guaranteed export credits"
        ),
    )
    NON_BANKS_NON_GUARANTEED_PORTIONS_OF_GUARANTEED_EXPORT_CREDITS = (
        452,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Non-banks non-guaranteed portions of guaranteed export credits",
        ),
    )
    BANK_EXPORT_CREDITS = (
        453,
        pgettext_lazy("IATI codelist FinanceType", "Bank export credits"),
    )
    COMMON_EQUITY = (
        510,
        pgettext_lazy("IATI codelist FinanceType", "Common equity"),
    )
    ACQUISITION_OF_EQUITY_NOT_PART_OF_JOINT_VENTURE_IN_DEVELOPING_COUNTRIES = (
        511,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Acquisition of equity not part of joint venture in developing countries",
        ),
    )
    OTHER_ACQUISITION_OF_EQUITY = (
        512,
        pgettext_lazy("IATI codelist FinanceType", "Other acquisition of equity"),
    )
    SHARES_IN_COLLECTIVE_INVESTMENT_VEHICLES = (
        520,
        pgettext_lazy(
            "IATI codelist FinanceType", "Shares in collective investment vehicles"
        ),
    )
    REINVESTED_EARNINGS = (
        530,
        pgettext_lazy("IATI codelist FinanceType", "Reinvested earnings"),
    )
    DEBT_FORGIVENESS__ODA_CLAIMS__P_ = (
        610,
        pgettext_lazy("IATI codelist FinanceType", "Debt forgiveness:  ODA claims (P)"),
    )
    DEBT_FORGIVENESS__ODA_CLAIMS__I_ = (
        611,
        pgettext_lazy("IATI codelist FinanceType", "Debt forgiveness: ODA claims (I)"),
    )
    DEBT_FORGIVENESS__OOF_CLAIMS__P_ = (
        612,
        pgettext_lazy("IATI codelist FinanceType", "Debt forgiveness: OOF claims (P)"),
    )
    DEBT_FORGIVENESS__OOF_CLAIMS__I_ = (
        613,
        pgettext_lazy("IATI codelist FinanceType", "Debt forgiveness: OOF claims (I)"),
    )
    DEBT_FORGIVENESS__PRIVATE_CLAIMS__P_ = (
        614,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt forgiveness:  Private claims (P)"
        ),
    )
    DEBT_FORGIVENESS__PRIVATE_CLAIMS__I_ = (
        615,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt forgiveness:  Private claims (I)"
        ),
    )
    DEBT_FORGIVENESS__OOF_CLAIMS__DSR_ = (
        616,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt forgiveness: OOF claims (DSR)"
        ),
    )
    DEBT_FORGIVENESS__PRIVATE_CLAIMS__DSR_ = (
        617,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt forgiveness:  Private claims (DSR)"
        ),
    )
    DEBT_FORGIVENESS__OTHER = (
        618,
        pgettext_lazy("IATI codelist FinanceType", "Debt forgiveness: Other"),
    )
    DEBT_RESCHEDULING__ODA_CLAIMS__P_ = (
        620,
        pgettext_lazy("IATI codelist FinanceType", "Debt rescheduling: ODA claims (P)"),
    )
    DEBT_RESCHEDULING__ODA_CLAIMS__I_ = (
        621,
        pgettext_lazy("IATI codelist FinanceType", "Debt rescheduling: ODA claims (I)"),
    )
    DEBT_RESCHEDULING__OOF_CLAIMS__P_ = (
        622,
        pgettext_lazy("IATI codelist FinanceType", "Debt rescheduling: OOF claims (P)"),
    )
    DEBT_RESCHEDULING__OOF_CLAIMS__I_ = (
        623,
        pgettext_lazy("IATI codelist FinanceType", "Debt rescheduling: OOF claims (I)"),
    )
    DEBT_RESCHEDULING__PRIVATE_CLAIMS__P_ = (
        624,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt rescheduling:  Private claims (P)"
        ),
    )
    DEBT_RESCHEDULING__PRIVATE_CLAIMS__I_ = (
        625,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt rescheduling:  Private claims (I)"
        ),
    )
    DEBT_RESCHEDULING__OOF_CLAIMS__DSR_ = (
        626,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt rescheduling: OOF claims (DSR)"
        ),
    )
    DEBT_RESCHEDULING__PRIVATE_CLAIMS__DSR_ = (
        627,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt rescheduling:  Private claims (DSR)"
        ),
    )
    DEBT_RESCHEDULING__OOF_CLAIM__DSR___ORIGINAL_LOAN_PRINCIPAL_ = (
        630,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt rescheduling: OOF claim (DSR – original loan principal)",
        ),
    )
    DEBT_RESCHEDULING__OOF_CLAIM__DSR___ORIGINAL_LOAN_INTEREST_ = (
        631,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt rescheduling: OOF claim (DSR – original loan interest)",
        ),
    )
    DEBT_RESCHEDULING__PRIVATE_CLAIM__DSR___ORIGINAL_LOAN_PRINCIPAL_ = (
        632,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt rescheduling: Private claim (DSR – original loan principal)",
        ),
    )
    DEBT_FORGIVENESS_CONVERSION__EXPORT_CREDIT_CLAIMS__P_ = (
        633,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt forgiveness/conversion: export credit claims (P)",
        ),
    )
    DEBT_FORGIVENESS_CONVERSION__EXPORT_CREDIT_CLAIMS__I_ = (
        634,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt forgiveness/conversion:  export credit claims (I)",
        ),
    )
    DEBT_FORGIVENESS__EXPORT_CREDIT_CLAIMS__DSR_ = (
        635,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt forgiveness:  export credit claims (DSR)"
        ),
    )
    DEBT_RESCHEDULING__EXPORT_CREDIT_CLAIMS__P_ = (
        636,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt rescheduling:  export credit claims (P)"
        ),
    )
    DEBT_RESCHEDULING__EXPORT_CREDIT_CLAIMS__I_ = (
        637,
        pgettext_lazy(
            "IATI codelist FinanceType", "Debt rescheduling:  export credit claims (I)"
        ),
    )
    DEBT_RESCHEDULING__EXPORT_CREDIT_CLAIMS__DSR_ = (
        638,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt rescheduling:  export credit claims (DSR)",
        ),
    )
    DEBT_RESCHEDULING__EXPORT_CREDIT_CLAIM__DSR___ORIGINAL_LOAN_PRINCIPAL_ = (
        639,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Debt rescheduling:  export credit claim (DSR – original loan principal)",
        ),
    )
    FOREIGN_DIRECT_INVESTMENT__NEW_CAPITAL_OUTFLOW__INCLUDES_REINVESTED_EARNINGS_IF_SEPARATE_IDENTIFICATION_NOT_AVAILABLE_ = (
        710,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Foreign direct investment, new capital outflow (includes reinvested earnings if separate identification not available)",
        ),
    )
    OTHER_FOREIGN_DIRECT_INVESTMENT__INCLUDING_REINVESTED_EARNINGS = (
        711,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Other foreign direct investment, including reinvested earnings",
        ),
    )
    FOREIGN_DIRECT_INVESTMENT__REINVESTED_EARNINGS = (
        712,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Foreign direct investment, reinvested earnings",
        ),
    )
    BANK_BONDS = (
        810,
        pgettext_lazy("IATI codelist FinanceType", "Bank bonds"),
    )
    NON_BANK_BONDS = (
        811,
        pgettext_lazy("IATI codelist FinanceType", "Non-bank  bonds"),
    )
    OTHER_BANK_SECURITIES_CLAIMS = (
        910,
        pgettext_lazy("IATI codelist FinanceType", "Other bank securities/claims"),
    )
    OTHER_NON_BANK_SECURITIES_CLAIMS = (
        911,
        pgettext_lazy("IATI codelist FinanceType", "Other non-bank securities/claims"),
    )
    PURCHASE_OF_SECURITIES_FROM_ISSUING_AGENCIES = (
        912,
        pgettext_lazy(
            "IATI codelist FinanceType", "Purchase of securities from issuing agencies"
        ),
    )
    SECURITIES_AND_OTHER_INSTRUMENTS_ORIGINALLY_ISSUED_BY_MULTILATERAL_AGENCIES = (
        913,
        pgettext_lazy(
            "IATI codelist FinanceType",
            "Securities and other instruments originally issued by multilateral agencies",
        ),
    )
