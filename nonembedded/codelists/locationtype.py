from django.db import models
from django.utils.translation import pgettext_lazy


class LocationType(models.TextChoices):
    """
    US NGA Feature Designation Codes On this codelist 'category' is used for the Feature Class.
    """

    ABANDONED_AIRFIELD = (
        "AIRQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned airfield"),
    )
    ABANDONED_CAMP = (
        "CMPQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned camp"),
    )
    ABANDONED_CANAL = (
        "CNLQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned canal"),
    )
    ABANDONED_FACTORY = (
        "MFGQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned factory"),
    )
    ABANDONED_FARM = (
        "FRMQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned farm"),
    )
    ABANDONED_MINE = (
        "MNQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned mine"),
    )
    ABANDONED_MISSION = (
        "MSSNQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned mission"),
    )
    ABANDONED_OIL_WELL = (
        "OILQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned oil well"),
    )
    ABANDONED_POLICE_POST = (
        "PPQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned police post"),
    )
    ABANDONED_POPULATED_PLACE = (
        "PPLQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned populated place"),
    )
    ABANDONED_PRISON = (
        "PRNQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned prison"),
    )
    ABANDONED_RAILROAD = (
        "RRQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned railroad"),
    )
    ABANDONED_RAILROAD_STATION = (
        "RSTNQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned railroad station"),
    )
    ABANDONED_RAILROAD_STOP = (
        "RSTPQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned railroad stop"),
    )
    ABANDONED_WATERCOURSE = (
        "STMQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned watercourse"),
    )
    ABANDONED_WELL = (
        "WLLQ",
        pgettext_lazy("IATI codelist LocationType", "abandoned well"),
    )
    ADMINISTRATIVE_DIVISION = (
        "ADMD",
        pgettext_lazy("IATI codelist LocationType", "administrative division"),
    )
    ADMINISTRATIVE_FACILITY = (
        "ADMF",
        pgettext_lazy("IATI codelist LocationType", "administrative facility"),
    )
    AGRICULTURAL_COLONY = (
        "AGRC",
        pgettext_lazy("IATI codelist LocationType", "agricultural colony"),
    )
    AGRICULTURAL_FACILITY = (
        "AGRF",
        pgettext_lazy("IATI codelist LocationType", "agricultural facility"),
    )
    AGRICULTURAL_RESERVE = (
        "RESA",
        pgettext_lazy("IATI codelist LocationType", "agricultural reserve"),
    )
    AGRICULTURAL_SCHOOL = (
        "SCHA",
        pgettext_lazy("IATI codelist LocationType", "agricultural school"),
    )
    AIRBASE = (
        "AIRB",
        pgettext_lazy("IATI codelist LocationType", "airbase"),
    )
    AIRFIELD = (
        "AIRF",
        pgettext_lazy("IATI codelist LocationType", "airfield"),
    )
    AIRPORT = (
        "AIRP",
        pgettext_lazy("IATI codelist LocationType", "airport"),
    )
    AMPHITHEATER = (
        "AMTH",
        pgettext_lazy("IATI codelist LocationType", "amphitheater"),
    )
    ANABRANCH = (
        "STMA",
        pgettext_lazy("IATI codelist LocationType", "anabranch"),
    )
    ANCHORAGE = (
        "ANCH",
        pgettext_lazy("IATI codelist LocationType", "anchorage"),
    )
    ANCIENT_ROAD = (
        "RDA",
        pgettext_lazy("IATI codelist LocationType", "ancient road"),
    )
    ANCIENT_SITE = (
        "ANS",
        pgettext_lazy("IATI codelist LocationType", "ancient site"),
    )
    ANCIENT_WALL = (
        "WALLA",
        pgettext_lazy("IATI codelist LocationType", "ancient wall"),
    )
    APARTMENT_BUILDING = (
        "BLDA",
        pgettext_lazy("IATI codelist LocationType", "apartment building"),
    )
    AQUACULTURE_FACILITY = (
        "AQC",
        pgettext_lazy("IATI codelist LocationType", "aquaculture facility"),
    )
    AQUEDUCT = (
        "CNLA",
        pgettext_lazy("IATI codelist LocationType", "aqueduct"),
    )
    ARCH = (
        "ARCH",
        pgettext_lazy("IATI codelist LocationType", "arch"),
    )
    ARCTIC_LAND = (
        "LAND",
        pgettext_lazy("IATI codelist LocationType", "Arctic land"),
    )
    AREA = (
        "AREA",
        pgettext_lazy("IATI codelist LocationType", "area"),
    )
    ARTIFICIAL_ISLAND = (
        "ISLF",
        pgettext_lazy("IATI codelist LocationType", "artificial island"),
    )
    ARTILLERY_RANGE = (
        "RNGA",
        pgettext_lazy("IATI codelist LocationType", "artillery range"),
    )
    ASPHALT_LAKE = (
        "ASPH",
        pgettext_lazy("IATI codelist LocationType", "asphalt lake"),
    )
    ASTRONOMICAL_STATION = (
        "ASTR",
        pgettext_lazy("IATI codelist LocationType", "astronomical station"),
    )
    ASYLUM = (
        "ASYL",
        pgettext_lazy("IATI codelist LocationType", "asylum"),
    )
    ATHLETIC_FIELD = (
        "ATHF",
        pgettext_lazy("IATI codelist LocationType", "athletic field"),
    )
    ATOLL_S_ = (
        "ATOL",
        pgettext_lazy("IATI codelist LocationType", "atoll(s)"),
    )
    ATOMIC_CENTER = (
        "CTRA",
        pgettext_lazy("IATI codelist LocationType", "atomic center"),
    )
    BADLANDS = (
        "BDLD",
        pgettext_lazy("IATI codelist LocationType", "badlands"),
    )
    BALING_STATION = (
        "BSTN",
        pgettext_lazy("IATI codelist LocationType", "baling station"),
    )
    BANANA_PLANTATION = (
        "ESTB",
        pgettext_lazy("IATI codelist LocationType", "banana plantation"),
    )
    BANK = (
        "BAN",
        pgettext_lazy("IATI codelist LocationType", "bank"),
    )
    BANK_S_ = (
        "BNK",
        pgettext_lazy("IATI codelist LocationType", "bank(s)"),
    )
    BAR = (
        "BAR",
        pgettext_lazy("IATI codelist LocationType", "bar"),
    )
    BARRACKS = (
        "BRKS",
        pgettext_lazy("IATI codelist LocationType", "barracks"),
    )
    BATTLEFIELD = (
        "BTL",
        pgettext_lazy("IATI codelist LocationType", "battlefield"),
    )
    BAY = (
        "BAY",
        pgettext_lazy("IATI codelist LocationType", "bay"),
    )
    BAYS = (
        "BAYS",
        pgettext_lazy("IATI codelist LocationType", "bays"),
    )
    BEACH = (
        "BCH",
        pgettext_lazy("IATI codelist LocationType", "beach"),
    )
    BEACH_RIDGE = (
        "RDGB",
        pgettext_lazy("IATI codelist LocationType", "beach ridge"),
    )
    BEACHES = (
        "BCHS",
        pgettext_lazy("IATI codelist LocationType", "beaches"),
    )
    BEACON = (
        "BCN",
        pgettext_lazy("IATI codelist LocationType", "beacon"),
    )
    BENCH = (
        "BNCH",
        pgettext_lazy("IATI codelist LocationType", "bench"),
    )
    BIGHT_S_ = (
        "BGHT",
        pgettext_lazy("IATI codelist LocationType", "bight(s)"),
    )
    BLOWHOLE_S_ = (
        "BLHL",
        pgettext_lazy("IATI codelist LocationType", "blowhole(s)"),
    )
    BLOWOUT_S_ = (
        "BLOW",
        pgettext_lazy("IATI codelist LocationType", "blowout(s)"),
    )
    BOATYARD = (
        "BTYD",
        pgettext_lazy("IATI codelist LocationType", "boatyard"),
    )
    BOG_S_ = (
        "BOG",
        pgettext_lazy("IATI codelist LocationType", "bog(s)"),
    )
    BORDER_POST = (
        "PSTB",
        pgettext_lazy("IATI codelist LocationType", "border post"),
    )
    BOULDER_FIELD = (
        "BLDR",
        pgettext_lazy("IATI codelist LocationType", "boulder field"),
    )
    BOUNDARY_MARKER = (
        "BP",
        pgettext_lazy("IATI codelist LocationType", "boundary marker"),
    )
    BREAKWATER = (
        "BRKW",
        pgettext_lazy("IATI codelist LocationType", "breakwater"),
    )
    BREWERY = (
        "MFGB",
        pgettext_lazy("IATI codelist LocationType", "brewery"),
    )
    BRIDGE = (
        "BDG",
        pgettext_lazy("IATI codelist LocationType", "bridge"),
    )
    BUFFER_ZONE = (
        "ZNB",
        pgettext_lazy("IATI codelist LocationType", "buffer zone"),
    )
    BUILDING_S_ = (
        "BLDG",
        pgettext_lazy("IATI codelist LocationType", "building(s)"),
    )
    BURIAL_CAVE_S_ = (
        "BUR",
        pgettext_lazy("IATI codelist LocationType", "burial cave(s)"),
    )
    BUSH_ES_ = (
        "BUSH",
        pgettext_lazy("IATI codelist LocationType", "bush(es)"),
    )
    BUSINESS_CENTER = (
        "CTRB",
        pgettext_lazy("IATI codelist LocationType", "business center"),
    )
    BUTTE_S_ = (
        "BUTE",
        pgettext_lazy("IATI codelist LocationType", "butte(s)"),
    )
    CAIRN = (
        "CARN",
        pgettext_lazy("IATI codelist LocationType", "cairn"),
    )
    CALDERA = (
        "CLDA",
        pgettext_lazy("IATI codelist LocationType", "caldera"),
    )
    CAMP_S_ = (
        "CMP",
        pgettext_lazy("IATI codelist LocationType", "camp(s)"),
    )
    CANAL = (
        "CNL",
        pgettext_lazy("IATI codelist LocationType", "canal"),
    )
    CANAL_BEND = (
        "CNLB",
        pgettext_lazy("IATI codelist LocationType", "canal bend"),
    )
    CANAL_TUNNEL = (
        "TNLC",
        pgettext_lazy("IATI codelist LocationType", "canal tunnel"),
    )
    CANALIZED_STREAM = (
        "STMC",
        pgettext_lazy("IATI codelist LocationType", "canalized stream"),
    )
    CANNERY = (
        "MFGC",
        pgettext_lazy("IATI codelist LocationType", "cannery"),
    )
    CANYON = (
        "CNYN",
        pgettext_lazy("IATI codelist LocationType", "canyon"),
    )
    CAPE = (
        "CAPE",
        pgettext_lazy("IATI codelist LocationType", "cape"),
    )
    CAPITAL_OF_A_POLITICAL_ENTITY = (
        "PPLC",
        pgettext_lazy("IATI codelist LocationType", "capital of a political entity"),
    )
    CARAVAN_ROUTE = (
        "RTE",
        pgettext_lazy("IATI codelist LocationType", "caravan route"),
    )
    CASINO = (
        "CSNO",
        pgettext_lazy("IATI codelist LocationType", "casino"),
    )
    CASTLE = (
        "CSTL",
        pgettext_lazy("IATI codelist LocationType", "castle"),
    )
    CATTLE_DIPPING_TANK = (
        "TNKD",
        pgettext_lazy("IATI codelist LocationType", "cattle dipping tank"),
    )
    CAUSEWAY = (
        "CSWY",
        pgettext_lazy("IATI codelist LocationType", "causeway"),
    )
    CAVE_S_ = (
        "CAVE",
        pgettext_lazy("IATI codelist LocationType", "cave(s)"),
    )
    CEMETERY = (
        "CMTY",
        pgettext_lazy("IATI codelist LocationType", "cemetery"),
    )
    CHANNEL = (
        "CHN",
        pgettext_lazy("IATI codelist LocationType", "channel"),
    )
    CHROME_MINE_S_ = (
        "MNCR",
        pgettext_lazy("IATI codelist LocationType", "chrome mine(s)"),
    )
    CHURCH = (
        "CH",
        pgettext_lazy("IATI codelist LocationType", "church"),
    )
    CIRQUE = (
        "CRQ",
        pgettext_lazy("IATI codelist LocationType", "cirque"),
    )
    CIRQUES = (
        "CRQS",
        pgettext_lazy("IATI codelist LocationType", "cirques"),
    )
    CLEARING = (
        "CLG",
        pgettext_lazy("IATI codelist LocationType", "clearing"),
    )
    CLEFT_S_ = (
        "CFT",
        pgettext_lazy("IATI codelist LocationType", "cleft(s)"),
    )
    CLIFF_S_ = (
        "CLF",
        pgettext_lazy("IATI codelist LocationType", "cliff(s)"),
    )
    CLINIC = (
        "HSPC",
        pgettext_lazy("IATI codelist LocationType", "clinic"),
    )
    COAL_MINE_S_ = (
        "MNC",
        pgettext_lazy("IATI codelist LocationType", "coal mine(s)"),
    )
    COALFIELD = (
        "COLF",
        pgettext_lazy("IATI codelist LocationType", "coalfield"),
    )
    COAST = (
        "CST",
        pgettext_lazy("IATI codelist LocationType", "coast"),
    )
    COAST_GUARD_STATION = (
        "STNC",
        pgettext_lazy("IATI codelist LocationType", "coast guard station"),
    )
    COCONUT_GROVE = (
        "GRVC",
        pgettext_lazy("IATI codelist LocationType", "coconut grove"),
    )
    COLLEGE = (
        "SCHC",
        pgettext_lazy("IATI codelist LocationType", "college"),
    )
    COMMON = (
        "CMN",
        pgettext_lazy("IATI codelist LocationType", "common"),
    )
    COMMUNICATION_CENTER = (
        "COMC",
        pgettext_lazy("IATI codelist LocationType", "communication center"),
    )
    COMMUNITY_CENTER = (
        "CTRCM",
        pgettext_lazy("IATI codelist LocationType", "community center"),
    )
    CONCESSION_AREA = (
        "CNS",
        pgettext_lazy("IATI codelist LocationType", "concession area"),
    )
    CONE_S_ = (
        "CONE",
        pgettext_lazy("IATI codelist LocationType", "cone(s)"),
    )
    CONFLUENCE = (
        "CNFL",
        pgettext_lazy("IATI codelist LocationType", "confluence"),
    )
    CONTINENTAL_RISE = (
        "CRSU",
        pgettext_lazy("IATI codelist LocationType", "continental rise"),
    )
    CONVENT = (
        "CVNT",
        pgettext_lazy("IATI codelist LocationType", "convent"),
    )
    COPPER_MINE_S_ = (
        "MNCU",
        pgettext_lazy("IATI codelist LocationType", "copper mine(s)"),
    )
    COPPER_WORKS = (
        "MFGCU",
        pgettext_lazy("IATI codelist LocationType", "copper works"),
    )
    CORAL_REEF_S_ = (
        "RFC",
        pgettext_lazy("IATI codelist LocationType", "coral reef(s)"),
    )
    CORRAL_S_ = (
        "CRRL",
        pgettext_lazy("IATI codelist LocationType", "corral(s)"),
    )
    CORRIDOR = (
        "CRDR",
        pgettext_lazy("IATI codelist LocationType", "corridor"),
    )
    COTTON_PLANTATION = (
        "ESTC",
        pgettext_lazy("IATI codelist LocationType", "cotton plantation"),
    )
    COUNTRY_HOUSE = (
        "HSEC",
        pgettext_lazy("IATI codelist LocationType", "country house"),
    )
    COURTHOUSE = (
        "CTHSE",
        pgettext_lazy("IATI codelist LocationType", "courthouse"),
    )
    COVE_S_ = (
        "COVE",
        pgettext_lazy("IATI codelist LocationType", "cove(s)"),
    )
    CRATER_LAKE = (
        "LKC",
        pgettext_lazy("IATI codelist LocationType", "crater lake"),
    )
    CRATER_LAKES = (
        "LKSC",
        pgettext_lazy("IATI codelist LocationType", "crater lakes"),
    )
    CRATER_S_ = (
        "CRTR",
        pgettext_lazy("IATI codelist LocationType", "crater(s)"),
    )
    CUESTA_S_ = (
        "CUET",
        pgettext_lazy("IATI codelist LocationType", "cuesta(s)"),
    )
    CULTIVATED_AREA = (
        "CULT",
        pgettext_lazy("IATI codelist LocationType", "cultivated area"),
    )
    CURRENT = (
        "CRNT",
        pgettext_lazy("IATI codelist LocationType", "current"),
    )
    CUSTOMS_HOUSE = (
        "CSTM",
        pgettext_lazy("IATI codelist LocationType", "customs house"),
    )
    CUSTOMS_POST = (
        "PSTC",
        pgettext_lazy("IATI codelist LocationType", "customs post"),
    )
    CUTOFF = (
        "CUTF",
        pgettext_lazy("IATI codelist LocationType", "cutoff"),
    )
    DAIRY = (
        "DARY",
        pgettext_lazy("IATI codelist LocationType", "dairy"),
    )
    DAM = (
        "DAM",
        pgettext_lazy("IATI codelist LocationType", "dam"),
    )
    DEEP = (
        "DEPU",
        pgettext_lazy("IATI codelist LocationType", "deep"),
    )
    DELTA = (
        "DLTA",
        pgettext_lazy("IATI codelist LocationType", "delta"),
    )
    DEPENDENT_POLITICAL_ENTITY = (
        "PCLD",
        pgettext_lazy("IATI codelist LocationType", "dependent political entity"),
    )
    DEPRESSION_S_ = (
        "DPR",
        pgettext_lazy("IATI codelist LocationType", "depression(s)"),
    )
    DESERT = (
        "DSRT",
        pgettext_lazy("IATI codelist LocationType", "desert"),
    )
    DESTROYED_POPULATED_PLACE = (
        "PPLW",
        pgettext_lazy("IATI codelist LocationType", "destroyed populated place"),
    )
    DIATOMITE_MINE_S_ = (
        "MNDT",
        pgettext_lazy("IATI codelist LocationType", "diatomite mine(s)"),
    )
    DIKE = (
        "DIKE",
        pgettext_lazy("IATI codelist LocationType", "dike"),
    )
    DIPLOMATIC_FACILITY = (
        "DIP",
        pgettext_lazy("IATI codelist LocationType", "diplomatic facility"),
    )
    DISPENSARY = (
        "HSPD",
        pgettext_lazy("IATI codelist LocationType", "dispensary"),
    )
    DISTRIBUTARY__IES_ = (
        "STMD",
        pgettext_lazy("IATI codelist LocationType", "distributary(-ies)"),
    )
    DITCH = (
        "DTCH",
        pgettext_lazy("IATI codelist LocationType", "ditch"),
    )
    DITCH_MOUTH_S_ = (
        "DTCHM",
        pgettext_lazy("IATI codelist LocationType", "ditch mouth(s)"),
    )
    DIVIDE = (
        "DVD",
        pgettext_lazy("IATI codelist LocationType", "divide"),
    )
    DOCK_S_ = (
        "DCK",
        pgettext_lazy("IATI codelist LocationType", "dock(s)"),
    )
    DOCKING_BASIN = (
        "DCKB",
        pgettext_lazy("IATI codelist LocationType", "docking basin"),
    )
    DOCKYARD = (
        "DCKY",
        pgettext_lazy("IATI codelist LocationType", "dockyard"),
    )
    DRAINAGE_BASIN = (
        "BSND",
        pgettext_lazy("IATI codelist LocationType", "drainage basin"),
    )
    DRAINAGE_CANAL = (
        "CNLD",
        pgettext_lazy("IATI codelist LocationType", "drainage canal"),
    )
    DRAINAGE_DITCH = (
        "DTCHD",
        pgettext_lazy("IATI codelist LocationType", "drainage ditch"),
    )
    DRY_DOCK = (
        "DCKD",
        pgettext_lazy("IATI codelist LocationType", "dry dock"),
    )
    DRY_STREAM_BED = (
        "SBED",
        pgettext_lazy("IATI codelist LocationType", "dry stream bed"),
    )
    DUNE_S_ = (
        "DUNE",
        pgettext_lazy("IATI codelist LocationType", "dune(s)"),
    )
    ECONOMIC_REGION = (
        "RGNE",
        pgettext_lazy("IATI codelist LocationType", "economic region"),
    )
    ESCARPMENT = (
        "SCRP",
        pgettext_lazy("IATI codelist LocationType", "escarpment"),
    )
    ESTATE_S_ = (
        "EST",
        pgettext_lazy("IATI codelist LocationType", "estate(s)"),
    )
    ESTUARY = (
        "ESTY",
        pgettext_lazy("IATI codelist LocationType", "estuary"),
    )
    EXPERIMENT_STATION = (
        "STNE",
        pgettext_lazy("IATI codelist LocationType", "experiment station"),
    )
    FACILITY = (
        "FCL",
        pgettext_lazy("IATI codelist LocationType", "facility"),
    )
    FACILITY_CENTER = (
        "CTRF",
        pgettext_lazy("IATI codelist LocationType", "facility center"),
    )
    FACTORY = (
        "MFG",
        pgettext_lazy("IATI codelist LocationType", "factory"),
    )
    FAN_S_ = (
        "FAN",
        pgettext_lazy("IATI codelist LocationType", "fan(s)"),
    )
    FARM = (
        "FRM",
        pgettext_lazy("IATI codelist LocationType", "farm"),
    )
    FARM_VILLAGE = (
        "PPLF",
        pgettext_lazy("IATI codelist LocationType", "farm village"),
    )
    FARMS = (
        "FRMS",
        pgettext_lazy("IATI codelist LocationType", "farms"),
    )
    FARMSTEAD = (
        "FRMT",
        pgettext_lazy("IATI codelist LocationType", "farmstead"),
    )
    FERRY = (
        "FY",
        pgettext_lazy("IATI codelist LocationType", "ferry"),
    )
    FERRY_TERMINAL = (
        "FYT",
        pgettext_lazy("IATI codelist LocationType", "ferry terminal"),
    )
    FIELD_S_ = (
        "FLD",
        pgettext_lazy("IATI codelist LocationType", "field(s)"),
    )
    FIRE_STATION = (
        "FIRE",
        pgettext_lazy("IATI codelist LocationType", "fire station"),
    )
    FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM1",
        pgettext_lazy(
            "IATI codelist LocationType", "first-order administrative division"
        ),
    )
    FISHING_AREA = (
        "FISH",
        pgettext_lazy("IATI codelist LocationType", "fishing area"),
    )
    FISHPONDS = (
        "PNDSF",
        pgettext_lazy("IATI codelist LocationType", "fishponds"),
    )
    FISSURE = (
        "FSR",
        pgettext_lazy("IATI codelist LocationType", "fissure"),
    )
    FJORD = (
        "FJD",
        pgettext_lazy("IATI codelist LocationType", "fjord"),
    )
    FJORDS = (
        "FJDS",
        pgettext_lazy("IATI codelist LocationType", "fjords"),
    )
    FORD = (
        "FORD",
        pgettext_lazy("IATI codelist LocationType", "ford"),
    )
    FOREST_RESERVE = (
        "RESF",
        pgettext_lazy("IATI codelist LocationType", "forest reserve"),
    )
    FOREST_STATION = (
        "STNF",
        pgettext_lazy("IATI codelist LocationType", "forest station"),
    )
    FOREST_S_ = (
        "FRST",
        pgettext_lazy("IATI codelist LocationType", "forest(s)"),
    )
    FORMER_INLET = (
        "INLTQ",
        pgettext_lazy("IATI codelist LocationType", "former inlet"),
    )
    FORMER_SUGAR_MILL = (
        "MLSGQ",
        pgettext_lazy("IATI codelist LocationType", "former sugar mill"),
    )
    FORT = (
        "FT",
        pgettext_lazy("IATI codelist LocationType", "fort"),
    )
    FOSSILIZED_FOREST = (
        "FRSTF",
        pgettext_lazy("IATI codelist LocationType", "fossilized forest"),
    )
    FOUNDRY = (
        "FNDY",
        pgettext_lazy("IATI codelist LocationType", "foundry"),
    )
    FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM4",
        pgettext_lazy(
            "IATI codelist LocationType", "fourth-order administrative division"
        ),
    )
    FREE_TRADE_ZONE = (
        "ZNF",
        pgettext_lazy("IATI codelist LocationType", "free trade zone"),
    )
    FREELY_ASSOCIATED_STATE = (
        "PCLF",
        pgettext_lazy("IATI codelist LocationType", "freely associated state"),
    )
    FUEL_DEPOT = (
        "DPOF",
        pgettext_lazy("IATI codelist LocationType", "fuel depot"),
    )
    GAP = (
        "GAP",
        pgettext_lazy("IATI codelist LocationType", "gap"),
    )
    GARDEN_S_ = (
        "GDN",
        pgettext_lazy("IATI codelist LocationType", "garden(s)"),
    )
    GAS_OIL_SEPARATOR_PLANT = (
        "GOSP",
        pgettext_lazy("IATI codelist LocationType", "gas-oil separator plant"),
    )
    GASFIELD = (
        "GASF",
        pgettext_lazy("IATI codelist LocationType", "gasfield"),
    )
    GATE = (
        "GATE",
        pgettext_lazy("IATI codelist LocationType", "gate"),
    )
    GEYSER = (
        "GYSR",
        pgettext_lazy("IATI codelist LocationType", "geyser"),
    )
    GHĀT = (
        "GHAT",
        pgettext_lazy("IATI codelist LocationType", "ghāt"),
    )
    GLACIER_S_ = (
        "GLCR",
        pgettext_lazy("IATI codelist LocationType", "glacier(s)"),
    )
    GOLD_MINE_S_ = (
        "MNAU",
        pgettext_lazy("IATI codelist LocationType", "gold mine(s)"),
    )
    GOLF_COURSE = (
        "RECG",
        pgettext_lazy("IATI codelist LocationType", "golf course"),
    )
    GORGE_S_ = (
        "GRGE",
        pgettext_lazy("IATI codelist LocationType", "gorge(s)"),
    )
    GRASSLAND = (
        "GRSLD",
        pgettext_lazy("IATI codelist LocationType", "grassland"),
    )
    GRAVE = (
        "GRVE",
        pgettext_lazy("IATI codelist LocationType", "grave"),
    )
    GRAVEL_AREA = (
        "GVL",
        pgettext_lazy("IATI codelist LocationType", "gravel area"),
    )
    GRAZING_AREA = (
        "GRAZ",
        pgettext_lazy("IATI codelist LocationType", "grazing area"),
    )
    GUEST_HOUSE = (
        "GHSE",
        pgettext_lazy("IATI codelist LocationType", "guest house"),
    )
    GULF = (
        "GULF",
        pgettext_lazy("IATI codelist LocationType", "gulf"),
    )
    HALTING_PLACE = (
        "HLT",
        pgettext_lazy("IATI codelist LocationType", "halting place"),
    )
    HAMMOCK_S_ = (
        "HMCK",
        pgettext_lazy("IATI codelist LocationType", "hammock(s)"),
    )
    HANGAR = (
        "AIRG",
        pgettext_lazy("IATI codelist LocationType", "hangar"),
    )
    HANGING_VALLEY = (
        "VALG",
        pgettext_lazy("IATI codelist LocationType", "hanging valley"),
    )
    HARBOR_S_ = (
        "HBR",
        pgettext_lazy("IATI codelist LocationType", "harbor(s)"),
    )
    HEADLAND = (
        "HDLD",
        pgettext_lazy("IATI codelist LocationType", "headland"),
    )
    HEADWATERS = (
        "STMH",
        pgettext_lazy("IATI codelist LocationType", "headwaters"),
    )
    HEATH = (
        "HTH",
        pgettext_lazy("IATI codelist LocationType", "heath"),
    )
    HELIPORT = (
        "AIRH",
        pgettext_lazy("IATI codelist LocationType", "heliport"),
    )
    HERMITAGE = (
        "HERM",
        pgettext_lazy("IATI codelist LocationType", "hermitage"),
    )
    HILL = (
        "HLL",
        pgettext_lazy("IATI codelist LocationType", "hill"),
    )
    HILLS = (
        "HLLS",
        pgettext_lazy("IATI codelist LocationType", "hills"),
    )
    HISTORICAL_ADMINISTRATIVE_DIVISION = (
        "ADMDH",
        pgettext_lazy(
            "IATI codelist LocationType", "historical administrative division"
        ),
    )
    HISTORICAL_FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM1H",
        pgettext_lazy(
            "IATI codelist LocationType",
            "historical first-order administrative division",
        ),
    )
    HISTORICAL_FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM4H",
        pgettext_lazy(
            "IATI codelist LocationType",
            "historical fourth-order administrative division",
        ),
    )
    HISTORICAL_POLITICAL_ENTITY = (
        "PCLH",
        pgettext_lazy("IATI codelist LocationType", "historical political entity"),
    )
    HISTORICAL_POPULATED_PLACE = (
        "PPLH",
        pgettext_lazy("IATI codelist LocationType", "historical populated place"),
    )
    HISTORICAL_RAILROAD = (
        "RRH",
        pgettext_lazy("IATI codelist LocationType", "historical railroad"),
    )
    HISTORICAL_RAILROAD_STATION = (
        "RSTNH",
        pgettext_lazy("IATI codelist LocationType", "historical railroad station"),
    )
    HISTORICAL_REGION = (
        "RGNH",
        pgettext_lazy("IATI codelist LocationType", "historical region"),
    )
    HISTORICAL_SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM2H",
        pgettext_lazy(
            "IATI codelist LocationType",
            "historical second-order administrative division",
        ),
    )
    HISTORICAL_SITE = (
        "HSTS",
        pgettext_lazy("IATI codelist LocationType", "historical site"),
    )
    HISTORICAL_THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM3H",
        pgettext_lazy(
            "IATI codelist LocationType",
            "historical third-order administrative division",
        ),
    )
    HISTORICAL_UNDERSEA_FEATURE = (
        "UFHU",
        pgettext_lazy("IATI codelist LocationType", "historical undersea feature"),
    )
    HOMESTEAD = (
        "HMSD",
        pgettext_lazy("IATI codelist LocationType", "homestead"),
    )
    HOSPITAL = (
        "HSP",
        pgettext_lazy("IATI codelist LocationType", "hospital"),
    )
    HOT_SPRING_S_ = (
        "SPNT",
        pgettext_lazy("IATI codelist LocationType", "hot spring(s)"),
    )
    HOTEL = (
        "HTL",
        pgettext_lazy("IATI codelist LocationType", "hotel"),
    )
    HOUSE_S_ = (
        "HSE",
        pgettext_lazy("IATI codelist LocationType", "house(s)"),
    )
    HOUSING_DEVELOPMENT = (
        "DEVH",
        pgettext_lazy("IATI codelist LocationType", "housing development"),
    )
    HUNTING_RESERVE = (
        "RESH",
        pgettext_lazy("IATI codelist LocationType", "hunting reserve"),
    )
    HUT = (
        "HUT",
        pgettext_lazy("IATI codelist LocationType", "hut"),
    )
    HUTS = (
        "HUTS",
        pgettext_lazy("IATI codelist LocationType", "huts"),
    )
    HYDROELECTRIC_POWER_STATION = (
        "PSH",
        pgettext_lazy("IATI codelist LocationType", "hydroelectric power station"),
    )
    ICECAP = (
        "CAPG",
        pgettext_lazy("IATI codelist LocationType", "icecap"),
    )
    ICECAP_DEPRESSION = (
        "DPRG",
        pgettext_lazy("IATI codelist LocationType", "icecap depression"),
    )
    ICECAP_DOME = (
        "DOMG",
        pgettext_lazy("IATI codelist LocationType", "icecap dome"),
    )
    ICECAP_RIDGE = (
        "RDGG",
        pgettext_lazy("IATI codelist LocationType", "icecap ridge"),
    )
    INDEPENDENT_POLITICAL_ENTITY = (
        "PCLI",
        pgettext_lazy("IATI codelist LocationType", "independent political entity"),
    )
    INDUSTRIAL_AREA = (
        "INDS",
        pgettext_lazy("IATI codelist LocationType", "industrial area"),
    )
    INLET = (
        "INLT",
        pgettext_lazy("IATI codelist LocationType", "inlet"),
    )
    INSPECTION_STATION = (
        "STNI",
        pgettext_lazy("IATI codelist LocationType", "inspection station"),
    )
    INTERDUNE_TROUGH_S_ = (
        "TRGD",
        pgettext_lazy("IATI codelist LocationType", "interdune trough(s)"),
    )
    INTERFLUVE = (
        "INTF",
        pgettext_lazy("IATI codelist LocationType", "interfluve"),
    )
    INTERMITTENT_LAKE = (
        "LKI",
        pgettext_lazy("IATI codelist LocationType", "intermittent lake"),
    )
    INTERMITTENT_LAKES = (
        "LKSI",
        pgettext_lazy("IATI codelist LocationType", "intermittent lakes"),
    )
    INTERMITTENT_OXBOW_LAKE = (
        "LKOI",
        pgettext_lazy("IATI codelist LocationType", "intermittent oxbow lake"),
    )
    INTERMITTENT_POND = (
        "PNDI",
        pgettext_lazy("IATI codelist LocationType", "intermittent pond"),
    )
    INTERMITTENT_PONDS = (
        "PNDSI",
        pgettext_lazy("IATI codelist LocationType", "intermittent ponds"),
    )
    INTERMITTENT_POOL = (
        "POOLI",
        pgettext_lazy("IATI codelist LocationType", "intermittent pool"),
    )
    INTERMITTENT_RESERVOIR = (
        "RSVI",
        pgettext_lazy("IATI codelist LocationType", "intermittent reservoir"),
    )
    INTERMITTENT_SALT_LAKE = (
        "LKNI",
        pgettext_lazy("IATI codelist LocationType", "intermittent salt lake"),
    )
    INTERMITTENT_SALT_LAKES = (
        "LKSNI",
        pgettext_lazy("IATI codelist LocationType", "intermittent salt lakes"),
    )
    INTERMITTENT_SALT_POND_S_ = (
        "PNDNI",
        pgettext_lazy("IATI codelist LocationType", "intermittent salt pond(s)"),
    )
    INTERMITTENT_STREAM = (
        "STMI",
        pgettext_lazy("IATI codelist LocationType", "intermittent stream"),
    )
    INTERMITTENT_WETLAND = (
        "WTLDI",
        pgettext_lazy("IATI codelist LocationType", "intermittent wetland"),
    )
    INTERSECTION = (
        "RDIN",
        pgettext_lazy("IATI codelist LocationType", "intersection"),
    )
    IRON_MINE_S_ = (
        "MNFE",
        pgettext_lazy("IATI codelist LocationType", "iron mine(s)"),
    )
    IRRIGATED_FIELD_S_ = (
        "FLDI",
        pgettext_lazy("IATI codelist LocationType", "irrigated field(s)"),
    )
    IRRIGATION_CANAL = (
        "CNLI",
        pgettext_lazy("IATI codelist LocationType", "irrigation canal"),
    )
    IRRIGATION_DITCH = (
        "DTCHI",
        pgettext_lazy("IATI codelist LocationType", "irrigation ditch"),
    )
    IRRIGATION_SYSTEM = (
        "SYSI",
        pgettext_lazy("IATI codelist LocationType", "irrigation system"),
    )
    ISLAND = (
        "ISL",
        pgettext_lazy("IATI codelist LocationType", "island"),
    )
    ISLANDS = (
        "ISLS",
        pgettext_lazy("IATI codelist LocationType", "islands"),
    )
    ISRAELI_SETTLEMENT = (
        "STLMT",
        pgettext_lazy("IATI codelist LocationType", "Israeli settlement"),
    )
    ISTHMUS = (
        "ISTH",
        pgettext_lazy("IATI codelist LocationType", "isthmus"),
    )
    JETTY = (
        "JTY",
        pgettext_lazy("IATI codelist LocationType", "jetty"),
    )
    KARST_AREA = (
        "KRST",
        pgettext_lazy("IATI codelist LocationType", "karst area"),
    )
    LABOR_CAMP = (
        "CMPLA",
        pgettext_lazy("IATI codelist LocationType", "labor camp"),
    )
    LAGOON = (
        "LGN",
        pgettext_lazy("IATI codelist LocationType", "lagoon"),
    )
    LAGOONS = (
        "LGNS",
        pgettext_lazy("IATI codelist LocationType", "lagoons"),
    )
    LAKE = (
        "LK",
        pgettext_lazy("IATI codelist LocationType", "lake"),
    )
    LAKE_BED_S_ = (
        "LBED",
        pgettext_lazy("IATI codelist LocationType", "lake bed(s)"),
    )
    LAKE_CHANNEL_S_ = (
        "CHNL",
        pgettext_lazy("IATI codelist LocationType", "lake channel(s)"),
    )
    LAKE_REGION = (
        "RGNL",
        pgettext_lazy("IATI codelist LocationType", "lake region"),
    )
    LAKES = (
        "LKS",
        pgettext_lazy("IATI codelist LocationType", "lakes"),
    )
    LAND_TIED_ISLAND = (
        "ISLT",
        pgettext_lazy("IATI codelist LocationType", "land-tied island"),
    )
    LANDFILL = (
        "LNDF",
        pgettext_lazy("IATI codelist LocationType", "landfill"),
    )
    LANDING = (
        "LDNG",
        pgettext_lazy("IATI codelist LocationType", "landing"),
    )
    LAVA_AREA = (
        "LAVA",
        pgettext_lazy("IATI codelist LocationType", "lava area"),
    )
    LEAD_MINE_S_ = (
        "MNPB",
        pgettext_lazy("IATI codelist LocationType", "lead mine(s)"),
    )
    LEASED_AREA = (
        "LTER",
        pgettext_lazy("IATI codelist LocationType", "leased area"),
    )
    LEPER_COLONY = (
        "LEPC",
        pgettext_lazy("IATI codelist LocationType", "leper colony"),
    )
    LEPROSARIUM = (
        "HSPL",
        pgettext_lazy("IATI codelist LocationType", "leprosarium"),
    )
    LEVEE = (
        "LEV",
        pgettext_lazy("IATI codelist LocationType", "levee"),
    )
    LIGHTHOUSE = (
        "LTHSE",
        pgettext_lazy("IATI codelist LocationType", "lighthouse"),
    )
    LIMEKILN = (
        "MFGLM",
        pgettext_lazy("IATI codelist LocationType", "limekiln"),
    )
    LOCAL_GOVERNMENT_OFFICE = (
        "GOVL",
        pgettext_lazy("IATI codelist LocationType", "local government office"),
    )
    LOCALITY = (
        "LCTY",
        pgettext_lazy("IATI codelist LocationType", "locality"),
    )
    LOCK_S_ = (
        "LOCK",
        pgettext_lazy("IATI codelist LocationType", "lock(s)"),
    )
    LOGGING_CAMP = (
        "CMPL",
        pgettext_lazy("IATI codelist LocationType", "logging camp"),
    )
    LOST_RIVER = (
        "STMSB",
        pgettext_lazy("IATI codelist LocationType", "lost river"),
    )
    MANEUVER_AREA = (
        "MVA",
        pgettext_lazy("IATI codelist LocationType", "maneuver area"),
    )
    MANGROVE_ISLAND = (
        "ISLM",
        pgettext_lazy("IATI codelist LocationType", "mangrove island"),
    )
    MANGROVE_SWAMP = (
        "MGV",
        pgettext_lazy("IATI codelist LocationType", "mangrove swamp"),
    )
    MARINA = (
        "MAR",
        pgettext_lazy("IATI codelist LocationType", "marina"),
    )
    MARINE_CHANNEL = (
        "CHNM",
        pgettext_lazy("IATI codelist LocationType", "marine channel"),
    )
    MARITIME_SCHOOL = (
        "SCHN",
        pgettext_lazy("IATI codelist LocationType", "maritime school"),
    )
    MARKET = (
        "MKT",
        pgettext_lazy("IATI codelist LocationType", "market"),
    )
    MARSH_ES_ = (
        "MRSH",
        pgettext_lazy("IATI codelist LocationType", "marsh(es)"),
    )
    MEADOW = (
        "MDW",
        pgettext_lazy("IATI codelist LocationType", "meadow"),
    )
    MEANDER_NECK = (
        "NKM",
        pgettext_lazy("IATI codelist LocationType", "meander neck"),
    )
    MEDICAL_CENTER = (
        "CTRM",
        pgettext_lazy("IATI codelist LocationType", "medical center"),
    )
    MESA_S_ = (
        "MESA",
        pgettext_lazy("IATI codelist LocationType", "mesa(s)"),
    )
    METEOROLOGICAL_STATION = (
        "STNM",
        pgettext_lazy("IATI codelist LocationType", "meteorological station"),
    )
    MILITARY_BASE = (
        "MILB",
        pgettext_lazy("IATI codelist LocationType", "military base"),
    )
    MILITARY_INSTALLATION = (
        "INSM",
        pgettext_lazy("IATI codelist LocationType", "military installation"),
    )
    MILITARY_SCHOOL = (
        "SCHM",
        pgettext_lazy("IATI codelist LocationType", "military school"),
    )
    MILL_S_ = (
        "ML",
        pgettext_lazy("IATI codelist LocationType", "mill(s)"),
    )
    MINE_S_ = (
        "MN",
        pgettext_lazy("IATI codelist LocationType", "mine(s)"),
    )
    MINING_AREA = (
        "MNA",
        pgettext_lazy("IATI codelist LocationType", "mining area"),
    )
    MINING_CAMP = (
        "CMPMN",
        pgettext_lazy("IATI codelist LocationType", "mining camp"),
    )
    MISSION = (
        "MSSN",
        pgettext_lazy("IATI codelist LocationType", "mission"),
    )
    MOLE = (
        "MOLE",
        pgettext_lazy("IATI codelist LocationType", "mole"),
    )
    MONASTERY = (
        "MSTY",
        pgettext_lazy("IATI codelist LocationType", "monastery"),
    )
    MONUMENT = (
        "MNMT",
        pgettext_lazy("IATI codelist LocationType", "monument"),
    )
    MOOR_S_ = (
        "MOOR",
        pgettext_lazy("IATI codelist LocationType", "moor(s)"),
    )
    MORAINE = (
        "MRN",
        pgettext_lazy("IATI codelist LocationType", "moraine"),
    )
    MOSQUE = (
        "MSQE",
        pgettext_lazy("IATI codelist LocationType", "mosque"),
    )
    MOUND_S_ = (
        "MND",
        pgettext_lazy("IATI codelist LocationType", "mound(s)"),
    )
    MOUNTAIN = (
        "MT",
        pgettext_lazy("IATI codelist LocationType", "mountain"),
    )
    MOUNTAINS = (
        "MTS",
        pgettext_lazy("IATI codelist LocationType", "mountains"),
    )
    MUD_FLAT_S_ = (
        "FLTM",
        pgettext_lazy("IATI codelist LocationType", "mud flat(s)"),
    )
    MUNITIONS_PLANT = (
        "MFGM",
        pgettext_lazy("IATI codelist LocationType", "munitions plant"),
    )
    MUSEUM = (
        "MUS",
        pgettext_lazy("IATI codelist LocationType", "museum"),
    )
    NARROWS = (
        "NRWS",
        pgettext_lazy("IATI codelist LocationType", "narrows"),
    )
    NATURAL_TUNNEL = (
        "TNLN",
        pgettext_lazy("IATI codelist LocationType", "natural tunnel"),
    )
    NATURE_RESERVE = (
        "RESN",
        pgettext_lazy("IATI codelist LocationType", "nature reserve"),
    )
    NAVAL_BASE = (
        "NVB",
        pgettext_lazy("IATI codelist LocationType", "naval base"),
    )
    NAVIGATION_CANAL_S_ = (
        "CNLN",
        pgettext_lazy("IATI codelist LocationType", "navigation canal(s)"),
    )
    NAVIGATION_CHANNEL = (
        "CHNN",
        pgettext_lazy("IATI codelist LocationType", "navigation channel"),
    )
    NICKEL_MINE_S_ = (
        "MNNI",
        pgettext_lazy("IATI codelist LocationType", "nickel mine(s)"),
    )
    NOVITIATE = (
        "NOV",
        pgettext_lazy("IATI codelist LocationType", "novitiate"),
    )
    NUCLEAR_POWER_STATION = (
        "PSN",
        pgettext_lazy("IATI codelist LocationType", "nuclear power station"),
    )
    NUNATAK = (
        "NTK",
        pgettext_lazy("IATI codelist LocationType", "nunatak"),
    )
    NUNATAKS = (
        "NTKS",
        pgettext_lazy("IATI codelist LocationType", "nunataks"),
    )
    NURSERY__IES_ = (
        "NSY",
        pgettext_lazy("IATI codelist LocationType", "nursery(-ies)"),
    )
    OASIS__ES_ = (
        "OAS",
        pgettext_lazy("IATI codelist LocationType", "oasis(-es)"),
    )
    OBSERVATION_POINT = (
        "OBPT",
        pgettext_lazy("IATI codelist LocationType", "observation point"),
    )
    OBSERVATORY = (
        "OBS",
        pgettext_lazy("IATI codelist LocationType", "observatory"),
    )
    OCEAN = (
        "OCN",
        pgettext_lazy("IATI codelist LocationType", "ocean"),
    )
    OFFICE_BUILDING = (
        "BLDO",
        pgettext_lazy("IATI codelist LocationType", "office building"),
    )
    OIL_CAMP = (
        "CMPO",
        pgettext_lazy("IATI codelist LocationType", "oil camp"),
    )
    OIL_PALM_PLANTATION = (
        "ESTO",
        pgettext_lazy("IATI codelist LocationType", "oil palm plantation"),
    )
    OIL_PIPELINE = (
        "OILP",
        pgettext_lazy("IATI codelist LocationType", "oil pipeline"),
    )
    OIL_PIPELINE_JUNCTION = (
        "OILJ",
        pgettext_lazy("IATI codelist LocationType", "oil pipeline junction"),
    )
    OIL_PIPELINE_TERMINAL = (
        "TRMO",
        pgettext_lazy("IATI codelist LocationType", "oil pipeline terminal"),
    )
    OIL_PUMPING_STATION = (
        "PMPO",
        pgettext_lazy("IATI codelist LocationType", "oil pumping station"),
    )
    OIL_REFINERY = (
        "OILR",
        pgettext_lazy("IATI codelist LocationType", "oil refinery"),
    )
    OIL_WELL = (
        "OILW",
        pgettext_lazy("IATI codelist LocationType", "oil well"),
    )
    OILFIELD = (
        "OILF",
        pgettext_lazy("IATI codelist LocationType", "oilfield"),
    )
    OLIVE_GROVE = (
        "GRVO",
        pgettext_lazy("IATI codelist LocationType", "olive grove"),
    )
    OLIVE_OIL_MILL = (
        "MLO",
        pgettext_lazy("IATI codelist LocationType", "olive oil mill"),
    )
    ORCHARD_S_ = (
        "OCH",
        pgettext_lazy("IATI codelist LocationType", "orchard(s)"),
    )
    ORE_TREATMENT_PLANT = (
        "MLM",
        pgettext_lazy("IATI codelist LocationType", "ore treatment plant"),
    )
    OVERFALLS = (
        "OVF",
        pgettext_lazy("IATI codelist LocationType", "overfalls"),
    )
    OXBOW_LAKE = (
        "LKO",
        pgettext_lazy("IATI codelist LocationType", "oxbow lake"),
    )
    PAGODA = (
        "PGDA",
        pgettext_lazy("IATI codelist LocationType", "pagoda"),
    )
    PALACE = (
        "PAL",
        pgettext_lazy("IATI codelist LocationType", "palace"),
    )
    PALM_GROVE = (
        "GRVP",
        pgettext_lazy("IATI codelist LocationType", "palm grove"),
    )
    PALM_TREE_RESERVE = (
        "RESP",
        pgettext_lazy("IATI codelist LocationType", "palm tree reserve"),
    )
    PAN = (
        "PAN",
        pgettext_lazy("IATI codelist LocationType", "pan"),
    )
    PANS = (
        "PANS",
        pgettext_lazy("IATI codelist LocationType", "pans"),
    )
    PARISH = (
        "PRSH",
        pgettext_lazy("IATI codelist LocationType", "parish"),
    )
    PARK = (
        "PRK",
        pgettext_lazy("IATI codelist LocationType", "park"),
    )
    PARK_GATE = (
        "PRKGT",
        pgettext_lazy("IATI codelist LocationType", "park gate"),
    )
    PARK_HEADQUARTERS = (
        "PRKHQ",
        pgettext_lazy("IATI codelist LocationType", "park headquarters"),
    )
    PARKING_GARAGE = (
        "GARG",
        pgettext_lazy("IATI codelist LocationType", "parking garage"),
    )
    PARKING_LOT = (
        "PKLT",
        pgettext_lazy("IATI codelist LocationType", "parking lot"),
    )
    PASS = (
        "PASS",
        pgettext_lazy("IATI codelist LocationType", "pass"),
    )
    PATROL_POST = (
        "PSTP",
        pgettext_lazy("IATI codelist LocationType", "patrol post"),
    )
    PEAK = (
        "PK",
        pgettext_lazy("IATI codelist LocationType", "peak"),
    )
    PEAKS = (
        "PKS",
        pgettext_lazy("IATI codelist LocationType", "peaks"),
    )
    PEAT_CUTTING_AREA = (
        "PEAT",
        pgettext_lazy("IATI codelist LocationType", "peat cutting area"),
    )
    PENINSULA = (
        "PEN",
        pgettext_lazy("IATI codelist LocationType", "peninsula"),
    )
    PETROLEUM_BASIN = (
        "BSNP",
        pgettext_lazy("IATI codelist LocationType", "petroleum basin"),
    )
    PHOSPHATE_WORKS = (
        "MFGPH",
        pgettext_lazy("IATI codelist LocationType", "phosphate works"),
    )
    PIER = (
        "PIER",
        pgettext_lazy("IATI codelist LocationType", "pier"),
    )
    PINE_GROVE = (
        "GRVPN",
        pgettext_lazy("IATI codelist LocationType", "pine grove"),
    )
    PLACER_MINE_S_ = (
        "MNPL",
        pgettext_lazy("IATI codelist LocationType", "placer mine(s)"),
    )
    PLAIN_S_ = (
        "PLN",
        pgettext_lazy("IATI codelist LocationType", "plain(s)"),
    )
    PLATEAU = (
        "PLAT",
        pgettext_lazy("IATI codelist LocationType", "plateau"),
    )
    POINT = (
        "PT",
        pgettext_lazy("IATI codelist LocationType", "point"),
    )
    POINTS = (
        "PTS",
        pgettext_lazy("IATI codelist LocationType", "points"),
    )
    POLDER = (
        "PLDR",
        pgettext_lazy("IATI codelist LocationType", "polder"),
    )
    POLICE_POST = (
        "PP",
        pgettext_lazy("IATI codelist LocationType", "police post"),
    )
    POLITICAL_ENTITY = (
        "PCL",
        pgettext_lazy("IATI codelist LocationType", "political entity"),
    )
    POND = (
        "PND",
        pgettext_lazy("IATI codelist LocationType", "pond"),
    )
    PONDS = (
        "PNDS",
        pgettext_lazy("IATI codelist LocationType", "ponds"),
    )
    POOL_S_ = (
        "POOL",
        pgettext_lazy("IATI codelist LocationType", "pool(s)"),
    )
    POPULATED_LOCALITY = (
        "PPLL",
        pgettext_lazy("IATI codelist LocationType", "populated locality"),
    )
    POPULATED_PLACE = (
        "PPL",
        pgettext_lazy("IATI codelist LocationType", "populated place"),
    )
    POPULATED_PLACES = (
        "PPLS",
        pgettext_lazy("IATI codelist LocationType", "populated places"),
    )
    PORT = (
        "PRT",
        pgettext_lazy("IATI codelist LocationType", "port"),
    )
    PORTAGE = (
        "PTGE",
        pgettext_lazy("IATI codelist LocationType", "portage"),
    )
    POST_OFFICE = (
        "PO",
        pgettext_lazy("IATI codelist LocationType", "post office"),
    )
    POWER_STATION = (
        "PS",
        pgettext_lazy("IATI codelist LocationType", "power station"),
    )
    PRISON = (
        "PRN",
        pgettext_lazy("IATI codelist LocationType", "prison"),
    )
    PROMENADE = (
        "PRMN",
        pgettext_lazy("IATI codelist LocationType", "promenade"),
    )
    PROMONTORY__IES_ = (
        "PROM",
        pgettext_lazy("IATI codelist LocationType", "promontory(-ies)"),
    )
    PYRAMID = (
        "PYR",
        pgettext_lazy("IATI codelist LocationType", "pyramid"),
    )
    PYRAMIDS = (
        "PYRS",
        pgettext_lazy("IATI codelist LocationType", "pyramids"),
    )
    QUARRY__IES_ = (
        "MNQR",
        pgettext_lazy("IATI codelist LocationType", "quarry(-ies)"),
    )
    QUAY = (
        "QUAY",
        pgettext_lazy("IATI codelist LocationType", "quay"),
    )
    QUICKSAND = (
        "QCKS",
        pgettext_lazy("IATI codelist LocationType", "quicksand"),
    )
    RACETRACK = (
        "RECR",
        pgettext_lazy("IATI codelist LocationType", "racetrack"),
    )
    RADIO_OBSERVATORY = (
        "OBSR",
        pgettext_lazy("IATI codelist LocationType", "radio observatory"),
    )
    RADIO_STATION = (
        "STNR",
        pgettext_lazy("IATI codelist LocationType", "radio station"),
    )
    RAILROAD = (
        "RR",
        pgettext_lazy("IATI codelist LocationType", "railroad"),
    )
    RAILROAD_JUNCTION = (
        "RJCT",
        pgettext_lazy("IATI codelist LocationType", "railroad junction"),
    )
    RAILROAD_SIDING = (
        "RSD",
        pgettext_lazy("IATI codelist LocationType", "railroad siding"),
    )
    RAILROAD_SIGNAL = (
        "RSGNL",
        pgettext_lazy("IATI codelist LocationType", "railroad signal"),
    )
    RAILROAD_STATION = (
        "RSTN",
        pgettext_lazy("IATI codelist LocationType", "railroad station"),
    )
    RAILROAD_STOP = (
        "RSTP",
        pgettext_lazy("IATI codelist LocationType", "railroad stop"),
    )
    RAILROAD_TUNNEL = (
        "TNLRR",
        pgettext_lazy("IATI codelist LocationType", "railroad tunnel"),
    )
    RAILROAD_YARD = (
        "RYD",
        pgettext_lazy("IATI codelist LocationType", "railroad yard"),
    )
    RANCH_ES_ = (
        "RNCH",
        pgettext_lazy("IATI codelist LocationType", "ranch(es)"),
    )
    RAPIDS = (
        "RPDS",
        pgettext_lazy("IATI codelist LocationType", "rapids"),
    )
    RAVINE_S_ = (
        "RVN",
        pgettext_lazy("IATI codelist LocationType", "ravine(s)"),
    )
    REACH = (
        "RCH",
        pgettext_lazy("IATI codelist LocationType", "reach"),
    )
    REEF_S_ = (
        "RF",
        pgettext_lazy("IATI codelist LocationType", "reef(s)"),
    )
    REFORMATORY = (
        "PRNJ",
        pgettext_lazy("IATI codelist LocationType", "reformatory"),
    )
    REFUGEE_CAMP = (
        "CMPRF",
        pgettext_lazy("IATI codelist LocationType", "refugee camp"),
    )
    REGION = (
        "RGN",
        pgettext_lazy("IATI codelist LocationType", "region"),
    )
    RELIGIOUS_CENTER = (
        "CTRR",
        pgettext_lazy("IATI codelist LocationType", "religious center"),
    )
    RELIGIOUS_POPULATED_PLACE = (
        "PPLR",
        pgettext_lazy("IATI codelist LocationType", "religious populated place"),
    )
    RELIGIOUS_SITE = (
        "RLG",
        pgettext_lazy("IATI codelist LocationType", "religious site"),
    )
    RESEARCH_INSTITUTE = (
        "ITTR",
        pgettext_lazy("IATI codelist LocationType", "research institute"),
    )
    RESERVATION = (
        "RESV",
        pgettext_lazy("IATI codelist LocationType", "reservation"),
    )
    RESERVE = (
        "RES",
        pgettext_lazy("IATI codelist LocationType", "reserve"),
    )
    RESERVOIR_S_ = (
        "RSV",
        pgettext_lazy("IATI codelist LocationType", "reservoir(s)"),
    )
    RESORT = (
        "RSRT",
        pgettext_lazy("IATI codelist LocationType", "resort"),
    )
    RESTHOUSE = (
        "RHSE",
        pgettext_lazy("IATI codelist LocationType", "resthouse"),
    )
    RETREAT = (
        "RLGR",
        pgettext_lazy("IATI codelist LocationType", "retreat"),
    )
    RIDGE_S_ = (
        "RDGE",
        pgettext_lazy("IATI codelist LocationType", "ridge(s)"),
    )
    ROAD = (
        "RD",
        pgettext_lazy("IATI codelist LocationType", "road"),
    )
    ROAD_BEND = (
        "RDB",
        pgettext_lazy("IATI codelist LocationType", "road bend"),
    )
    ROAD_CUT = (
        "RDCUT",
        pgettext_lazy("IATI codelist LocationType", "road cut"),
    )
    ROAD_JUNCTION = (
        "RDJCT",
        pgettext_lazy("IATI codelist LocationType", "road junction"),
    )
    ROAD_TUNNEL = (
        "TNLRD",
        pgettext_lazy("IATI codelist LocationType", "road tunnel"),
    )
    ROADSTEAD = (
        "RDST",
        pgettext_lazy("IATI codelist LocationType", "roadstead"),
    )
    ROCK = (
        "RK",
        pgettext_lazy("IATI codelist LocationType", "rock"),
    )
    ROCK_DESERT = (
        "HMDA",
        pgettext_lazy("IATI codelist LocationType", "rock desert"),
    )
    ROCKFALL = (
        "RKFL",
        pgettext_lazy("IATI codelist LocationType", "rockfall"),
    )
    ROCKS = (
        "RKS",
        pgettext_lazy("IATI codelist LocationType", "rocks"),
    )
    ROOKERY = (
        "RKRY",
        pgettext_lazy("IATI codelist LocationType", "rookery"),
    )
    RUBBER_PLANTATION = (
        "ESTR",
        pgettext_lazy("IATI codelist LocationType", "rubber plantation"),
    )
    RUIN_S_ = (
        "RUIN",
        pgettext_lazy("IATI codelist LocationType", "ruin(s)"),
    )
    RUINED_BRIDGE = (
        "BDGQ",
        pgettext_lazy("IATI codelist LocationType", "ruined bridge"),
    )
    RUINED_DAM = (
        "DAMQ",
        pgettext_lazy("IATI codelist LocationType", "ruined dam"),
    )
    SABKHA_S_ = (
        "SBKH",
        pgettext_lazy("IATI codelist LocationType", "sabkha(s)"),
    )
    SADDLE = (
        "SDL",
        pgettext_lazy("IATI codelist LocationType", "saddle"),
    )
    SALT_AREA = (
        "SALT",
        pgettext_lazy("IATI codelist LocationType", "salt area"),
    )
    SALT_EVAPORATION_PONDS = (
        "MFGN",
        pgettext_lazy("IATI codelist LocationType", "salt evaporation ponds"),
    )
    SALT_LAKE = (
        "LKN",
        pgettext_lazy("IATI codelist LocationType", "salt lake"),
    )
    SALT_LAKES = (
        "LKSN",
        pgettext_lazy("IATI codelist LocationType", "salt lakes"),
    )
    SALT_MARSH = (
        "MRSHN",
        pgettext_lazy("IATI codelist LocationType", "salt marsh"),
    )
    SALT_MINE_S_ = (
        "MNN",
        pgettext_lazy("IATI codelist LocationType", "salt mine(s)"),
    )
    SALT_POND = (
        "PNDN",
        pgettext_lazy("IATI codelist LocationType", "salt pond"),
    )
    SALT_PONDS = (
        "PNDSN",
        pgettext_lazy("IATI codelist LocationType", "salt ponds"),
    )
    SANATORIUM = (
        "SNTR",
        pgettext_lazy("IATI codelist LocationType", "sanatorium"),
    )
    SAND_AREA = (
        "SAND",
        pgettext_lazy("IATI codelist LocationType", "sand area"),
    )
    SANDY_DESERT = (
        "ERG",
        pgettext_lazy("IATI codelist LocationType", "sandy desert"),
    )
    SATELLITE_STATION = (
        "STNS",
        pgettext_lazy("IATI codelist LocationType", "satellite station"),
    )
    SAWMILL = (
        "MLSW",
        pgettext_lazy("IATI codelist LocationType", "sawmill"),
    )
    SCHOOL = (
        "SCH",
        pgettext_lazy("IATI codelist LocationType", "school"),
    )
    SCHOOL_DISTRICT = (
        "ADMS",
        pgettext_lazy("IATI codelist LocationType", "school district"),
    )
    SCIENTIFIC_RESEARCH_BASE = (
        "STNB",
        pgettext_lazy("IATI codelist LocationType", "scientific research base"),
    )
    SCRUBLAND = (
        "SCRB",
        pgettext_lazy("IATI codelist LocationType", "scrubland"),
    )
    SEA = (
        "SEA",
        pgettext_lazy("IATI codelist LocationType", "sea"),
    )
    SEACHANNEL = (
        "SCNU",
        pgettext_lazy("IATI codelist LocationType", "seachannel"),
    )
    SEACHANNELS = (
        "SCSU",
        pgettext_lazy("IATI codelist LocationType", "seachannels"),
    )
    SEAMOUNT = (
        "SMU",
        pgettext_lazy("IATI codelist LocationType", "seamount"),
    )
    SEAMOUNTS = (
        "SMSU",
        pgettext_lazy("IATI codelist LocationType", "seamounts"),
    )
    SEAPLANE_LANDING_AREA = (
        "AIRS",
        pgettext_lazy("IATI codelist LocationType", "seaplane landing area"),
    )
    SEAT_OF_A_FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA",
        pgettext_lazy(
            "IATI codelist LocationType",
            "seat of a first-order administrative division",
        ),
    )
    SEAT_OF_A_FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA4",
        pgettext_lazy(
            "IATI codelist LocationType",
            "seat of a fourth-order administrative division",
        ),
    )
    SEAT_OF_A_SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA2",
        pgettext_lazy(
            "IATI codelist LocationType",
            "seat of a second-order administrative division",
        ),
    )
    SEAT_OF_A_THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA3",
        pgettext_lazy(
            "IATI codelist LocationType",
            "seat of a third-order administrative division",
        ),
    )
    SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM2",
        pgettext_lazy(
            "IATI codelist LocationType", "second-order administrative division"
        ),
    )
    SECTION_OF_BANK = (
        "BNKX",
        pgettext_lazy("IATI codelist LocationType", "section of bank"),
    )
    SECTION_OF_CANAL = (
        "CNLX",
        pgettext_lazy("IATI codelist LocationType", "section of canal"),
    )
    SECTION_OF_ESTATE = (
        "ESTX",
        pgettext_lazy("IATI codelist LocationType", "section of estate"),
    )
    SECTION_OF_HARBOR = (
        "HBRX",
        pgettext_lazy("IATI codelist LocationType", "section of harbor"),
    )
    SECTION_OF_INDEPENDENT_POLITICAL_ENTITY = (
        "PCLIX",
        pgettext_lazy(
            "IATI codelist LocationType", "section of independent political entity"
        ),
    )
    SECTION_OF_INTERMITTENT_STREAM = (
        "STMIX",
        pgettext_lazy("IATI codelist LocationType", "section of intermittent stream"),
    )
    SECTION_OF_ISLAND = (
        "ISLX",
        pgettext_lazy("IATI codelist LocationType", "section of island"),
    )
    SECTION_OF_LAGOON = (
        "LGNX",
        pgettext_lazy("IATI codelist LocationType", "section of lagoon"),
    )
    SECTION_OF_LAKE = (
        "LKX",
        pgettext_lazy("IATI codelist LocationType", "section of lake"),
    )
    SECTION_OF_PENINSULA = (
        "PENX",
        pgettext_lazy("IATI codelist LocationType", "section of peninsula"),
    )
    SECTION_OF_PLAIN = (
        "PLNX",
        pgettext_lazy("IATI codelist LocationType", "section of plain"),
    )
    SECTION_OF_PLATEAU = (
        "PLATX",
        pgettext_lazy("IATI codelist LocationType", "section of plateau"),
    )
    SECTION_OF_POPULATED_PLACE = (
        "PPLX",
        pgettext_lazy("IATI codelist LocationType", "section of populated place"),
    )
    SECTION_OF_REEF = (
        "RFX",
        pgettext_lazy("IATI codelist LocationType", "section of reef"),
    )
    SECTION_OF_STREAM = (
        "STMX",
        pgettext_lazy("IATI codelist LocationType", "section of stream"),
    )
    SECTION_OF_VALLEY = (
        "VALX",
        pgettext_lazy("IATI codelist LocationType", "section of valley"),
    )
    SECTION_OF_WADI = (
        "WADX",
        pgettext_lazy("IATI codelist LocationType", "section of wadi"),
    )
    SECTION_OF_WATERFALL_S_ = (
        "FLLSX",
        pgettext_lazy("IATI codelist LocationType", "section of waterfall(s)"),
    )
    SEMI_INDEPENDENT_POLITICAL_ENTITY = (
        "PCLS",
        pgettext_lazy(
            "IATI codelist LocationType", "semi-independent political entity"
        ),
    )
    SEWAGE_TREATMENT_PLANT = (
        "SWT",
        pgettext_lazy("IATI codelist LocationType", "sewage treatment plant"),
    )
    SHEEPFOLD = (
        "SHPF",
        pgettext_lazy("IATI codelist LocationType", "sheepfold"),
    )
    SHOAL_S_ = (
        "SHOL",
        pgettext_lazy("IATI codelist LocationType", "shoal(s)"),
    )
    SHOPPING_CENTER_OR_MALL = (
        "SHOPC",
        pgettext_lazy("IATI codelist LocationType", "shopping center or mall"),
    )
    SHORE = (
        "SHOR",
        pgettext_lazy("IATI codelist LocationType", "shore"),
    )
    SHRINE = (
        "SHRN",
        pgettext_lazy("IATI codelist LocationType", "shrine"),
    )
    SILL = (
        "SILL",
        pgettext_lazy("IATI codelist LocationType", "sill"),
    )
    SINKHOLE = (
        "SINK",
        pgettext_lazy("IATI codelist LocationType", "sinkhole"),
    )
    SISAL_PLANTATION = (
        "ESTSL",
        pgettext_lazy("IATI codelist LocationType", "sisal plantation"),
    )
    SLIDE = (
        "SLID",
        pgettext_lazy("IATI codelist LocationType", "slide"),
    )
    SLOPE_S_ = (
        "SLP",
        pgettext_lazy("IATI codelist LocationType", "slope(s)"),
    )
    SLUICE = (
        "SLCE",
        pgettext_lazy("IATI codelist LocationType", "sluice"),
    )
    SNOWFIELD = (
        "SNOW",
        pgettext_lazy("IATI codelist LocationType", "snowfield"),
    )
    SOUND = (
        "SD",
        pgettext_lazy("IATI codelist LocationType", "sound"),
    )
    SPA = (
        "SPA",
        pgettext_lazy("IATI codelist LocationType", "spa"),
    )
    SPACE_CENTER = (
        "CTRS",
        pgettext_lazy("IATI codelist LocationType", "space center"),
    )
    SPILLWAY = (
        "SPLY",
        pgettext_lazy("IATI codelist LocationType", "spillway"),
    )
    SPIT = (
        "SPIT",
        pgettext_lazy("IATI codelist LocationType", "spit"),
    )
    SPRING_S_ = (
        "SPNG",
        pgettext_lazy("IATI codelist LocationType", "spring(s)"),
    )
    SPUR_S_ = (
        "SPUR",
        pgettext_lazy("IATI codelist LocationType", "spur(s)"),
    )
    SQUARE = (
        "SQR",
        pgettext_lazy("IATI codelist LocationType", "square"),
    )
    STABLE = (
        "STBL",
        pgettext_lazy("IATI codelist LocationType", "stable"),
    )
    STADIUM = (
        "STDM",
        pgettext_lazy("IATI codelist LocationType", "stadium"),
    )
    STEPS = (
        "STPS",
        pgettext_lazy("IATI codelist LocationType", "steps"),
    )
    STOCK_ROUTE = (
        "STKR",
        pgettext_lazy("IATI codelist LocationType", "stock route"),
    )
    STONY_DESERT = (
        "REG",
        pgettext_lazy("IATI codelist LocationType", "stony desert"),
    )
    STORE = (
        "RET",
        pgettext_lazy("IATI codelist LocationType", "store"),
    )
    STOREHOUSE = (
        "SHSE",
        pgettext_lazy("IATI codelist LocationType", "storehouse"),
    )
    STRAIT = (
        "STRT",
        pgettext_lazy("IATI codelist LocationType", "strait"),
    )
    STREAM = (
        "STM",
        pgettext_lazy("IATI codelist LocationType", "stream"),
    )
    STREAM_BANK = (
        "BNKR",
        pgettext_lazy("IATI codelist LocationType", "stream bank"),
    )
    STREAM_BEND = (
        "STMB",
        pgettext_lazy("IATI codelist LocationType", "stream bend"),
    )
    STREAM_GAUGING_STATION = (
        "STMGS",
        pgettext_lazy("IATI codelist LocationType", "stream gauging station"),
    )
    STREAM_MOUTH_S_ = (
        "STMM",
        pgettext_lazy("IATI codelist LocationType", "stream mouth(s)"),
    )
    STREAMS = (
        "STMS",
        pgettext_lazy("IATI codelist LocationType", "streams"),
    )
    STREET = (
        "ST",
        pgettext_lazy("IATI codelist LocationType", "street"),
    )
    SUB_SURFACE_DAM = (
        "DAMSB",
        pgettext_lazy("IATI codelist LocationType", "sub-surface dam"),
    )
    SUBWAY = (
        "SUBW",
        pgettext_lazy("IATI codelist LocationType", "subway"),
    )
    SUBWAY_STATION = (
        "SUBS",
        pgettext_lazy("IATI codelist LocationType", "subway station"),
    )
    SUGAR_MILL = (
        "MLSG",
        pgettext_lazy("IATI codelist LocationType", "sugar mill"),
    )
    SUGAR_PLANTATION = (
        "ESTSG",
        pgettext_lazy("IATI codelist LocationType", "sugar plantation"),
    )
    SUGAR_REFINERY = (
        "MFGSG",
        pgettext_lazy("IATI codelist LocationType", "sugar refinery"),
    )
    SULPHUR_SPRING_S_ = (
        "SPNS",
        pgettext_lazy("IATI codelist LocationType", "sulphur spring(s)"),
    )
    SWAMP = (
        "SWMP",
        pgettext_lazy("IATI codelist LocationType", "swamp"),
    )
    SYNAGOGUE = (
        "SYG",
        pgettext_lazy("IATI codelist LocationType", "synagogue"),
    )
    TABLEMOUNT__OR_GUYOT_ = (
        "TMTU",
        pgettext_lazy("IATI codelist LocationType", "tablemount (or guyot)"),
    )
    TABLEMOUNTS__OR_GUYOTS_ = (
        "TMSU",
        pgettext_lazy("IATI codelist LocationType", "tablemounts (or guyots)"),
    )
    TALUS_SLOPE = (
        "TAL",
        pgettext_lazy("IATI codelist LocationType", "talus slope"),
    )
    TANK_FARM = (
        "OILT",
        pgettext_lazy("IATI codelist LocationType", "tank farm"),
    )
    TEA_PLANTATION = (
        "ESTT",
        pgettext_lazy("IATI codelist LocationType", "tea plantation"),
    )
    TECHNICAL_SCHOOL = (
        "SCHT",
        pgettext_lazy("IATI codelist LocationType", "technical school"),
    )
    TEMPLE_S_ = (
        "TMPL",
        pgettext_lazy("IATI codelist LocationType", "temple(s)"),
    )
    TERMINAL = (
        "AIRT",
        pgettext_lazy("IATI codelist LocationType", "terminal"),
    )
    TERRACE = (
        "TRR",
        pgettext_lazy("IATI codelist LocationType", "terrace"),
    )
    TERRITORY = (
        "TERR",
        pgettext_lazy("IATI codelist LocationType", "territory"),
    )
    THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM3",
        pgettext_lazy(
            "IATI codelist LocationType", "third-order administrative division"
        ),
    )
    TIDAL_CREEK_S_ = (
        "CRKT",
        pgettext_lazy("IATI codelist LocationType", "tidal creek(s)"),
    )
    TIDAL_FLAT_S_ = (
        "FLTT",
        pgettext_lazy("IATI codelist LocationType", "tidal flat(s)"),
    )
    TIN_MINE_S_ = (
        "MNSN",
        pgettext_lazy("IATI codelist LocationType", "tin mine(s)"),
    )
    TOLL_GATE_BARRIER = (
        "TOLL",
        pgettext_lazy("IATI codelist LocationType", "toll gate/barrier"),
    )
    TOMB_S_ = (
        "TMB",
        pgettext_lazy("IATI codelist LocationType", "tomb(s)"),
    )
    TOWER = (
        "TOWR",
        pgettext_lazy("IATI codelist LocationType", "tower"),
    )
    TRAFFIC_CIRCLE = (
        "RDCR",
        pgettext_lazy("IATI codelist LocationType", "traffic circle"),
    )
    TRAIL = (
        "TRL",
        pgettext_lazy("IATI codelist LocationType", "trail"),
    )
    TRANSIT_TERMINAL = (
        "TRANT",
        pgettext_lazy("IATI codelist LocationType", "transit terminal"),
    )
    TREE_S_ = (
        "TREE",
        pgettext_lazy("IATI codelist LocationType", "tree(s)"),
    )
    TRIANGULATION_STATION = (
        "TRIG",
        pgettext_lazy("IATI codelist LocationType", "triangulation station"),
    )
    TRIBAL_AREA = (
        "TRB",
        pgettext_lazy("IATI codelist LocationType", "tribal area"),
    )
    TUNDRA = (
        "TUND",
        pgettext_lazy("IATI codelist LocationType", "tundra"),
    )
    TUNNEL = (
        "TNL",
        pgettext_lazy("IATI codelist LocationType", "tunnel"),
    )
    TUNNELS = (
        "TNLS",
        pgettext_lazy("IATI codelist LocationType", "tunnels"),
    )
    UNDERGROUND_IRRIGATION_CANAL_S_ = (
        "CNLSB",
        pgettext_lazy("IATI codelist LocationType", "underground irrigation canal(s)"),
    )
    UNDERGROUND_LAKE = (
        "LKSB",
        pgettext_lazy("IATI codelist LocationType", "underground lake"),
    )
    UNDERSEA_APRON = (
        "APNU",
        pgettext_lazy("IATI codelist LocationType", "undersea apron"),
    )
    UNDERSEA_ARCH = (
        "ARCU",
        pgettext_lazy("IATI codelist LocationType", "undersea arch"),
    )
    UNDERSEA_ARRUGADO = (
        "ARRU",
        pgettext_lazy("IATI codelist LocationType", "undersea arrugado"),
    )
    UNDERSEA_BANK = (
        "BNKU",
        pgettext_lazy("IATI codelist LocationType", "undersea bank"),
    )
    UNDERSEA_BANKS = (
        "BKSU",
        pgettext_lazy("IATI codelist LocationType", "undersea banks"),
    )
    UNDERSEA_BASIN = (
        "BSNU",
        pgettext_lazy("IATI codelist LocationType", "undersea basin"),
    )
    UNDERSEA_BENCH = (
        "BNCU",
        pgettext_lazy("IATI codelist LocationType", "undersea bench"),
    )
    UNDERSEA_BORDERLAND = (
        "BDLU",
        pgettext_lazy("IATI codelist LocationType", "undersea borderland"),
    )
    UNDERSEA_CANYON = (
        "CNYU",
        pgettext_lazy("IATI codelist LocationType", "undersea canyon"),
    )
    UNDERSEA_CANYONS = (
        "CNSU",
        pgettext_lazy("IATI codelist LocationType", "undersea canyons"),
    )
    UNDERSEA_CORDILLERA = (
        "CDAU",
        pgettext_lazy("IATI codelist LocationType", "undersea cordillera"),
    )
    UNDERSEA_ESCARPMENT__OR_SCARP_ = (
        "ESCU",
        pgettext_lazy("IATI codelist LocationType", "undersea escarpment (or scarp)"),
    )
    UNDERSEA_FAN = (
        "FANU",
        pgettext_lazy("IATI codelist LocationType", "undersea fan"),
    )
    UNDERSEA_FLAT = (
        "FLTU",
        pgettext_lazy("IATI codelist LocationType", "undersea flat"),
    )
    UNDERSEA_FORK = (
        "FRKU",
        pgettext_lazy("IATI codelist LocationType", "undersea fork"),
    )
    UNDERSEA_FORKS = (
        "FRSU",
        pgettext_lazy("IATI codelist LocationType", "undersea forks"),
    )
    UNDERSEA_FRACTURE_ZONE = (
        "FRZU",
        pgettext_lazy("IATI codelist LocationType", "undersea fracture zone"),
    )
    UNDERSEA_FURROW = (
        "FURU",
        pgettext_lazy("IATI codelist LocationType", "undersea furrow"),
    )
    UNDERSEA_GAP = (
        "GAPU",
        pgettext_lazy("IATI codelist LocationType", "undersea gap"),
    )
    UNDERSEA_GULLY = (
        "GLYU",
        pgettext_lazy("IATI codelist LocationType", "undersea gully"),
    )
    UNDERSEA_HILL = (
        "HLLU",
        pgettext_lazy("IATI codelist LocationType", "undersea hill"),
    )
    UNDERSEA_HILLS = (
        "HLSU",
        pgettext_lazy("IATI codelist LocationType", "undersea hills"),
    )
    UNDERSEA_HOLE = (
        "HOLU",
        pgettext_lazy("IATI codelist LocationType", "undersea hole"),
    )
    UNDERSEA_KNOLL = (
        "KNLU",
        pgettext_lazy("IATI codelist LocationType", "undersea knoll"),
    )
    UNDERSEA_KNOLLS = (
        "KNSU",
        pgettext_lazy("IATI codelist LocationType", "undersea knolls"),
    )
    UNDERSEA_LEDGE = (
        "LDGU",
        pgettext_lazy("IATI codelist LocationType", "undersea ledge"),
    )
    UNDERSEA_LEVEE = (
        "LEVU",
        pgettext_lazy("IATI codelist LocationType", "undersea levee"),
    )
    UNDERSEA_MEDIAN_VALLEY = (
        "MDVU",
        pgettext_lazy("IATI codelist LocationType", "undersea median valley"),
    )
    UNDERSEA_MESA = (
        "MESU",
        pgettext_lazy("IATI codelist LocationType", "undersea mesa"),
    )
    UNDERSEA_MOAT = (
        "MOTU",
        pgettext_lazy("IATI codelist LocationType", "undersea moat"),
    )
    UNDERSEA_MOUND = (
        "MNDU",
        pgettext_lazy("IATI codelist LocationType", "undersea mound"),
    )
    UNDERSEA_MOUNTAIN = (
        "MTU",
        pgettext_lazy("IATI codelist LocationType", "undersea mountain"),
    )
    UNDERSEA_MOUNTAINS = (
        "MTSU",
        pgettext_lazy("IATI codelist LocationType", "undersea mountains"),
    )
    UNDERSEA_PEAK = (
        "PKU",
        pgettext_lazy("IATI codelist LocationType", "undersea peak"),
    )
    UNDERSEA_PEAKS = (
        "PKSU",
        pgettext_lazy("IATI codelist LocationType", "undersea peaks"),
    )
    UNDERSEA_PINNACLE = (
        "PNLU",
        pgettext_lazy("IATI codelist LocationType", "undersea pinnacle"),
    )
    UNDERSEA_PLAIN = (
        "PLNU",
        pgettext_lazy("IATI codelist LocationType", "undersea plain"),
    )
    UNDERSEA_PLATEAU = (
        "PLTU",
        pgettext_lazy("IATI codelist LocationType", "undersea plateau"),
    )
    UNDERSEA_PLATFORM = (
        "PLFU",
        pgettext_lazy("IATI codelist LocationType", "undersea platform"),
    )
    UNDERSEA_PROVINCE = (
        "PRVU",
        pgettext_lazy("IATI codelist LocationType", "undersea province"),
    )
    UNDERSEA_RAMP = (
        "RMPU",
        pgettext_lazy("IATI codelist LocationType", "undersea ramp"),
    )
    UNDERSEA_RANGE = (
        "RNGU",
        pgettext_lazy("IATI codelist LocationType", "undersea range"),
    )
    UNDERSEA_RAVINE = (
        "RAVU",
        pgettext_lazy("IATI codelist LocationType", "undersea ravine"),
    )
    UNDERSEA_REEF = (
        "RFU",
        pgettext_lazy("IATI codelist LocationType", "undersea reef"),
    )
    UNDERSEA_REEFS = (
        "RFSU",
        pgettext_lazy("IATI codelist LocationType", "undersea reefs"),
    )
    UNDERSEA_RIDGE = (
        "RDGU",
        pgettext_lazy("IATI codelist LocationType", "undersea ridge"),
    )
    UNDERSEA_RIDGES = (
        "RDSU",
        pgettext_lazy("IATI codelist LocationType", "undersea ridges"),
    )
    UNDERSEA_RISE = (
        "RISU",
        pgettext_lazy("IATI codelist LocationType", "undersea rise"),
    )
    UNDERSEA_SADDLE = (
        "SDLU",
        pgettext_lazy("IATI codelist LocationType", "undersea saddle"),
    )
    UNDERSEA_SHELF = (
        "SHFU",
        pgettext_lazy("IATI codelist LocationType", "undersea shelf"),
    )
    UNDERSEA_SHELF_EDGE = (
        "EDGU",
        pgettext_lazy("IATI codelist LocationType", "undersea shelf edge"),
    )
    UNDERSEA_SHELF_VALLEY = (
        "SHVU",
        pgettext_lazy("IATI codelist LocationType", "undersea shelf valley"),
    )
    UNDERSEA_SHOAL = (
        "SHLU",
        pgettext_lazy("IATI codelist LocationType", "undersea shoal"),
    )
    UNDERSEA_SHOALS = (
        "SHSU",
        pgettext_lazy("IATI codelist LocationType", "undersea shoals"),
    )
    UNDERSEA_SILL = (
        "SILU",
        pgettext_lazy("IATI codelist LocationType", "undersea sill"),
    )
    UNDERSEA_SLOPE = (
        "SLPU",
        pgettext_lazy("IATI codelist LocationType", "undersea slope"),
    )
    UNDERSEA_SPUR = (
        "SPRU",
        pgettext_lazy("IATI codelist LocationType", "undersea spur"),
    )
    UNDERSEA_TERRACE = (
        "TERU",
        pgettext_lazy("IATI codelist LocationType", "undersea terrace"),
    )
    UNDERSEA_TONGUE = (
        "TNGU",
        pgettext_lazy("IATI codelist LocationType", "undersea tongue"),
    )
    UNDERSEA_TRENCH = (
        "TRNU",
        pgettext_lazy("IATI codelist LocationType", "undersea trench"),
    )
    UNDERSEA_TROUGH = (
        "TRGU",
        pgettext_lazy("IATI codelist LocationType", "undersea trough"),
    )
    UNDERSEA_VALLEY = (
        "VALU",
        pgettext_lazy("IATI codelist LocationType", "undersea valley"),
    )
    UNDERSEA_VALLEYS = (
        "VLSU",
        pgettext_lazy("IATI codelist LocationType", "undersea valleys"),
    )
    UNITED_STATES_GOVERNMENT_ESTABLISHMENT = (
        "USGE",
        pgettext_lazy(
            "IATI codelist LocationType", "United States Government Establishment"
        ),
    )
    UPLAND = (
        "UPLD",
        pgettext_lazy("IATI codelist LocationType", "upland"),
    )
    VALLEY = (
        "VAL",
        pgettext_lazy("IATI codelist LocationType", "valley"),
    )
    VALLEYS = (
        "VALS",
        pgettext_lazy("IATI codelist LocationType", "valleys"),
    )
    VETERINARY_FACILITY = (
        "VETF",
        pgettext_lazy("IATI codelist LocationType", "veterinary facility"),
    )
    VINEYARD = (
        "VIN",
        pgettext_lazy("IATI codelist LocationType", "vineyard"),
    )
    VINEYARDS = (
        "VINS",
        pgettext_lazy("IATI codelist LocationType", "vineyards"),
    )
    VOLCANO = (
        "VLC",
        pgettext_lazy("IATI codelist LocationType", "volcano"),
    )
    WADI = (
        "WAD",
        pgettext_lazy("IATI codelist LocationType", "wadi"),
    )
    WADI_BEND = (
        "WADB",
        pgettext_lazy("IATI codelist LocationType", "wadi bend"),
    )
    WADI_JUNCTION = (
        "WADJ",
        pgettext_lazy("IATI codelist LocationType", "wadi junction"),
    )
    WADI_MOUTH = (
        "WADM",
        pgettext_lazy("IATI codelist LocationType", "wadi mouth"),
    )
    WADIES = (
        "WADS",
        pgettext_lazy("IATI codelist LocationType", "wadies"),
    )
    WALL = (
        "WALL",
        pgettext_lazy("IATI codelist LocationType", "wall"),
    )
    WATER_MILL = (
        "MLWTR",
        pgettext_lazy("IATI codelist LocationType", "water mill"),
    )
    WATER_PUMPING_STATION = (
        "PMPW",
        pgettext_lazy("IATI codelist LocationType", "water pumping station"),
    )
    WATER_TANK = (
        "RSVT",
        pgettext_lazy("IATI codelist LocationType", "water tank"),
    )
    WATERCOURSE = (
        "WTRC",
        pgettext_lazy("IATI codelist LocationType", "watercourse"),
    )
    WATERFALL_S_ = (
        "FLLS",
        pgettext_lazy("IATI codelist LocationType", "waterfall(s)"),
    )
    WATERHOLE_S_ = (
        "WTRH",
        pgettext_lazy("IATI codelist LocationType", "waterhole(s)"),
    )
    WATERWORKS = (
        "WTRW",
        pgettext_lazy("IATI codelist LocationType", "waterworks"),
    )
    WEIR_S_ = (
        "WEIR",
        pgettext_lazy("IATI codelist LocationType", "weir(s)"),
    )
    WELL = (
        "WLL",
        pgettext_lazy("IATI codelist LocationType", "well"),
    )
    WELLS = (
        "WLLS",
        pgettext_lazy("IATI codelist LocationType", "wells"),
    )
    WETLAND = (
        "WTLD",
        pgettext_lazy("IATI codelist LocationType", "wetland"),
    )
    WHALING_STATION = (
        "STNW",
        pgettext_lazy("IATI codelist LocationType", "whaling station"),
    )
    WHARF__VES_ = (
        "WHRF",
        pgettext_lazy("IATI codelist LocationType", "wharf(-ves)"),
    )
    WHIRLPOOL = (
        "WHRL",
        pgettext_lazy("IATI codelist LocationType", "whirlpool"),
    )
    WILDLIFE_RESERVE = (
        "RESW",
        pgettext_lazy("IATI codelist LocationType", "wildlife reserve"),
    )
    WINDMILL = (
        "MLWND",
        pgettext_lazy("IATI codelist LocationType", "windmill"),
    )
    WRECK = (
        "WRCK",
        pgettext_lazy("IATI codelist LocationType", "wreck"),
    )
    ZONE = (
        "ZN",
        pgettext_lazy("IATI codelist LocationType", "zone"),
    )
    ZOO = (
        "ZOO",
        pgettext_lazy("IATI codelist LocationType", "zoo"),
    )
