from django.db import models
from django.utils.translation import pgettext_lazy


class LocationType(models.TextChoices):
    """
    US NGA Feature Designation Codes On this codelist 'category' is used for the Feature Class.
    """

    ABANDONED_AIRFIELD = (
        "AIRQ",
        pgettext_lazy("LocationType", "abandoned airfield"),
    )
    ABANDONED_CAMP = (
        "CMPQ",
        pgettext_lazy("LocationType", "abandoned camp"),
    )
    ABANDONED_CANAL = (
        "CNLQ",
        pgettext_lazy("LocationType", "abandoned canal"),
    )
    ABANDONED_FACTORY = (
        "MFGQ",
        pgettext_lazy("LocationType", "abandoned factory"),
    )
    ABANDONED_FARM = (
        "FRMQ",
        pgettext_lazy("LocationType", "abandoned farm"),
    )
    ABANDONED_MINE = (
        "MNQ",
        pgettext_lazy("LocationType", "abandoned mine"),
    )
    ABANDONED_MISSION = (
        "MSSNQ",
        pgettext_lazy("LocationType", "abandoned mission"),
    )
    ABANDONED_OIL_WELL = (
        "OILQ",
        pgettext_lazy("LocationType", "abandoned oil well"),
    )
    ABANDONED_POLICE_POST = (
        "PPQ",
        pgettext_lazy("LocationType", "abandoned police post"),
    )
    ABANDONED_POPULATED_PLACE = (
        "PPLQ",
        pgettext_lazy("LocationType", "abandoned populated place"),
    )
    ABANDONED_PRISON = (
        "PRNQ",
        pgettext_lazy("LocationType", "abandoned prison"),
    )
    ABANDONED_RAILROAD = (
        "RRQ",
        pgettext_lazy("LocationType", "abandoned railroad"),
    )
    ABANDONED_RAILROAD_STATION = (
        "RSTNQ",
        pgettext_lazy("LocationType", "abandoned railroad station"),
    )
    ABANDONED_RAILROAD_STOP = (
        "RSTPQ",
        pgettext_lazy("LocationType", "abandoned railroad stop"),
    )
    ABANDONED_WATERCOURSE = (
        "STMQ",
        pgettext_lazy("LocationType", "abandoned watercourse"),
    )
    ABANDONED_WELL = (
        "WLLQ",
        pgettext_lazy("LocationType", "abandoned well"),
    )
    ADMINISTRATIVE_DIVISION = (
        "ADMD",
        pgettext_lazy("LocationType", "administrative division"),
    )
    ADMINISTRATIVE_FACILITY = (
        "ADMF",
        pgettext_lazy("LocationType", "administrative facility"),
    )
    AGRICULTURAL_COLONY = (
        "AGRC",
        pgettext_lazy("LocationType", "agricultural colony"),
    )
    AGRICULTURAL_FACILITY = (
        "AGRF",
        pgettext_lazy("LocationType", "agricultural facility"),
    )
    AGRICULTURAL_RESERVE = (
        "RESA",
        pgettext_lazy("LocationType", "agricultural reserve"),
    )
    AGRICULTURAL_SCHOOL = (
        "SCHA",
        pgettext_lazy("LocationType", "agricultural school"),
    )
    AIRBASE = (
        "AIRB",
        pgettext_lazy("LocationType", "airbase"),
    )
    AIRFIELD = (
        "AIRF",
        pgettext_lazy("LocationType", "airfield"),
    )
    AIRPORT = (
        "AIRP",
        pgettext_lazy("LocationType", "airport"),
    )
    AMPHITHEATER = (
        "AMTH",
        pgettext_lazy("LocationType", "amphitheater"),
    )
    ANABRANCH = (
        "STMA",
        pgettext_lazy("LocationType", "anabranch"),
    )
    ANCHORAGE = (
        "ANCH",
        pgettext_lazy("LocationType", "anchorage"),
    )
    ANCIENT_ROAD = (
        "RDA",
        pgettext_lazy("LocationType", "ancient road"),
    )
    ANCIENT_SITE = (
        "ANS",
        pgettext_lazy("LocationType", "ancient site"),
    )
    ANCIENT_WALL = (
        "WALLA",
        pgettext_lazy("LocationType", "ancient wall"),
    )
    APARTMENT_BUILDING = (
        "BLDA",
        pgettext_lazy("LocationType", "apartment building"),
    )
    AQUACULTURE_FACILITY = (
        "AQC",
        pgettext_lazy("LocationType", "aquaculture facility"),
    )
    AQUEDUCT = (
        "CNLA",
        pgettext_lazy("LocationType", "aqueduct"),
    )
    ARCH = (
        "ARCH",
        pgettext_lazy("LocationType", "arch"),
    )
    ARCTIC_LAND = (
        "LAND",
        pgettext_lazy("LocationType", "Arctic land"),
    )
    AREA = (
        "AREA",
        pgettext_lazy("LocationType", "area"),
    )
    ARTIFICIAL_ISLAND = (
        "ISLF",
        pgettext_lazy("LocationType", "artificial island"),
    )
    ARTILLERY_RANGE = (
        "RNGA",
        pgettext_lazy("LocationType", "artillery range"),
    )
    ASPHALT_LAKE = (
        "ASPH",
        pgettext_lazy("LocationType", "asphalt lake"),
    )
    ASTRONOMICAL_STATION = (
        "ASTR",
        pgettext_lazy("LocationType", "astronomical station"),
    )
    ASYLUM = (
        "ASYL",
        pgettext_lazy("LocationType", "asylum"),
    )
    ATHLETIC_FIELD = (
        "ATHF",
        pgettext_lazy("LocationType", "athletic field"),
    )
    ATOLL_S_ = (
        "ATOL",
        pgettext_lazy("LocationType", "atoll(s)"),
    )
    ATOMIC_CENTER = (
        "CTRA",
        pgettext_lazy("LocationType", "atomic center"),
    )
    BADLANDS = (
        "BDLD",
        pgettext_lazy("LocationType", "badlands"),
    )
    BALING_STATION = (
        "BSTN",
        pgettext_lazy("LocationType", "baling station"),
    )
    BANANA_PLANTATION = (
        "ESTB",
        pgettext_lazy("LocationType", "banana plantation"),
    )
    BANK = (
        "BAN",
        pgettext_lazy("LocationType", "bank"),
    )
    BANK_S_ = (
        "BNK",
        pgettext_lazy("LocationType", "bank(s)"),
    )
    BAR = (
        "BAR",
        pgettext_lazy("LocationType", "bar"),
    )
    BARRACKS = (
        "BRKS",
        pgettext_lazy("LocationType", "barracks"),
    )
    BATTLEFIELD = (
        "BTL",
        pgettext_lazy("LocationType", "battlefield"),
    )
    BAY = (
        "BAY",
        pgettext_lazy("LocationType", "bay"),
    )
    BAYS = (
        "BAYS",
        pgettext_lazy("LocationType", "bays"),
    )
    BEACH = (
        "BCH",
        pgettext_lazy("LocationType", "beach"),
    )
    BEACH_RIDGE = (
        "RDGB",
        pgettext_lazy("LocationType", "beach ridge"),
    )
    BEACHES = (
        "BCHS",
        pgettext_lazy("LocationType", "beaches"),
    )
    BEACON = (
        "BCN",
        pgettext_lazy("LocationType", "beacon"),
    )
    BENCH = (
        "BNCH",
        pgettext_lazy("LocationType", "bench"),
    )
    BIGHT_S_ = (
        "BGHT",
        pgettext_lazy("LocationType", "bight(s)"),
    )
    BLOWHOLE_S_ = (
        "BLHL",
        pgettext_lazy("LocationType", "blowhole(s)"),
    )
    BLOWOUT_S_ = (
        "BLOW",
        pgettext_lazy("LocationType", "blowout(s)"),
    )
    BOATYARD = (
        "BTYD",
        pgettext_lazy("LocationType", "boatyard"),
    )
    BOG_S_ = (
        "BOG",
        pgettext_lazy("LocationType", "bog(s)"),
    )
    BORDER_POST = (
        "PSTB",
        pgettext_lazy("LocationType", "border post"),
    )
    BOULDER_FIELD = (
        "BLDR",
        pgettext_lazy("LocationType", "boulder field"),
    )
    BOUNDARY_MARKER = (
        "BP",
        pgettext_lazy("LocationType", "boundary marker"),
    )
    BREAKWATER = (
        "BRKW",
        pgettext_lazy("LocationType", "breakwater"),
    )
    BREWERY = (
        "MFGB",
        pgettext_lazy("LocationType", "brewery"),
    )
    BRIDGE = (
        "BDG",
        pgettext_lazy("LocationType", "bridge"),
    )
    BUFFER_ZONE = (
        "ZNB",
        pgettext_lazy("LocationType", "buffer zone"),
    )
    BUILDING_S_ = (
        "BLDG",
        pgettext_lazy("LocationType", "building(s)"),
    )
    BURIAL_CAVE_S_ = (
        "BUR",
        pgettext_lazy("LocationType", "burial cave(s)"),
    )
    BUSH_ES_ = (
        "BUSH",
        pgettext_lazy("LocationType", "bush(es)"),
    )
    BUSINESS_CENTER = (
        "CTRB",
        pgettext_lazy("LocationType", "business center"),
    )
    BUTTE_S_ = (
        "BUTE",
        pgettext_lazy("LocationType", "butte(s)"),
    )
    CAIRN = (
        "CARN",
        pgettext_lazy("LocationType", "cairn"),
    )
    CALDERA = (
        "CLDA",
        pgettext_lazy("LocationType", "caldera"),
    )
    CAMP_S_ = (
        "CMP",
        pgettext_lazy("LocationType", "camp(s)"),
    )
    CANAL = (
        "CNL",
        pgettext_lazy("LocationType", "canal"),
    )
    CANAL_BEND = (
        "CNLB",
        pgettext_lazy("LocationType", "canal bend"),
    )
    CANAL_TUNNEL = (
        "TNLC",
        pgettext_lazy("LocationType", "canal tunnel"),
    )
    CANALIZED_STREAM = (
        "STMC",
        pgettext_lazy("LocationType", "canalized stream"),
    )
    CANNERY = (
        "MFGC",
        pgettext_lazy("LocationType", "cannery"),
    )
    CANYON = (
        "CNYN",
        pgettext_lazy("LocationType", "canyon"),
    )
    CAPE = (
        "CAPE",
        pgettext_lazy("LocationType", "cape"),
    )
    CAPITAL_OF_A_POLITICAL_ENTITY = (
        "PPLC",
        pgettext_lazy("LocationType", "capital of a political entity"),
    )
    CARAVAN_ROUTE = (
        "RTE",
        pgettext_lazy("LocationType", "caravan route"),
    )
    CASINO = (
        "CSNO",
        pgettext_lazy("LocationType", "casino"),
    )
    CASTLE = (
        "CSTL",
        pgettext_lazy("LocationType", "castle"),
    )
    CATTLE_DIPPING_TANK = (
        "TNKD",
        pgettext_lazy("LocationType", "cattle dipping tank"),
    )
    CAUSEWAY = (
        "CSWY",
        pgettext_lazy("LocationType", "causeway"),
    )
    CAVE_S_ = (
        "CAVE",
        pgettext_lazy("LocationType", "cave(s)"),
    )
    CEMETERY = (
        "CMTY",
        pgettext_lazy("LocationType", "cemetery"),
    )
    CHANNEL = (
        "CHN",
        pgettext_lazy("LocationType", "channel"),
    )
    CHROME_MINE_S_ = (
        "MNCR",
        pgettext_lazy("LocationType", "chrome mine(s)"),
    )
    CHURCH = (
        "CH",
        pgettext_lazy("LocationType", "church"),
    )
    CIRQUE = (
        "CRQ",
        pgettext_lazy("LocationType", "cirque"),
    )
    CIRQUES = (
        "CRQS",
        pgettext_lazy("LocationType", "cirques"),
    )
    CLEARING = (
        "CLG",
        pgettext_lazy("LocationType", "clearing"),
    )
    CLEFT_S_ = (
        "CFT",
        pgettext_lazy("LocationType", "cleft(s)"),
    )
    CLIFF_S_ = (
        "CLF",
        pgettext_lazy("LocationType", "cliff(s)"),
    )
    CLINIC = (
        "HSPC",
        pgettext_lazy("LocationType", "clinic"),
    )
    COAL_MINE_S_ = (
        "MNC",
        pgettext_lazy("LocationType", "coal mine(s)"),
    )
    COALFIELD = (
        "COLF",
        pgettext_lazy("LocationType", "coalfield"),
    )
    COAST = (
        "CST",
        pgettext_lazy("LocationType", "coast"),
    )
    COAST_GUARD_STATION = (
        "STNC",
        pgettext_lazy("LocationType", "coast guard station"),
    )
    COCONUT_GROVE = (
        "GRVC",
        pgettext_lazy("LocationType", "coconut grove"),
    )
    COLLEGE = (
        "SCHC",
        pgettext_lazy("LocationType", "college"),
    )
    COMMON = (
        "CMN",
        pgettext_lazy("LocationType", "common"),
    )
    COMMUNICATION_CENTER = (
        "COMC",
        pgettext_lazy("LocationType", "communication center"),
    )
    COMMUNITY_CENTER = (
        "CTRCM",
        pgettext_lazy("LocationType", "community center"),
    )
    CONCESSION_AREA = (
        "CNS",
        pgettext_lazy("LocationType", "concession area"),
    )
    CONE_S_ = (
        "CONE",
        pgettext_lazy("LocationType", "cone(s)"),
    )
    CONFLUENCE = (
        "CNFL",
        pgettext_lazy("LocationType", "confluence"),
    )
    CONTINENTAL_RISE = (
        "CRSU",
        pgettext_lazy("LocationType", "continental rise"),
    )
    CONVENT = (
        "CVNT",
        pgettext_lazy("LocationType", "convent"),
    )
    COPPER_MINE_S_ = (
        "MNCU",
        pgettext_lazy("LocationType", "copper mine(s)"),
    )
    COPPER_WORKS = (
        "MFGCU",
        pgettext_lazy("LocationType", "copper works"),
    )
    CORAL_REEF_S_ = (
        "RFC",
        pgettext_lazy("LocationType", "coral reef(s)"),
    )
    CORRAL_S_ = (
        "CRRL",
        pgettext_lazy("LocationType", "corral(s)"),
    )
    CORRIDOR = (
        "CRDR",
        pgettext_lazy("LocationType", "corridor"),
    )
    COTTON_PLANTATION = (
        "ESTC",
        pgettext_lazy("LocationType", "cotton plantation"),
    )
    COUNTRY_HOUSE = (
        "HSEC",
        pgettext_lazy("LocationType", "country house"),
    )
    COURTHOUSE = (
        "CTHSE",
        pgettext_lazy("LocationType", "courthouse"),
    )
    COVE_S_ = (
        "COVE",
        pgettext_lazy("LocationType", "cove(s)"),
    )
    CRATER_LAKE = (
        "LKC",
        pgettext_lazy("LocationType", "crater lake"),
    )
    CRATER_LAKES = (
        "LKSC",
        pgettext_lazy("LocationType", "crater lakes"),
    )
    CRATER_S_ = (
        "CRTR",
        pgettext_lazy("LocationType", "crater(s)"),
    )
    CUESTA_S_ = (
        "CUET",
        pgettext_lazy("LocationType", "cuesta(s)"),
    )
    CULTIVATED_AREA = (
        "CULT",
        pgettext_lazy("LocationType", "cultivated area"),
    )
    CURRENT = (
        "CRNT",
        pgettext_lazy("LocationType", "current"),
    )
    CUSTOMS_HOUSE = (
        "CSTM",
        pgettext_lazy("LocationType", "customs house"),
    )
    CUSTOMS_POST = (
        "PSTC",
        pgettext_lazy("LocationType", "customs post"),
    )
    CUTOFF = (
        "CUTF",
        pgettext_lazy("LocationType", "cutoff"),
    )
    DAIRY = (
        "DARY",
        pgettext_lazy("LocationType", "dairy"),
    )
    DAM = (
        "DAM",
        pgettext_lazy("LocationType", "dam"),
    )
    DEEP = (
        "DEPU",
        pgettext_lazy("LocationType", "deep"),
    )
    DELTA = (
        "DLTA",
        pgettext_lazy("LocationType", "delta"),
    )
    DEPENDENT_POLITICAL_ENTITY = (
        "PCLD",
        pgettext_lazy("LocationType", "dependent political entity"),
    )
    DEPRESSION_S_ = (
        "DPR",
        pgettext_lazy("LocationType", "depression(s)"),
    )
    DESERT = (
        "DSRT",
        pgettext_lazy("LocationType", "desert"),
    )
    DESTROYED_POPULATED_PLACE = (
        "PPLW",
        pgettext_lazy("LocationType", "destroyed populated place"),
    )
    DIATOMITE_MINE_S_ = (
        "MNDT",
        pgettext_lazy("LocationType", "diatomite mine(s)"),
    )
    DIKE = (
        "DIKE",
        pgettext_lazy("LocationType", "dike"),
    )
    DIPLOMATIC_FACILITY = (
        "DIP",
        pgettext_lazy("LocationType", "diplomatic facility"),
    )
    DISPENSARY = (
        "HSPD",
        pgettext_lazy("LocationType", "dispensary"),
    )
    DISTRIBUTARY__IES_ = (
        "STMD",
        pgettext_lazy("LocationType", "distributary(-ies)"),
    )
    DITCH = (
        "DTCH",
        pgettext_lazy("LocationType", "ditch"),
    )
    DITCH_MOUTH_S_ = (
        "DTCHM",
        pgettext_lazy("LocationType", "ditch mouth(s)"),
    )
    DIVIDE = (
        "DVD",
        pgettext_lazy("LocationType", "divide"),
    )
    DOCK_S_ = (
        "DCK",
        pgettext_lazy("LocationType", "dock(s)"),
    )
    DOCKING_BASIN = (
        "DCKB",
        pgettext_lazy("LocationType", "docking basin"),
    )
    DOCKYARD = (
        "DCKY",
        pgettext_lazy("LocationType", "dockyard"),
    )
    DRAINAGE_BASIN = (
        "BSND",
        pgettext_lazy("LocationType", "drainage basin"),
    )
    DRAINAGE_CANAL = (
        "CNLD",
        pgettext_lazy("LocationType", "drainage canal"),
    )
    DRAINAGE_DITCH = (
        "DTCHD",
        pgettext_lazy("LocationType", "drainage ditch"),
    )
    DRY_DOCK = (
        "DCKD",
        pgettext_lazy("LocationType", "dry dock"),
    )
    DRY_STREAM_BED = (
        "SBED",
        pgettext_lazy("LocationType", "dry stream bed"),
    )
    DUNE_S_ = (
        "DUNE",
        pgettext_lazy("LocationType", "dune(s)"),
    )
    ECONOMIC_REGION = (
        "RGNE",
        pgettext_lazy("LocationType", "economic region"),
    )
    ESCARPMENT = (
        "SCRP",
        pgettext_lazy("LocationType", "escarpment"),
    )
    ESTATE_S_ = (
        "EST",
        pgettext_lazy("LocationType", "estate(s)"),
    )
    ESTUARY = (
        "ESTY",
        pgettext_lazy("LocationType", "estuary"),
    )
    EXPERIMENT_STATION = (
        "STNE",
        pgettext_lazy("LocationType", "experiment station"),
    )
    FACILITY = (
        "FCL",
        pgettext_lazy("LocationType", "facility"),
    )
    FACILITY_CENTER = (
        "CTRF",
        pgettext_lazy("LocationType", "facility center"),
    )
    FACTORY = (
        "MFG",
        pgettext_lazy("LocationType", "factory"),
    )
    FAN_S_ = (
        "FAN",
        pgettext_lazy("LocationType", "fan(s)"),
    )
    FARM = (
        "FRM",
        pgettext_lazy("LocationType", "farm"),
    )
    FARM_VILLAGE = (
        "PPLF",
        pgettext_lazy("LocationType", "farm village"),
    )
    FARMS = (
        "FRMS",
        pgettext_lazy("LocationType", "farms"),
    )
    FARMSTEAD = (
        "FRMT",
        pgettext_lazy("LocationType", "farmstead"),
    )
    FERRY = (
        "FY",
        pgettext_lazy("LocationType", "ferry"),
    )
    FERRY_TERMINAL = (
        "FYT",
        pgettext_lazy("LocationType", "ferry terminal"),
    )
    FIELD_S_ = (
        "FLD",
        pgettext_lazy("LocationType", "field(s)"),
    )
    FIRE_STATION = (
        "FIRE",
        pgettext_lazy("LocationType", "fire station"),
    )
    FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM1",
        pgettext_lazy("LocationType", "first-order administrative division"),
    )
    FISHING_AREA = (
        "FISH",
        pgettext_lazy("LocationType", "fishing area"),
    )
    FISHPONDS = (
        "PNDSF",
        pgettext_lazy("LocationType", "fishponds"),
    )
    FISSURE = (
        "FSR",
        pgettext_lazy("LocationType", "fissure"),
    )
    FJORD = (
        "FJD",
        pgettext_lazy("LocationType", "fjord"),
    )
    FJORDS = (
        "FJDS",
        pgettext_lazy("LocationType", "fjords"),
    )
    FORD = (
        "FORD",
        pgettext_lazy("LocationType", "ford"),
    )
    FOREST_RESERVE = (
        "RESF",
        pgettext_lazy("LocationType", "forest reserve"),
    )
    FOREST_STATION = (
        "STNF",
        pgettext_lazy("LocationType", "forest station"),
    )
    FOREST_S_ = (
        "FRST",
        pgettext_lazy("LocationType", "forest(s)"),
    )
    FORMER_INLET = (
        "INLTQ",
        pgettext_lazy("LocationType", "former inlet"),
    )
    FORMER_SUGAR_MILL = (
        "MLSGQ",
        pgettext_lazy("LocationType", "former sugar mill"),
    )
    FORT = (
        "FT",
        pgettext_lazy("LocationType", "fort"),
    )
    FOSSILIZED_FOREST = (
        "FRSTF",
        pgettext_lazy("LocationType", "fossilized forest"),
    )
    FOUNDRY = (
        "FNDY",
        pgettext_lazy("LocationType", "foundry"),
    )
    FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM4",
        pgettext_lazy("LocationType", "fourth-order administrative division"),
    )
    FREE_TRADE_ZONE = (
        "ZNF",
        pgettext_lazy("LocationType", "free trade zone"),
    )
    FREELY_ASSOCIATED_STATE = (
        "PCLF",
        pgettext_lazy("LocationType", "freely associated state"),
    )
    FUEL_DEPOT = (
        "DPOF",
        pgettext_lazy("LocationType", "fuel depot"),
    )
    GAP = (
        "GAP",
        pgettext_lazy("LocationType", "gap"),
    )
    GARDEN_S_ = (
        "GDN",
        pgettext_lazy("LocationType", "garden(s)"),
    )
    GAS_OIL_SEPARATOR_PLANT = (
        "GOSP",
        pgettext_lazy("LocationType", "gas-oil separator plant"),
    )
    GASFIELD = (
        "GASF",
        pgettext_lazy("LocationType", "gasfield"),
    )
    GATE = (
        "GATE",
        pgettext_lazy("LocationType", "gate"),
    )
    GEYSER = (
        "GYSR",
        pgettext_lazy("LocationType", "geyser"),
    )
    GHĀT = (
        "GHAT",
        pgettext_lazy("LocationType", "ghāt"),
    )
    GLACIER_S_ = (
        "GLCR",
        pgettext_lazy("LocationType", "glacier(s)"),
    )
    GOLD_MINE_S_ = (
        "MNAU",
        pgettext_lazy("LocationType", "gold mine(s)"),
    )
    GOLF_COURSE = (
        "RECG",
        pgettext_lazy("LocationType", "golf course"),
    )
    GORGE_S_ = (
        "GRGE",
        pgettext_lazy("LocationType", "gorge(s)"),
    )
    GRASSLAND = (
        "GRSLD",
        pgettext_lazy("LocationType", "grassland"),
    )
    GRAVE = (
        "GRVE",
        pgettext_lazy("LocationType", "grave"),
    )
    GRAVEL_AREA = (
        "GVL",
        pgettext_lazy("LocationType", "gravel area"),
    )
    GRAZING_AREA = (
        "GRAZ",
        pgettext_lazy("LocationType", "grazing area"),
    )
    GUEST_HOUSE = (
        "GHSE",
        pgettext_lazy("LocationType", "guest house"),
    )
    GULF = (
        "GULF",
        pgettext_lazy("LocationType", "gulf"),
    )
    HALTING_PLACE = (
        "HLT",
        pgettext_lazy("LocationType", "halting place"),
    )
    HAMMOCK_S_ = (
        "HMCK",
        pgettext_lazy("LocationType", "hammock(s)"),
    )
    HANGAR = (
        "AIRG",
        pgettext_lazy("LocationType", "hangar"),
    )
    HANGING_VALLEY = (
        "VALG",
        pgettext_lazy("LocationType", "hanging valley"),
    )
    HARBOR_S_ = (
        "HBR",
        pgettext_lazy("LocationType", "harbor(s)"),
    )
    HEADLAND = (
        "HDLD",
        pgettext_lazy("LocationType", "headland"),
    )
    HEADWATERS = (
        "STMH",
        pgettext_lazy("LocationType", "headwaters"),
    )
    HEATH = (
        "HTH",
        pgettext_lazy("LocationType", "heath"),
    )
    HELIPORT = (
        "AIRH",
        pgettext_lazy("LocationType", "heliport"),
    )
    HERMITAGE = (
        "HERM",
        pgettext_lazy("LocationType", "hermitage"),
    )
    HILL = (
        "HLL",
        pgettext_lazy("LocationType", "hill"),
    )
    HILLS = (
        "HLLS",
        pgettext_lazy("LocationType", "hills"),
    )
    HISTORICAL_ADMINISTRATIVE_DIVISION = (
        "ADMDH",
        pgettext_lazy("LocationType", "historical administrative division"),
    )
    HISTORICAL_FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM1H",
        pgettext_lazy(
            "LocationType",
            "historical first-order administrative division",
        ),
    )
    HISTORICAL_FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM4H",
        pgettext_lazy(
            "LocationType",
            "historical fourth-order administrative division",
        ),
    )
    HISTORICAL_POLITICAL_ENTITY = (
        "PCLH",
        pgettext_lazy("LocationType", "historical political entity"),
    )
    HISTORICAL_POPULATED_PLACE = (
        "PPLH",
        pgettext_lazy("LocationType", "historical populated place"),
    )
    HISTORICAL_RAILROAD = (
        "RRH",
        pgettext_lazy("LocationType", "historical railroad"),
    )
    HISTORICAL_RAILROAD_STATION = (
        "RSTNH",
        pgettext_lazy("LocationType", "historical railroad station"),
    )
    HISTORICAL_REGION = (
        "RGNH",
        pgettext_lazy("LocationType", "historical region"),
    )
    HISTORICAL_SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM2H",
        pgettext_lazy(
            "LocationType",
            "historical second-order administrative division",
        ),
    )
    HISTORICAL_SITE = (
        "HSTS",
        pgettext_lazy("LocationType", "historical site"),
    )
    HISTORICAL_THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM3H",
        pgettext_lazy(
            "LocationType",
            "historical third-order administrative division",
        ),
    )
    HISTORICAL_UNDERSEA_FEATURE = (
        "UFHU",
        pgettext_lazy("LocationType", "historical undersea feature"),
    )
    HOMESTEAD = (
        "HMSD",
        pgettext_lazy("LocationType", "homestead"),
    )
    HOSPITAL = (
        "HSP",
        pgettext_lazy("LocationType", "hospital"),
    )
    HOT_SPRING_S_ = (
        "SPNT",
        pgettext_lazy("LocationType", "hot spring(s)"),
    )
    HOTEL = (
        "HTL",
        pgettext_lazy("LocationType", "hotel"),
    )
    HOUSE_S_ = (
        "HSE",
        pgettext_lazy("LocationType", "house(s)"),
    )
    HOUSING_DEVELOPMENT = (
        "DEVH",
        pgettext_lazy("LocationType", "housing development"),
    )
    HUNTING_RESERVE = (
        "RESH",
        pgettext_lazy("LocationType", "hunting reserve"),
    )
    HUT = (
        "HUT",
        pgettext_lazy("LocationType", "hut"),
    )
    HUTS = (
        "HUTS",
        pgettext_lazy("LocationType", "huts"),
    )
    HYDROELECTRIC_POWER_STATION = (
        "PSH",
        pgettext_lazy("LocationType", "hydroelectric power station"),
    )
    ICECAP = (
        "CAPG",
        pgettext_lazy("LocationType", "icecap"),
    )
    ICECAP_DEPRESSION = (
        "DPRG",
        pgettext_lazy("LocationType", "icecap depression"),
    )
    ICECAP_DOME = (
        "DOMG",
        pgettext_lazy("LocationType", "icecap dome"),
    )
    ICECAP_RIDGE = (
        "RDGG",
        pgettext_lazy("LocationType", "icecap ridge"),
    )
    INDEPENDENT_POLITICAL_ENTITY = (
        "PCLI",
        pgettext_lazy("LocationType", "independent political entity"),
    )
    INDUSTRIAL_AREA = (
        "INDS",
        pgettext_lazy("LocationType", "industrial area"),
    )
    INLET = (
        "INLT",
        pgettext_lazy("LocationType", "inlet"),
    )
    INSPECTION_STATION = (
        "STNI",
        pgettext_lazy("LocationType", "inspection station"),
    )
    INTERDUNE_TROUGH_S_ = (
        "TRGD",
        pgettext_lazy("LocationType", "interdune trough(s)"),
    )
    INTERFLUVE = (
        "INTF",
        pgettext_lazy("LocationType", "interfluve"),
    )
    INTERMITTENT_LAKE = (
        "LKI",
        pgettext_lazy("LocationType", "intermittent lake"),
    )
    INTERMITTENT_LAKES = (
        "LKSI",
        pgettext_lazy("LocationType", "intermittent lakes"),
    )
    INTERMITTENT_OXBOW_LAKE = (
        "LKOI",
        pgettext_lazy("LocationType", "intermittent oxbow lake"),
    )
    INTERMITTENT_POND = (
        "PNDI",
        pgettext_lazy("LocationType", "intermittent pond"),
    )
    INTERMITTENT_PONDS = (
        "PNDSI",
        pgettext_lazy("LocationType", "intermittent ponds"),
    )
    INTERMITTENT_POOL = (
        "POOLI",
        pgettext_lazy("LocationType", "intermittent pool"),
    )
    INTERMITTENT_RESERVOIR = (
        "RSVI",
        pgettext_lazy("LocationType", "intermittent reservoir"),
    )
    INTERMITTENT_SALT_LAKE = (
        "LKNI",
        pgettext_lazy("LocationType", "intermittent salt lake"),
    )
    INTERMITTENT_SALT_LAKES = (
        "LKSNI",
        pgettext_lazy("LocationType", "intermittent salt lakes"),
    )
    INTERMITTENT_SALT_POND_S_ = (
        "PNDNI",
        pgettext_lazy("LocationType", "intermittent salt pond(s)"),
    )
    INTERMITTENT_STREAM = (
        "STMI",
        pgettext_lazy("LocationType", "intermittent stream"),
    )
    INTERMITTENT_WETLAND = (
        "WTLDI",
        pgettext_lazy("LocationType", "intermittent wetland"),
    )
    INTERSECTION = (
        "RDIN",
        pgettext_lazy("LocationType", "intersection"),
    )
    IRON_MINE_S_ = (
        "MNFE",
        pgettext_lazy("LocationType", "iron mine(s)"),
    )
    IRRIGATED_FIELD_S_ = (
        "FLDI",
        pgettext_lazy("LocationType", "irrigated field(s)"),
    )
    IRRIGATION_CANAL = (
        "CNLI",
        pgettext_lazy("LocationType", "irrigation canal"),
    )
    IRRIGATION_DITCH = (
        "DTCHI",
        pgettext_lazy("LocationType", "irrigation ditch"),
    )
    IRRIGATION_SYSTEM = (
        "SYSI",
        pgettext_lazy("LocationType", "irrigation system"),
    )
    ISLAND = (
        "ISL",
        pgettext_lazy("LocationType", "island"),
    )
    ISLANDS = (
        "ISLS",
        pgettext_lazy("LocationType", "islands"),
    )
    ISRAELI_SETTLEMENT = (
        "STLMT",
        pgettext_lazy("LocationType", "Israeli settlement"),
    )
    ISTHMUS = (
        "ISTH",
        pgettext_lazy("LocationType", "isthmus"),
    )
    JETTY = (
        "JTY",
        pgettext_lazy("LocationType", "jetty"),
    )
    KARST_AREA = (
        "KRST",
        pgettext_lazy("LocationType", "karst area"),
    )
    LABOR_CAMP = (
        "CMPLA",
        pgettext_lazy("LocationType", "labor camp"),
    )
    LAGOON = (
        "LGN",
        pgettext_lazy("LocationType", "lagoon"),
    )
    LAGOONS = (
        "LGNS",
        pgettext_lazy("LocationType", "lagoons"),
    )
    LAKE = (
        "LK",
        pgettext_lazy("LocationType", "lake"),
    )
    LAKE_BED_S_ = (
        "LBED",
        pgettext_lazy("LocationType", "lake bed(s)"),
    )
    LAKE_CHANNEL_S_ = (
        "CHNL",
        pgettext_lazy("LocationType", "lake channel(s)"),
    )
    LAKE_REGION = (
        "RGNL",
        pgettext_lazy("LocationType", "lake region"),
    )
    LAKES = (
        "LKS",
        pgettext_lazy("LocationType", "lakes"),
    )
    LAND_TIED_ISLAND = (
        "ISLT",
        pgettext_lazy("LocationType", "land-tied island"),
    )
    LANDFILL = (
        "LNDF",
        pgettext_lazy("LocationType", "landfill"),
    )
    LANDING = (
        "LDNG",
        pgettext_lazy("LocationType", "landing"),
    )
    LAVA_AREA = (
        "LAVA",
        pgettext_lazy("LocationType", "lava area"),
    )
    LEAD_MINE_S_ = (
        "MNPB",
        pgettext_lazy("LocationType", "lead mine(s)"),
    )
    LEASED_AREA = (
        "LTER",
        pgettext_lazy("LocationType", "leased area"),
    )
    LEPER_COLONY = (
        "LEPC",
        pgettext_lazy("LocationType", "leper colony"),
    )
    LEPROSARIUM = (
        "HSPL",
        pgettext_lazy("LocationType", "leprosarium"),
    )
    LEVEE = (
        "LEV",
        pgettext_lazy("LocationType", "levee"),
    )
    LIGHTHOUSE = (
        "LTHSE",
        pgettext_lazy("LocationType", "lighthouse"),
    )
    LIMEKILN = (
        "MFGLM",
        pgettext_lazy("LocationType", "limekiln"),
    )
    LOCAL_GOVERNMENT_OFFICE = (
        "GOVL",
        pgettext_lazy("LocationType", "local government office"),
    )
    LOCALITY = (
        "LCTY",
        pgettext_lazy("LocationType", "locality"),
    )
    LOCK_S_ = (
        "LOCK",
        pgettext_lazy("LocationType", "lock(s)"),
    )
    LOGGING_CAMP = (
        "CMPL",
        pgettext_lazy("LocationType", "logging camp"),
    )
    LOST_RIVER = (
        "STMSB",
        pgettext_lazy("LocationType", "lost river"),
    )
    MANEUVER_AREA = (
        "MVA",
        pgettext_lazy("LocationType", "maneuver area"),
    )
    MANGROVE_ISLAND = (
        "ISLM",
        pgettext_lazy("LocationType", "mangrove island"),
    )
    MANGROVE_SWAMP = (
        "MGV",
        pgettext_lazy("LocationType", "mangrove swamp"),
    )
    MARINA = (
        "MAR",
        pgettext_lazy("LocationType", "marina"),
    )
    MARINE_CHANNEL = (
        "CHNM",
        pgettext_lazy("LocationType", "marine channel"),
    )
    MARITIME_SCHOOL = (
        "SCHN",
        pgettext_lazy("LocationType", "maritime school"),
    )
    MARKET = (
        "MKT",
        pgettext_lazy("LocationType", "market"),
    )
    MARSH_ES_ = (
        "MRSH",
        pgettext_lazy("LocationType", "marsh(es)"),
    )
    MEADOW = (
        "MDW",
        pgettext_lazy("LocationType", "meadow"),
    )
    MEANDER_NECK = (
        "NKM",
        pgettext_lazy("LocationType", "meander neck"),
    )
    MEDICAL_CENTER = (
        "CTRM",
        pgettext_lazy("LocationType", "medical center"),
    )
    MESA_S_ = (
        "MESA",
        pgettext_lazy("LocationType", "mesa(s)"),
    )
    METEOROLOGICAL_STATION = (
        "STNM",
        pgettext_lazy("LocationType", "meteorological station"),
    )
    MILITARY_BASE = (
        "MILB",
        pgettext_lazy("LocationType", "military base"),
    )
    MILITARY_INSTALLATION = (
        "INSM",
        pgettext_lazy("LocationType", "military installation"),
    )
    MILITARY_SCHOOL = (
        "SCHM",
        pgettext_lazy("LocationType", "military school"),
    )
    MILL_S_ = (
        "ML",
        pgettext_lazy("LocationType", "mill(s)"),
    )
    MINE_S_ = (
        "MN",
        pgettext_lazy("LocationType", "mine(s)"),
    )
    MINING_AREA = (
        "MNA",
        pgettext_lazy("LocationType", "mining area"),
    )
    MINING_CAMP = (
        "CMPMN",
        pgettext_lazy("LocationType", "mining camp"),
    )
    MISSION = (
        "MSSN",
        pgettext_lazy("LocationType", "mission"),
    )
    MOLE = (
        "MOLE",
        pgettext_lazy("LocationType", "mole"),
    )
    MONASTERY = (
        "MSTY",
        pgettext_lazy("LocationType", "monastery"),
    )
    MONUMENT = (
        "MNMT",
        pgettext_lazy("LocationType", "monument"),
    )
    MOOR_S_ = (
        "MOOR",
        pgettext_lazy("LocationType", "moor(s)"),
    )
    MORAINE = (
        "MRN",
        pgettext_lazy("LocationType", "moraine"),
    )
    MOSQUE = (
        "MSQE",
        pgettext_lazy("LocationType", "mosque"),
    )
    MOUND_S_ = (
        "MND",
        pgettext_lazy("LocationType", "mound(s)"),
    )
    MOUNTAIN = (
        "MT",
        pgettext_lazy("LocationType", "mountain"),
    )
    MOUNTAINS = (
        "MTS",
        pgettext_lazy("LocationType", "mountains"),
    )
    MUD_FLAT_S_ = (
        "FLTM",
        pgettext_lazy("LocationType", "mud flat(s)"),
    )
    MUNITIONS_PLANT = (
        "MFGM",
        pgettext_lazy("LocationType", "munitions plant"),
    )
    MUSEUM = (
        "MUS",
        pgettext_lazy("LocationType", "museum"),
    )
    NARROWS = (
        "NRWS",
        pgettext_lazy("LocationType", "narrows"),
    )
    NATURAL_TUNNEL = (
        "TNLN",
        pgettext_lazy("LocationType", "natural tunnel"),
    )
    NATURE_RESERVE = (
        "RESN",
        pgettext_lazy("LocationType", "nature reserve"),
    )
    NAVAL_BASE = (
        "NVB",
        pgettext_lazy("LocationType", "naval base"),
    )
    NAVIGATION_CANAL_S_ = (
        "CNLN",
        pgettext_lazy("LocationType", "navigation canal(s)"),
    )
    NAVIGATION_CHANNEL = (
        "CHNN",
        pgettext_lazy("LocationType", "navigation channel"),
    )
    NICKEL_MINE_S_ = (
        "MNNI",
        pgettext_lazy("LocationType", "nickel mine(s)"),
    )
    NOVITIATE = (
        "NOV",
        pgettext_lazy("LocationType", "novitiate"),
    )
    NUCLEAR_POWER_STATION = (
        "PSN",
        pgettext_lazy("LocationType", "nuclear power station"),
    )
    NUNATAK = (
        "NTK",
        pgettext_lazy("LocationType", "nunatak"),
    )
    NUNATAKS = (
        "NTKS",
        pgettext_lazy("LocationType", "nunataks"),
    )
    NURSERY__IES_ = (
        "NSY",
        pgettext_lazy("LocationType", "nursery(-ies)"),
    )
    OASIS__ES_ = (
        "OAS",
        pgettext_lazy("LocationType", "oasis(-es)"),
    )
    OBSERVATION_POINT = (
        "OBPT",
        pgettext_lazy("LocationType", "observation point"),
    )
    OBSERVATORY = (
        "OBS",
        pgettext_lazy("LocationType", "observatory"),
    )
    OCEAN = (
        "OCN",
        pgettext_lazy("LocationType", "ocean"),
    )
    OFFICE_BUILDING = (
        "BLDO",
        pgettext_lazy("LocationType", "office building"),
    )
    OIL_CAMP = (
        "CMPO",
        pgettext_lazy("LocationType", "oil camp"),
    )
    OIL_PALM_PLANTATION = (
        "ESTO",
        pgettext_lazy("LocationType", "oil palm plantation"),
    )
    OIL_PIPELINE = (
        "OILP",
        pgettext_lazy("LocationType", "oil pipeline"),
    )
    OIL_PIPELINE_JUNCTION = (
        "OILJ",
        pgettext_lazy("LocationType", "oil pipeline junction"),
    )
    OIL_PIPELINE_TERMINAL = (
        "TRMO",
        pgettext_lazy("LocationType", "oil pipeline terminal"),
    )
    OIL_PUMPING_STATION = (
        "PMPO",
        pgettext_lazy("LocationType", "oil pumping station"),
    )
    OIL_REFINERY = (
        "OILR",
        pgettext_lazy("LocationType", "oil refinery"),
    )
    OIL_WELL = (
        "OILW",
        pgettext_lazy("LocationType", "oil well"),
    )
    OILFIELD = (
        "OILF",
        pgettext_lazy("LocationType", "oilfield"),
    )
    OLIVE_GROVE = (
        "GRVO",
        pgettext_lazy("LocationType", "olive grove"),
    )
    OLIVE_OIL_MILL = (
        "MLO",
        pgettext_lazy("LocationType", "olive oil mill"),
    )
    ORCHARD_S_ = (
        "OCH",
        pgettext_lazy("LocationType", "orchard(s)"),
    )
    ORE_TREATMENT_PLANT = (
        "MLM",
        pgettext_lazy("LocationType", "ore treatment plant"),
    )
    OVERFALLS = (
        "OVF",
        pgettext_lazy("LocationType", "overfalls"),
    )
    OXBOW_LAKE = (
        "LKO",
        pgettext_lazy("LocationType", "oxbow lake"),
    )
    PAGODA = (
        "PGDA",
        pgettext_lazy("LocationType", "pagoda"),
    )
    PALACE = (
        "PAL",
        pgettext_lazy("LocationType", "palace"),
    )
    PALM_GROVE = (
        "GRVP",
        pgettext_lazy("LocationType", "palm grove"),
    )
    PALM_TREE_RESERVE = (
        "RESP",
        pgettext_lazy("LocationType", "palm tree reserve"),
    )
    PAN = (
        "PAN",
        pgettext_lazy("LocationType", "pan"),
    )
    PANS = (
        "PANS",
        pgettext_lazy("LocationType", "pans"),
    )
    PARISH = (
        "PRSH",
        pgettext_lazy("LocationType", "parish"),
    )
    PARK = (
        "PRK",
        pgettext_lazy("LocationType", "park"),
    )
    PARK_GATE = (
        "PRKGT",
        pgettext_lazy("LocationType", "park gate"),
    )
    PARK_HEADQUARTERS = (
        "PRKHQ",
        pgettext_lazy("LocationType", "park headquarters"),
    )
    PARKING_GARAGE = (
        "GARG",
        pgettext_lazy("LocationType", "parking garage"),
    )
    PARKING_LOT = (
        "PKLT",
        pgettext_lazy("LocationType", "parking lot"),
    )
    PASS = (
        "PASS",
        pgettext_lazy("LocationType", "pass"),
    )
    PATROL_POST = (
        "PSTP",
        pgettext_lazy("LocationType", "patrol post"),
    )
    PEAK = (
        "PK",
        pgettext_lazy("LocationType", "peak"),
    )
    PEAKS = (
        "PKS",
        pgettext_lazy("LocationType", "peaks"),
    )
    PEAT_CUTTING_AREA = (
        "PEAT",
        pgettext_lazy("LocationType", "peat cutting area"),
    )
    PENINSULA = (
        "PEN",
        pgettext_lazy("LocationType", "peninsula"),
    )
    PETROLEUM_BASIN = (
        "BSNP",
        pgettext_lazy("LocationType", "petroleum basin"),
    )
    PHOSPHATE_WORKS = (
        "MFGPH",
        pgettext_lazy("LocationType", "phosphate works"),
    )
    PIER = (
        "PIER",
        pgettext_lazy("LocationType", "pier"),
    )
    PINE_GROVE = (
        "GRVPN",
        pgettext_lazy("LocationType", "pine grove"),
    )
    PLACER_MINE_S_ = (
        "MNPL",
        pgettext_lazy("LocationType", "placer mine(s)"),
    )
    PLAIN_S_ = (
        "PLN",
        pgettext_lazy("LocationType", "plain(s)"),
    )
    PLATEAU = (
        "PLAT",
        pgettext_lazy("LocationType", "plateau"),
    )
    POINT = (
        "PT",
        pgettext_lazy("LocationType", "point"),
    )
    POINTS = (
        "PTS",
        pgettext_lazy("LocationType", "points"),
    )
    POLDER = (
        "PLDR",
        pgettext_lazy("LocationType", "polder"),
    )
    POLICE_POST = (
        "PP",
        pgettext_lazy("LocationType", "police post"),
    )
    POLITICAL_ENTITY = (
        "PCL",
        pgettext_lazy("LocationType", "political entity"),
    )
    POND = (
        "PND",
        pgettext_lazy("LocationType", "pond"),
    )
    PONDS = (
        "PNDS",
        pgettext_lazy("LocationType", "ponds"),
    )
    POOL_S_ = (
        "POOL",
        pgettext_lazy("LocationType", "pool(s)"),
    )
    POPULATED_LOCALITY = (
        "PPLL",
        pgettext_lazy("LocationType", "populated locality"),
    )
    POPULATED_PLACE = (
        "PPL",
        pgettext_lazy("LocationType", "populated place"),
    )
    POPULATED_PLACES = (
        "PPLS",
        pgettext_lazy("LocationType", "populated places"),
    )
    PORT = (
        "PRT",
        pgettext_lazy("LocationType", "port"),
    )
    PORTAGE = (
        "PTGE",
        pgettext_lazy("LocationType", "portage"),
    )
    POST_OFFICE = (
        "PO",
        pgettext_lazy("LocationType", "post office"),
    )
    POWER_STATION = (
        "PS",
        pgettext_lazy("LocationType", "power station"),
    )
    PRISON = (
        "PRN",
        pgettext_lazy("LocationType", "prison"),
    )
    PROMENADE = (
        "PRMN",
        pgettext_lazy("LocationType", "promenade"),
    )
    PROMONTORY__IES_ = (
        "PROM",
        pgettext_lazy("LocationType", "promontory(-ies)"),
    )
    PYRAMID = (
        "PYR",
        pgettext_lazy("LocationType", "pyramid"),
    )
    PYRAMIDS = (
        "PYRS",
        pgettext_lazy("LocationType", "pyramids"),
    )
    QUARRY__IES_ = (
        "MNQR",
        pgettext_lazy("LocationType", "quarry(-ies)"),
    )
    QUAY = (
        "QUAY",
        pgettext_lazy("LocationType", "quay"),
    )
    QUICKSAND = (
        "QCKS",
        pgettext_lazy("LocationType", "quicksand"),
    )
    RACETRACK = (
        "RECR",
        pgettext_lazy("LocationType", "racetrack"),
    )
    RADIO_OBSERVATORY = (
        "OBSR",
        pgettext_lazy("LocationType", "radio observatory"),
    )
    RADIO_STATION = (
        "STNR",
        pgettext_lazy("LocationType", "radio station"),
    )
    RAILROAD = (
        "RR",
        pgettext_lazy("LocationType", "railroad"),
    )
    RAILROAD_JUNCTION = (
        "RJCT",
        pgettext_lazy("LocationType", "railroad junction"),
    )
    RAILROAD_SIDING = (
        "RSD",
        pgettext_lazy("LocationType", "railroad siding"),
    )
    RAILROAD_SIGNAL = (
        "RSGNL",
        pgettext_lazy("LocationType", "railroad signal"),
    )
    RAILROAD_STATION = (
        "RSTN",
        pgettext_lazy("LocationType", "railroad station"),
    )
    RAILROAD_STOP = (
        "RSTP",
        pgettext_lazy("LocationType", "railroad stop"),
    )
    RAILROAD_TUNNEL = (
        "TNLRR",
        pgettext_lazy("LocationType", "railroad tunnel"),
    )
    RAILROAD_YARD = (
        "RYD",
        pgettext_lazy("LocationType", "railroad yard"),
    )
    RANCH_ES_ = (
        "RNCH",
        pgettext_lazy("LocationType", "ranch(es)"),
    )
    RAPIDS = (
        "RPDS",
        pgettext_lazy("LocationType", "rapids"),
    )
    RAVINE_S_ = (
        "RVN",
        pgettext_lazy("LocationType", "ravine(s)"),
    )
    REACH = (
        "RCH",
        pgettext_lazy("LocationType", "reach"),
    )
    REEF_S_ = (
        "RF",
        pgettext_lazy("LocationType", "reef(s)"),
    )
    REFORMATORY = (
        "PRNJ",
        pgettext_lazy("LocationType", "reformatory"),
    )
    REFUGEE_CAMP = (
        "CMPRF",
        pgettext_lazy("LocationType", "refugee camp"),
    )
    REGION = (
        "RGN",
        pgettext_lazy("LocationType", "region"),
    )
    RELIGIOUS_CENTER = (
        "CTRR",
        pgettext_lazy("LocationType", "religious center"),
    )
    RELIGIOUS_POPULATED_PLACE = (
        "PPLR",
        pgettext_lazy("LocationType", "religious populated place"),
    )
    RELIGIOUS_SITE = (
        "RLG",
        pgettext_lazy("LocationType", "religious site"),
    )
    RESEARCH_INSTITUTE = (
        "ITTR",
        pgettext_lazy("LocationType", "research institute"),
    )
    RESERVATION = (
        "RESV",
        pgettext_lazy("LocationType", "reservation"),
    )
    RESERVE = (
        "RES",
        pgettext_lazy("LocationType", "reserve"),
    )
    RESERVOIR_S_ = (
        "RSV",
        pgettext_lazy("LocationType", "reservoir(s)"),
    )
    RESORT = (
        "RSRT",
        pgettext_lazy("LocationType", "resort"),
    )
    RESTHOUSE = (
        "RHSE",
        pgettext_lazy("LocationType", "resthouse"),
    )
    RETREAT = (
        "RLGR",
        pgettext_lazy("LocationType", "retreat"),
    )
    RIDGE_S_ = (
        "RDGE",
        pgettext_lazy("LocationType", "ridge(s)"),
    )
    ROAD = (
        "RD",
        pgettext_lazy("LocationType", "road"),
    )
    ROAD_BEND = (
        "RDB",
        pgettext_lazy("LocationType", "road bend"),
    )
    ROAD_CUT = (
        "RDCUT",
        pgettext_lazy("LocationType", "road cut"),
    )
    ROAD_JUNCTION = (
        "RDJCT",
        pgettext_lazy("LocationType", "road junction"),
    )
    ROAD_TUNNEL = (
        "TNLRD",
        pgettext_lazy("LocationType", "road tunnel"),
    )
    ROADSTEAD = (
        "RDST",
        pgettext_lazy("LocationType", "roadstead"),
    )
    ROCK = (
        "RK",
        pgettext_lazy("LocationType", "rock"),
    )
    ROCK_DESERT = (
        "HMDA",
        pgettext_lazy("LocationType", "rock desert"),
    )
    ROCKFALL = (
        "RKFL",
        pgettext_lazy("LocationType", "rockfall"),
    )
    ROCKS = (
        "RKS",
        pgettext_lazy("LocationType", "rocks"),
    )
    ROOKERY = (
        "RKRY",
        pgettext_lazy("LocationType", "rookery"),
    )
    RUBBER_PLANTATION = (
        "ESTR",
        pgettext_lazy("LocationType", "rubber plantation"),
    )
    RUIN_S_ = (
        "RUIN",
        pgettext_lazy("LocationType", "ruin(s)"),
    )
    RUINED_BRIDGE = (
        "BDGQ",
        pgettext_lazy("LocationType", "ruined bridge"),
    )
    RUINED_DAM = (
        "DAMQ",
        pgettext_lazy("LocationType", "ruined dam"),
    )
    SABKHA_S_ = (
        "SBKH",
        pgettext_lazy("LocationType", "sabkha(s)"),
    )
    SADDLE = (
        "SDL",
        pgettext_lazy("LocationType", "saddle"),
    )
    SALT_AREA = (
        "SALT",
        pgettext_lazy("LocationType", "salt area"),
    )
    SALT_EVAPORATION_PONDS = (
        "MFGN",
        pgettext_lazy("LocationType", "salt evaporation ponds"),
    )
    SALT_LAKE = (
        "LKN",
        pgettext_lazy("LocationType", "salt lake"),
    )
    SALT_LAKES = (
        "LKSN",
        pgettext_lazy("LocationType", "salt lakes"),
    )
    SALT_MARSH = (
        "MRSHN",
        pgettext_lazy("LocationType", "salt marsh"),
    )
    SALT_MINE_S_ = (
        "MNN",
        pgettext_lazy("LocationType", "salt mine(s)"),
    )
    SALT_POND = (
        "PNDN",
        pgettext_lazy("LocationType", "salt pond"),
    )
    SALT_PONDS = (
        "PNDSN",
        pgettext_lazy("LocationType", "salt ponds"),
    )
    SANATORIUM = (
        "SNTR",
        pgettext_lazy("LocationType", "sanatorium"),
    )
    SAND_AREA = (
        "SAND",
        pgettext_lazy("LocationType", "sand area"),
    )
    SANDY_DESERT = (
        "ERG",
        pgettext_lazy("LocationType", "sandy desert"),
    )
    SATELLITE_STATION = (
        "STNS",
        pgettext_lazy("LocationType", "satellite station"),
    )
    SAWMILL = (
        "MLSW",
        pgettext_lazy("LocationType", "sawmill"),
    )
    SCHOOL = (
        "SCH",
        pgettext_lazy("LocationType", "school"),
    )
    SCHOOL_DISTRICT = (
        "ADMS",
        pgettext_lazy("LocationType", "school district"),
    )
    SCIENTIFIC_RESEARCH_BASE = (
        "STNB",
        pgettext_lazy("LocationType", "scientific research base"),
    )
    SCRUBLAND = (
        "SCRB",
        pgettext_lazy("LocationType", "scrubland"),
    )
    SEA = (
        "SEA",
        pgettext_lazy("LocationType", "sea"),
    )
    SEACHANNEL = (
        "SCNU",
        pgettext_lazy("LocationType", "seachannel"),
    )
    SEACHANNELS = (
        "SCSU",
        pgettext_lazy("LocationType", "seachannels"),
    )
    SEAMOUNT = (
        "SMU",
        pgettext_lazy("LocationType", "seamount"),
    )
    SEAMOUNTS = (
        "SMSU",
        pgettext_lazy("LocationType", "seamounts"),
    )
    SEAPLANE_LANDING_AREA = (
        "AIRS",
        pgettext_lazy("LocationType", "seaplane landing area"),
    )
    SEAT_OF_A_FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA",
        pgettext_lazy(
            "LocationType",
            "seat of a first-order administrative division",
        ),
    )
    SEAT_OF_A_FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA4",
        pgettext_lazy(
            "LocationType",
            "seat of a fourth-order administrative division",
        ),
    )
    SEAT_OF_A_SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA2",
        pgettext_lazy(
            "LocationType",
            "seat of a second-order administrative division",
        ),
    )
    SEAT_OF_A_THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA3",
        pgettext_lazy(
            "LocationType",
            "seat of a third-order administrative division",
        ),
    )
    SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM2",
        pgettext_lazy("LocationType", "second-order administrative division"),
    )
    SECTION_OF_BANK = (
        "BNKX",
        pgettext_lazy("LocationType", "section of bank"),
    )
    SECTION_OF_CANAL = (
        "CNLX",
        pgettext_lazy("LocationType", "section of canal"),
    )
    SECTION_OF_ESTATE = (
        "ESTX",
        pgettext_lazy("LocationType", "section of estate"),
    )
    SECTION_OF_HARBOR = (
        "HBRX",
        pgettext_lazy("LocationType", "section of harbor"),
    )
    SECTION_OF_INDEPENDENT_POLITICAL_ENTITY = (
        "PCLIX",
        pgettext_lazy("LocationType", "section of independent political entity"),
    )
    SECTION_OF_INTERMITTENT_STREAM = (
        "STMIX",
        pgettext_lazy("LocationType", "section of intermittent stream"),
    )
    SECTION_OF_ISLAND = (
        "ISLX",
        pgettext_lazy("LocationType", "section of island"),
    )
    SECTION_OF_LAGOON = (
        "LGNX",
        pgettext_lazy("LocationType", "section of lagoon"),
    )
    SECTION_OF_LAKE = (
        "LKX",
        pgettext_lazy("LocationType", "section of lake"),
    )
    SECTION_OF_PENINSULA = (
        "PENX",
        pgettext_lazy("LocationType", "section of peninsula"),
    )
    SECTION_OF_PLAIN = (
        "PLNX",
        pgettext_lazy("LocationType", "section of plain"),
    )
    SECTION_OF_PLATEAU = (
        "PLATX",
        pgettext_lazy("LocationType", "section of plateau"),
    )
    SECTION_OF_POPULATED_PLACE = (
        "PPLX",
        pgettext_lazy("LocationType", "section of populated place"),
    )
    SECTION_OF_REEF = (
        "RFX",
        pgettext_lazy("LocationType", "section of reef"),
    )
    SECTION_OF_STREAM = (
        "STMX",
        pgettext_lazy("LocationType", "section of stream"),
    )
    SECTION_OF_VALLEY = (
        "VALX",
        pgettext_lazy("LocationType", "section of valley"),
    )
    SECTION_OF_WADI = (
        "WADX",
        pgettext_lazy("LocationType", "section of wadi"),
    )
    SECTION_OF_WATERFALL_S_ = (
        "FLLSX",
        pgettext_lazy("LocationType", "section of waterfall(s)"),
    )
    SEMI_INDEPENDENT_POLITICAL_ENTITY = (
        "PCLS",
        pgettext_lazy("LocationType", "semi-independent political entity"),
    )
    SEWAGE_TREATMENT_PLANT = (
        "SWT",
        pgettext_lazy("LocationType", "sewage treatment plant"),
    )
    SHEEPFOLD = (
        "SHPF",
        pgettext_lazy("LocationType", "sheepfold"),
    )
    SHOAL_S_ = (
        "SHOL",
        pgettext_lazy("LocationType", "shoal(s)"),
    )
    SHOPPING_CENTER_OR_MALL = (
        "SHOPC",
        pgettext_lazy("LocationType", "shopping center or mall"),
    )
    SHORE = (
        "SHOR",
        pgettext_lazy("LocationType", "shore"),
    )
    SHRINE = (
        "SHRN",
        pgettext_lazy("LocationType", "shrine"),
    )
    SILL = (
        "SILL",
        pgettext_lazy("LocationType", "sill"),
    )
    SINKHOLE = (
        "SINK",
        pgettext_lazy("LocationType", "sinkhole"),
    )
    SISAL_PLANTATION = (
        "ESTSL",
        pgettext_lazy("LocationType", "sisal plantation"),
    )
    SLIDE = (
        "SLID",
        pgettext_lazy("LocationType", "slide"),
    )
    SLOPE_S_ = (
        "SLP",
        pgettext_lazy("LocationType", "slope(s)"),
    )
    SLUICE = (
        "SLCE",
        pgettext_lazy("LocationType", "sluice"),
    )
    SNOWFIELD = (
        "SNOW",
        pgettext_lazy("LocationType", "snowfield"),
    )
    SOUND = (
        "SD",
        pgettext_lazy("LocationType", "sound"),
    )
    SPA = (
        "SPA",
        pgettext_lazy("LocationType", "spa"),
    )
    SPACE_CENTER = (
        "CTRS",
        pgettext_lazy("LocationType", "space center"),
    )
    SPILLWAY = (
        "SPLY",
        pgettext_lazy("LocationType", "spillway"),
    )
    SPIT = (
        "SPIT",
        pgettext_lazy("LocationType", "spit"),
    )
    SPRING_S_ = (
        "SPNG",
        pgettext_lazy("LocationType", "spring(s)"),
    )
    SPUR_S_ = (
        "SPUR",
        pgettext_lazy("LocationType", "spur(s)"),
    )
    SQUARE = (
        "SQR",
        pgettext_lazy("LocationType", "square"),
    )
    STABLE = (
        "STBL",
        pgettext_lazy("LocationType", "stable"),
    )
    STADIUM = (
        "STDM",
        pgettext_lazy("LocationType", "stadium"),
    )
    STEPS = (
        "STPS",
        pgettext_lazy("LocationType", "steps"),
    )
    STOCK_ROUTE = (
        "STKR",
        pgettext_lazy("LocationType", "stock route"),
    )
    STONY_DESERT = (
        "REG",
        pgettext_lazy("LocationType", "stony desert"),
    )
    STORE = (
        "RET",
        pgettext_lazy("LocationType", "store"),
    )
    STOREHOUSE = (
        "SHSE",
        pgettext_lazy("LocationType", "storehouse"),
    )
    STRAIT = (
        "STRT",
        pgettext_lazy("LocationType", "strait"),
    )
    STREAM = (
        "STM",
        pgettext_lazy("LocationType", "stream"),
    )
    STREAM_BANK = (
        "BNKR",
        pgettext_lazy("LocationType", "stream bank"),
    )
    STREAM_BEND = (
        "STMB",
        pgettext_lazy("LocationType", "stream bend"),
    )
    STREAM_GAUGING_STATION = (
        "STMGS",
        pgettext_lazy("LocationType", "stream gauging station"),
    )
    STREAM_MOUTH_S_ = (
        "STMM",
        pgettext_lazy("LocationType", "stream mouth(s)"),
    )
    STREAMS = (
        "STMS",
        pgettext_lazy("LocationType", "streams"),
    )
    STREET = (
        "ST",
        pgettext_lazy("LocationType", "street"),
    )
    SUB_SURFACE_DAM = (
        "DAMSB",
        pgettext_lazy("LocationType", "sub-surface dam"),
    )
    SUBWAY = (
        "SUBW",
        pgettext_lazy("LocationType", "subway"),
    )
    SUBWAY_STATION = (
        "SUBS",
        pgettext_lazy("LocationType", "subway station"),
    )
    SUGAR_MILL = (
        "MLSG",
        pgettext_lazy("LocationType", "sugar mill"),
    )
    SUGAR_PLANTATION = (
        "ESTSG",
        pgettext_lazy("LocationType", "sugar plantation"),
    )
    SUGAR_REFINERY = (
        "MFGSG",
        pgettext_lazy("LocationType", "sugar refinery"),
    )
    SULPHUR_SPRING_S_ = (
        "SPNS",
        pgettext_lazy("LocationType", "sulphur spring(s)"),
    )
    SWAMP = (
        "SWMP",
        pgettext_lazy("LocationType", "swamp"),
    )
    SYNAGOGUE = (
        "SYG",
        pgettext_lazy("LocationType", "synagogue"),
    )
    TABLEMOUNT__OR_GUYOT_ = (
        "TMTU",
        pgettext_lazy("LocationType", "tablemount (or guyot)"),
    )
    TABLEMOUNTS__OR_GUYOTS_ = (
        "TMSU",
        pgettext_lazy("LocationType", "tablemounts (or guyots)"),
    )
    TALUS_SLOPE = (
        "TAL",
        pgettext_lazy("LocationType", "talus slope"),
    )
    TANK_FARM = (
        "OILT",
        pgettext_lazy("LocationType", "tank farm"),
    )
    TEA_PLANTATION = (
        "ESTT",
        pgettext_lazy("LocationType", "tea plantation"),
    )
    TECHNICAL_SCHOOL = (
        "SCHT",
        pgettext_lazy("LocationType", "technical school"),
    )
    TEMPLE_S_ = (
        "TMPL",
        pgettext_lazy("LocationType", "temple(s)"),
    )
    TERMINAL = (
        "AIRT",
        pgettext_lazy("LocationType", "terminal"),
    )
    TERRACE = (
        "TRR",
        pgettext_lazy("LocationType", "terrace"),
    )
    TERRITORY = (
        "TERR",
        pgettext_lazy("LocationType", "territory"),
    )
    THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM3",
        pgettext_lazy("LocationType", "third-order administrative division"),
    )
    TIDAL_CREEK_S_ = (
        "CRKT",
        pgettext_lazy("LocationType", "tidal creek(s)"),
    )
    TIDAL_FLAT_S_ = (
        "FLTT",
        pgettext_lazy("LocationType", "tidal flat(s)"),
    )
    TIN_MINE_S_ = (
        "MNSN",
        pgettext_lazy("LocationType", "tin mine(s)"),
    )
    TOLL_GATE_BARRIER = (
        "TOLL",
        pgettext_lazy("LocationType", "toll gate/barrier"),
    )
    TOMB_S_ = (
        "TMB",
        pgettext_lazy("LocationType", "tomb(s)"),
    )
    TOWER = (
        "TOWR",
        pgettext_lazy("LocationType", "tower"),
    )
    TRAFFIC_CIRCLE = (
        "RDCR",
        pgettext_lazy("LocationType", "traffic circle"),
    )
    TRAIL = (
        "TRL",
        pgettext_lazy("LocationType", "trail"),
    )
    TRANSIT_TERMINAL = (
        "TRANT",
        pgettext_lazy("LocationType", "transit terminal"),
    )
    TREE_S_ = (
        "TREE",
        pgettext_lazy("LocationType", "tree(s)"),
    )
    TRIANGULATION_STATION = (
        "TRIG",
        pgettext_lazy("LocationType", "triangulation station"),
    )
    TRIBAL_AREA = (
        "TRB",
        pgettext_lazy("LocationType", "tribal area"),
    )
    TUNDRA = (
        "TUND",
        pgettext_lazy("LocationType", "tundra"),
    )
    TUNNEL = (
        "TNL",
        pgettext_lazy("LocationType", "tunnel"),
    )
    TUNNELS = (
        "TNLS",
        pgettext_lazy("LocationType", "tunnels"),
    )
    UNDERGROUND_IRRIGATION_CANAL_S_ = (
        "CNLSB",
        pgettext_lazy("LocationType", "underground irrigation canal(s)"),
    )
    UNDERGROUND_LAKE = (
        "LKSB",
        pgettext_lazy("LocationType", "underground lake"),
    )
    UNDERSEA_APRON = (
        "APNU",
        pgettext_lazy("LocationType", "undersea apron"),
    )
    UNDERSEA_ARCH = (
        "ARCU",
        pgettext_lazy("LocationType", "undersea arch"),
    )
    UNDERSEA_ARRUGADO = (
        "ARRU",
        pgettext_lazy("LocationType", "undersea arrugado"),
    )
    UNDERSEA_BANK = (
        "BNKU",
        pgettext_lazy("LocationType", "undersea bank"),
    )
    UNDERSEA_BANKS = (
        "BKSU",
        pgettext_lazy("LocationType", "undersea banks"),
    )
    UNDERSEA_BASIN = (
        "BSNU",
        pgettext_lazy("LocationType", "undersea basin"),
    )
    UNDERSEA_BENCH = (
        "BNCU",
        pgettext_lazy("LocationType", "undersea bench"),
    )
    UNDERSEA_BORDERLAND = (
        "BDLU",
        pgettext_lazy("LocationType", "undersea borderland"),
    )
    UNDERSEA_CANYON = (
        "CNYU",
        pgettext_lazy("LocationType", "undersea canyon"),
    )
    UNDERSEA_CANYONS = (
        "CNSU",
        pgettext_lazy("LocationType", "undersea canyons"),
    )
    UNDERSEA_CORDILLERA = (
        "CDAU",
        pgettext_lazy("LocationType", "undersea cordillera"),
    )
    UNDERSEA_ESCARPMENT__OR_SCARP_ = (
        "ESCU",
        pgettext_lazy("LocationType", "undersea escarpment (or scarp)"),
    )
    UNDERSEA_FAN = (
        "FANU",
        pgettext_lazy("LocationType", "undersea fan"),
    )
    UNDERSEA_FLAT = (
        "FLTU",
        pgettext_lazy("LocationType", "undersea flat"),
    )
    UNDERSEA_FORK = (
        "FRKU",
        pgettext_lazy("LocationType", "undersea fork"),
    )
    UNDERSEA_FORKS = (
        "FRSU",
        pgettext_lazy("LocationType", "undersea forks"),
    )
    UNDERSEA_FRACTURE_ZONE = (
        "FRZU",
        pgettext_lazy("LocationType", "undersea fracture zone"),
    )
    UNDERSEA_FURROW = (
        "FURU",
        pgettext_lazy("LocationType", "undersea furrow"),
    )
    UNDERSEA_GAP = (
        "GAPU",
        pgettext_lazy("LocationType", "undersea gap"),
    )
    UNDERSEA_GULLY = (
        "GLYU",
        pgettext_lazy("LocationType", "undersea gully"),
    )
    UNDERSEA_HILL = (
        "HLLU",
        pgettext_lazy("LocationType", "undersea hill"),
    )
    UNDERSEA_HILLS = (
        "HLSU",
        pgettext_lazy("LocationType", "undersea hills"),
    )
    UNDERSEA_HOLE = (
        "HOLU",
        pgettext_lazy("LocationType", "undersea hole"),
    )
    UNDERSEA_KNOLL = (
        "KNLU",
        pgettext_lazy("LocationType", "undersea knoll"),
    )
    UNDERSEA_KNOLLS = (
        "KNSU",
        pgettext_lazy("LocationType", "undersea knolls"),
    )
    UNDERSEA_LEDGE = (
        "LDGU",
        pgettext_lazy("LocationType", "undersea ledge"),
    )
    UNDERSEA_LEVEE = (
        "LEVU",
        pgettext_lazy("LocationType", "undersea levee"),
    )
    UNDERSEA_MEDIAN_VALLEY = (
        "MDVU",
        pgettext_lazy("LocationType", "undersea median valley"),
    )
    UNDERSEA_MESA = (
        "MESU",
        pgettext_lazy("LocationType", "undersea mesa"),
    )
    UNDERSEA_MOAT = (
        "MOTU",
        pgettext_lazy("LocationType", "undersea moat"),
    )
    UNDERSEA_MOUND = (
        "MNDU",
        pgettext_lazy("LocationType", "undersea mound"),
    )
    UNDERSEA_MOUNTAIN = (
        "MTU",
        pgettext_lazy("LocationType", "undersea mountain"),
    )
    UNDERSEA_MOUNTAINS = (
        "MTSU",
        pgettext_lazy("LocationType", "undersea mountains"),
    )
    UNDERSEA_PEAK = (
        "PKU",
        pgettext_lazy("LocationType", "undersea peak"),
    )
    UNDERSEA_PEAKS = (
        "PKSU",
        pgettext_lazy("LocationType", "undersea peaks"),
    )
    UNDERSEA_PINNACLE = (
        "PNLU",
        pgettext_lazy("LocationType", "undersea pinnacle"),
    )
    UNDERSEA_PLAIN = (
        "PLNU",
        pgettext_lazy("LocationType", "undersea plain"),
    )
    UNDERSEA_PLATEAU = (
        "PLTU",
        pgettext_lazy("LocationType", "undersea plateau"),
    )
    UNDERSEA_PLATFORM = (
        "PLFU",
        pgettext_lazy("LocationType", "undersea platform"),
    )
    UNDERSEA_PROVINCE = (
        "PRVU",
        pgettext_lazy("LocationType", "undersea province"),
    )
    UNDERSEA_RAMP = (
        "RMPU",
        pgettext_lazy("LocationType", "undersea ramp"),
    )
    UNDERSEA_RANGE = (
        "RNGU",
        pgettext_lazy("LocationType", "undersea range"),
    )
    UNDERSEA_RAVINE = (
        "RAVU",
        pgettext_lazy("LocationType", "undersea ravine"),
    )
    UNDERSEA_REEF = (
        "RFU",
        pgettext_lazy("LocationType", "undersea reef"),
    )
    UNDERSEA_REEFS = (
        "RFSU",
        pgettext_lazy("LocationType", "undersea reefs"),
    )
    UNDERSEA_RIDGE = (
        "RDGU",
        pgettext_lazy("LocationType", "undersea ridge"),
    )
    UNDERSEA_RIDGES = (
        "RDSU",
        pgettext_lazy("LocationType", "undersea ridges"),
    )
    UNDERSEA_RISE = (
        "RISU",
        pgettext_lazy("LocationType", "undersea rise"),
    )
    UNDERSEA_SADDLE = (
        "SDLU",
        pgettext_lazy("LocationType", "undersea saddle"),
    )
    UNDERSEA_SHELF = (
        "SHFU",
        pgettext_lazy("LocationType", "undersea shelf"),
    )
    UNDERSEA_SHELF_EDGE = (
        "EDGU",
        pgettext_lazy("LocationType", "undersea shelf edge"),
    )
    UNDERSEA_SHELF_VALLEY = (
        "SHVU",
        pgettext_lazy("LocationType", "undersea shelf valley"),
    )
    UNDERSEA_SHOAL = (
        "SHLU",
        pgettext_lazy("LocationType", "undersea shoal"),
    )
    UNDERSEA_SHOALS = (
        "SHSU",
        pgettext_lazy("LocationType", "undersea shoals"),
    )
    UNDERSEA_SILL = (
        "SILU",
        pgettext_lazy("LocationType", "undersea sill"),
    )
    UNDERSEA_SLOPE = (
        "SLPU",
        pgettext_lazy("LocationType", "undersea slope"),
    )
    UNDERSEA_SPUR = (
        "SPRU",
        pgettext_lazy("LocationType", "undersea spur"),
    )
    UNDERSEA_TERRACE = (
        "TERU",
        pgettext_lazy("LocationType", "undersea terrace"),
    )
    UNDERSEA_TONGUE = (
        "TNGU",
        pgettext_lazy("LocationType", "undersea tongue"),
    )
    UNDERSEA_TRENCH = (
        "TRNU",
        pgettext_lazy("LocationType", "undersea trench"),
    )
    UNDERSEA_TROUGH = (
        "TRGU",
        pgettext_lazy("LocationType", "undersea trough"),
    )
    UNDERSEA_VALLEY = (
        "VALU",
        pgettext_lazy("LocationType", "undersea valley"),
    )
    UNDERSEA_VALLEYS = (
        "VLSU",
        pgettext_lazy("LocationType", "undersea valleys"),
    )
    UNITED_STATES_GOVERNMENT_ESTABLISHMENT = (
        "USGE",
        pgettext_lazy("LocationType", "United States Government Establishment"),
    )
    UPLAND = (
        "UPLD",
        pgettext_lazy("LocationType", "upland"),
    )
    VALLEY = (
        "VAL",
        pgettext_lazy("LocationType", "valley"),
    )
    VALLEYS = (
        "VALS",
        pgettext_lazy("LocationType", "valleys"),
    )
    VETERINARY_FACILITY = (
        "VETF",
        pgettext_lazy("LocationType", "veterinary facility"),
    )
    VINEYARD = (
        "VIN",
        pgettext_lazy("LocationType", "vineyard"),
    )
    VINEYARDS = (
        "VINS",
        pgettext_lazy("LocationType", "vineyards"),
    )
    VOLCANO = (
        "VLC",
        pgettext_lazy("LocationType", "volcano"),
    )
    WADI = (
        "WAD",
        pgettext_lazy("LocationType", "wadi"),
    )
    WADI_BEND = (
        "WADB",
        pgettext_lazy("LocationType", "wadi bend"),
    )
    WADI_JUNCTION = (
        "WADJ",
        pgettext_lazy("LocationType", "wadi junction"),
    )
    WADI_MOUTH = (
        "WADM",
        pgettext_lazy("LocationType", "wadi mouth"),
    )
    WADIES = (
        "WADS",
        pgettext_lazy("LocationType", "wadies"),
    )
    WALL = (
        "WALL",
        pgettext_lazy("LocationType", "wall"),
    )
    WATER_MILL = (
        "MLWTR",
        pgettext_lazy("LocationType", "water mill"),
    )
    WATER_PUMPING_STATION = (
        "PMPW",
        pgettext_lazy("LocationType", "water pumping station"),
    )
    WATER_TANK = (
        "RSVT",
        pgettext_lazy("LocationType", "water tank"),
    )
    WATERCOURSE = (
        "WTRC",
        pgettext_lazy("LocationType", "watercourse"),
    )
    WATERFALL_S_ = (
        "FLLS",
        pgettext_lazy("LocationType", "waterfall(s)"),
    )
    WATERHOLE_S_ = (
        "WTRH",
        pgettext_lazy("LocationType", "waterhole(s)"),
    )
    WATERWORKS = (
        "WTRW",
        pgettext_lazy("LocationType", "waterworks"),
    )
    WEIR_S_ = (
        "WEIR",
        pgettext_lazy("LocationType", "weir(s)"),
    )
    WELL = (
        "WLL",
        pgettext_lazy("LocationType", "well"),
    )
    WELLS = (
        "WLLS",
        pgettext_lazy("LocationType", "wells"),
    )
    WETLAND = (
        "WTLD",
        pgettext_lazy("LocationType", "wetland"),
    )
    WHALING_STATION = (
        "STNW",
        pgettext_lazy("LocationType", "whaling station"),
    )
    WHARF__VES_ = (
        "WHRF",
        pgettext_lazy("LocationType", "wharf(-ves)"),
    )
    WHIRLPOOL = (
        "WHRL",
        pgettext_lazy("LocationType", "whirlpool"),
    )
    WILDLIFE_RESERVE = (
        "RESW",
        pgettext_lazy("LocationType", "wildlife reserve"),
    )
    WINDMILL = (
        "MLWND",
        pgettext_lazy("LocationType", "windmill"),
    )
    WRECK = (
        "WRCK",
        pgettext_lazy("LocationType", "wreck"),
    )
    ZONE = (
        "ZN",
        pgettext_lazy("LocationType", "zone"),
    )
    ZOO = (
        "ZOO",
        pgettext_lazy("LocationType", "zoo"),
    )
