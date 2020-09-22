from django.db import models
from django.utils.translation import pgettext_lazy


class Language(models.TextChoices):
    AFAR = (
        "aa",
        pgettext_lazy("Language", "Afar"),
    )
    ABKHAZIAN = (
        "ab",
        pgettext_lazy("Language", "Abkhazian"),
    )
    AVESTAN = (
        "ae",
        pgettext_lazy("Language", "Avestan"),
    )
    AFRIKAANS = (
        "af",
        pgettext_lazy("Language", "Afrikaans"),
    )
    AKAN = (
        "ak",
        pgettext_lazy("Language", "Akan"),
    )
    AMHARIC = (
        "am",
        pgettext_lazy("Language", "Amharic"),
    )
    ARAGONESE = (
        "an",
        pgettext_lazy("Language", "Aragonese"),
    )
    ARABIC = (
        "ar",
        pgettext_lazy("Language", "Arabic"),
    )
    ASSAMESE = (
        "as",
        pgettext_lazy("Language", "Assamese"),
    )
    AVARIC = (
        "av",
        pgettext_lazy("Language", "Avaric"),
    )
    AYMARA = (
        "ay",
        pgettext_lazy("Language", "Aymara"),
    )
    AZERBAIJANI = (
        "az",
        pgettext_lazy("Language", "Azerbaijani"),
    )
    BASHKIR = (
        "ba",
        pgettext_lazy("Language", "Bashkir"),
    )
    BELARUSIAN = (
        "be",
        pgettext_lazy("Language", "Belarusian"),
    )
    BULGARIAN = (
        "bg",
        pgettext_lazy("Language", "Bulgarian"),
    )
    BIHARI_LANGUAGES = (
        "bh",
        pgettext_lazy("Language", "Bihari languages"),
    )
    BISLAMA = (
        "bi",
        pgettext_lazy("Language", "Bislama"),
    )
    BAMBARA = (
        "bm",
        pgettext_lazy("Language", "Bambara"),
    )
    BENGALI = (
        "bn",
        pgettext_lazy("Language", "Bengali"),
    )
    TIBETAN = (
        "bo",
        pgettext_lazy("Language", "Tibetan"),
    )
    BRETON = (
        "br",
        pgettext_lazy("Language", "Breton"),
    )
    BOSNIAN = (
        "bs",
        pgettext_lazy("Language", "Bosnian"),
    )
    CATALAN__VALENCIAN = (
        "ca",
        pgettext_lazy("Language", "Catalan; Valencian"),
    )
    CHECHEN = (
        "ce",
        pgettext_lazy("Language", "Chechen"),
    )
    CHAMORRO = (
        "ch",
        pgettext_lazy("Language", "Chamorro"),
    )
    CORSICAN = (
        "co",
        pgettext_lazy("Language", "Corsican"),
    )
    CREE = (
        "cr",
        pgettext_lazy("Language", "Cree"),
    )
    CZECH = (
        "cs",
        pgettext_lazy("Language", "Czech"),
    )
    CHUVASH = (
        "cv",
        pgettext_lazy("Language", "Chuvash"),
    )
    WELSH = (
        "cy",
        pgettext_lazy("Language", "Welsh"),
    )
    DANISH = (
        "da",
        pgettext_lazy("Language", "Danish"),
    )
    GERMAN = (
        "de",
        pgettext_lazy("Language", "German"),
    )
    DIVEHI__DHIVEHI__MALDIVIAN = (
        "dv",
        pgettext_lazy("Language", "Divehi; Dhivehi; Maldivian"),
    )
    DZONGKHA = (
        "dz",
        pgettext_lazy("Language", "Dzongkha"),
    )
    EWE = (
        "ee",
        pgettext_lazy("Language", "Ewe"),
    )
    GREEK = (
        "el",
        pgettext_lazy("Language", "Greek"),
    )
    ENGLISH = (
        "en",
        pgettext_lazy("Language", "English"),
    )
    ESPERANTO = (
        "eo",
        pgettext_lazy("Language", "Esperanto"),
    )
    SPANISH__CASTILIAN = (
        "es",
        pgettext_lazy("Language", "Spanish; Castilian"),
    )
    ESTONIAN = (
        "et",
        pgettext_lazy("Language", "Estonian"),
    )
    BASQUE = (
        "eu",
        pgettext_lazy("Language", "Basque"),
    )
    PERSIAN = (
        "fa",
        pgettext_lazy("Language", "Persian"),
    )
    FULAH = (
        "ff",
        pgettext_lazy("Language", "Fulah"),
    )
    FINNISH = (
        "fi",
        pgettext_lazy("Language", "Finnish"),
    )
    FIJIAN = (
        "fj",
        pgettext_lazy("Language", "Fijian"),
    )
    FAROESE = (
        "fo",
        pgettext_lazy("Language", "Faroese"),
    )
    FRENCH = (
        "fr",
        pgettext_lazy("Language", "French"),
    )
    WESTERN_FRISIAN = (
        "fy",
        pgettext_lazy("Language", "Western Frisian"),
    )
    IRISH = (
        "ga",
        pgettext_lazy("Language", "Irish"),
    )
    GAELIC__SCOTTISH_GAELIC = (
        "gd",
        pgettext_lazy("Language", "Gaelic; Scottish Gaelic"),
    )
    GALICIAN = (
        "gl",
        pgettext_lazy("Language", "Galician"),
    )
    GUARANI = (
        "gn",
        pgettext_lazy("Language", "Guarani"),
    )
    GUJARATI = (
        "gu",
        pgettext_lazy("Language", "Gujarati"),
    )
    MANX = (
        "gv",
        pgettext_lazy("Language", "Manx"),
    )
    HAUSA = (
        "ha",
        pgettext_lazy("Language", "Hausa"),
    )
    HEBREW = (
        "he",
        pgettext_lazy("Language", "Hebrew"),
    )
    HINDI = (
        "hi",
        pgettext_lazy("Language", "Hindi"),
    )
    HIRI_MOTU = (
        "ho",
        pgettext_lazy("Language", "Hiri Motu"),
    )
    CROATIAN = (
        "hr",
        pgettext_lazy("Language", "Croatian"),
    )
    HAITIAN__HAITIAN_CREOLE = (
        "ht",
        pgettext_lazy("Language", "Haitian; Haitian Creole"),
    )
    HUNGARIAN = (
        "hu",
        pgettext_lazy("Language", "Hungarian"),
    )
    ARMENIAN = (
        "hy",
        pgettext_lazy("Language", "Armenian"),
    )
    HERERO = (
        "hz",
        pgettext_lazy("Language", "Herero"),
    )
    INDONESIAN = (
        "id",
        pgettext_lazy("Language", "Indonesian"),
    )
    IGBO = (
        "ig",
        pgettext_lazy("Language", "Igbo"),
    )
    SICHUAN_YI__NUOSU = (
        "ii",
        pgettext_lazy("Language", "Sichuan Yi; Nuosu"),
    )
    INUPIAQ = (
        "ik",
        pgettext_lazy("Language", "Inupiaq"),
    )
    IDO = (
        "io",
        pgettext_lazy("Language", "Ido"),
    )
    ICELANDIC = (
        "is",
        pgettext_lazy("Language", "Icelandic"),
    )
    ITALIAN = (
        "it",
        pgettext_lazy("Language", "Italian"),
    )
    INUKTITUT = (
        "iu",
        pgettext_lazy("Language", "Inuktitut"),
    )
    JAPANESE = (
        "ja",
        pgettext_lazy("Language", "Japanese"),
    )
    JAVANESE = (
        "jv",
        pgettext_lazy("Language", "Javanese"),
    )
    GEORGIAN = (
        "ka",
        pgettext_lazy("Language", "Georgian"),
    )
    KONGO = (
        "kg",
        pgettext_lazy("Language", "Kongo"),
    )
    KIKUYU__GIKUYU = (
        "ki",
        pgettext_lazy("Language", "Kikuyu; Gikuyu"),
    )
    KUANYAMA__KWANYAMA = (
        "kj",
        pgettext_lazy("Language", "Kuanyama; Kwanyama"),
    )
    KAZAKH = (
        "kk",
        pgettext_lazy("Language", "Kazakh"),
    )
    KALAALLISUT__GREENLANDIC = (
        "kl",
        pgettext_lazy("Language", "Kalaallisut; Greenlandic"),
    )
    CENTRAL_KHMER = (
        "km",
        pgettext_lazy("Language", "Central Khmer"),
    )
    KANNADA = (
        "kn",
        pgettext_lazy("Language", "Kannada"),
    )
    KOREAN = (
        "ko",
        pgettext_lazy("Language", "Korean"),
    )
    KANURI = (
        "kr",
        pgettext_lazy("Language", "Kanuri"),
    )
    KASHMIRI = (
        "ks",
        pgettext_lazy("Language", "Kashmiri"),
    )
    KURDISH = (
        "ku",
        pgettext_lazy("Language", "Kurdish"),
    )
    KOMI = (
        "kv",
        pgettext_lazy("Language", "Komi"),
    )
    CORNISH = (
        "kw",
        pgettext_lazy("Language", "Cornish"),
    )
    KIRGHIZ__KYRGYZ = (
        "ky",
        pgettext_lazy("Language", "Kirghiz; Kyrgyz"),
    )
    LATIN = (
        "la",
        pgettext_lazy("Language", "Latin"),
    )
    LUXEMBOURGISH__LETZEBURGESCH = (
        "lb",
        pgettext_lazy("Language", "Luxembourgish; Letzeburgesch"),
    )
    GANDA = (
        "lg",
        pgettext_lazy("Language", "Ganda"),
    )
    LIMBURGAN__LIMBURGER__LIMBURGISH = (
        "li",
        pgettext_lazy("Language", "Limburgan; Limburger; Limburgish"),
    )
    LINGALA = (
        "ln",
        pgettext_lazy("Language", "Lingala"),
    )
    LAO = (
        "lo",
        pgettext_lazy("Language", "Lao"),
    )
    LITHUANIAN = (
        "lt",
        pgettext_lazy("Language", "Lithuanian"),
    )
    LUBA_KATANGA = (
        "lu",
        pgettext_lazy("Language", "Luba-Katanga"),
    )
    LATVIAN = (
        "lv",
        pgettext_lazy("Language", "Latvian"),
    )
    MALAGASY = (
        "mg",
        pgettext_lazy("Language", "Malagasy"),
    )
    MARSHALLESE = (
        "mh",
        pgettext_lazy("Language", "Marshallese"),
    )
    MAORI = (
        "mi",
        pgettext_lazy("Language", "Maori"),
    )
    MACEDONIAN = (
        "mk",
        pgettext_lazy("Language", "Macedonian"),
    )
    MALAYALAM = (
        "ml",
        pgettext_lazy("Language", "Malayalam"),
    )
    MONGOLIAN = (
        "mn",
        pgettext_lazy("Language", "Mongolian"),
    )
    MARATHI = (
        "mr",
        pgettext_lazy("Language", "Marathi"),
    )
    MALAY = (
        "ms",
        pgettext_lazy("Language", "Malay"),
    )
    MALTESE = (
        "mt",
        pgettext_lazy("Language", "Maltese"),
    )
    BURMESE = (
        "my",
        pgettext_lazy("Language", "Burmese"),
    )
    NAURU = (
        "na",
        pgettext_lazy("Language", "Nauru"),
    )
    BOKMÅL__NORWEGIAN__NORWEGIAN_BOKMÅL = (
        "nb",
        pgettext_lazy("Language", "Bokmål, Norwegian; Norwegian Bokmål"),
    )
    NDEBELE__NORTH__NORTH_NDEBELE = (
        "nd",
        pgettext_lazy("Language", "Ndebele, North; North Ndebele"),
    )
    NEPALI = (
        "ne",
        pgettext_lazy("Language", "Nepali"),
    )
    NDONGA = (
        "ng",
        pgettext_lazy("Language", "Ndonga"),
    )
    DUTCH__FLEMISH = (
        "nl",
        pgettext_lazy("Language", "Dutch; Flemish"),
    )
    NORWEGIAN_NYNORSK__NYNORSK__NORWEGIAN = (
        "nn",
        pgettext_lazy("Language", "Norwegian Nynorsk; Nynorsk, Norwegian"),
    )
    NORWEGIAN = (
        "no",
        pgettext_lazy("Language", "Norwegian"),
    )
    NDEBELE__SOUTH__SOUTH_NDEBELE = (
        "nr",
        pgettext_lazy("Language", "Ndebele, South; South Ndebele"),
    )
    NAVAJO__NAVAHO = (
        "nv",
        pgettext_lazy("Language", "Navajo; Navaho"),
    )
    CHICHEWA__CHEWA__NYANJA = (
        "ny",
        pgettext_lazy("Language", "Chichewa; Chewa; Nyanja"),
    )
    OCCITAN__POST_1500_ = (
        "oc",
        pgettext_lazy("Language", "Occitan (post 1500)"),
    )
    OJIBWA = (
        "oj",
        pgettext_lazy("Language", "Ojibwa"),
    )
    OROMO = (
        "om",
        pgettext_lazy("Language", "Oromo"),
    )
    ORIYA = (
        "or",
        pgettext_lazy("Language", "Oriya"),
    )
    OSSETIAN__OSSETIC = (
        "os",
        pgettext_lazy("Language", "Ossetian; Ossetic"),
    )
    PANJABI__PUNJABI = (
        "pa",
        pgettext_lazy("Language", "Panjabi; Punjabi"),
    )
    PALI = (
        "pi",
        pgettext_lazy("Language", "Pali"),
    )
    POLISH = (
        "pl",
        pgettext_lazy("Language", "Polish"),
    )
    PUSHTO__PASHTO = (
        "ps",
        pgettext_lazy("Language", "Pushto; Pashto"),
    )
    PORTUGUESE = (
        "pt",
        pgettext_lazy("Language", "Portuguese"),
    )
    QUECHUA = (
        "qu",
        pgettext_lazy("Language", "Quechua"),
    )
    ROMANSH = (
        "rm",
        pgettext_lazy("Language", "Romansh"),
    )
    RUNDI = (
        "rn",
        pgettext_lazy("Language", "Rundi"),
    )
    ROMANIAN__MOLDAVIAN__MOLDOVAN = (
        "ro",
        pgettext_lazy("Language", "Romanian; Moldavian; Moldovan"),
    )
    RUSSIAN = (
        "ru",
        pgettext_lazy("Language", "Russian"),
    )
    KINYARWANDA = (
        "rw",
        pgettext_lazy("Language", "Kinyarwanda"),
    )
    SANSKRIT = (
        "sa",
        pgettext_lazy("Language", "Sanskrit"),
    )
    SARDINIAN = (
        "sc",
        pgettext_lazy("Language", "Sardinian"),
    )
    SINDHI = (
        "sd",
        pgettext_lazy("Language", "Sindhi"),
    )
    NORTHERN_SAMI = (
        "se",
        pgettext_lazy("Language", "Northern Sami"),
    )
    SANGO = (
        "sg",
        pgettext_lazy("Language", "Sango"),
    )
    SINHALA__SINHALESE = (
        "si",
        pgettext_lazy("Language", "Sinhala; Sinhalese"),
    )
    SLOVAK = (
        "sk",
        pgettext_lazy("Language", "Slovak"),
    )
    SLOVENIAN = (
        "sl",
        pgettext_lazy("Language", "Slovenian"),
    )
    SAMOAN = (
        "sm",
        pgettext_lazy("Language", "Samoan"),
    )
    SHONA = (
        "sn",
        pgettext_lazy("Language", "Shona"),
    )
    SOMALI = (
        "so",
        pgettext_lazy("Language", "Somali"),
    )
    ALBANIAN = (
        "sq",
        pgettext_lazy("Language", "Albanian"),
    )
    SERBIAN = (
        "sr",
        pgettext_lazy("Language", "Serbian"),
    )
    SWATI = (
        "ss",
        pgettext_lazy("Language", "Swati"),
    )
    SOTHO__SOUTHERN = (
        "st",
        pgettext_lazy("Language", "Sotho, Southern"),
    )
    SUNDANESE = (
        "su",
        pgettext_lazy("Language", "Sundanese"),
    )
    SWEDISH = (
        "sv",
        pgettext_lazy("Language", "Swedish"),
    )
    SWAHILI = (
        "sw",
        pgettext_lazy("Language", "Swahili"),
    )
    TAMIL = (
        "ta",
        pgettext_lazy("Language", "Tamil"),
    )
    TELUGU = (
        "te",
        pgettext_lazy("Language", "Telugu"),
    )
    TAJIK = (
        "tg",
        pgettext_lazy("Language", "Tajik"),
    )
    THAI = (
        "th",
        pgettext_lazy("Language", "Thai"),
    )
    TIGRINYA = (
        "ti",
        pgettext_lazy("Language", "Tigrinya"),
    )
    TURKMEN = (
        "tk",
        pgettext_lazy("Language", "Turkmen"),
    )
    TAGALOG = (
        "tl",
        pgettext_lazy("Language", "Tagalog"),
    )
    TSWANA = (
        "tn",
        pgettext_lazy("Language", "Tswana"),
    )
    TONGA__TONGA_ISLANDS_ = (
        "to",
        pgettext_lazy("Language", "Tonga (Tonga Islands)"),
    )
    TURKISH = (
        "tr",
        pgettext_lazy("Language", "Turkish"),
    )
    TSONGA = (
        "ts",
        pgettext_lazy("Language", "Tsonga"),
    )
    TATAR = (
        "tt",
        pgettext_lazy("Language", "Tatar"),
    )
    TWI = (
        "tw",
        pgettext_lazy("Language", "Twi"),
    )
    TAHITIAN = (
        "ty",
        pgettext_lazy("Language", "Tahitian"),
    )
    UIGHUR__UYGHUR = (
        "ug",
        pgettext_lazy("Language", "Uighur; Uyghur"),
    )
    UKRAINIAN = (
        "uk",
        pgettext_lazy("Language", "Ukrainian"),
    )
    URDU = (
        "ur",
        pgettext_lazy("Language", "Urdu"),
    )
    UZBEK = (
        "uz",
        pgettext_lazy("Language", "Uzbek"),
    )
    VENDA = (
        "ve",
        pgettext_lazy("Language", "Venda"),
    )
    VIETNAMESE = (
        "vi",
        pgettext_lazy("Language", "Vietnamese"),
    )
    VOLAPÜK = (
        "vo",
        pgettext_lazy("Language", "Volapük"),
    )
    WALLOON = (
        "wa",
        pgettext_lazy("Language", "Walloon"),
    )
    WOLOF = (
        "wo",
        pgettext_lazy("Language", "Wolof"),
    )
    XHOSA = (
        "xh",
        pgettext_lazy("Language", "Xhosa"),
    )
    YIDDISH = (
        "yi",
        pgettext_lazy("Language", "Yiddish"),
    )
    YORUBA = (
        "yo",
        pgettext_lazy("Language", "Yoruba"),
    )
    ZHUANG__CHUANG = (
        "za",
        pgettext_lazy("Language", "Zhuang; Chuang"),
    )
    CHINESE = (
        "zh",
        pgettext_lazy("Language", "Chinese"),
    )
    ZULU = (
        "zu",
        pgettext_lazy("Language", "Zulu"),
    )
