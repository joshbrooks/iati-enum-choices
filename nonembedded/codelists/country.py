from django.db import models
from django.utils.translation import pgettext_lazy


class Country(models.TextChoices):
    """
    The Country codelist is generated from the ISO 3166-1 part of the ISO 3166 standard. The standard makes allowance, alongside the officially assigned codes, for code elements to be expanded by using either reserved codes or user-assigned codes. IATI currently defines additional codes in the XA -XZ range.
    """

    AFGHANISTAN = (
        "AF",
        pgettext_lazy("IATI codelist Country", "Afghanistan"),
    )
    ÅLAND_ISLANDS = (
        "AX",
        pgettext_lazy("IATI codelist Country", "Åland Islands"),
    )
    ALBANIA = (
        "AL",
        pgettext_lazy("IATI codelist Country", "Albania"),
    )
    ALGERIA = (
        "DZ",
        pgettext_lazy("IATI codelist Country", "Algeria"),
    )
    AMERICAN_SAMOA = (
        "AS",
        pgettext_lazy("IATI codelist Country", "American Samoa"),
    )
    ANDORRA = (
        "AD",
        pgettext_lazy("IATI codelist Country", "Andorra"),
    )
    ANGOLA = (
        "AO",
        pgettext_lazy("IATI codelist Country", "Angola"),
    )
    ANGUILLA = (
        "AI",
        pgettext_lazy("IATI codelist Country", "Anguilla"),
    )
    ANTARCTICA = (
        "AQ",
        pgettext_lazy("IATI codelist Country", "Antarctica"),
    )
    ANTIGUA_AND_BARBUDA = (
        "AG",
        pgettext_lazy("IATI codelist Country", "Antigua and Barbuda"),
    )
    ARGENTINA = (
        "AR",
        pgettext_lazy("IATI codelist Country", "Argentina"),
    )
    ARMENIA = (
        "AM",
        pgettext_lazy("IATI codelist Country", "Armenia"),
    )
    ARUBA = (
        "AW",
        pgettext_lazy("IATI codelist Country", "Aruba"),
    )
    AUSTRALIA = (
        "AU",
        pgettext_lazy("IATI codelist Country", "Australia"),
    )
    AUSTRIA = (
        "AT",
        pgettext_lazy("IATI codelist Country", "Austria"),
    )
    AZERBAIJAN = (
        "AZ",
        pgettext_lazy("IATI codelist Country", "Azerbaijan"),
    )
    BAHAMAS__THE_ = (
        "BS",
        pgettext_lazy("IATI codelist Country", "Bahamas (the)"),
    )
    BAHRAIN = (
        "BH",
        pgettext_lazy("IATI codelist Country", "Bahrain"),
    )
    BANGLADESH = (
        "BD",
        pgettext_lazy("IATI codelist Country", "Bangladesh"),
    )
    BARBADOS = (
        "BB",
        pgettext_lazy("IATI codelist Country", "Barbados"),
    )
    BELARUS = (
        "BY",
        pgettext_lazy("IATI codelist Country", "Belarus"),
    )
    BELGIUM = (
        "BE",
        pgettext_lazy("IATI codelist Country", "Belgium"),
    )
    BELIZE = (
        "BZ",
        pgettext_lazy("IATI codelist Country", "Belize"),
    )
    BENIN = (
        "BJ",
        pgettext_lazy("IATI codelist Country", "Benin"),
    )
    BERMUDA = (
        "BM",
        pgettext_lazy("IATI codelist Country", "Bermuda"),
    )
    BHUTAN = (
        "BT",
        pgettext_lazy("IATI codelist Country", "Bhutan"),
    )
    BOLIVIA__PLURINATIONAL_STATE_OF_ = (
        "BO",
        pgettext_lazy("IATI codelist Country", "Bolivia (Plurinational State of)"),
    )
    BONAIRE__SINT_EUSTATIUS_AND_SABA = (
        "BQ",
        pgettext_lazy("IATI codelist Country", "Bonaire, Sint Eustatius and Saba"),
    )
    BOSNIA_AND_HERZEGOVINA = (
        "BA",
        pgettext_lazy("IATI codelist Country", "Bosnia and Herzegovina"),
    )
    BOTSWANA = (
        "BW",
        pgettext_lazy("IATI codelist Country", "Botswana"),
    )
    BOUVET_ISLAND = (
        "BV",
        pgettext_lazy("IATI codelist Country", "Bouvet Island"),
    )
    BRAZIL = (
        "BR",
        pgettext_lazy("IATI codelist Country", "Brazil"),
    )
    BRITISH_INDIAN_OCEAN_TERRITORY__THE_ = (
        "IO",
        pgettext_lazy("IATI codelist Country", "British Indian Ocean Territory (the)"),
    )
    BRUNEI_DARUSSALAM = (
        "BN",
        pgettext_lazy("IATI codelist Country", "Brunei Darussalam"),
    )
    BULGARIA = (
        "BG",
        pgettext_lazy("IATI codelist Country", "Bulgaria"),
    )
    BURKINA_FASO = (
        "BF",
        pgettext_lazy("IATI codelist Country", "Burkina Faso"),
    )
    BURUNDI = (
        "BI",
        pgettext_lazy("IATI codelist Country", "Burundi"),
    )
    CAMBODIA = (
        "KH",
        pgettext_lazy("IATI codelist Country", "Cambodia"),
    )
    CAMEROON = (
        "CM",
        pgettext_lazy("IATI codelist Country", "Cameroon"),
    )
    CANADA = (
        "CA",
        pgettext_lazy("IATI codelist Country", "Canada"),
    )
    CABO_VERDE = (
        "CV",
        pgettext_lazy("IATI codelist Country", "Cabo Verde"),
    )
    CAYMAN_ISLANDS__THE_ = (
        "KY",
        pgettext_lazy("IATI codelist Country", "Cayman Islands (the)"),
    )
    CENTRAL_AFRICAN_REPUBLIC__THE_ = (
        "CF",
        pgettext_lazy("IATI codelist Country", "Central African Republic (the)"),
    )
    CHAD = (
        "TD",
        pgettext_lazy("IATI codelist Country", "Chad"),
    )
    CHILE = (
        "CL",
        pgettext_lazy("IATI codelist Country", "Chile"),
    )
    CHINA = (
        "CN",
        pgettext_lazy("IATI codelist Country", "China"),
    )
    CHRISTMAS_ISLAND = (
        "CX",
        pgettext_lazy("IATI codelist Country", "Christmas Island"),
    )
    COCOS__KEELING__ISLANDS__THE_ = (
        "CC",
        pgettext_lazy("IATI codelist Country", "Cocos (Keeling) Islands (the)"),
    )
    COLOMBIA = (
        "CO",
        pgettext_lazy("IATI codelist Country", "Colombia"),
    )
    COMOROS__THE_ = (
        "KM",
        pgettext_lazy("IATI codelist Country", "Comoros (the)"),
    )
    CONGO__THE_ = (
        "CG",
        pgettext_lazy("IATI codelist Country", "Congo (the)"),
    )
    CONGO__THE_DEMOCRATIC_REPUBLIC_OF_THE_ = (
        "CD",
        pgettext_lazy(
            "IATI codelist Country", "Congo (the Democratic Republic of the)"
        ),
    )
    COOK_ISLANDS__THE_ = (
        "CK",
        pgettext_lazy("IATI codelist Country", "Cook Islands (the)"),
    )
    COSTA_RICA = (
        "CR",
        pgettext_lazy("IATI codelist Country", "Costa Rica"),
    )
    CÔTE_D_IVOIRE = (
        "CI",
        pgettext_lazy("IATI codelist Country", "Côte d'Ivoire"),
    )
    CROATIA = (
        "HR",
        pgettext_lazy("IATI codelist Country", "Croatia"),
    )
    CUBA = (
        "CU",
        pgettext_lazy("IATI codelist Country", "Cuba"),
    )
    CURAÇAO = (
        "CW",
        pgettext_lazy("IATI codelist Country", "Curaçao"),
    )
    CYPRUS = (
        "CY",
        pgettext_lazy("IATI codelist Country", "Cyprus"),
    )
    CZECHIA = (
        "CZ",
        pgettext_lazy("IATI codelist Country", "Czechia"),
    )
    DENMARK = (
        "DK",
        pgettext_lazy("IATI codelist Country", "Denmark"),
    )
    DJIBOUTI = (
        "DJ",
        pgettext_lazy("IATI codelist Country", "Djibouti"),
    )
    DOMINICA = (
        "DM",
        pgettext_lazy("IATI codelist Country", "Dominica"),
    )
    DOMINICAN_REPUBLIC__THE_ = (
        "DO",
        pgettext_lazy("IATI codelist Country", "Dominican Republic (the)"),
    )
    ECUADOR = (
        "EC",
        pgettext_lazy("IATI codelist Country", "Ecuador"),
    )
    EGYPT = (
        "EG",
        pgettext_lazy("IATI codelist Country", "Egypt"),
    )
    EL_SALVADOR = (
        "SV",
        pgettext_lazy("IATI codelist Country", "El Salvador"),
    )
    EQUATORIAL_GUINEA = (
        "GQ",
        pgettext_lazy("IATI codelist Country", "Equatorial Guinea"),
    )
    ERITREA = (
        "ER",
        pgettext_lazy("IATI codelist Country", "Eritrea"),
    )
    ESTONIA = (
        "EE",
        pgettext_lazy("IATI codelist Country", "Estonia"),
    )
    ETHIOPIA = (
        "ET",
        pgettext_lazy("IATI codelist Country", "Ethiopia"),
    )
    FALKLAND_ISLANDS__THE___MALVINAS_ = (
        "FK",
        pgettext_lazy("IATI codelist Country", "Falkland Islands (the) [Malvinas]"),
    )
    FAROE_ISLANDS__THE_ = (
        "FO",
        pgettext_lazy("IATI codelist Country", "Faroe Islands (the)"),
    )
    FIJI = (
        "FJ",
        pgettext_lazy("IATI codelist Country", "Fiji"),
    )
    FINLAND = (
        "FI",
        pgettext_lazy("IATI codelist Country", "Finland"),
    )
    FRANCE = (
        "FR",
        pgettext_lazy("IATI codelist Country", "France"),
    )
    FRENCH_GUIANA = (
        "GF",
        pgettext_lazy("IATI codelist Country", "French Guiana"),
    )
    FRENCH_POLYNESIA = (
        "PF",
        pgettext_lazy("IATI codelist Country", "French Polynesia"),
    )
    FRENCH_SOUTHERN_TERRITORIES__THE_ = (
        "TF",
        pgettext_lazy("IATI codelist Country", "French Southern Territories (the)"),
    )
    GABON = (
        "GA",
        pgettext_lazy("IATI codelist Country", "Gabon"),
    )
    GAMBIA__THE_ = (
        "GM",
        pgettext_lazy("IATI codelist Country", "Gambia (the)"),
    )
    GEORGIA = (
        "GE",
        pgettext_lazy("IATI codelist Country", "Georgia"),
    )
    GERMANY = (
        "DE",
        pgettext_lazy("IATI codelist Country", "Germany"),
    )
    GHANA = (
        "GH",
        pgettext_lazy("IATI codelist Country", "Ghana"),
    )
    GIBRALTAR = (
        "GI",
        pgettext_lazy("IATI codelist Country", "Gibraltar"),
    )
    GREECE = (
        "GR",
        pgettext_lazy("IATI codelist Country", "Greece"),
    )
    GREENLAND = (
        "GL",
        pgettext_lazy("IATI codelist Country", "Greenland"),
    )
    GRENADA = (
        "GD",
        pgettext_lazy("IATI codelist Country", "Grenada"),
    )
    GUADELOUPE = (
        "GP",
        pgettext_lazy("IATI codelist Country", "Guadeloupe"),
    )
    GUAM = (
        "GU",
        pgettext_lazy("IATI codelist Country", "Guam"),
    )
    GUATEMALA = (
        "GT",
        pgettext_lazy("IATI codelist Country", "Guatemala"),
    )
    GUERNSEY = (
        "GG",
        pgettext_lazy("IATI codelist Country", "Guernsey"),
    )
    GUINEA = (
        "GN",
        pgettext_lazy("IATI codelist Country", "Guinea"),
    )
    GUINEA_BISSAU = (
        "GW",
        pgettext_lazy("IATI codelist Country", "Guinea-Bissau"),
    )
    GUYANA = (
        "GY",
        pgettext_lazy("IATI codelist Country", "Guyana"),
    )
    HAITI = (
        "HT",
        pgettext_lazy("IATI codelist Country", "Haiti"),
    )
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = (
        "HM",
        pgettext_lazy("IATI codelist Country", "Heard Island and McDonald Islands"),
    )
    HOLY_SEE__THE_ = (
        "VA",
        pgettext_lazy("IATI codelist Country", "Holy See (the)"),
    )
    HONDURAS = (
        "HN",
        pgettext_lazy("IATI codelist Country", "Honduras"),
    )
    HONG_KONG = (
        "HK",
        pgettext_lazy("IATI codelist Country", "Hong Kong"),
    )
    HUNGARY = (
        "HU",
        pgettext_lazy("IATI codelist Country", "Hungary"),
    )
    ICELAND = (
        "IS",
        pgettext_lazy("IATI codelist Country", "Iceland"),
    )
    INDIA = (
        "IN",
        pgettext_lazy("IATI codelist Country", "India"),
    )
    INDONESIA = (
        "ID",
        pgettext_lazy("IATI codelist Country", "Indonesia"),
    )
    IRAN__ISLAMIC_REPUBLIC_OF_ = (
        "IR",
        pgettext_lazy("IATI codelist Country", "Iran (Islamic Republic of)"),
    )
    IRAQ = (
        "IQ",
        pgettext_lazy("IATI codelist Country", "Iraq"),
    )
    IRELAND = (
        "IE",
        pgettext_lazy("IATI codelist Country", "Ireland"),
    )
    ISLE_OF_MAN = (
        "IM",
        pgettext_lazy("IATI codelist Country", "Isle of Man"),
    )
    ISRAEL = (
        "IL",
        pgettext_lazy("IATI codelist Country", "Israel"),
    )
    ITALY = (
        "IT",
        pgettext_lazy("IATI codelist Country", "Italy"),
    )
    JAMAICA = (
        "JM",
        pgettext_lazy("IATI codelist Country", "Jamaica"),
    )
    JAPAN = (
        "JP",
        pgettext_lazy("IATI codelist Country", "Japan"),
    )
    JERSEY = (
        "JE",
        pgettext_lazy("IATI codelist Country", "Jersey"),
    )
    JORDAN = (
        "JO",
        pgettext_lazy("IATI codelist Country", "Jordan"),
    )
    KAZAKHSTAN = (
        "KZ",
        pgettext_lazy("IATI codelist Country", "Kazakhstan"),
    )
    KENYA = (
        "KE",
        pgettext_lazy("IATI codelist Country", "Kenya"),
    )
    KIRIBATI = (
        "KI",
        pgettext_lazy("IATI codelist Country", "Kiribati"),
    )
    KOREA__THE_DEMOCRATIC_PEOPLE_S_REPUBLIC_OF_ = (
        "KP",
        pgettext_lazy(
            "IATI codelist Country", "Korea (the Democratic People's Republic of)"
        ),
    )
    KOREA__THE_REPUBLIC_OF_ = (
        "KR",
        pgettext_lazy("IATI codelist Country", "Korea (the Republic of)"),
    )
    KOSOVO = (
        "XK",
        pgettext_lazy("IATI codelist Country", "Kosovo"),
    )
    KUWAIT = (
        "KW",
        pgettext_lazy("IATI codelist Country", "Kuwait"),
    )
    KYRGYZSTAN = (
        "KG",
        pgettext_lazy("IATI codelist Country", "Kyrgyzstan"),
    )
    LAO_PEOPLE_S_DEMOCRATIC_REPUBLIC__THE_ = (
        "LA",
        pgettext_lazy(
            "IATI codelist Country", "Lao People's Democratic Republic (the)"
        ),
    )
    LATVIA = (
        "LV",
        pgettext_lazy("IATI codelist Country", "Latvia"),
    )
    LEBANON = (
        "LB",
        pgettext_lazy("IATI codelist Country", "Lebanon"),
    )
    LESOTHO = (
        "LS",
        pgettext_lazy("IATI codelist Country", "Lesotho"),
    )
    LIBERIA = (
        "LR",
        pgettext_lazy("IATI codelist Country", "Liberia"),
    )
    LIBYA = (
        "LY",
        pgettext_lazy("IATI codelist Country", "Libya"),
    )
    LIECHTENSTEIN = (
        "LI",
        pgettext_lazy("IATI codelist Country", "Liechtenstein"),
    )
    LITHUANIA = (
        "LT",
        pgettext_lazy("IATI codelist Country", "Lithuania"),
    )
    LUXEMBOURG = (
        "LU",
        pgettext_lazy("IATI codelist Country", "Luxembourg"),
    )
    MACAO = (
        "MO",
        pgettext_lazy("IATI codelist Country", "Macao"),
    )
    NORTH_MACEDONIA = (
        "MK",
        pgettext_lazy("IATI codelist Country", "North Macedonia"),
    )
    MADAGASCAR = (
        "MG",
        pgettext_lazy("IATI codelist Country", "Madagascar"),
    )
    MALAWI = (
        "MW",
        pgettext_lazy("IATI codelist Country", "Malawi"),
    )
    MALAYSIA = (
        "MY",
        pgettext_lazy("IATI codelist Country", "Malaysia"),
    )
    MALDIVES = (
        "MV",
        pgettext_lazy("IATI codelist Country", "Maldives"),
    )
    MALI = (
        "ML",
        pgettext_lazy("IATI codelist Country", "Mali"),
    )
    MALTA = (
        "MT",
        pgettext_lazy("IATI codelist Country", "Malta"),
    )
    MARSHALL_ISLANDS__THE_ = (
        "MH",
        pgettext_lazy("IATI codelist Country", "Marshall Islands (the)"),
    )
    MARTINIQUE = (
        "MQ",
        pgettext_lazy("IATI codelist Country", "Martinique"),
    )
    MAURITANIA = (
        "MR",
        pgettext_lazy("IATI codelist Country", "Mauritania"),
    )
    MAURITIUS = (
        "MU",
        pgettext_lazy("IATI codelist Country", "Mauritius"),
    )
    MAYOTTE = (
        "YT",
        pgettext_lazy("IATI codelist Country", "Mayotte"),
    )
    MEXICO = (
        "MX",
        pgettext_lazy("IATI codelist Country", "Mexico"),
    )
    MICRONESIA__FEDERATED_STATES_OF_ = (
        "FM",
        pgettext_lazy("IATI codelist Country", "Micronesia (Federated States of)"),
    )
    MOLDOVA__THE_REPUBLIC_OF_ = (
        "MD",
        pgettext_lazy("IATI codelist Country", "Moldova (the Republic of)"),
    )
    MONACO = (
        "MC",
        pgettext_lazy("IATI codelist Country", "Monaco"),
    )
    MONGOLIA = (
        "MN",
        pgettext_lazy("IATI codelist Country", "Mongolia"),
    )
    MONTENEGRO = (
        "ME",
        pgettext_lazy("IATI codelist Country", "Montenegro"),
    )
    MONTSERRAT = (
        "MS",
        pgettext_lazy("IATI codelist Country", "Montserrat"),
    )
    MOROCCO = (
        "MA",
        pgettext_lazy("IATI codelist Country", "Morocco"),
    )
    MOZAMBIQUE = (
        "MZ",
        pgettext_lazy("IATI codelist Country", "Mozambique"),
    )
    MYANMAR = (
        "MM",
        pgettext_lazy("IATI codelist Country", "Myanmar"),
    )
    NAMIBIA = (
        "NA",
        pgettext_lazy("IATI codelist Country", "Namibia"),
    )
    NAURU = (
        "NR",
        pgettext_lazy("IATI codelist Country", "Nauru"),
    )
    NEPAL = (
        "NP",
        pgettext_lazy("IATI codelist Country", "Nepal"),
    )
    NETHERLANDS__THE_ = (
        "NL",
        pgettext_lazy("IATI codelist Country", "Netherlands (the)"),
    )
    NETHERLAND_ANTILLES = (
        "AN",
        pgettext_lazy("IATI codelist Country", "NETHERLAND ANTILLES"),
    )
    NEW_CALEDONIA = (
        "NC",
        pgettext_lazy("IATI codelist Country", "New Caledonia"),
    )
    NEW_ZEALAND = (
        "NZ",
        pgettext_lazy("IATI codelist Country", "New Zealand"),
    )
    NICARAGUA = (
        "NI",
        pgettext_lazy("IATI codelist Country", "Nicaragua"),
    )
    NIGER__THE_ = (
        "NE",
        pgettext_lazy("IATI codelist Country", "Niger (the)"),
    )
    NIGERIA = (
        "NG",
        pgettext_lazy("IATI codelist Country", "Nigeria"),
    )
    NIUE = (
        "NU",
        pgettext_lazy("IATI codelist Country", "Niue"),
    )
    NORFOLK_ISLAND = (
        "NF",
        pgettext_lazy("IATI codelist Country", "Norfolk Island"),
    )
    NORTHERN_MARIANA_ISLANDS__THE_ = (
        "MP",
        pgettext_lazy("IATI codelist Country", "Northern Mariana Islands (the)"),
    )
    NORWAY = (
        "NO",
        pgettext_lazy("IATI codelist Country", "Norway"),
    )
    OMAN = (
        "OM",
        pgettext_lazy("IATI codelist Country", "Oman"),
    )
    PAKISTAN = (
        "PK",
        pgettext_lazy("IATI codelist Country", "Pakistan"),
    )
    PALAU = (
        "PW",
        pgettext_lazy("IATI codelist Country", "Palau"),
    )
    PALESTINE__STATE_OF = (
        "PS",
        pgettext_lazy("IATI codelist Country", "Palestine, State of"),
    )
    PANAMA = (
        "PA",
        pgettext_lazy("IATI codelist Country", "Panama"),
    )
    PAPUA_NEW_GUINEA = (
        "PG",
        pgettext_lazy("IATI codelist Country", "Papua New Guinea"),
    )
    PARAGUAY = (
        "PY",
        pgettext_lazy("IATI codelist Country", "Paraguay"),
    )
    PERU = (
        "PE",
        pgettext_lazy("IATI codelist Country", "Peru"),
    )
    PHILIPPINES__THE_ = (
        "PH",
        pgettext_lazy("IATI codelist Country", "Philippines (the)"),
    )
    PITCAIRN = (
        "PN",
        pgettext_lazy("IATI codelist Country", "Pitcairn"),
    )
    POLAND = (
        "PL",
        pgettext_lazy("IATI codelist Country", "Poland"),
    )
    PORTUGAL = (
        "PT",
        pgettext_lazy("IATI codelist Country", "Portugal"),
    )
    PUERTO_RICO = (
        "PR",
        pgettext_lazy("IATI codelist Country", "Puerto Rico"),
    )
    QATAR = (
        "QA",
        pgettext_lazy("IATI codelist Country", "Qatar"),
    )
    RÉUNION = (
        "RE",
        pgettext_lazy("IATI codelist Country", "Réunion"),
    )
    ROMANIA = (
        "RO",
        pgettext_lazy("IATI codelist Country", "Romania"),
    )
    RUSSIAN_FEDERATION__THE_ = (
        "RU",
        pgettext_lazy("IATI codelist Country", "Russian Federation (the)"),
    )
    RWANDA = (
        "RW",
        pgettext_lazy("IATI codelist Country", "Rwanda"),
    )
    SAINT_BARTHÉLEMY = (
        "BL",
        pgettext_lazy("IATI codelist Country", "Saint Barthélemy"),
    )
    SAINT_HELENA__ASCENSION_AND_TRISTAN_DA_CUNHA = (
        "SH",
        pgettext_lazy(
            "IATI codelist Country", "Saint Helena, Ascension and Tristan da Cunha"
        ),
    )
    SAINT_KITTS_AND_NEVIS = (
        "KN",
        pgettext_lazy("IATI codelist Country", "Saint Kitts and Nevis"),
    )
    SAINT_LUCIA = (
        "LC",
        pgettext_lazy("IATI codelist Country", "Saint Lucia"),
    )
    SAINT_MARTIN__FRENCH_PART_ = (
        "MF",
        pgettext_lazy("IATI codelist Country", "Saint Martin (French part)"),
    )
    SAINT_PIERRE_AND_MIQUELON = (
        "PM",
        pgettext_lazy("IATI codelist Country", "Saint Pierre and Miquelon"),
    )
    SAINT_VINCENT_AND_THE_GRENADINES = (
        "VC",
        pgettext_lazy("IATI codelist Country", "Saint Vincent and the Grenadines"),
    )
    SAMOA = (
        "WS",
        pgettext_lazy("IATI codelist Country", "Samoa"),
    )
    SAN_MARINO = (
        "SM",
        pgettext_lazy("IATI codelist Country", "San Marino"),
    )
    SAO_TOME_AND_PRINCIPE = (
        "ST",
        pgettext_lazy("IATI codelist Country", "Sao Tome and Principe"),
    )
    SAUDI_ARABIA = (
        "SA",
        pgettext_lazy("IATI codelist Country", "Saudi Arabia"),
    )
    SENEGAL = (
        "SN",
        pgettext_lazy("IATI codelist Country", "Senegal"),
    )
    SERBIA = (
        "RS",
        pgettext_lazy("IATI codelist Country", "Serbia"),
    )
    SEYCHELLES = (
        "SC",
        pgettext_lazy("IATI codelist Country", "Seychelles"),
    )
    SIERRA_LEONE = (
        "SL",
        pgettext_lazy("IATI codelist Country", "Sierra Leone"),
    )
    SINGAPORE = (
        "SG",
        pgettext_lazy("IATI codelist Country", "Singapore"),
    )
    SINT_MAARTEN__DUTCH_PART_ = (
        "SX",
        pgettext_lazy("IATI codelist Country", "Sint Maarten (Dutch part)"),
    )
    SLOVAKIA = (
        "SK",
        pgettext_lazy("IATI codelist Country", "Slovakia"),
    )
    SLOVENIA = (
        "SI",
        pgettext_lazy("IATI codelist Country", "Slovenia"),
    )
    SOLOMON_ISLANDS = (
        "SB",
        pgettext_lazy("IATI codelist Country", "Solomon Islands"),
    )
    SOMALIA = (
        "SO",
        pgettext_lazy("IATI codelist Country", "Somalia"),
    )
    SOUTH_AFRICA = (
        "ZA",
        pgettext_lazy("IATI codelist Country", "South Africa"),
    )
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = (
        "GS",
        pgettext_lazy(
            "IATI codelist Country", "South Georgia and the South Sandwich Islands"
        ),
    )
    SOUTH_SUDAN = (
        "SS",
        pgettext_lazy("IATI codelist Country", "South Sudan"),
    )
    SPAIN = (
        "ES",
        pgettext_lazy("IATI codelist Country", "Spain"),
    )
    SRI_LANKA = (
        "LK",
        pgettext_lazy("IATI codelist Country", "Sri Lanka"),
    )
    SUDAN__THE_ = (
        "SD",
        pgettext_lazy("IATI codelist Country", "Sudan (the)"),
    )
    SURINAME = (
        "SR",
        pgettext_lazy("IATI codelist Country", "Suriname"),
    )
    SVALBARD_AND_JAN_MAYEN = (
        "SJ",
        pgettext_lazy("IATI codelist Country", "Svalbard and Jan Mayen"),
    )
    ESWATINI = (
        "SZ",
        pgettext_lazy("IATI codelist Country", "Eswatini"),
    )
    SWEDEN = (
        "SE",
        pgettext_lazy("IATI codelist Country", "Sweden"),
    )
    SWITZERLAND = (
        "CH",
        pgettext_lazy("IATI codelist Country", "Switzerland"),
    )
    SYRIAN_ARAB_REPUBLIC = (
        "SY",
        pgettext_lazy("IATI codelist Country", "Syrian Arab Republic"),
    )
    TAIWAN__PROVINCE_OF_CHINA_ = (
        "TW",
        pgettext_lazy("IATI codelist Country", "Taiwan (Province of China)"),
    )
    TAJIKISTAN = (
        "TJ",
        pgettext_lazy("IATI codelist Country", "Tajikistan"),
    )
    TANZANIA__UNITED_REPUBLIC_OF = (
        "TZ",
        pgettext_lazy("IATI codelist Country", "Tanzania, United Republic of"),
    )
    THAILAND = (
        "TH",
        pgettext_lazy("IATI codelist Country", "Thailand"),
    )
    TIMOR_LESTE = (
        "TL",
        pgettext_lazy("IATI codelist Country", "Timor-Leste"),
    )
    TOGO = (
        "TG",
        pgettext_lazy("IATI codelist Country", "Togo"),
    )
    TOKELAU = (
        "TK",
        pgettext_lazy("IATI codelist Country", "Tokelau"),
    )
    TONGA = (
        "TO",
        pgettext_lazy("IATI codelist Country", "Tonga"),
    )
    TRINIDAD_AND_TOBAGO = (
        "TT",
        pgettext_lazy("IATI codelist Country", "Trinidad and Tobago"),
    )
    TUNISIA = (
        "TN",
        pgettext_lazy("IATI codelist Country", "Tunisia"),
    )
    TURKEY = (
        "TR",
        pgettext_lazy("IATI codelist Country", "Turkey"),
    )
    TURKMENISTAN = (
        "TM",
        pgettext_lazy("IATI codelist Country", "Turkmenistan"),
    )
    TURKS_AND_CAICOS_ISLANDS__THE_ = (
        "TC",
        pgettext_lazy("IATI codelist Country", "Turks and Caicos Islands (the)"),
    )
    TUVALU = (
        "TV",
        pgettext_lazy("IATI codelist Country", "Tuvalu"),
    )
    UGANDA = (
        "UG",
        pgettext_lazy("IATI codelist Country", "Uganda"),
    )
    UKRAINE = (
        "UA",
        pgettext_lazy("IATI codelist Country", "Ukraine"),
    )
    UNITED_ARAB_EMIRATES__THE_ = (
        "AE",
        pgettext_lazy("IATI codelist Country", "United Arab Emirates (the)"),
    )
    UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND__THE_ = (
        "GB",
        pgettext_lazy(
            "IATI codelist Country",
            "United Kingdom of Great Britain and Northern Ireland (the)",
        ),
    )
    UNITED_STATES_OF_AMERICA__THE_ = (
        "US",
        pgettext_lazy("IATI codelist Country", "United States of America (the)"),
    )
    UNITED_STATES_MINOR_OUTLYING_ISLANDS__THE_ = (
        "UM",
        pgettext_lazy(
            "IATI codelist Country", "United States Minor Outlying Islands (the)"
        ),
    )
    URUGUAY = (
        "UY",
        pgettext_lazy("IATI codelist Country", "Uruguay"),
    )
    UZBEKISTAN = (
        "UZ",
        pgettext_lazy("IATI codelist Country", "Uzbekistan"),
    )
    VANUATU = (
        "VU",
        pgettext_lazy("IATI codelist Country", "Vanuatu"),
    )
    VENEZUELA__BOLIVARIAN_REPUBLIC_OF_ = (
        "VE",
        pgettext_lazy("IATI codelist Country", "Venezuela (Bolivarian Republic of)"),
    )
    VIET_NAM = (
        "VN",
        pgettext_lazy("IATI codelist Country", "Viet Nam"),
    )
    VIRGIN_ISLANDS__BRITISH_ = (
        "VG",
        pgettext_lazy("IATI codelist Country", "Virgin Islands (British)"),
    )
    VIRGIN_ISLANDS__U_S__ = (
        "VI",
        pgettext_lazy("IATI codelist Country", "Virgin Islands (U.S.)"),
    )
    WALLIS_AND_FUTUNA = (
        "WF",
        pgettext_lazy("IATI codelist Country", "Wallis and Futuna"),
    )
    WESTERN_SAHARA = (
        "EH",
        pgettext_lazy("IATI codelist Country", "Western Sahara"),
    )
    YEMEN = (
        "YE",
        pgettext_lazy("IATI codelist Country", "Yemen"),
    )
    ZAMBIA = (
        "ZM",
        pgettext_lazy("IATI codelist Country", "Zambia"),
    )
    ZIMBABWE = (
        "ZW",
        pgettext_lazy("IATI codelist Country", "Zimbabwe"),
    )
