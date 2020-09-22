from django.db import models
from django.utils.translation import pgettext_lazy


class Language(models.TextChoices):
    AFAR = (
        "aa",
        pgettext_lazy("IATI codelist Language", "Afar"),
    )
    ABKHAZIAN = (
        "ab",
        pgettext_lazy("IATI codelist Language", "Abkhazian"),
    )
    AVESTAN = (
        "ae",
        pgettext_lazy("IATI codelist Language", "Avestan"),
    )
    AFRIKAANS = (
        "af",
        pgettext_lazy("IATI codelist Language", "Afrikaans"),
    )
    AKAN = (
        "ak",
        pgettext_lazy("IATI codelist Language", "Akan"),
    )
    AMHARIC = (
        "am",
        pgettext_lazy("IATI codelist Language", "Amharic"),
    )
    ARAGONESE = (
        "an",
        pgettext_lazy("IATI codelist Language", "Aragonese"),
    )
    ARABIC = (
        "ar",
        pgettext_lazy("IATI codelist Language", "Arabic"),
    )
    ASSAMESE = (
        "as",
        pgettext_lazy("IATI codelist Language", "Assamese"),
    )
    AVARIC = (
        "av",
        pgettext_lazy("IATI codelist Language", "Avaric"),
    )
    AYMARA = (
        "ay",
        pgettext_lazy("IATI codelist Language", "Aymara"),
    )
    AZERBAIJANI = (
        "az",
        pgettext_lazy("IATI codelist Language", "Azerbaijani"),
    )
    BASHKIR = (
        "ba",
        pgettext_lazy("IATI codelist Language", "Bashkir"),
    )
    BELARUSIAN = (
        "be",
        pgettext_lazy("IATI codelist Language", "Belarusian"),
    )
    BULGARIAN = (
        "bg",
        pgettext_lazy("IATI codelist Language", "Bulgarian"),
    )
    BIHARI_LANGUAGES = (
        "bh",
        pgettext_lazy("IATI codelist Language", "Bihari languages"),
    )
    BISLAMA = (
        "bi",
        pgettext_lazy("IATI codelist Language", "Bislama"),
    )
    BAMBARA = (
        "bm",
        pgettext_lazy("IATI codelist Language", "Bambara"),
    )
    BENGALI = (
        "bn",
        pgettext_lazy("IATI codelist Language", "Bengali"),
    )
    TIBETAN = (
        "bo",
        pgettext_lazy("IATI codelist Language", "Tibetan"),
    )
    BRETON = (
        "br",
        pgettext_lazy("IATI codelist Language", "Breton"),
    )
    BOSNIAN = (
        "bs",
        pgettext_lazy("IATI codelist Language", "Bosnian"),
    )
    CATALAN__VALENCIAN = (
        "ca",
        pgettext_lazy("IATI codelist Language", "Catalan; Valencian"),
    )
    CHECHEN = (
        "ce",
        pgettext_lazy("IATI codelist Language", "Chechen"),
    )
    CHAMORRO = (
        "ch",
        pgettext_lazy("IATI codelist Language", "Chamorro"),
    )
    CORSICAN = (
        "co",
        pgettext_lazy("IATI codelist Language", "Corsican"),
    )
    CREE = (
        "cr",
        pgettext_lazy("IATI codelist Language", "Cree"),
    )
    CZECH = (
        "cs",
        pgettext_lazy("IATI codelist Language", "Czech"),
    )
    CHUVASH = (
        "cv",
        pgettext_lazy("IATI codelist Language", "Chuvash"),
    )
    WELSH = (
        "cy",
        pgettext_lazy("IATI codelist Language", "Welsh"),
    )
    DANISH = (
        "da",
        pgettext_lazy("IATI codelist Language", "Danish"),
    )
    GERMAN = (
        "de",
        pgettext_lazy("IATI codelist Language", "German"),
    )
    DIVEHI__DHIVEHI__MALDIVIAN = (
        "dv",
        pgettext_lazy("IATI codelist Language", "Divehi; Dhivehi; Maldivian"),
    )
    DZONGKHA = (
        "dz",
        pgettext_lazy("IATI codelist Language", "Dzongkha"),
    )
    EWE = (
        "ee",
        pgettext_lazy("IATI codelist Language", "Ewe"),
    )
    GREEK = (
        "el",
        pgettext_lazy("IATI codelist Language", "Greek"),
    )
    ENGLISH = (
        "en",
        pgettext_lazy("IATI codelist Language", "English"),
    )
    ESPERANTO = (
        "eo",
        pgettext_lazy("IATI codelist Language", "Esperanto"),
    )
    SPANISH__CASTILIAN = (
        "es",
        pgettext_lazy("IATI codelist Language", "Spanish; Castilian"),
    )
    ESTONIAN = (
        "et",
        pgettext_lazy("IATI codelist Language", "Estonian"),
    )
    BASQUE = (
        "eu",
        pgettext_lazy("IATI codelist Language", "Basque"),
    )
    PERSIAN = (
        "fa",
        pgettext_lazy("IATI codelist Language", "Persian"),
    )
    FULAH = (
        "ff",
        pgettext_lazy("IATI codelist Language", "Fulah"),
    )
    FINNISH = (
        "fi",
        pgettext_lazy("IATI codelist Language", "Finnish"),
    )
    FIJIAN = (
        "fj",
        pgettext_lazy("IATI codelist Language", "Fijian"),
    )
    FAROESE = (
        "fo",
        pgettext_lazy("IATI codelist Language", "Faroese"),
    )
    FRENCH = (
        "fr",
        pgettext_lazy("IATI codelist Language", "French"),
    )
    WESTERN_FRISIAN = (
        "fy",
        pgettext_lazy("IATI codelist Language", "Western Frisian"),
    )
    IRISH = (
        "ga",
        pgettext_lazy("IATI codelist Language", "Irish"),
    )
    GAELIC__SCOTTISH_GAELIC = (
        "gd",
        pgettext_lazy("IATI codelist Language", "Gaelic; Scottish Gaelic"),
    )
    GALICIAN = (
        "gl",
        pgettext_lazy("IATI codelist Language", "Galician"),
    )
    GUARANI = (
        "gn",
        pgettext_lazy("IATI codelist Language", "Guarani"),
    )
    GUJARATI = (
        "gu",
        pgettext_lazy("IATI codelist Language", "Gujarati"),
    )
    MANX = (
        "gv",
        pgettext_lazy("IATI codelist Language", "Manx"),
    )
    HAUSA = (
        "ha",
        pgettext_lazy("IATI codelist Language", "Hausa"),
    )
    HEBREW = (
        "he",
        pgettext_lazy("IATI codelist Language", "Hebrew"),
    )
    HINDI = (
        "hi",
        pgettext_lazy("IATI codelist Language", "Hindi"),
    )
    HIRI_MOTU = (
        "ho",
        pgettext_lazy("IATI codelist Language", "Hiri Motu"),
    )
    CROATIAN = (
        "hr",
        pgettext_lazy("IATI codelist Language", "Croatian"),
    )
    HAITIAN__HAITIAN_CREOLE = (
        "ht",
        pgettext_lazy("IATI codelist Language", "Haitian; Haitian Creole"),
    )
    HUNGARIAN = (
        "hu",
        pgettext_lazy("IATI codelist Language", "Hungarian"),
    )
    ARMENIAN = (
        "hy",
        pgettext_lazy("IATI codelist Language", "Armenian"),
    )
    HERERO = (
        "hz",
        pgettext_lazy("IATI codelist Language", "Herero"),
    )
    INDONESIAN = (
        "id",
        pgettext_lazy("IATI codelist Language", "Indonesian"),
    )
    IGBO = (
        "ig",
        pgettext_lazy("IATI codelist Language", "Igbo"),
    )
    SICHUAN_YI__NUOSU = (
        "ii",
        pgettext_lazy("IATI codelist Language", "Sichuan Yi; Nuosu"),
    )
    INUPIAQ = (
        "ik",
        pgettext_lazy("IATI codelist Language", "Inupiaq"),
    )
    IDO = (
        "io",
        pgettext_lazy("IATI codelist Language", "Ido"),
    )
    ICELANDIC = (
        "is",
        pgettext_lazy("IATI codelist Language", "Icelandic"),
    )
    ITALIAN = (
        "it",
        pgettext_lazy("IATI codelist Language", "Italian"),
    )
    INUKTITUT = (
        "iu",
        pgettext_lazy("IATI codelist Language", "Inuktitut"),
    )
    JAPANESE = (
        "ja",
        pgettext_lazy("IATI codelist Language", "Japanese"),
    )
    JAVANESE = (
        "jv",
        pgettext_lazy("IATI codelist Language", "Javanese"),
    )
    GEORGIAN = (
        "ka",
        pgettext_lazy("IATI codelist Language", "Georgian"),
    )
    KONGO = (
        "kg",
        pgettext_lazy("IATI codelist Language", "Kongo"),
    )
    KIKUYU__GIKUYU = (
        "ki",
        pgettext_lazy("IATI codelist Language", "Kikuyu; Gikuyu"),
    )
    KUANYAMA__KWANYAMA = (
        "kj",
        pgettext_lazy("IATI codelist Language", "Kuanyama; Kwanyama"),
    )
    KAZAKH = (
        "kk",
        pgettext_lazy("IATI codelist Language", "Kazakh"),
    )
    KALAALLISUT__GREENLANDIC = (
        "kl",
        pgettext_lazy("IATI codelist Language", "Kalaallisut; Greenlandic"),
    )
    CENTRAL_KHMER = (
        "km",
        pgettext_lazy("IATI codelist Language", "Central Khmer"),
    )
    KANNADA = (
        "kn",
        pgettext_lazy("IATI codelist Language", "Kannada"),
    )
    KOREAN = (
        "ko",
        pgettext_lazy("IATI codelist Language", "Korean"),
    )
    KANURI = (
        "kr",
        pgettext_lazy("IATI codelist Language", "Kanuri"),
    )
    KASHMIRI = (
        "ks",
        pgettext_lazy("IATI codelist Language", "Kashmiri"),
    )
    KURDISH = (
        "ku",
        pgettext_lazy("IATI codelist Language", "Kurdish"),
    )
    KOMI = (
        "kv",
        pgettext_lazy("IATI codelist Language", "Komi"),
    )
    CORNISH = (
        "kw",
        pgettext_lazy("IATI codelist Language", "Cornish"),
    )
    KIRGHIZ__KYRGYZ = (
        "ky",
        pgettext_lazy("IATI codelist Language", "Kirghiz; Kyrgyz"),
    )
    LATIN = (
        "la",
        pgettext_lazy("IATI codelist Language", "Latin"),
    )
    LUXEMBOURGISH__LETZEBURGESCH = (
        "lb",
        pgettext_lazy("IATI codelist Language", "Luxembourgish; Letzeburgesch"),
    )
    GANDA = (
        "lg",
        pgettext_lazy("IATI codelist Language", "Ganda"),
    )
    LIMBURGAN__LIMBURGER__LIMBURGISH = (
        "li",
        pgettext_lazy("IATI codelist Language", "Limburgan; Limburger; Limburgish"),
    )
    LINGALA = (
        "ln",
        pgettext_lazy("IATI codelist Language", "Lingala"),
    )
    LAO = (
        "lo",
        pgettext_lazy("IATI codelist Language", "Lao"),
    )
    LITHUANIAN = (
        "lt",
        pgettext_lazy("IATI codelist Language", "Lithuanian"),
    )
    LUBA_KATANGA = (
        "lu",
        pgettext_lazy("IATI codelist Language", "Luba-Katanga"),
    )
    LATVIAN = (
        "lv",
        pgettext_lazy("IATI codelist Language", "Latvian"),
    )
    MALAGASY = (
        "mg",
        pgettext_lazy("IATI codelist Language", "Malagasy"),
    )
    MARSHALLESE = (
        "mh",
        pgettext_lazy("IATI codelist Language", "Marshallese"),
    )
    MAORI = (
        "mi",
        pgettext_lazy("IATI codelist Language", "Maori"),
    )
    MACEDONIAN = (
        "mk",
        pgettext_lazy("IATI codelist Language", "Macedonian"),
    )
    MALAYALAM = (
        "ml",
        pgettext_lazy("IATI codelist Language", "Malayalam"),
    )
    MONGOLIAN = (
        "mn",
        pgettext_lazy("IATI codelist Language", "Mongolian"),
    )
    MARATHI = (
        "mr",
        pgettext_lazy("IATI codelist Language", "Marathi"),
    )
    MALAY = (
        "ms",
        pgettext_lazy("IATI codelist Language", "Malay"),
    )
    MALTESE = (
        "mt",
        pgettext_lazy("IATI codelist Language", "Maltese"),
    )
    BURMESE = (
        "my",
        pgettext_lazy("IATI codelist Language", "Burmese"),
    )
    NAURU = (
        "na",
        pgettext_lazy("IATI codelist Language", "Nauru"),
    )
    BOKMÅL__NORWEGIAN__NORWEGIAN_BOKMÅL = (
        "nb",
        pgettext_lazy("IATI codelist Language", "Bokmål, Norwegian; Norwegian Bokmål"),
    )
    NDEBELE__NORTH__NORTH_NDEBELE = (
        "nd",
        pgettext_lazy("IATI codelist Language", "Ndebele, North; North Ndebele"),
    )
    NEPALI = (
        "ne",
        pgettext_lazy("IATI codelist Language", "Nepali"),
    )
    NDONGA = (
        "ng",
        pgettext_lazy("IATI codelist Language", "Ndonga"),
    )
    DUTCH__FLEMISH = (
        "nl",
        pgettext_lazy("IATI codelist Language", "Dutch; Flemish"),
    )
    NORWEGIAN_NYNORSK__NYNORSK__NORWEGIAN = (
        "nn",
        pgettext_lazy(
            "IATI codelist Language", "Norwegian Nynorsk; Nynorsk, Norwegian"
        ),
    )
    NORWEGIAN = (
        "no",
        pgettext_lazy("IATI codelist Language", "Norwegian"),
    )
    NDEBELE__SOUTH__SOUTH_NDEBELE = (
        "nr",
        pgettext_lazy("IATI codelist Language", "Ndebele, South; South Ndebele"),
    )
    NAVAJO__NAVAHO = (
        "nv",
        pgettext_lazy("IATI codelist Language", "Navajo; Navaho"),
    )
    CHICHEWA__CHEWA__NYANJA = (
        "ny",
        pgettext_lazy("IATI codelist Language", "Chichewa; Chewa; Nyanja"),
    )
    OCCITAN__POST_1500_ = (
        "oc",
        pgettext_lazy("IATI codelist Language", "Occitan (post 1500)"),
    )
    OJIBWA = (
        "oj",
        pgettext_lazy("IATI codelist Language", "Ojibwa"),
    )
    OROMO = (
        "om",
        pgettext_lazy("IATI codelist Language", "Oromo"),
    )
    ORIYA = (
        "or",
        pgettext_lazy("IATI codelist Language", "Oriya"),
    )
    OSSETIAN__OSSETIC = (
        "os",
        pgettext_lazy("IATI codelist Language", "Ossetian; Ossetic"),
    )
    PANJABI__PUNJABI = (
        "pa",
        pgettext_lazy("IATI codelist Language", "Panjabi; Punjabi"),
    )
    PALI = (
        "pi",
        pgettext_lazy("IATI codelist Language", "Pali"),
    )
    POLISH = (
        "pl",
        pgettext_lazy("IATI codelist Language", "Polish"),
    )
    PUSHTO__PASHTO = (
        "ps",
        pgettext_lazy("IATI codelist Language", "Pushto; Pashto"),
    )
    PORTUGUESE = (
        "pt",
        pgettext_lazy("IATI codelist Language", "Portuguese"),
    )
    QUECHUA = (
        "qu",
        pgettext_lazy("IATI codelist Language", "Quechua"),
    )
    ROMANSH = (
        "rm",
        pgettext_lazy("IATI codelist Language", "Romansh"),
    )
    RUNDI = (
        "rn",
        pgettext_lazy("IATI codelist Language", "Rundi"),
    )
    ROMANIAN__MOLDAVIAN__MOLDOVAN = (
        "ro",
        pgettext_lazy("IATI codelist Language", "Romanian; Moldavian; Moldovan"),
    )
    RUSSIAN = (
        "ru",
        pgettext_lazy("IATI codelist Language", "Russian"),
    )
    KINYARWANDA = (
        "rw",
        pgettext_lazy("IATI codelist Language", "Kinyarwanda"),
    )
    SANSKRIT = (
        "sa",
        pgettext_lazy("IATI codelist Language", "Sanskrit"),
    )
    SARDINIAN = (
        "sc",
        pgettext_lazy("IATI codelist Language", "Sardinian"),
    )
    SINDHI = (
        "sd",
        pgettext_lazy("IATI codelist Language", "Sindhi"),
    )
    NORTHERN_SAMI = (
        "se",
        pgettext_lazy("IATI codelist Language", "Northern Sami"),
    )
    SANGO = (
        "sg",
        pgettext_lazy("IATI codelist Language", "Sango"),
    )
    SINHALA__SINHALESE = (
        "si",
        pgettext_lazy("IATI codelist Language", "Sinhala; Sinhalese"),
    )
    SLOVAK = (
        "sk",
        pgettext_lazy("IATI codelist Language", "Slovak"),
    )
    SLOVENIAN = (
        "sl",
        pgettext_lazy("IATI codelist Language", "Slovenian"),
    )
    SAMOAN = (
        "sm",
        pgettext_lazy("IATI codelist Language", "Samoan"),
    )
    SHONA = (
        "sn",
        pgettext_lazy("IATI codelist Language", "Shona"),
    )
    SOMALI = (
        "so",
        pgettext_lazy("IATI codelist Language", "Somali"),
    )
    ALBANIAN = (
        "sq",
        pgettext_lazy("IATI codelist Language", "Albanian"),
    )
    SERBIAN = (
        "sr",
        pgettext_lazy("IATI codelist Language", "Serbian"),
    )
    SWATI = (
        "ss",
        pgettext_lazy("IATI codelist Language", "Swati"),
    )
    SOTHO__SOUTHERN = (
        "st",
        pgettext_lazy("IATI codelist Language", "Sotho, Southern"),
    )
    SUNDANESE = (
        "su",
        pgettext_lazy("IATI codelist Language", "Sundanese"),
    )
    SWEDISH = (
        "sv",
        pgettext_lazy("IATI codelist Language", "Swedish"),
    )
    SWAHILI = (
        "sw",
        pgettext_lazy("IATI codelist Language", "Swahili"),
    )
    TAMIL = (
        "ta",
        pgettext_lazy("IATI codelist Language", "Tamil"),
    )
    TELUGU = (
        "te",
        pgettext_lazy("IATI codelist Language", "Telugu"),
    )
    TAJIK = (
        "tg",
        pgettext_lazy("IATI codelist Language", "Tajik"),
    )
    THAI = (
        "th",
        pgettext_lazy("IATI codelist Language", "Thai"),
    )
    TIGRINYA = (
        "ti",
        pgettext_lazy("IATI codelist Language", "Tigrinya"),
    )
    TURKMEN = (
        "tk",
        pgettext_lazy("IATI codelist Language", "Turkmen"),
    )
    TAGALOG = (
        "tl",
        pgettext_lazy("IATI codelist Language", "Tagalog"),
    )
    TSWANA = (
        "tn",
        pgettext_lazy("IATI codelist Language", "Tswana"),
    )
    TONGA__TONGA_ISLANDS_ = (
        "to",
        pgettext_lazy("IATI codelist Language", "Tonga (Tonga Islands)"),
    )
    TURKISH = (
        "tr",
        pgettext_lazy("IATI codelist Language", "Turkish"),
    )
    TSONGA = (
        "ts",
        pgettext_lazy("IATI codelist Language", "Tsonga"),
    )
    TATAR = (
        "tt",
        pgettext_lazy("IATI codelist Language", "Tatar"),
    )
    TWI = (
        "tw",
        pgettext_lazy("IATI codelist Language", "Twi"),
    )
    TAHITIAN = (
        "ty",
        pgettext_lazy("IATI codelist Language", "Tahitian"),
    )
    UIGHUR__UYGHUR = (
        "ug",
        pgettext_lazy("IATI codelist Language", "Uighur; Uyghur"),
    )
    UKRAINIAN = (
        "uk",
        pgettext_lazy("IATI codelist Language", "Ukrainian"),
    )
    URDU = (
        "ur",
        pgettext_lazy("IATI codelist Language", "Urdu"),
    )
    UZBEK = (
        "uz",
        pgettext_lazy("IATI codelist Language", "Uzbek"),
    )
    VENDA = (
        "ve",
        pgettext_lazy("IATI codelist Language", "Venda"),
    )
    VIETNAMESE = (
        "vi",
        pgettext_lazy("IATI codelist Language", "Vietnamese"),
    )
    VOLAPÜK = (
        "vo",
        pgettext_lazy("IATI codelist Language", "Volapük"),
    )
    WALLOON = (
        "wa",
        pgettext_lazy("IATI codelist Language", "Walloon"),
    )
    WOLOF = (
        "wo",
        pgettext_lazy("IATI codelist Language", "Wolof"),
    )
    XHOSA = (
        "xh",
        pgettext_lazy("IATI codelist Language", "Xhosa"),
    )
    YIDDISH = (
        "yi",
        pgettext_lazy("IATI codelist Language", "Yiddish"),
    )
    YORUBA = (
        "yo",
        pgettext_lazy("IATI codelist Language", "Yoruba"),
    )
    ZHUANG__CHUANG = (
        "za",
        pgettext_lazy("IATI codelist Language", "Zhuang; Chuang"),
    )
    CHINESE = (
        "zh",
        pgettext_lazy("IATI codelist Language", "Chinese"),
    )
    ZULU = (
        "zu",
        pgettext_lazy("IATI codelist Language", "Zulu"),
    )
