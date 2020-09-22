from django.db import models
from django.utils.translation import pgettext_lazy


class Currency(models.TextChoices):
    """
    ISO 4217 Currency used for all transactions and budgets
    """

    UAE_DIRHAM = (
        "AED",
        pgettext_lazy("Currency", "UAE Dirham"),
    )
    AFGHANI = (
        "AFN",
        pgettext_lazy("Currency", "Afghani"),
    )
    LEK = (
        "ALL",
        pgettext_lazy("Currency", "Lek"),
    )
    ARMENIAN_DRAM = (
        "AMD",
        pgettext_lazy("Currency", "Armenian Dram"),
    )
    NETHERLANDS_ANTILLIAN_GUILDER = (
        "ANG",
        pgettext_lazy("Currency", "Netherlands Antillian Guilder"),
    )
    KWANZA = (
        "AOA",
        pgettext_lazy("Currency", "Kwanza"),
    )
    ARGENTINE_PESO = (
        "ARS",
        pgettext_lazy("Currency", "Argentine Peso"),
    )
    AUSTRALIAN_DOLLAR = (
        "AUD",
        pgettext_lazy("Currency", "Australian Dollar"),
    )
    ARUBAN_GUILDER = (
        "AWG",
        pgettext_lazy("Currency", "Aruban Guilder"),
    )
    AZERBAIJANIAN_MANAT = (
        "AZN",
        pgettext_lazy("Currency", "Azerbaijanian Manat"),
    )
    CONVERTIBLE_MARKS = (
        "BAM",
        pgettext_lazy("Currency", "Convertible Marks"),
    )
    BARBADOS_DOLLAR = (
        "BBD",
        pgettext_lazy("Currency", "Barbados Dollar"),
    )
    TAKA = (
        "BDT",
        pgettext_lazy("Currency", "Taka"),
    )
    BULGARIAN_LEV = (
        "BGN",
        pgettext_lazy("Currency", "Bulgarian Lev"),
    )
    BAHRAINI_DINAR = (
        "BHD",
        pgettext_lazy("Currency", "Bahraini Dinar"),
    )
    BURUNDI_FRANC = (
        "BIF",
        pgettext_lazy("Currency", "Burundi Franc"),
    )
    BERMUDIAN_DOLLAR = (
        "BMD",
        pgettext_lazy("Currency", "Bermudian Dollar"),
    )
    BRUNEI_DOLLAR = (
        "BND",
        pgettext_lazy("Currency", "Brunei Dollar"),
    )
    BOLIVIANO = (
        "BOB",
        pgettext_lazy("Currency", "Boliviano"),
    )
    MVDOL = (
        "BOV",
        pgettext_lazy("Currency", "Mvdol"),
    )
    BRAZILIAN_REAL = (
        "BRL",
        pgettext_lazy("Currency", "Brazilian Real"),
    )
    BAHAMIAN_DOLLAR = (
        "BSD",
        pgettext_lazy("Currency", "Bahamian Dollar"),
    )
    NGULTRUM = (
        "BTN",
        pgettext_lazy("Currency", "Ngultrum"),
    )
    PULA = (
        "BWP",
        pgettext_lazy("Currency", "Pula"),
    )
    BELARUSSIAN_RUBLE = (
        "BYR",
        pgettext_lazy("Currency", "Belarussian Ruble"),
    )
    BELARUSSIAN_RUBLE = (
        "BYN",
        pgettext_lazy("Currency", "Belarussian Ruble"),
    )
    BELIZE_DOLLAR = (
        "BZD",
        pgettext_lazy("Currency", "Belize Dollar"),
    )
    CANADIAN_DOLLAR = (
        "CAD",
        pgettext_lazy("Currency", "Canadian Dollar"),
    )
    CONGOLESE_FRANC = (
        "CDF",
        pgettext_lazy("Currency", "Congolese Franc"),
    )
    SWISS_FRANC = (
        "CHF",
        pgettext_lazy("Currency", "Swiss Franc"),
    )
    UNIDADES_DE_FOMENTO = (
        "CLF",
        pgettext_lazy("Currency", "Unidades de fomento"),
    )
    CHILEAN_PESO = (
        "CLP",
        pgettext_lazy("Currency", "Chilean Peso"),
    )
    YUAN_RENMINBI = (
        "CNY",
        pgettext_lazy("Currency", "Yuan Renminbi"),
    )
    COLOMBIAN_PESO = (
        "COP",
        pgettext_lazy("Currency", "Colombian Peso"),
    )
    UNIDAD_DE_VALOR_REAL = (
        "COU",
        pgettext_lazy("Currency", "Unidad de Valor Real"),
    )
    COSTA_RICAN_COLON = (
        "CRC",
        pgettext_lazy("Currency", "Costa Rican Colon"),
    )
    PESO_CONVERTIBLE = (
        "CUC",
        pgettext_lazy("Currency", "Peso Convertible"),
    )
    CUBAN_PESO = (
        "CUP",
        pgettext_lazy("Currency", "Cuban Peso"),
    )
    CAPE_VERDE_ESCUDO = (
        "CVE",
        pgettext_lazy("Currency", "Cape Verde Escudo"),
    )
    CZECH_KORUNA = (
        "CZK",
        pgettext_lazy("Currency", "Czech Koruna"),
    )
    DJIBOUTI_FRANC = (
        "DJF",
        pgettext_lazy("Currency", "Djibouti Franc"),
    )
    DANISH_KRONE = (
        "DKK",
        pgettext_lazy("Currency", "Danish Krone"),
    )
    DOMINICAN_PESO = (
        "DOP",
        pgettext_lazy("Currency", "Dominican Peso"),
    )
    ALGERIAN_DINAR = (
        "DZD",
        pgettext_lazy("Currency", "Algerian Dinar"),
    )
    KROON = (
        "EEK",
        pgettext_lazy("Currency", "Kroon"),
    )
    EGYPTIAN_POUND = (
        "EGP",
        pgettext_lazy("Currency", "Egyptian Pound"),
    )
    NAKFA = (
        "ERN",
        pgettext_lazy("Currency", "Nakfa"),
    )
    ETHIOPIAN_BIRR = (
        "ETB",
        pgettext_lazy("Currency", "Ethiopian Birr"),
    )
    EURO = (
        "EUR",
        pgettext_lazy("Currency", "Euro"),
    )
    FIJI_DOLLAR = (
        "FJD",
        pgettext_lazy("Currency", "Fiji Dollar"),
    )
    FALKLAND_ISLANDS_POUND = (
        "FKP",
        pgettext_lazy("Currency", "Falkland Islands Pound"),
    )
    POUND_STERLING = (
        "GBP",
        pgettext_lazy("Currency", "Pound Sterling"),
    )
    LARI = (
        "GEL",
        pgettext_lazy("Currency", "Lari"),
    )
    CEDI = (
        "GHS",
        pgettext_lazy("Currency", "Cedi"),
    )
    GIBRALTAR_POUND = (
        "GIP",
        pgettext_lazy("Currency", "Gibraltar Pound"),
    )
    DALASI = (
        "GMD",
        pgettext_lazy("Currency", "Dalasi"),
    )
    GUINEA_FRANC = (
        "GNF",
        pgettext_lazy("Currency", "Guinea Franc"),
    )
    QUETZAL = (
        "GTQ",
        pgettext_lazy("Currency", "Quetzal"),
    )
    GUYANA_DOLLAR = (
        "GYD",
        pgettext_lazy("Currency", "Guyana Dollar"),
    )
    HONG_KONG_DOLLAR = (
        "HKD",
        pgettext_lazy("Currency", "Hong Kong Dollar"),
    )
    LEMPIRA = (
        "HNL",
        pgettext_lazy("Currency", "Lempira"),
    )
    KUNA = (
        "HRK",
        pgettext_lazy("Currency", "Kuna"),
    )
    GOURDE = (
        "HTG",
        pgettext_lazy("Currency", "Gourde"),
    )
    FORINT = (
        "HUF",
        pgettext_lazy("Currency", "Forint"),
    )
    RUPIAH = (
        "IDR",
        pgettext_lazy("Currency", "Rupiah"),
    )
    NEW_ISRAELI_SHEQEL = (
        "ILS",
        pgettext_lazy("Currency", "New Israeli Sheqel"),
    )
    INDIAN_RUPEE = (
        "INR",
        pgettext_lazy("Currency", "Indian Rupee"),
    )
    IRAQI_DINAR = (
        "IQD",
        pgettext_lazy("Currency", "Iraqi Dinar"),
    )
    IRANIAN_RIAL = (
        "IRR",
        pgettext_lazy("Currency", "Iranian Rial"),
    )
    ICELAND_KRONA = (
        "ISK",
        pgettext_lazy("Currency", "Iceland Krona"),
    )
    JAMAICAN_DOLLAR = (
        "JMD",
        pgettext_lazy("Currency", "Jamaican Dollar"),
    )
    JORDANIAN_DINAR = (
        "JOD",
        pgettext_lazy("Currency", "Jordanian Dinar"),
    )
    YEN = (
        "JPY",
        pgettext_lazy("Currency", "Yen"),
    )
    KENYAN_SHILLING = (
        "KES",
        pgettext_lazy("Currency", "Kenyan Shilling"),
    )
    SOM = (
        "KGS",
        pgettext_lazy("Currency", "Som"),
    )
    RIEL = (
        "KHR",
        pgettext_lazy("Currency", "Riel"),
    )
    COMORO_FRANC = (
        "KMF",
        pgettext_lazy("Currency", "Comoro Franc"),
    )
    NORTH_KOREAN_WON = (
        "KPW",
        pgettext_lazy("Currency", "North Korean Won"),
    )
    WON = (
        "KRW",
        pgettext_lazy("Currency", "Won"),
    )
    KUWAITI_DINAR = (
        "KWD",
        pgettext_lazy("Currency", "Kuwaiti Dinar"),
    )
    CAYMAN_ISLANDS_DOLLAR = (
        "KYD",
        pgettext_lazy("Currency", "Cayman Islands Dollar"),
    )
    TENGE = (
        "KZT",
        pgettext_lazy("Currency", "Tenge"),
    )
    KIP = (
        "LAK",
        pgettext_lazy("Currency", "Kip"),
    )
    LEBANESE_POUND = (
        "LBP",
        pgettext_lazy("Currency", "Lebanese Pound"),
    )
    SRI_LANKA_RUPEE = (
        "LKR",
        pgettext_lazy("Currency", "Sri Lanka Rupee"),
    )
    LIBERIAN_DOLLAR = (
        "LRD",
        pgettext_lazy("Currency", "Liberian Dollar"),
    )
    LOTI = (
        "LSL",
        pgettext_lazy("Currency", "Loti"),
    )
    LITHUANIAN_LITAS = (
        "LTL",
        pgettext_lazy("Currency", "Lithuanian Litas"),
    )
    LATVIAN_LATS = (
        "LVL",
        pgettext_lazy("Currency", "Latvian Lats"),
    )
    LIBYAN_DINAR = (
        "LYD",
        pgettext_lazy("Currency", "Libyan Dinar"),
    )
    MOROCCAN_DIRHAM = (
        "MAD",
        pgettext_lazy("Currency", "Moroccan Dirham"),
    )
    MOLDOVAN_LEU = (
        "MDL",
        pgettext_lazy("Currency", "Moldovan Leu"),
    )
    MALAGASY_ARIARY = (
        "MGA",
        pgettext_lazy("Currency", "Malagasy Ariary"),
    )
    DENAR = (
        "MKD",
        pgettext_lazy("Currency", "Denar"),
    )
    KYAT = (
        "MMK",
        pgettext_lazy("Currency", "Kyat"),
    )
    TUGRIK = (
        "MNT",
        pgettext_lazy("Currency", "Tugrik"),
    )
    PATACA = (
        "MOP",
        pgettext_lazy("Currency", "Pataca"),
    )
    OUGUIYA = (
        "MRO",
        pgettext_lazy("Currency", "Ouguiya"),
    )
    OUGUIYA = (
        "MRU",
        pgettext_lazy("Currency", "Ouguiya"),
    )
    MAURITIUS_RUPEE = (
        "MUR",
        pgettext_lazy("Currency", "Mauritius Rupee"),
    )
    RUFIYAA = (
        "MVR",
        pgettext_lazy("Currency", "Rufiyaa"),
    )
    MALAWI_KWACHA = (
        "MWK",
        pgettext_lazy("Currency", "Malawi Kwacha"),
    )
    MEXICAN_PESO = (
        "MXN",
        pgettext_lazy("Currency", "Mexican Peso"),
    )
    MEXICAN_UNIDAD_DE_INVERSION__UDI_ = (
        "MXV",
        pgettext_lazy("Currency", "Mexican Unidad de Inversion (UDI)"),
    )
    MALAYSIAN_RINGGIT = (
        "MYR",
        pgettext_lazy("Currency", "Malaysian Ringgit"),
    )
    METICAL = (
        "MZN",
        pgettext_lazy("Currency", "Metical"),
    )
    NAMIBIA_DOLLAR = (
        "NAD",
        pgettext_lazy("Currency", "Namibia Dollar"),
    )
    NAIRA = (
        "NGN",
        pgettext_lazy("Currency", "Naira"),
    )
    CORDOBA_ORO = (
        "NIO",
        pgettext_lazy("Currency", "Cordoba Oro"),
    )
    NORWEGIAN_KRONE = (
        "NOK",
        pgettext_lazy("Currency", "Norwegian Krone"),
    )
    NEPALESE_RUPEE = (
        "NPR",
        pgettext_lazy("Currency", "Nepalese Rupee"),
    )
    NEW_ZEALAND_DOLLAR = (
        "NZD",
        pgettext_lazy("Currency", "New Zealand Dollar"),
    )
    RIAL_OMANI = (
        "OMR",
        pgettext_lazy("Currency", "Rial Omani"),
    )
    BALBOA = (
        "PAB",
        pgettext_lazy("Currency", "Balboa"),
    )
    NUEVO_SOL = (
        "PEN",
        pgettext_lazy("Currency", "Nuevo Sol"),
    )
    KINA = (
        "PGK",
        pgettext_lazy("Currency", "Kina"),
    )
    PHILIPPINE_PESO = (
        "PHP",
        pgettext_lazy("Currency", "Philippine Peso"),
    )
    PAKISTAN_RUPEE = (
        "PKR",
        pgettext_lazy("Currency", "Pakistan Rupee"),
    )
    ZLOTY = (
        "PLN",
        pgettext_lazy("Currency", "Zloty"),
    )
    GUARANI = (
        "PYG",
        pgettext_lazy("Currency", "Guarani"),
    )
    QATARI_RIAL = (
        "QAR",
        pgettext_lazy("Currency", "Qatari Rial"),
    )
    ROMANIAN_LEU = (
        "RON",
        pgettext_lazy("Currency", "Romanian Leu"),
    )
    SERBIAN_DINAR = (
        "RSD",
        pgettext_lazy("Currency", "Serbian Dinar"),
    )
    RUSSIAN_RUBLE = (
        "RUB",
        pgettext_lazy("Currency", "Russian Ruble"),
    )
    RWANDA_FRANC = (
        "RWF",
        pgettext_lazy("Currency", "Rwanda Franc"),
    )
    SAUDI_RIYAL = (
        "SAR",
        pgettext_lazy("Currency", "Saudi Riyal"),
    )
    SOLOMON_ISLANDS_DOLLAR = (
        "SBD",
        pgettext_lazy("Currency", "Solomon Islands Dollar"),
    )
    SEYCHELLES_RUPEE = (
        "SCR",
        pgettext_lazy("Currency", "Seychelles Rupee"),
    )
    SUDANESE_POUND = (
        "SDG",
        pgettext_lazy("Currency", "Sudanese Pound"),
    )
    SWEDISH_KRONA = (
        "SEK",
        pgettext_lazy("Currency", "Swedish Krona"),
    )
    SINGAPORE_DOLLAR = (
        "SGD",
        pgettext_lazy("Currency", "Singapore Dollar"),
    )
    SAINT_HELENA_POUND = (
        "SHP",
        pgettext_lazy("Currency", "Saint Helena Pound"),
    )
    LEONE = (
        "SLL",
        pgettext_lazy("Currency", "Leone"),
    )
    SOMALI_SHILLING = (
        "SOS",
        pgettext_lazy("Currency", "Somali Shilling"),
    )
    SOUTH_SUDANESE_POUND = (
        "SSP",
        pgettext_lazy("Currency", "South Sudanese Pound"),
    )
    SURINAM_DOLLAR = (
        "SRD",
        pgettext_lazy("Currency", "Surinam Dollar"),
    )
    DOBRA = (
        "STD",
        pgettext_lazy("Currency", "Dobra"),
    )
    DOBRA = (
        "STN",
        pgettext_lazy("Currency", "Dobra"),
    )
    EL_SALVADOR_COLON = (
        "SVC",
        pgettext_lazy("Currency", "El Salvador Colon"),
    )
    SYRIAN_POUND = (
        "SYP",
        pgettext_lazy("Currency", "Syrian Pound"),
    )
    LILANGENI = (
        "SZL",
        pgettext_lazy("Currency", "Lilangeni"),
    )
    BAHT = (
        "THB",
        pgettext_lazy("Currency", "Baht"),
    )
    SOMONI = (
        "TJS",
        pgettext_lazy("Currency", "Somoni"),
    )
    MANAT = (
        "TMT",
        pgettext_lazy("Currency", "Manat"),
    )
    TUNISIAN_DINAR = (
        "TND",
        pgettext_lazy("Currency", "Tunisian Dinar"),
    )
    PAANGA = (
        "TOP",
        pgettext_lazy("Currency", "Paanga"),
    )
    TURKISH_LIRA = (
        "TRY",
        pgettext_lazy("Currency", "Turkish Lira"),
    )
    TRINIDAD_AND_TOBAGO_DOLLAR = (
        "TTD",
        pgettext_lazy("Currency", "Trinidad and Tobago Dollar"),
    )
    NEW_TAIWAN_DOLLAR = (
        "TWD",
        pgettext_lazy("Currency", "New Taiwan Dollar"),
    )
    TANZANIAN_SHILLING = (
        "TZS",
        pgettext_lazy("Currency", "Tanzanian Shilling"),
    )
    HRYVNIA = (
        "UAH",
        pgettext_lazy("Currency", "Hryvnia"),
    )
    UGANDA_SHILLING = (
        "UGX",
        pgettext_lazy("Currency", "Uganda Shilling"),
    )
    US_DOLLAR = (
        "USD",
        pgettext_lazy("Currency", "US Dollar"),
    )
    US_DOLLAR__NEXT_DAY_ = (
        "USN",
        pgettext_lazy("Currency", "US Dollar (Next day)"),
    )
    US_DOLLAR__SAME_DAY_ = (
        "USS",
        pgettext_lazy("Currency", "US Dollar (Same day)"),
    )
    URUGUAY_PESO_EN_UNIDADES_INDEXADAS = (
        "UYI",
        pgettext_lazy("Currency", "Uruguay Peso en Unidades Indexadas"),
    )
    PESO_URUGUAYO = (
        "UYU",
        pgettext_lazy("Currency", "Peso Uruguayo"),
    )
    UZBEKISTAN_SUM = (
        "UZS",
        pgettext_lazy("Currency", "Uzbekistan Sum"),
    )
    BOLIVAR = (
        "VEF",
        pgettext_lazy("Currency", "Bolivar"),
    )
    BOLIVAR_SOBERANO = (
        "VES",
        pgettext_lazy("Currency", "Bolivar Soberano"),
    )
    DONG = (
        "VND",
        pgettext_lazy("Currency", "Dong"),
    )
    VATU = (
        "VUV",
        pgettext_lazy("Currency", "Vatu"),
    )
    TALA = (
        "WST",
        pgettext_lazy("Currency", "Tala"),
    )
    CFA_FRANC_BEAC = (
        "XAF",
        pgettext_lazy("Currency", "CFA Franc BEAC"),
    )
    BITCOIN = (
        "XBT",
        pgettext_lazy("Currency", "Bitcoin"),
    )
    EAST_CARIBBEAN_DOLLAR = (
        "XCD",
        pgettext_lazy("Currency", "East Caribbean Dollar"),
    )
    INTERNATIONAL_MONETARY_FUND__IMF__SPECIAL_DRAWING_RIGHT__SDR_ = (
        "XDR",
        pgettext_lazy(
            "Currency",
            "International Monetary Fund (IMF) Special Drawing Right (SDR)",
        ),
    )
    CFA_FRANC_BCEAO = (
        "XOF",
        pgettext_lazy("Currency", "CFA Franc BCEAO"),
    )
    CFP_FRANC = (
        "XPF",
        pgettext_lazy("Currency", "CFP Franc"),
    )
    YEMENI_RIAL = (
        "YER",
        pgettext_lazy("Currency", "Yemeni Rial"),
    )
    RAND = (
        "ZAR",
        pgettext_lazy("Currency", "Rand"),
    )
    ZAMBIAN_KWACHA = (
        "ZMK",
        pgettext_lazy("Currency", "Zambian Kwacha"),
    )
    ZAMBIAN_KWACHA = (
        "ZMW",
        pgettext_lazy("Currency", "Zambian Kwacha"),
    )
    ZIMBABWE_DOLLAR = (
        "ZWL",
        pgettext_lazy("Currency", "Zimbabwe Dollar"),
    )
