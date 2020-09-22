from django.db import models
from django.utils.translation import pgettext_lazy


class Country(models.TextChoices):
    """
    The Country codelist is generated from the ISO 3166-1 part of the ISO 3166 standard. The standard makes allowance, alongside the officially assigned codes, for code elements to be expanded by using either reserved codes or user-assigned codes. IATI currently defines additional codes in the XA -XZ range.
    """

    AFGHANISTAN = (
        "AF",
        pgettext_lazy("Country", "Afghanistan"),
    )
    ÅLAND_ISLANDS = (
        "AX",
        pgettext_lazy("Country", "Åland Islands"),
    )
    ALBANIA = (
        "AL",
        pgettext_lazy("Country", "Albania"),
    )
    ALGERIA = (
        "DZ",
        pgettext_lazy("Country", "Algeria"),
    )
    AMERICAN_SAMOA = (
        "AS",
        pgettext_lazy("Country", "American Samoa"),
    )
    ANDORRA = (
        "AD",
        pgettext_lazy("Country", "Andorra"),
    )
    ANGOLA = (
        "AO",
        pgettext_lazy("Country", "Angola"),
    )
    ANGUILLA = (
        "AI",
        pgettext_lazy("Country", "Anguilla"),
    )
    ANTARCTICA = (
        "AQ",
        pgettext_lazy("Country", "Antarctica"),
    )
    ANTIGUA_AND_BARBUDA = (
        "AG",
        pgettext_lazy("Country", "Antigua and Barbuda"),
    )
    ARGENTINA = (
        "AR",
        pgettext_lazy("Country", "Argentina"),
    )
    ARMENIA = (
        "AM",
        pgettext_lazy("Country", "Armenia"),
    )
    ARUBA = (
        "AW",
        pgettext_lazy("Country", "Aruba"),
    )
    AUSTRALIA = (
        "AU",
        pgettext_lazy("Country", "Australia"),
    )
    AUSTRIA = (
        "AT",
        pgettext_lazy("Country", "Austria"),
    )
    AZERBAIJAN = (
        "AZ",
        pgettext_lazy("Country", "Azerbaijan"),
    )
    BAHAMAS__THE_ = (
        "BS",
        pgettext_lazy("Country", "Bahamas (the)"),
    )
    BAHRAIN = (
        "BH",
        pgettext_lazy("Country", "Bahrain"),
    )
    BANGLADESH = (
        "BD",
        pgettext_lazy("Country", "Bangladesh"),
    )
    BARBADOS = (
        "BB",
        pgettext_lazy("Country", "Barbados"),
    )
    BELARUS = (
        "BY",
        pgettext_lazy("Country", "Belarus"),
    )
    BELGIUM = (
        "BE",
        pgettext_lazy("Country", "Belgium"),
    )
    BELIZE = (
        "BZ",
        pgettext_lazy("Country", "Belize"),
    )
    BENIN = (
        "BJ",
        pgettext_lazy("Country", "Benin"),
    )
    BERMUDA = (
        "BM",
        pgettext_lazy("Country", "Bermuda"),
    )
    BHUTAN = (
        "BT",
        pgettext_lazy("Country", "Bhutan"),
    )
    BOLIVIA__PLURINATIONAL_STATE_OF_ = (
        "BO",
        pgettext_lazy("Country", "Bolivia (Plurinational State of)"),
    )
    BONAIRE__SINT_EUSTATIUS_AND_SABA = (
        "BQ",
        pgettext_lazy("Country", "Bonaire, Sint Eustatius and Saba"),
    )
    BOSNIA_AND_HERZEGOVINA = (
        "BA",
        pgettext_lazy("Country", "Bosnia and Herzegovina"),
    )
    BOTSWANA = (
        "BW",
        pgettext_lazy("Country", "Botswana"),
    )
    BOUVET_ISLAND = (
        "BV",
        pgettext_lazy("Country", "Bouvet Island"),
    )
    BRAZIL = (
        "BR",
        pgettext_lazy("Country", "Brazil"),
    )
    BRITISH_INDIAN_OCEAN_TERRITORY__THE_ = (
        "IO",
        pgettext_lazy("Country", "British Indian Ocean Territory (the)"),
    )
    BRUNEI_DARUSSALAM = (
        "BN",
        pgettext_lazy("Country", "Brunei Darussalam"),
    )
    BULGARIA = (
        "BG",
        pgettext_lazy("Country", "Bulgaria"),
    )
    BURKINA_FASO = (
        "BF",
        pgettext_lazy("Country", "Burkina Faso"),
    )
    BURUNDI = (
        "BI",
        pgettext_lazy("Country", "Burundi"),
    )
    CAMBODIA = (
        "KH",
        pgettext_lazy("Country", "Cambodia"),
    )
    CAMEROON = (
        "CM",
        pgettext_lazy("Country", "Cameroon"),
    )
    CANADA = (
        "CA",
        pgettext_lazy("Country", "Canada"),
    )
    CABO_VERDE = (
        "CV",
        pgettext_lazy("Country", "Cabo Verde"),
    )
    CAYMAN_ISLANDS__THE_ = (
        "KY",
        pgettext_lazy("Country", "Cayman Islands (the)"),
    )
    CENTRAL_AFRICAN_REPUBLIC__THE_ = (
        "CF",
        pgettext_lazy("Country", "Central African Republic (the)"),
    )
    CHAD = (
        "TD",
        pgettext_lazy("Country", "Chad"),
    )
    CHILE = (
        "CL",
        pgettext_lazy("Country", "Chile"),
    )
    CHINA = (
        "CN",
        pgettext_lazy("Country", "China"),
    )
    CHRISTMAS_ISLAND = (
        "CX",
        pgettext_lazy("Country", "Christmas Island"),
    )
    COCOS__KEELING__ISLANDS__THE_ = (
        "CC",
        pgettext_lazy("Country", "Cocos (Keeling) Islands (the)"),
    )
    COLOMBIA = (
        "CO",
        pgettext_lazy("Country", "Colombia"),
    )
    COMOROS__THE_ = (
        "KM",
        pgettext_lazy("Country", "Comoros (the)"),
    )
    CONGO__THE_ = (
        "CG",
        pgettext_lazy("Country", "Congo (the)"),
    )
    CONGO__THE_DEMOCRATIC_REPUBLIC_OF_THE_ = (
        "CD",
        pgettext_lazy("Country", "Congo (the Democratic Republic of the)"),
    )
    COOK_ISLANDS__THE_ = (
        "CK",
        pgettext_lazy("Country", "Cook Islands (the)"),
    )
    COSTA_RICA = (
        "CR",
        pgettext_lazy("Country", "Costa Rica"),
    )
    CÔTE_D_IVOIRE = (
        "CI",
        pgettext_lazy("Country", "Côte d'Ivoire"),
    )
    CROATIA = (
        "HR",
        pgettext_lazy("Country", "Croatia"),
    )
    CUBA = (
        "CU",
        pgettext_lazy("Country", "Cuba"),
    )
    CURAÇAO = (
        "CW",
        pgettext_lazy("Country", "Curaçao"),
    )
    CYPRUS = (
        "CY",
        pgettext_lazy("Country", "Cyprus"),
    )
    CZECHIA = (
        "CZ",
        pgettext_lazy("Country", "Czechia"),
    )
    DENMARK = (
        "DK",
        pgettext_lazy("Country", "Denmark"),
    )
    DJIBOUTI = (
        "DJ",
        pgettext_lazy("Country", "Djibouti"),
    )
    DOMINICA = (
        "DM",
        pgettext_lazy("Country", "Dominica"),
    )
    DOMINICAN_REPUBLIC__THE_ = (
        "DO",
        pgettext_lazy("Country", "Dominican Republic (the)"),
    )
    ECUADOR = (
        "EC",
        pgettext_lazy("Country", "Ecuador"),
    )
    EGYPT = (
        "EG",
        pgettext_lazy("Country", "Egypt"),
    )
    EL_SALVADOR = (
        "SV",
        pgettext_lazy("Country", "El Salvador"),
    )
    EQUATORIAL_GUINEA = (
        "GQ",
        pgettext_lazy("Country", "Equatorial Guinea"),
    )
    ERITREA = (
        "ER",
        pgettext_lazy("Country", "Eritrea"),
    )
    ESTONIA = (
        "EE",
        pgettext_lazy("Country", "Estonia"),
    )
    ETHIOPIA = (
        "ET",
        pgettext_lazy("Country", "Ethiopia"),
    )
    FALKLAND_ISLANDS__THE___MALVINAS_ = (
        "FK",
        pgettext_lazy("Country", "Falkland Islands (the) [Malvinas]"),
    )
    FAROE_ISLANDS__THE_ = (
        "FO",
        pgettext_lazy("Country", "Faroe Islands (the)"),
    )
    FIJI = (
        "FJ",
        pgettext_lazy("Country", "Fiji"),
    )
    FINLAND = (
        "FI",
        pgettext_lazy("Country", "Finland"),
    )
    FRANCE = (
        "FR",
        pgettext_lazy("Country", "France"),
    )
    FRENCH_GUIANA = (
        "GF",
        pgettext_lazy("Country", "French Guiana"),
    )
    FRENCH_POLYNESIA = (
        "PF",
        pgettext_lazy("Country", "French Polynesia"),
    )
    FRENCH_SOUTHERN_TERRITORIES__THE_ = (
        "TF",
        pgettext_lazy("Country", "French Southern Territories (the)"),
    )
    GABON = (
        "GA",
        pgettext_lazy("Country", "Gabon"),
    )
    GAMBIA__THE_ = (
        "GM",
        pgettext_lazy("Country", "Gambia (the)"),
    )
    GEORGIA = (
        "GE",
        pgettext_lazy("Country", "Georgia"),
    )
    GERMANY = (
        "DE",
        pgettext_lazy("Country", "Germany"),
    )
    GHANA = (
        "GH",
        pgettext_lazy("Country", "Ghana"),
    )
    GIBRALTAR = (
        "GI",
        pgettext_lazy("Country", "Gibraltar"),
    )
    GREECE = (
        "GR",
        pgettext_lazy("Country", "Greece"),
    )
    GREENLAND = (
        "GL",
        pgettext_lazy("Country", "Greenland"),
    )
    GRENADA = (
        "GD",
        pgettext_lazy("Country", "Grenada"),
    )
    GUADELOUPE = (
        "GP",
        pgettext_lazy("Country", "Guadeloupe"),
    )
    GUAM = (
        "GU",
        pgettext_lazy("Country", "Guam"),
    )
    GUATEMALA = (
        "GT",
        pgettext_lazy("Country", "Guatemala"),
    )
    GUERNSEY = (
        "GG",
        pgettext_lazy("Country", "Guernsey"),
    )
    GUINEA = (
        "GN",
        pgettext_lazy("Country", "Guinea"),
    )
    GUINEA_BISSAU = (
        "GW",
        pgettext_lazy("Country", "Guinea-Bissau"),
    )
    GUYANA = (
        "GY",
        pgettext_lazy("Country", "Guyana"),
    )
    HAITI = (
        "HT",
        pgettext_lazy("Country", "Haiti"),
    )
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = (
        "HM",
        pgettext_lazy("Country", "Heard Island and McDonald Islands"),
    )
    HOLY_SEE__THE_ = (
        "VA",
        pgettext_lazy("Country", "Holy See (the)"),
    )
    HONDURAS = (
        "HN",
        pgettext_lazy("Country", "Honduras"),
    )
    HONG_KONG = (
        "HK",
        pgettext_lazy("Country", "Hong Kong"),
    )
    HUNGARY = (
        "HU",
        pgettext_lazy("Country", "Hungary"),
    )
    ICELAND = (
        "IS",
        pgettext_lazy("Country", "Iceland"),
    )
    INDIA = (
        "IN",
        pgettext_lazy("Country", "India"),
    )
    INDONESIA = (
        "ID",
        pgettext_lazy("Country", "Indonesia"),
    )
    IRAN__ISLAMIC_REPUBLIC_OF_ = (
        "IR",
        pgettext_lazy("Country", "Iran (Islamic Republic of)"),
    )
    IRAQ = (
        "IQ",
        pgettext_lazy("Country", "Iraq"),
    )
    IRELAND = (
        "IE",
        pgettext_lazy("Country", "Ireland"),
    )
    ISLE_OF_MAN = (
        "IM",
        pgettext_lazy("Country", "Isle of Man"),
    )
    ISRAEL = (
        "IL",
        pgettext_lazy("Country", "Israel"),
    )
    ITALY = (
        "IT",
        pgettext_lazy("Country", "Italy"),
    )
    JAMAICA = (
        "JM",
        pgettext_lazy("Country", "Jamaica"),
    )
    JAPAN = (
        "JP",
        pgettext_lazy("Country", "Japan"),
    )
    JERSEY = (
        "JE",
        pgettext_lazy("Country", "Jersey"),
    )
    JORDAN = (
        "JO",
        pgettext_lazy("Country", "Jordan"),
    )
    KAZAKHSTAN = (
        "KZ",
        pgettext_lazy("Country", "Kazakhstan"),
    )
    KENYA = (
        "KE",
        pgettext_lazy("Country", "Kenya"),
    )
    KIRIBATI = (
        "KI",
        pgettext_lazy("Country", "Kiribati"),
    )
    KOREA__THE_DEMOCRATIC_PEOPLE_S_REPUBLIC_OF_ = (
        "KP",
        pgettext_lazy("Country", "Korea (the Democratic People's Republic of)"),
    )
    KOREA__THE_REPUBLIC_OF_ = (
        "KR",
        pgettext_lazy("Country", "Korea (the Republic of)"),
    )
    KOSOVO = (
        "XK",
        pgettext_lazy("Country", "Kosovo"),
    )
    KUWAIT = (
        "KW",
        pgettext_lazy("Country", "Kuwait"),
    )
    KYRGYZSTAN = (
        "KG",
        pgettext_lazy("Country", "Kyrgyzstan"),
    )
    LAO_PEOPLE_S_DEMOCRATIC_REPUBLIC__THE_ = (
        "LA",
        pgettext_lazy("Country", "Lao People's Democratic Republic (the)"),
    )
    LATVIA = (
        "LV",
        pgettext_lazy("Country", "Latvia"),
    )
    LEBANON = (
        "LB",
        pgettext_lazy("Country", "Lebanon"),
    )
    LESOTHO = (
        "LS",
        pgettext_lazy("Country", "Lesotho"),
    )
    LIBERIA = (
        "LR",
        pgettext_lazy("Country", "Liberia"),
    )
    LIBYA = (
        "LY",
        pgettext_lazy("Country", "Libya"),
    )
    LIECHTENSTEIN = (
        "LI",
        pgettext_lazy("Country", "Liechtenstein"),
    )
    LITHUANIA = (
        "LT",
        pgettext_lazy("Country", "Lithuania"),
    )
    LUXEMBOURG = (
        "LU",
        pgettext_lazy("Country", "Luxembourg"),
    )
    MACAO = (
        "MO",
        pgettext_lazy("Country", "Macao"),
    )
    NORTH_MACEDONIA = (
        "MK",
        pgettext_lazy("Country", "North Macedonia"),
    )
    MADAGASCAR = (
        "MG",
        pgettext_lazy("Country", "Madagascar"),
    )
    MALAWI = (
        "MW",
        pgettext_lazy("Country", "Malawi"),
    )
    MALAYSIA = (
        "MY",
        pgettext_lazy("Country", "Malaysia"),
    )
    MALDIVES = (
        "MV",
        pgettext_lazy("Country", "Maldives"),
    )
    MALI = (
        "ML",
        pgettext_lazy("Country", "Mali"),
    )
    MALTA = (
        "MT",
        pgettext_lazy("Country", "Malta"),
    )
    MARSHALL_ISLANDS__THE_ = (
        "MH",
        pgettext_lazy("Country", "Marshall Islands (the)"),
    )
    MARTINIQUE = (
        "MQ",
        pgettext_lazy("Country", "Martinique"),
    )
    MAURITANIA = (
        "MR",
        pgettext_lazy("Country", "Mauritania"),
    )
    MAURITIUS = (
        "MU",
        pgettext_lazy("Country", "Mauritius"),
    )
    MAYOTTE = (
        "YT",
        pgettext_lazy("Country", "Mayotte"),
    )
    MEXICO = (
        "MX",
        pgettext_lazy("Country", "Mexico"),
    )
    MICRONESIA__FEDERATED_STATES_OF_ = (
        "FM",
        pgettext_lazy("Country", "Micronesia (Federated States of)"),
    )
    MOLDOVA__THE_REPUBLIC_OF_ = (
        "MD",
        pgettext_lazy("Country", "Moldova (the Republic of)"),
    )
    MONACO = (
        "MC",
        pgettext_lazy("Country", "Monaco"),
    )
    MONGOLIA = (
        "MN",
        pgettext_lazy("Country", "Mongolia"),
    )
    MONTENEGRO = (
        "ME",
        pgettext_lazy("Country", "Montenegro"),
    )
    MONTSERRAT = (
        "MS",
        pgettext_lazy("Country", "Montserrat"),
    )
    MOROCCO = (
        "MA",
        pgettext_lazy("Country", "Morocco"),
    )
    MOZAMBIQUE = (
        "MZ",
        pgettext_lazy("Country", "Mozambique"),
    )
    MYANMAR = (
        "MM",
        pgettext_lazy("Country", "Myanmar"),
    )
    NAMIBIA = (
        "NA",
        pgettext_lazy("Country", "Namibia"),
    )
    NAURU = (
        "NR",
        pgettext_lazy("Country", "Nauru"),
    )
    NEPAL = (
        "NP",
        pgettext_lazy("Country", "Nepal"),
    )
    NETHERLANDS__THE_ = (
        "NL",
        pgettext_lazy("Country", "Netherlands (the)"),
    )
    NETHERLAND_ANTILLES = (
        "AN",
        pgettext_lazy("Country", "NETHERLAND ANTILLES"),
    )
    NEW_CALEDONIA = (
        "NC",
        pgettext_lazy("Country", "New Caledonia"),
    )
    NEW_ZEALAND = (
        "NZ",
        pgettext_lazy("Country", "New Zealand"),
    )
    NICARAGUA = (
        "NI",
        pgettext_lazy("Country", "Nicaragua"),
    )
    NIGER__THE_ = (
        "NE",
        pgettext_lazy("Country", "Niger (the)"),
    )
    NIGERIA = (
        "NG",
        pgettext_lazy("Country", "Nigeria"),
    )
    NIUE = (
        "NU",
        pgettext_lazy("Country", "Niue"),
    )
    NORFOLK_ISLAND = (
        "NF",
        pgettext_lazy("Country", "Norfolk Island"),
    )
    NORTHERN_MARIANA_ISLANDS__THE_ = (
        "MP",
        pgettext_lazy("Country", "Northern Mariana Islands (the)"),
    )
    NORWAY = (
        "NO",
        pgettext_lazy("Country", "Norway"),
    )
    OMAN = (
        "OM",
        pgettext_lazy("Country", "Oman"),
    )
    PAKISTAN = (
        "PK",
        pgettext_lazy("Country", "Pakistan"),
    )
    PALAU = (
        "PW",
        pgettext_lazy("Country", "Palau"),
    )
    PALESTINE__STATE_OF = (
        "PS",
        pgettext_lazy("Country", "Palestine, State of"),
    )
    PANAMA = (
        "PA",
        pgettext_lazy("Country", "Panama"),
    )
    PAPUA_NEW_GUINEA = (
        "PG",
        pgettext_lazy("Country", "Papua New Guinea"),
    )
    PARAGUAY = (
        "PY",
        pgettext_lazy("Country", "Paraguay"),
    )
    PERU = (
        "PE",
        pgettext_lazy("Country", "Peru"),
    )
    PHILIPPINES__THE_ = (
        "PH",
        pgettext_lazy("Country", "Philippines (the)"),
    )
    PITCAIRN = (
        "PN",
        pgettext_lazy("Country", "Pitcairn"),
    )
    POLAND = (
        "PL",
        pgettext_lazy("Country", "Poland"),
    )
    PORTUGAL = (
        "PT",
        pgettext_lazy("Country", "Portugal"),
    )
    PUERTO_RICO = (
        "PR",
        pgettext_lazy("Country", "Puerto Rico"),
    )
    QATAR = (
        "QA",
        pgettext_lazy("Country", "Qatar"),
    )
    RÉUNION = (
        "RE",
        pgettext_lazy("Country", "Réunion"),
    )
    ROMANIA = (
        "RO",
        pgettext_lazy("Country", "Romania"),
    )
    RUSSIAN_FEDERATION__THE_ = (
        "RU",
        pgettext_lazy("Country", "Russian Federation (the)"),
    )
    RWANDA = (
        "RW",
        pgettext_lazy("Country", "Rwanda"),
    )
    SAINT_BARTHÉLEMY = (
        "BL",
        pgettext_lazy("Country", "Saint Barthélemy"),
    )
    SAINT_HELENA__ASCENSION_AND_TRISTAN_DA_CUNHA = (
        "SH",
        pgettext_lazy("Country", "Saint Helena, Ascension and Tristan da Cunha"),
    )
    SAINT_KITTS_AND_NEVIS = (
        "KN",
        pgettext_lazy("Country", "Saint Kitts and Nevis"),
    )
    SAINT_LUCIA = (
        "LC",
        pgettext_lazy("Country", "Saint Lucia"),
    )
    SAINT_MARTIN__FRENCH_PART_ = (
        "MF",
        pgettext_lazy("Country", "Saint Martin (French part)"),
    )
    SAINT_PIERRE_AND_MIQUELON = (
        "PM",
        pgettext_lazy("Country", "Saint Pierre and Miquelon"),
    )
    SAINT_VINCENT_AND_THE_GRENADINES = (
        "VC",
        pgettext_lazy("Country", "Saint Vincent and the Grenadines"),
    )
    SAMOA = (
        "WS",
        pgettext_lazy("Country", "Samoa"),
    )
    SAN_MARINO = (
        "SM",
        pgettext_lazy("Country", "San Marino"),
    )
    SAO_TOME_AND_PRINCIPE = (
        "ST",
        pgettext_lazy("Country", "Sao Tome and Principe"),
    )
    SAUDI_ARABIA = (
        "SA",
        pgettext_lazy("Country", "Saudi Arabia"),
    )
    SENEGAL = (
        "SN",
        pgettext_lazy("Country", "Senegal"),
    )
    SERBIA = (
        "RS",
        pgettext_lazy("Country", "Serbia"),
    )
    SEYCHELLES = (
        "SC",
        pgettext_lazy("Country", "Seychelles"),
    )
    SIERRA_LEONE = (
        "SL",
        pgettext_lazy("Country", "Sierra Leone"),
    )
    SINGAPORE = (
        "SG",
        pgettext_lazy("Country", "Singapore"),
    )
    SINT_MAARTEN__DUTCH_PART_ = (
        "SX",
        pgettext_lazy("Country", "Sint Maarten (Dutch part)"),
    )
    SLOVAKIA = (
        "SK",
        pgettext_lazy("Country", "Slovakia"),
    )
    SLOVENIA = (
        "SI",
        pgettext_lazy("Country", "Slovenia"),
    )
    SOLOMON_ISLANDS = (
        "SB",
        pgettext_lazy("Country", "Solomon Islands"),
    )
    SOMALIA = (
        "SO",
        pgettext_lazy("Country", "Somalia"),
    )
    SOUTH_AFRICA = (
        "ZA",
        pgettext_lazy("Country", "South Africa"),
    )
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = (
        "GS",
        pgettext_lazy("Country", "South Georgia and the South Sandwich Islands"),
    )
    SOUTH_SUDAN = (
        "SS",
        pgettext_lazy("Country", "South Sudan"),
    )
    SPAIN = (
        "ES",
        pgettext_lazy("Country", "Spain"),
    )
    SRI_LANKA = (
        "LK",
        pgettext_lazy("Country", "Sri Lanka"),
    )
    SUDAN__THE_ = (
        "SD",
        pgettext_lazy("Country", "Sudan (the)"),
    )
    SURINAME = (
        "SR",
        pgettext_lazy("Country", "Suriname"),
    )
    SVALBARD_AND_JAN_MAYEN = (
        "SJ",
        pgettext_lazy("Country", "Svalbard and Jan Mayen"),
    )
    ESWATINI = (
        "SZ",
        pgettext_lazy("Country", "Eswatini"),
    )
    SWEDEN = (
        "SE",
        pgettext_lazy("Country", "Sweden"),
    )
    SWITZERLAND = (
        "CH",
        pgettext_lazy("Country", "Switzerland"),
    )
    SYRIAN_ARAB_REPUBLIC = (
        "SY",
        pgettext_lazy("Country", "Syrian Arab Republic"),
    )
    TAIWAN__PROVINCE_OF_CHINA_ = (
        "TW",
        pgettext_lazy("Country", "Taiwan (Province of China)"),
    )
    TAJIKISTAN = (
        "TJ",
        pgettext_lazy("Country", "Tajikistan"),
    )
    TANZANIA__UNITED_REPUBLIC_OF = (
        "TZ",
        pgettext_lazy("Country", "Tanzania, United Republic of"),
    )
    THAILAND = (
        "TH",
        pgettext_lazy("Country", "Thailand"),
    )
    TIMOR_LESTE = (
        "TL",
        pgettext_lazy("Country", "Timor-Leste"),
    )
    TOGO = (
        "TG",
        pgettext_lazy("Country", "Togo"),
    )
    TOKELAU = (
        "TK",
        pgettext_lazy("Country", "Tokelau"),
    )
    TONGA = (
        "TO",
        pgettext_lazy("Country", "Tonga"),
    )
    TRINIDAD_AND_TOBAGO = (
        "TT",
        pgettext_lazy("Country", "Trinidad and Tobago"),
    )
    TUNISIA = (
        "TN",
        pgettext_lazy("Country", "Tunisia"),
    )
    TURKEY = (
        "TR",
        pgettext_lazy("Country", "Turkey"),
    )
    TURKMENISTAN = (
        "TM",
        pgettext_lazy("Country", "Turkmenistan"),
    )
    TURKS_AND_CAICOS_ISLANDS__THE_ = (
        "TC",
        pgettext_lazy("Country", "Turks and Caicos Islands (the)"),
    )
    TUVALU = (
        "TV",
        pgettext_lazy("Country", "Tuvalu"),
    )
    UGANDA = (
        "UG",
        pgettext_lazy("Country", "Uganda"),
    )
    UKRAINE = (
        "UA",
        pgettext_lazy("Country", "Ukraine"),
    )
    UNITED_ARAB_EMIRATES__THE_ = (
        "AE",
        pgettext_lazy("Country", "United Arab Emirates (the)"),
    )
    UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND__THE_ = (
        "GB",
        pgettext_lazy(
            "Country",
            "United Kingdom of Great Britain and Northern Ireland (the)",
        ),
    )
    UNITED_STATES_OF_AMERICA__THE_ = (
        "US",
        pgettext_lazy("Country", "United States of America (the)"),
    )
    UNITED_STATES_MINOR_OUTLYING_ISLANDS__THE_ = (
        "UM",
        pgettext_lazy("Country", "United States Minor Outlying Islands (the)"),
    )
    URUGUAY = (
        "UY",
        pgettext_lazy("Country", "Uruguay"),
    )
    UZBEKISTAN = (
        "UZ",
        pgettext_lazy("Country", "Uzbekistan"),
    )
    VANUATU = (
        "VU",
        pgettext_lazy("Country", "Vanuatu"),
    )
    VENEZUELA__BOLIVARIAN_REPUBLIC_OF_ = (
        "VE",
        pgettext_lazy("Country", "Venezuela (Bolivarian Republic of)"),
    )
    VIET_NAM = (
        "VN",
        pgettext_lazy("Country", "Viet Nam"),
    )
    VIRGIN_ISLANDS__BRITISH_ = (
        "VG",
        pgettext_lazy("Country", "Virgin Islands (British)"),
    )
    VIRGIN_ISLANDS__U_S__ = (
        "VI",
        pgettext_lazy("Country", "Virgin Islands (U.S.)"),
    )
    WALLIS_AND_FUTUNA = (
        "WF",
        pgettext_lazy("Country", "Wallis and Futuna"),
    )
    WESTERN_SAHARA = (
        "EH",
        pgettext_lazy("Country", "Western Sahara"),
    )
    YEMEN = (
        "YE",
        pgettext_lazy("Country", "Yemen"),
    )
    ZAMBIA = (
        "ZM",
        pgettext_lazy("Country", "Zambia"),
    )
    ZIMBABWE = (
        "ZW",
        pgettext_lazy("Country", "Zimbabwe"),
    )
