from django.db import models
from django.utils.translation import pgettext_lazy


class Currency(models.TextChoices):
    """
    ISO 4217 Currency used for all transactions and budgets
    """

    UAE_DIRHAM = (
        "AED",
        pgettext_lazy("IATI codelist Currency", "UAE Dirham"),
    )
    AFGHANI = (
        "AFN",
        pgettext_lazy("IATI codelist Currency", "Afghani"),
    )
    LEK = (
        "ALL",
        pgettext_lazy("IATI codelist Currency", "Lek"),
    )
    ARMENIAN_DRAM = (
        "AMD",
        pgettext_lazy("IATI codelist Currency", "Armenian Dram"),
    )
    NETHERLANDS_ANTILLIAN_GUILDER = (
        "ANG",
        pgettext_lazy("IATI codelist Currency", "Netherlands Antillian Guilder"),
    )
    KWANZA = (
        "AOA",
        pgettext_lazy("IATI codelist Currency", "Kwanza"),
    )
    ARGENTINE_PESO = (
        "ARS",
        pgettext_lazy("IATI codelist Currency", "Argentine Peso"),
    )
    AUSTRALIAN_DOLLAR = (
        "AUD",
        pgettext_lazy("IATI codelist Currency", "Australian Dollar"),
    )
    ARUBAN_GUILDER = (
        "AWG",
        pgettext_lazy("IATI codelist Currency", "Aruban Guilder"),
    )
    AZERBAIJANIAN_MANAT = (
        "AZN",
        pgettext_lazy("IATI codelist Currency", "Azerbaijanian Manat"),
    )
    CONVERTIBLE_MARKS = (
        "BAM",
        pgettext_lazy("IATI codelist Currency", "Convertible Marks"),
    )
    BARBADOS_DOLLAR = (
        "BBD",
        pgettext_lazy("IATI codelist Currency", "Barbados Dollar"),
    )
    TAKA = (
        "BDT",
        pgettext_lazy("IATI codelist Currency", "Taka"),
    )
    BULGARIAN_LEV = (
        "BGN",
        pgettext_lazy("IATI codelist Currency", "Bulgarian Lev"),
    )
    BAHRAINI_DINAR = (
        "BHD",
        pgettext_lazy("IATI codelist Currency", "Bahraini Dinar"),
    )
    BURUNDI_FRANC = (
        "BIF",
        pgettext_lazy("IATI codelist Currency", "Burundi Franc"),
    )
    BERMUDIAN_DOLLAR = (
        "BMD",
        pgettext_lazy("IATI codelist Currency", "Bermudian Dollar"),
    )
    BRUNEI_DOLLAR = (
        "BND",
        pgettext_lazy("IATI codelist Currency", "Brunei Dollar"),
    )
    BOLIVIANO = (
        "BOB",
        pgettext_lazy("IATI codelist Currency", "Boliviano"),
    )
    MVDOL = (
        "BOV",
        pgettext_lazy("IATI codelist Currency", "Mvdol"),
    )
    BRAZILIAN_REAL = (
        "BRL",
        pgettext_lazy("IATI codelist Currency", "Brazilian Real"),
    )
    BAHAMIAN_DOLLAR = (
        "BSD",
        pgettext_lazy("IATI codelist Currency", "Bahamian Dollar"),
    )
    NGULTRUM = (
        "BTN",
        pgettext_lazy("IATI codelist Currency", "Ngultrum"),
    )
    PULA = (
        "BWP",
        pgettext_lazy("IATI codelist Currency", "Pula"),
    )
    BELARUSSIAN_RUBLE = (
        "BYR",
        pgettext_lazy("IATI codelist Currency", "Belarussian Ruble"),
    )
    BELARUSSIAN_RUBLE = (
        "BYN",
        pgettext_lazy("IATI codelist Currency", "Belarussian Ruble"),
    )
    BELIZE_DOLLAR = (
        "BZD",
        pgettext_lazy("IATI codelist Currency", "Belize Dollar"),
    )
    CANADIAN_DOLLAR = (
        "CAD",
        pgettext_lazy("IATI codelist Currency", "Canadian Dollar"),
    )
    CONGOLESE_FRANC = (
        "CDF",
        pgettext_lazy("IATI codelist Currency", "Congolese Franc"),
    )
    SWISS_FRANC = (
        "CHF",
        pgettext_lazy("IATI codelist Currency", "Swiss Franc"),
    )
    UNIDADES_DE_FOMENTO = (
        "CLF",
        pgettext_lazy("IATI codelist Currency", "Unidades de fomento"),
    )
    CHILEAN_PESO = (
        "CLP",
        pgettext_lazy("IATI codelist Currency", "Chilean Peso"),
    )
    YUAN_RENMINBI = (
        "CNY",
        pgettext_lazy("IATI codelist Currency", "Yuan Renminbi"),
    )
    COLOMBIAN_PESO = (
        "COP",
        pgettext_lazy("IATI codelist Currency", "Colombian Peso"),
    )
    UNIDAD_DE_VALOR_REAL = (
        "COU",
        pgettext_lazy("IATI codelist Currency", "Unidad de Valor Real"),
    )
    COSTA_RICAN_COLON = (
        "CRC",
        pgettext_lazy("IATI codelist Currency", "Costa Rican Colon"),
    )
    PESO_CONVERTIBLE = (
        "CUC",
        pgettext_lazy("IATI codelist Currency", "Peso Convertible"),
    )
    CUBAN_PESO = (
        "CUP",
        pgettext_lazy("IATI codelist Currency", "Cuban Peso"),
    )
    CAPE_VERDE_ESCUDO = (
        "CVE",
        pgettext_lazy("IATI codelist Currency", "Cape Verde Escudo"),
    )
    CZECH_KORUNA = (
        "CZK",
        pgettext_lazy("IATI codelist Currency", "Czech Koruna"),
    )
    DJIBOUTI_FRANC = (
        "DJF",
        pgettext_lazy("IATI codelist Currency", "Djibouti Franc"),
    )
    DANISH_KRONE = (
        "DKK",
        pgettext_lazy("IATI codelist Currency", "Danish Krone"),
    )
    DOMINICAN_PESO = (
        "DOP",
        pgettext_lazy("IATI codelist Currency", "Dominican Peso"),
    )
    ALGERIAN_DINAR = (
        "DZD",
        pgettext_lazy("IATI codelist Currency", "Algerian Dinar"),
    )
    KROON = (
        "EEK",
        pgettext_lazy("IATI codelist Currency", "Kroon"),
    )
    EGYPTIAN_POUND = (
        "EGP",
        pgettext_lazy("IATI codelist Currency", "Egyptian Pound"),
    )
    NAKFA = (
        "ERN",
        pgettext_lazy("IATI codelist Currency", "Nakfa"),
    )
    ETHIOPIAN_BIRR = (
        "ETB",
        pgettext_lazy("IATI codelist Currency", "Ethiopian Birr"),
    )
    EURO = (
        "EUR",
        pgettext_lazy("IATI codelist Currency", "Euro"),
    )
    FIJI_DOLLAR = (
        "FJD",
        pgettext_lazy("IATI codelist Currency", "Fiji Dollar"),
    )
    FALKLAND_ISLANDS_POUND = (
        "FKP",
        pgettext_lazy("IATI codelist Currency", "Falkland Islands Pound"),
    )
    POUND_STERLING = (
        "GBP",
        pgettext_lazy("IATI codelist Currency", "Pound Sterling"),
    )
    LARI = (
        "GEL",
        pgettext_lazy("IATI codelist Currency", "Lari"),
    )
    CEDI = (
        "GHS",
        pgettext_lazy("IATI codelist Currency", "Cedi"),
    )
    GIBRALTAR_POUND = (
        "GIP",
        pgettext_lazy("IATI codelist Currency", "Gibraltar Pound"),
    )
    DALASI = (
        "GMD",
        pgettext_lazy("IATI codelist Currency", "Dalasi"),
    )
    GUINEA_FRANC = (
        "GNF",
        pgettext_lazy("IATI codelist Currency", "Guinea Franc"),
    )
    QUETZAL = (
        "GTQ",
        pgettext_lazy("IATI codelist Currency", "Quetzal"),
    )
    GUYANA_DOLLAR = (
        "GYD",
        pgettext_lazy("IATI codelist Currency", "Guyana Dollar"),
    )
    HONG_KONG_DOLLAR = (
        "HKD",
        pgettext_lazy("IATI codelist Currency", "Hong Kong Dollar"),
    )
    LEMPIRA = (
        "HNL",
        pgettext_lazy("IATI codelist Currency", "Lempira"),
    )
    KUNA = (
        "HRK",
        pgettext_lazy("IATI codelist Currency", "Kuna"),
    )
    GOURDE = (
        "HTG",
        pgettext_lazy("IATI codelist Currency", "Gourde"),
    )
    FORINT = (
        "HUF",
        pgettext_lazy("IATI codelist Currency", "Forint"),
    )
    RUPIAH = (
        "IDR",
        pgettext_lazy("IATI codelist Currency", "Rupiah"),
    )
    NEW_ISRAELI_SHEQEL = (
        "ILS",
        pgettext_lazy("IATI codelist Currency", "New Israeli Sheqel"),
    )
    INDIAN_RUPEE = (
        "INR",
        pgettext_lazy("IATI codelist Currency", "Indian Rupee"),
    )
    IRAQI_DINAR = (
        "IQD",
        pgettext_lazy("IATI codelist Currency", "Iraqi Dinar"),
    )
    IRANIAN_RIAL = (
        "IRR",
        pgettext_lazy("IATI codelist Currency", "Iranian Rial"),
    )
    ICELAND_KRONA = (
        "ISK",
        pgettext_lazy("IATI codelist Currency", "Iceland Krona"),
    )
    JAMAICAN_DOLLAR = (
        "JMD",
        pgettext_lazy("IATI codelist Currency", "Jamaican Dollar"),
    )
    JORDANIAN_DINAR = (
        "JOD",
        pgettext_lazy("IATI codelist Currency", "Jordanian Dinar"),
    )
    YEN = (
        "JPY",
        pgettext_lazy("IATI codelist Currency", "Yen"),
    )
    KENYAN_SHILLING = (
        "KES",
        pgettext_lazy("IATI codelist Currency", "Kenyan Shilling"),
    )
    SOM = (
        "KGS",
        pgettext_lazy("IATI codelist Currency", "Som"),
    )
    RIEL = (
        "KHR",
        pgettext_lazy("IATI codelist Currency", "Riel"),
    )
    COMORO_FRANC = (
        "KMF",
        pgettext_lazy("IATI codelist Currency", "Comoro Franc"),
    )
    NORTH_KOREAN_WON = (
        "KPW",
        pgettext_lazy("IATI codelist Currency", "North Korean Won"),
    )
    WON = (
        "KRW",
        pgettext_lazy("IATI codelist Currency", "Won"),
    )
    KUWAITI_DINAR = (
        "KWD",
        pgettext_lazy("IATI codelist Currency", "Kuwaiti Dinar"),
    )
    CAYMAN_ISLANDS_DOLLAR = (
        "KYD",
        pgettext_lazy("IATI codelist Currency", "Cayman Islands Dollar"),
    )
    TENGE = (
        "KZT",
        pgettext_lazy("IATI codelist Currency", "Tenge"),
    )
    KIP = (
        "LAK",
        pgettext_lazy("IATI codelist Currency", "Kip"),
    )
    LEBANESE_POUND = (
        "LBP",
        pgettext_lazy("IATI codelist Currency", "Lebanese Pound"),
    )
    SRI_LANKA_RUPEE = (
        "LKR",
        pgettext_lazy("IATI codelist Currency", "Sri Lanka Rupee"),
    )
    LIBERIAN_DOLLAR = (
        "LRD",
        pgettext_lazy("IATI codelist Currency", "Liberian Dollar"),
    )
    LOTI = (
        "LSL",
        pgettext_lazy("IATI codelist Currency", "Loti"),
    )
    LITHUANIAN_LITAS = (
        "LTL",
        pgettext_lazy("IATI codelist Currency", "Lithuanian Litas"),
    )
    LATVIAN_LATS = (
        "LVL",
        pgettext_lazy("IATI codelist Currency", "Latvian Lats"),
    )
    LIBYAN_DINAR = (
        "LYD",
        pgettext_lazy("IATI codelist Currency", "Libyan Dinar"),
    )
    MOROCCAN_DIRHAM = (
        "MAD",
        pgettext_lazy("IATI codelist Currency", "Moroccan Dirham"),
    )
    MOLDOVAN_LEU = (
        "MDL",
        pgettext_lazy("IATI codelist Currency", "Moldovan Leu"),
    )
    MALAGASY_ARIARY = (
        "MGA",
        pgettext_lazy("IATI codelist Currency", "Malagasy Ariary"),
    )
    DENAR = (
        "MKD",
        pgettext_lazy("IATI codelist Currency", "Denar"),
    )
    KYAT = (
        "MMK",
        pgettext_lazy("IATI codelist Currency", "Kyat"),
    )
    TUGRIK = (
        "MNT",
        pgettext_lazy("IATI codelist Currency", "Tugrik"),
    )
    PATACA = (
        "MOP",
        pgettext_lazy("IATI codelist Currency", "Pataca"),
    )
    OUGUIYA = (
        "MRO",
        pgettext_lazy("IATI codelist Currency", "Ouguiya"),
    )
    OUGUIYA = (
        "MRU",
        pgettext_lazy("IATI codelist Currency", "Ouguiya"),
    )
    MAURITIUS_RUPEE = (
        "MUR",
        pgettext_lazy("IATI codelist Currency", "Mauritius Rupee"),
    )
    RUFIYAA = (
        "MVR",
        pgettext_lazy("IATI codelist Currency", "Rufiyaa"),
    )
    MALAWI_KWACHA = (
        "MWK",
        pgettext_lazy("IATI codelist Currency", "Malawi Kwacha"),
    )
    MEXICAN_PESO = (
        "MXN",
        pgettext_lazy("IATI codelist Currency", "Mexican Peso"),
    )
    MEXICAN_UNIDAD_DE_INVERSION__UDI_ = (
        "MXV",
        pgettext_lazy("IATI codelist Currency", "Mexican Unidad de Inversion (UDI)"),
    )
    MALAYSIAN_RINGGIT = (
        "MYR",
        pgettext_lazy("IATI codelist Currency", "Malaysian Ringgit"),
    )
    METICAL = (
        "MZN",
        pgettext_lazy("IATI codelist Currency", "Metical"),
    )
    NAMIBIA_DOLLAR = (
        "NAD",
        pgettext_lazy("IATI codelist Currency", "Namibia Dollar"),
    )
    NAIRA = (
        "NGN",
        pgettext_lazy("IATI codelist Currency", "Naira"),
    )
    CORDOBA_ORO = (
        "NIO",
        pgettext_lazy("IATI codelist Currency", "Cordoba Oro"),
    )
    NORWEGIAN_KRONE = (
        "NOK",
        pgettext_lazy("IATI codelist Currency", "Norwegian Krone"),
    )
    NEPALESE_RUPEE = (
        "NPR",
        pgettext_lazy("IATI codelist Currency", "Nepalese Rupee"),
    )
    NEW_ZEALAND_DOLLAR = (
        "NZD",
        pgettext_lazy("IATI codelist Currency", "New Zealand Dollar"),
    )
    RIAL_OMANI = (
        "OMR",
        pgettext_lazy("IATI codelist Currency", "Rial Omani"),
    )
    BALBOA = (
        "PAB",
        pgettext_lazy("IATI codelist Currency", "Balboa"),
    )
    NUEVO_SOL = (
        "PEN",
        pgettext_lazy("IATI codelist Currency", "Nuevo Sol"),
    )
    KINA = (
        "PGK",
        pgettext_lazy("IATI codelist Currency", "Kina"),
    )
    PHILIPPINE_PESO = (
        "PHP",
        pgettext_lazy("IATI codelist Currency", "Philippine Peso"),
    )
    PAKISTAN_RUPEE = (
        "PKR",
        pgettext_lazy("IATI codelist Currency", "Pakistan Rupee"),
    )
    ZLOTY = (
        "PLN",
        pgettext_lazy("IATI codelist Currency", "Zloty"),
    )
    GUARANI = (
        "PYG",
        pgettext_lazy("IATI codelist Currency", "Guarani"),
    )
    QATARI_RIAL = (
        "QAR",
        pgettext_lazy("IATI codelist Currency", "Qatari Rial"),
    )
    ROMANIAN_LEU = (
        "RON",
        pgettext_lazy("IATI codelist Currency", "Romanian Leu"),
    )
    SERBIAN_DINAR = (
        "RSD",
        pgettext_lazy("IATI codelist Currency", "Serbian Dinar"),
    )
    RUSSIAN_RUBLE = (
        "RUB",
        pgettext_lazy("IATI codelist Currency", "Russian Ruble"),
    )
    RWANDA_FRANC = (
        "RWF",
        pgettext_lazy("IATI codelist Currency", "Rwanda Franc"),
    )
    SAUDI_RIYAL = (
        "SAR",
        pgettext_lazy("IATI codelist Currency", "Saudi Riyal"),
    )
    SOLOMON_ISLANDS_DOLLAR = (
        "SBD",
        pgettext_lazy("IATI codelist Currency", "Solomon Islands Dollar"),
    )
    SEYCHELLES_RUPEE = (
        "SCR",
        pgettext_lazy("IATI codelist Currency", "Seychelles Rupee"),
    )
    SUDANESE_POUND = (
        "SDG",
        pgettext_lazy("IATI codelist Currency", "Sudanese Pound"),
    )
    SWEDISH_KRONA = (
        "SEK",
        pgettext_lazy("IATI codelist Currency", "Swedish Krona"),
    )
    SINGAPORE_DOLLAR = (
        "SGD",
        pgettext_lazy("IATI codelist Currency", "Singapore Dollar"),
    )
    SAINT_HELENA_POUND = (
        "SHP",
        pgettext_lazy("IATI codelist Currency", "Saint Helena Pound"),
    )
    LEONE = (
        "SLL",
        pgettext_lazy("IATI codelist Currency", "Leone"),
    )
    SOMALI_SHILLING = (
        "SOS",
        pgettext_lazy("IATI codelist Currency", "Somali Shilling"),
    )
    SOUTH_SUDANESE_POUND = (
        "SSP",
        pgettext_lazy("IATI codelist Currency", "South Sudanese Pound"),
    )
    SURINAM_DOLLAR = (
        "SRD",
        pgettext_lazy("IATI codelist Currency", "Surinam Dollar"),
    )
    DOBRA = (
        "STD",
        pgettext_lazy("IATI codelist Currency", "Dobra"),
    )
    DOBRA = (
        "STN",
        pgettext_lazy("IATI codelist Currency", "Dobra"),
    )
    EL_SALVADOR_COLON = (
        "SVC",
        pgettext_lazy("IATI codelist Currency", "El Salvador Colon"),
    )
    SYRIAN_POUND = (
        "SYP",
        pgettext_lazy("IATI codelist Currency", "Syrian Pound"),
    )
    LILANGENI = (
        "SZL",
        pgettext_lazy("IATI codelist Currency", "Lilangeni"),
    )
    BAHT = (
        "THB",
        pgettext_lazy("IATI codelist Currency", "Baht"),
    )
    SOMONI = (
        "TJS",
        pgettext_lazy("IATI codelist Currency", "Somoni"),
    )
    MANAT = (
        "TMT",
        pgettext_lazy("IATI codelist Currency", "Manat"),
    )
    TUNISIAN_DINAR = (
        "TND",
        pgettext_lazy("IATI codelist Currency", "Tunisian Dinar"),
    )
    PAANGA = (
        "TOP",
        pgettext_lazy("IATI codelist Currency", "Paanga"),
    )
    TURKISH_LIRA = (
        "TRY",
        pgettext_lazy("IATI codelist Currency", "Turkish Lira"),
    )
    TRINIDAD_AND_TOBAGO_DOLLAR = (
        "TTD",
        pgettext_lazy("IATI codelist Currency", "Trinidad and Tobago Dollar"),
    )
    NEW_TAIWAN_DOLLAR = (
        "TWD",
        pgettext_lazy("IATI codelist Currency", "New Taiwan Dollar"),
    )
    TANZANIAN_SHILLING = (
        "TZS",
        pgettext_lazy("IATI codelist Currency", "Tanzanian Shilling"),
    )
    HRYVNIA = (
        "UAH",
        pgettext_lazy("IATI codelist Currency", "Hryvnia"),
    )
    UGANDA_SHILLING = (
        "UGX",
        pgettext_lazy("IATI codelist Currency", "Uganda Shilling"),
    )
    US_DOLLAR = (
        "USD",
        pgettext_lazy("IATI codelist Currency", "US Dollar"),
    )
    US_DOLLAR__NEXT_DAY_ = (
        "USN",
        pgettext_lazy("IATI codelist Currency", "US Dollar (Next day)"),
    )
    US_DOLLAR__SAME_DAY_ = (
        "USS",
        pgettext_lazy("IATI codelist Currency", "US Dollar (Same day)"),
    )
    URUGUAY_PESO_EN_UNIDADES_INDEXADAS = (
        "UYI",
        pgettext_lazy("IATI codelist Currency", "Uruguay Peso en Unidades Indexadas"),
    )
    PESO_URUGUAYO = (
        "UYU",
        pgettext_lazy("IATI codelist Currency", "Peso Uruguayo"),
    )
    UZBEKISTAN_SUM = (
        "UZS",
        pgettext_lazy("IATI codelist Currency", "Uzbekistan Sum"),
    )
    BOLIVAR = (
        "VEF",
        pgettext_lazy("IATI codelist Currency", "Bolivar"),
    )
    BOLIVAR_SOBERANO = (
        "VES",
        pgettext_lazy("IATI codelist Currency", "Bolivar Soberano"),
    )
    DONG = (
        "VND",
        pgettext_lazy("IATI codelist Currency", "Dong"),
    )
    VATU = (
        "VUV",
        pgettext_lazy("IATI codelist Currency", "Vatu"),
    )
    TALA = (
        "WST",
        pgettext_lazy("IATI codelist Currency", "Tala"),
    )
    CFA_FRANC_BEAC = (
        "XAF",
        pgettext_lazy("IATI codelist Currency", "CFA Franc BEAC"),
    )
    BITCOIN = (
        "XBT",
        pgettext_lazy("IATI codelist Currency", "Bitcoin"),
    )
    EAST_CARIBBEAN_DOLLAR = (
        "XCD",
        pgettext_lazy("IATI codelist Currency", "East Caribbean Dollar"),
    )
    INTERNATIONAL_MONETARY_FUND__IMF__SPECIAL_DRAWING_RIGHT__SDR_ = (
        "XDR",
        pgettext_lazy(
            "IATI codelist Currency",
            "International Monetary Fund (IMF) Special Drawing Right (SDR)",
        ),
    )
    CFA_FRANC_BCEAO = (
        "XOF",
        pgettext_lazy("IATI codelist Currency", "CFA Franc BCEAO"),
    )
    CFP_FRANC = (
        "XPF",
        pgettext_lazy("IATI codelist Currency", "CFP Franc"),
    )
    YEMENI_RIAL = (
        "YER",
        pgettext_lazy("IATI codelist Currency", "Yemeni Rial"),
    )
    RAND = (
        "ZAR",
        pgettext_lazy("IATI codelist Currency", "Rand"),
    )
    ZAMBIAN_KWACHA = (
        "ZMK",
        pgettext_lazy("IATI codelist Currency", "Zambian Kwacha"),
    )
    ZAMBIAN_KWACHA = (
        "ZMW",
        pgettext_lazy("IATI codelist Currency", "Zambian Kwacha"),
    )
    ZIMBABWE_DOLLAR = (
        "ZWL",
        pgettext_lazy("IATI codelist Currency", "Zimbabwe Dollar"),
    )
