from django.db import models
from django.utils.translation import pgettext_lazy


class LocationTypeDescription(models.TextChoices):
    """
    US NGA Feature Designation Codes On this codelist 'category' is used for the Feature Class.
    """

    ABANDONED_AIRFIELD = (
        "AIRQ",
        pgettext_lazy("LocationType description", "abandoned airfield"),
    )
    ABANDONED_CAMP = (
        "CMPQ",
        pgettext_lazy("LocationType description", "abandoned camp"),
    )
    ABANDONED_CANAL = (
        "CNLQ",
        pgettext_lazy("LocationType description", "abandoned canal"),
    )
    ABANDONED_FACTORY = (
        "MFGQ",
        pgettext_lazy("LocationType description", "abandoned factory"),
    )
    ABANDONED_FARM = (
        "FRMQ",
        pgettext_lazy("LocationType description", "abandoned farm"),
    )
    ABANDONED_MINE = (
        "MNQ",
        pgettext_lazy("LocationType description", "abandoned mine"),
    )
    ABANDONED_MISSION = (
        "MSSNQ",
        pgettext_lazy("LocationType description", "abandoned mission"),
    )
    ABANDONED_OIL_WELL = (
        "OILQ",
        pgettext_lazy("LocationType description", "abandoned oil well"),
    )
    ABANDONED_POLICE_POST = (
        "PPQ",
        pgettext_lazy("LocationType description", "abandoned police post"),
    )
    ABANDONED_POPULATED_PLACE = (
        "PPLQ",
        pgettext_lazy("LocationType description", "abandoned populated place"),
    )
    ABANDONED_PRISON = (
        "PRNQ",
        pgettext_lazy("LocationType description", "abandoned prison"),
    )
    ABANDONED_RAILROAD = (
        "RRQ",
        pgettext_lazy("LocationType description", "abandoned railroad"),
    )
    ABANDONED_RAILROAD_STATION = (
        "RSTNQ",
        pgettext_lazy("LocationType description", "abandoned railroad station"),
    )
    ABANDONED_RAILROAD_STOP = (
        "RSTPQ",
        pgettext_lazy("LocationType description", "abandoned railroad stop"),
    )
    ABANDONED_WATERCOURSE = (
        "STMQ",
        pgettext_lazy(
            "LocationType description",
            "a former stream or distributary no longer carrying flowing water, but still evident due to lakes, wetland, topographic or vegetation patterns",
        ),
    )
    ABANDONED_WELL = (
        "WLLQ",
        pgettext_lazy("LocationType description", "abandoned well"),
    )
    ADMINISTRATIVE_DIVISION = (
        "ADMD",
        pgettext_lazy(
            "LocationType description",
            "an administrative division of a political entity, undifferentiated as to administrative level",
        ),
    )
    ADMINISTRATIVE_FACILITY = (
        "ADMF",
        pgettext_lazy("LocationType description", "a government building"),
    )
    AGRICULTURAL_COLONY = (
        "AGRC",
        pgettext_lazy(
            "LocationType description",
            "a tract of land set aside for agricultural settlement",
        ),
    )
    AGRICULTURAL_FACILITY = (
        "AGRF",
        pgettext_lazy(
            "LocationType description",
            "a building and/or tract of land used for improving agriculture",
        ),
    )
    AGRICULTURAL_RESERVE = (
        "RESA",
        pgettext_lazy(
            "LocationType description",
            "a tract of land reserved for agricultural reclamation and/or development",
        ),
    )
    AGRICULTURAL_SCHOOL = (
        "SCHA",
        pgettext_lazy(
            "LocationType description",
            "a school with a curriculum focused on agriculture",
        ),
    )
    AIRBASE = (
        "AIRB",
        pgettext_lazy(
            "LocationType description",
            "an area used to store supplies, provide barracks for air force personnel, hangars and runways for aircraft, and from which operations are initiated",
        ),
    )
    AIRFIELD = (
        "AIRF",
        pgettext_lazy(
            "LocationType description",
            "a place on land where aircraft land and take off; no facilities provided for the commercial handling of passengers and cargo",
        ),
    )
    AIRPORT = (
        "AIRP",
        pgettext_lazy(
            "LocationType description",
            "a place where aircraft regularly land and take off, with runways, navigational aids, and major facilities for the commercial handling of passengers and cargo",
        ),
    )
    AMPHITHEATER = (
        "AMTH",
        pgettext_lazy(
            "LocationType description",
            "an oval or circular structure with rising tiers of seats about a stage or open space",
        ),
    )
    ANABRANCH = (
        "STMA",
        pgettext_lazy(
            "LocationType description",
            "a diverging branch flowing out of a main stream and rejoining it downstream",
        ),
    )
    ANCHORAGE = (
        "ANCH",
        pgettext_lazy("LocationType description", "an area where vessels may anchor"),
    )
    ANCIENT_ROAD = (
        "RDA",
        pgettext_lazy(
            "LocationType description",
            "the remains of a road used by ancient cultures",
        ),
    )
    ANCIENT_SITE = (
        "ANS",
        pgettext_lazy(
            "LocationType description",
            "a place where archeological remains, old structures, or cultural artifacts are located",
        ),
    )
    ANCIENT_WALL = (
        "WALLA",
        pgettext_lazy(
            "LocationType description",
            "the remains of a linear defensive stone structure",
        ),
    )
    APARTMENT_BUILDING = (
        "BLDA",
        pgettext_lazy(
            "LocationType description",
            "a building containing several individual apartments",
        ),
    )
    AQUACULTURE_FACILITY = (
        "AQC",
        pgettext_lazy(
            "LocationType description",
            "facility or area for the cultivation of aquatic animals and plants, especially fish, shellfish, and seaweed, in natural or controlled marine or freshwater environments; underwater agriculture",
        ),
    )
    AQUEDUCT = (
        "CNLA",
        pgettext_lazy("LocationType description", "a conduit used to carry water"),
    )
    ARCH = (
        "ARCH",
        pgettext_lazy(
            "LocationType description",
            "a natural or man-made structure in the form of an arch",
        ),
    )
    ARCTIC_LAND = (
        "LAND",
        pgettext_lazy("LocationType description", "a tract of land in the Arctic"),
    )
    AREA = (
        "AREA",
        pgettext_lazy(
            "LocationType description",
            "a tract of land without homogeneous character or boundaries",
        ),
    )
    ARTIFICIAL_ISLAND = (
        "ISLF",
        pgettext_lazy(
            "LocationType description",
            "an island created by landfill or diking and filling in a wetland, bay, or lagoon",
        ),
    )
    ARTILLERY_RANGE = (
        "RNGA",
        pgettext_lazy(
            "LocationType description",
            "a tract of land used for artillery firing practice",
        ),
    )
    ASPHALT_LAKE = (
        "ASPH",
        pgettext_lazy(
            "LocationType description",
            "a small basin containing naturally occurring asphalt",
        ),
    )
    ASTRONOMICAL_STATION = (
        "ASTR",
        pgettext_lazy(
            "LocationType description",
            "a point on the earth whose position has been determined by observations of celestial bodies",
        ),
    )
    ASYLUM = (
        "ASYL",
        pgettext_lazy(
            "LocationType description",
            "a facility where the insane are cared for and protected",
        ),
    )
    ATHLETIC_FIELD = (
        "ATHF",
        pgettext_lazy(
            "LocationType description",
            "a tract of land used for playing team sports, and athletic track and field events",
        ),
    )
    ATOLL_S_ = (
        "ATOL",
        pgettext_lazy(
            "LocationType description",
            "a ring-shaped coral reef which has closely spaced islands on it encircling a lagoon",
        ),
    )
    ATOMIC_CENTER = (
        "CTRA",
        pgettext_lazy(
            "LocationType description",
            "a facility where atomic research is carried out",
        ),
    )
    BADLANDS = (
        "BDLD",
        pgettext_lazy(
            "LocationType description",
            "an area characterized by a maze of very closely spaced, deep, narrow, steep-sided ravines, and sharp crests and pinnacles",
        ),
    )
    BALING_STATION = (
        "BSTN",
        pgettext_lazy(
            "LocationType description",
            "a facility for baling agricultural products",
        ),
    )
    BANANA_PLANTATION = (
        "ESTB",
        pgettext_lazy(
            "LocationType description",
            "an estate that specializes in the growing of bananas",
        ),
    )
    BANK = (
        "BAN",
        pgettext_lazy(
            "LocationType description",
            "an establishment for the custody, loan, exchange or issue of money, for the extension of credit, and for facilitating the transmission of funds",
        ),
    )
    BANK_S_ = (
        "BNK",
        pgettext_lazy(
            "LocationType description",
            "an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for most surface navigation",
        ),
    )
    BAR = (
        "BAR",
        pgettext_lazy(
            "LocationType description",
            "a shallow ridge or mound of coarse unconsolidated material in a stream channel, at the mouth of a stream, estuary, or lagoon and in the wave-break zone along coasts",
        ),
    )
    BARRACKS = (
        "BRKS",
        pgettext_lazy(
            "LocationType description",
            "a building for lodging military personnel",
        ),
    )
    BATTLEFIELD = (
        "BTL",
        pgettext_lazy(
            "LocationType description",
            "a site of a land battle of historical importance",
        ),
    )
    BAY = (
        "BAY",
        pgettext_lazy(
            "LocationType description",
            "a coastal indentation between two capes or headlands, larger than a cove but smaller than a gulf",
        ),
    )
    BAYS = (
        "BAYS",
        pgettext_lazy(
            "LocationType description",
            "coastal indentations between two capes or headlands, larger than a cove but smaller than a gulf",
        ),
    )
    BEACH = (
        "BCH",
        pgettext_lazy(
            "LocationType description",
            "a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves",
        ),
    )
    BEACH_RIDGE = (
        "RDGB",
        pgettext_lazy(
            "LocationType description",
            "a ridge of sand just inland and parallel to the beach, usually in series",
        ),
    )
    BEACHES = (
        "BCHS",
        pgettext_lazy(
            "LocationType description",
            "a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves",
        ),
    )
    BEACON = (
        "BCN",
        pgettext_lazy(
            "LocationType description",
            "a fixed artificial navigation mark",
        ),
    )
    BENCH = (
        "BNCH",
        pgettext_lazy(
            "LocationType description",
            "a long, narrow bedrock platform bounded by steeper slopes above and below, usually overlooking a waterbody",
        ),
    )
    BIGHT_S_ = (
        "BGHT",
        pgettext_lazy(
            "LocationType description",
            "an open body of water forming a slight recession in a coastline",
        ),
    )
    BLOWHOLE_S_ = (
        "BLHL",
        pgettext_lazy(
            "LocationType description",
            "a hole in coastal rock through which sea water is forced by a rising tide or waves and spurted through an outlet into the air",
        ),
    )
    BLOWOUT_S_ = (
        "BLOW",
        pgettext_lazy(
            "LocationType description",
            "a small depression in sandy terrain, caused by wind erosion",
        ),
    )
    BOATYARD = (
        "BTYD",
        pgettext_lazy(
            "LocationType description",
            "a waterside facility for servicing, repairing, and building small vessels",
        ),
    )
    BOG_S_ = (
        "BOG",
        pgettext_lazy(
            "LocationType description",
            "a wetland characterized by peat forming sphagnum moss, sedge, and other acid-water plants",
        ),
    )
    BORDER_POST = (
        "PSTB",
        pgettext_lazy(
            "LocationType description",
            "a post or station at an international boundary for the regulation of movement of people and goods",
        ),
    )
    BOULDER_FIELD = (
        "BLDR",
        pgettext_lazy(
            "LocationType description",
            "a high altitude or high latitude bare, flat area covered with large angular rocks",
        ),
    )
    BOUNDARY_MARKER = (
        "BP",
        pgettext_lazy(
            "LocationType description",
            "a fixture marking a point along a boundary",
        ),
    )
    BREAKWATER = (
        "BRKW",
        pgettext_lazy(
            "LocationType description",
            "a structure erected to break the force of waves at the entrance to a harbor or port",
        ),
    )
    BREWERY = (
        "MFGB",
        pgettext_lazy(
            "LocationType description",
            "one or more buildings where beer is brewed",
        ),
    )
    BRIDGE = (
        "BDG",
        pgettext_lazy(
            "LocationType description",
            "a structure erected across an obstacle such as a stream, road, etc., in order to carry roads, railroads, and pedestrians across",
        ),
    )
    BUFFER_ZONE = (
        "ZNB",
        pgettext_lazy(
            "LocationType description",
            "a zone recognized as a buffer between two nations in which military presence is minimal or absent",
        ),
    )
    BUILDING_S_ = (
        "BLDG",
        pgettext_lazy(
            "LocationType description",
            "a structure built for permanent use, as a house, factory, etc.",
        ),
    )
    BURIAL_CAVE_S_ = (
        "BUR",
        pgettext_lazy("LocationType description", "a cave used for human burials"),
    )
    BUSH_ES_ = (
        "BUSH",
        pgettext_lazy(
            "LocationType description",
            "a small clump of conspicuous bushes in an otherwise bare area",
        ),
    )
    BUSINESS_CENTER = (
        "CTRB",
        pgettext_lazy(
            "LocationType description",
            "a place where a number of businesses are located",
        ),
    )
    BUTTE_S_ = (
        "BUTE",
        pgettext_lazy(
            "LocationType description",
            "a small, isolated, usually flat-topped hill with steep sides",
        ),
    )
    CAIRN = (
        "CARN",
        pgettext_lazy(
            "LocationType description",
            "a heap of stones erected as a landmark or for other purposes",
        ),
    )
    CALDERA = (
        "CLDA",
        pgettext_lazy(
            "LocationType description",
            "a depression measuring kilometers across formed by the collapse of a volcanic mountain",
        ),
    )
    CAMP_S_ = (
        "CMP",
        pgettext_lazy(
            "LocationType description",
            "a site occupied by tents, huts, or other shelters for temporary use",
        ),
    )
    CANAL = (
        "CNL",
        pgettext_lazy("LocationType description", "an artificial watercourse"),
    )
    CANAL_BEND = (
        "CNLB",
        pgettext_lazy(
            "LocationType description",
            "a conspicuously curved or bent section of a canal",
        ),
    )
    CANAL_TUNNEL = (
        "TNLC",
        pgettext_lazy(
            "LocationType description",
            "a tunnel through which a canal passes",
        ),
    )
    CANALIZED_STREAM = (
        "STMC",
        pgettext_lazy(
            "LocationType description",
            "a stream that has been substantially ditched, diked, or straightened",
        ),
    )
    CANNERY = (
        "MFGC",
        pgettext_lazy(
            "LocationType description",
            "a building where food items are canned",
        ),
    )
    CANYON = (
        "CNYN",
        pgettext_lazy(
            "LocationType description",
            "a deep, narrow valley with steep sides cutting into a plateau or mountainous area",
        ),
    )
    CAPE = (
        "CAPE",
        pgettext_lazy(
            "LocationType description",
            "a land area, more prominent than a point, projecting into the sea and marking a notable change in coastal direction",
        ),
    )
    CAPITAL_OF_A_POLITICAL_ENTITY = (
        "PPLC",
        pgettext_lazy("LocationType description", "capital of a political entity"),
    )
    CARAVAN_ROUTE = (
        "RTE",
        pgettext_lazy("LocationType description", "the route taken by caravans"),
    )
    CASINO = (
        "CSNO",
        pgettext_lazy(
            "LocationType description",
            "a building used for entertainment, especially gambling",
        ),
    )
    CASTLE = (
        "CSTL",
        pgettext_lazy(
            "LocationType description",
            "a large fortified building or set of buildings",
        ),
    )
    CATTLE_DIPPING_TANK = (
        "TNKD",
        pgettext_lazy(
            "LocationType description",
            "a small artificial pond used for immersing cattle in chemically treated water for disease control",
        ),
    )
    CAUSEWAY = (
        "CSWY",
        pgettext_lazy(
            "LocationType description",
            "a raised roadway across wet ground or shallow water",
        ),
    )
    CAVE_S_ = (
        "CAVE",
        pgettext_lazy(
            "LocationType description",
            "an underground passageway or chamber, or cavity on the side of a cliff",
        ),
    )
    CEMETERY = (
        "CMTY",
        pgettext_lazy("LocationType description", "a burial place or ground"),
    )
    CHANNEL = (
        "CHN",
        pgettext_lazy(
            "LocationType description",
            "the deepest part of a stream, bay, lagoon, or strait, through which the main current flows",
        ),
    )
    CHROME_MINE_S_ = (
        "MNCR",
        pgettext_lazy(
            "LocationType description",
            "a mine where chrome ore is extracted",
        ),
    )
    CHURCH = (
        "CH",
        pgettext_lazy(
            "LocationType description",
            "a building for public Christian worship",
        ),
    )
    CIRQUE = (
        "CRQ",
        pgettext_lazy(
            "LocationType description",
            "a bowl-like hollow partially surrounded by cliffs or steep slopes at the head of a glaciated valley",
        ),
    )
    CIRQUES = (
        "CRQS",
        pgettext_lazy(
            "LocationType description",
            "bowl-like hollows partially surrounded by cliffs or steep slopes at the head of a glaciated valley",
        ),
    )
    CLEARING = (
        "CLG",
        pgettext_lazy(
            "LocationType description",
            "an area in a forest with trees removed",
        ),
    )
    CLEFT_S_ = (
        "CFT",
        pgettext_lazy(
            "LocationType description",
            "a deep narrow slot, notch, or groove in a coastal cliff",
        ),
    )
    CLIFF_S_ = (
        "CLF",
        pgettext_lazy(
            "LocationType description",
            "a high, steep to perpendicular slope overlooking a waterbody or lower area",
        ),
    )
    CLINIC = (
        "HSPC",
        pgettext_lazy(
            "LocationType description",
            "a medical facility associated with a hospital for outpatients",
        ),
    )
    COAL_MINE_S_ = (
        "MNC",
        pgettext_lazy("LocationType description", "a mine where coal is extracted"),
    )
    COALFIELD = (
        "COLF",
        pgettext_lazy(
            "LocationType description",
            "a region in which coal deposits of possible economic value occur",
        ),
    )
    COAST = (
        "CST",
        pgettext_lazy(
            "LocationType description",
            "a zone of variable width straddling the shoreline",
        ),
    )
    COAST_GUARD_STATION = (
        "STNC",
        pgettext_lazy(
            "LocationType description",
            "a facility from which the coast is guarded by armed vessels",
        ),
    )
    COCONUT_GROVE = (
        "GRVC",
        pgettext_lazy("LocationType description", "a planting of coconut trees"),
    )
    COLLEGE = (
        "SCHC",
        pgettext_lazy(
            "LocationType description",
            "the grounds and buildings of an institution of higher learning",
        ),
    )
    COMMON = (
        "CMN",
        pgettext_lazy(
            "LocationType description",
            "a park or pasture for community use",
        ),
    )
    COMMUNICATION_CENTER = (
        "COMC",
        pgettext_lazy(
            "LocationType description",
            "a facility, including buildings, antennae, towers and electronic equipment for receiving and transmitting information",
        ),
    )
    COMMUNITY_CENTER = (
        "CTRCM",
        pgettext_lazy(
            "LocationType description",
            "a facility for community recreation and other activities",
        ),
    )
    CONCESSION_AREA = (
        "CNS",
        pgettext_lazy(
            "LocationType description",
            "a lease of land by a government for economic development, e.g., mining, forestry",
        ),
    )
    CONE_S_ = (
        "CONE",
        pgettext_lazy(
            "LocationType description",
            "a conical landform composed of mud or volcanic material",
        ),
    )
    CONFLUENCE = (
        "CNFL",
        pgettext_lazy(
            "LocationType description",
            "a place where two or more streams or intermittent streams flow together",
        ),
    )
    CONTINENTAL_RISE = (
        "CRSU",
        pgettext_lazy(
            "LocationType description",
            "a gentle slope rising from oceanic depths towards the foot of a continental slope",
        ),
    )
    CONVENT = (
        "CVNT",
        pgettext_lazy(
            "LocationType description",
            "a building where a community of nuns lives in seclusion",
        ),
    )
    COPPER_MINE_S_ = (
        "MNCU",
        pgettext_lazy(
            "LocationType description",
            "a mine where copper ore is extracted",
        ),
    )
    COPPER_WORKS = (
        "MFGCU",
        pgettext_lazy(
            "LocationType description",
            "a facility for processing copper ore",
        ),
    )
    CORAL_REEF_S_ = (
        "RFC",
        pgettext_lazy(
            "LocationType description",
            "a surface-navigation hazard composed of coral",
        ),
    )
    CORRAL_S_ = (
        "CRRL",
        pgettext_lazy(
            "LocationType description",
            "a pen or enclosure for confining or capturing animals",
        ),
    )
    CORRIDOR = (
        "CRDR",
        pgettext_lazy(
            "LocationType description",
            "a strip or area of land having significance as an access way",
        ),
    )
    COTTON_PLANTATION = (
        "ESTC",
        pgettext_lazy(
            "LocationType description",
            "an estate specializing in the cultivation of cotton",
        ),
    )
    COUNTRY_HOUSE = (
        "HSEC",
        pgettext_lazy(
            "LocationType description",
            "a large house, mansion, or chateau, on a large estate",
        ),
    )
    COURTHOUSE = (
        "CTHSE",
        pgettext_lazy(
            "LocationType description",
            "a building in which courts of law are held",
        ),
    )
    COVE_S_ = (
        "COVE",
        pgettext_lazy(
            "LocationType description",
            "a small coastal indentation, smaller than a bay",
        ),
    )
    CRATER_LAKE = (
        "LKC",
        pgettext_lazy("LocationType description", "a lake in a crater or caldera"),
    )
    CRATER_LAKES = (
        "LKSC",
        pgettext_lazy("LocationType description", "lakes in a crater or caldera"),
    )
    CRATER_S_ = (
        "CRTR",
        pgettext_lazy(
            "LocationType description",
            "a generally circular saucer or bowl-shaped depression caused by volcanic or meteorite explosive action",
        ),
    )
    CUESTA_S_ = (
        "CUET",
        pgettext_lazy(
            "LocationType description",
            "an asymmetric ridge formed on tilted strata",
        ),
    )
    CULTIVATED_AREA = (
        "CULT",
        pgettext_lazy("LocationType description", "an area under cultivation"),
    )
    CURRENT = (
        "CRNT",
        pgettext_lazy(
            "LocationType description",
            "a horizontal flow of water in a given direction with uniform velocity",
        ),
    )
    CUSTOMS_HOUSE = (
        "CSTM",
        pgettext_lazy(
            "LocationType description",
            "a building in a port where customs and duties are paid, and where vessels are entered and cleared",
        ),
    )
    CUSTOMS_POST = (
        "PSTC",
        pgettext_lazy(
            "LocationType description",
            "a building at an international boundary where customs and duties are paid on goods",
        ),
    )
    CUTOFF = (
        "CUTF",
        pgettext_lazy(
            "LocationType description",
            "a channel formed as a result of a stream cutting through a meander neck",
        ),
    )
    DAIRY = (
        "DARY",
        pgettext_lazy(
            "LocationType description",
            "a facility for the processing, sale and distribution of milk or milk products",
        ),
    )
    DAM = (
        "DAM",
        pgettext_lazy(
            "LocationType description",
            "a barrier constructed across a stream to impound water",
        ),
    )
    DEEP = (
        "DEPU",
        pgettext_lazy(
            "LocationType description",
            "a localized deep area within the confines of a larger feature, such as a trough, basin or trench",
        ),
    )
    DELTA = (
        "DLTA",
        pgettext_lazy(
            "LocationType description",
            "a flat plain formed by alluvial deposits at the mouth of a stream",
        ),
    )
    DEPENDENT_POLITICAL_ENTITY = (
        "PCLD",
        pgettext_lazy("LocationType description", "dependent political entity"),
    )
    DEPRESSION_S_ = (
        "DPR",
        pgettext_lazy(
            "LocationType description",
            "a low area surrounded by higher land and usually characterized by interior drainage",
        ),
    )
    DESERT = (
        "DSRT",
        pgettext_lazy(
            "LocationType description",
            "a large area with little or no vegetation due to extreme environmental conditions",
        ),
    )
    DESTROYED_POPULATED_PLACE = (
        "PPLW",
        pgettext_lazy(
            "LocationType description",
            "a village, town or city destroyed by a natural disaster, or by war",
        ),
    )
    DIATOMITE_MINE_S_ = (
        "MNDT",
        pgettext_lazy(
            "LocationType description",
            "a place where diatomaceous earth is extracted",
        ),
    )
    DIKE = (
        "DIKE",
        pgettext_lazy(
            "LocationType description",
            "an earth or stone embankment usually constructed for flood or stream control",
        ),
    )
    DIPLOMATIC_FACILITY = (
        "DIP",
        pgettext_lazy(
            "LocationType description",
            "office, residence, or facility of a foreign government, which may include an embassy, consulate, chancery, office of charge d’affaires, or other diplomatic, economic, military, or cultural mission",
        ),
    )
    DISPENSARY = (
        "HSPD",
        pgettext_lazy(
            "LocationType description",
            "a building where medical or dental aid is dispensed",
        ),
    )
    DISTRIBUTARY__IES_ = (
        "STMD",
        pgettext_lazy(
            "LocationType description",
            "a branch which flows away from the main stream, as in a delta or irrigation canal",
        ),
    )
    DITCH = (
        "DTCH",
        pgettext_lazy(
            "LocationType description",
            "a small artificial watercourse dug for draining or irrigating the land",
        ),
    )
    DITCH_MOUTH_S_ = (
        "DTCHM",
        pgettext_lazy(
            "LocationType description",
            "an area where a drainage ditch enters a lagoon, lake or bay",
        ),
    )
    DIVIDE = (
        "DVD",
        pgettext_lazy(
            "LocationType description",
            "a line separating adjacent drainage basins",
        ),
    )
    DOCK_S_ = (
        "DCK",
        pgettext_lazy(
            "LocationType description",
            "a waterway between two piers, or cut into the land for the berthing of ships",
        ),
    )
    DOCKING_BASIN = (
        "DCKB",
        pgettext_lazy(
            "LocationType description",
            "a part of a harbor where ships dock",
        ),
    )
    DOCKYARD = (
        "DCKY",
        pgettext_lazy(
            "LocationType description",
            "a facility for servicing, building, or repairing ships",
        ),
    )
    DRAINAGE_BASIN = (
        "BSND",
        pgettext_lazy("LocationType description", "an area drained by a stream"),
    )
    DRAINAGE_CANAL = (
        "CNLD",
        pgettext_lazy(
            "LocationType description",
            "an artificial waterway carrying water away from a wetland or from drainage ditches",
        ),
    )
    DRAINAGE_DITCH = (
        "DTCHD",
        pgettext_lazy(
            "LocationType description",
            "a ditch which serves to drain the land",
        ),
    )
    DRY_DOCK = (
        "DCKD",
        pgettext_lazy(
            "LocationType description",
            "a dock providing support for a vessel, and means for removing the water so that the bottom of the vessel can be exposed",
        ),
    )
    DRY_STREAM_BED = (
        "SBED",
        pgettext_lazy(
            "LocationType description",
            "a channel formerly containing the water of a stream",
        ),
    )
    DUNE_S_ = (
        "DUNE",
        pgettext_lazy(
            "LocationType description",
            "a wave form, ridge or star shape feature composed of sand",
        ),
    )
    ECONOMIC_REGION = (
        "RGNE",
        pgettext_lazy(
            "LocationType description",
            "a region of a country established for economic development or for statistical purposes",
        ),
    )
    ESCARPMENT = (
        "SCRP",
        pgettext_lazy(
            "LocationType description",
            "a long line of cliffs or steep slopes separating level surfaces above and below",
        ),
    )
    ESTATE_S_ = (
        "EST",
        pgettext_lazy(
            "LocationType description",
            "a large commercialized agricultural landholding with associated buildings and other facilities",
        ),
    )
    ESTUARY = (
        "ESTY",
        pgettext_lazy(
            "LocationType description",
            "a funnel-shaped stream mouth or embayment where fresh water mixes with sea water under tidal influences",
        ),
    )
    EXPERIMENT_STATION = (
        "STNE",
        pgettext_lazy(
            "LocationType description",
            "a facility for carrying out experiments",
        ),
    )
    FACILITY = (
        "FCL",
        pgettext_lazy(
            "LocationType description",
            "a building or buildings housing a center, institute, foundation, hospital, prison, mission, courthouse, etc.",
        ),
    )
    FACILITY_CENTER = (
        "CTRF",
        pgettext_lazy(
            "LocationType description",
            "a place where more than one facility is situated",
        ),
    )
    FACTORY = (
        "MFG",
        pgettext_lazy(
            "LocationType description",
            "one or more buildings where goods are manufactured, processed or fabricated",
        ),
    )
    FAN_S_ = (
        "FAN",
        pgettext_lazy(
            "LocationType description",
            "a fan-shaped wedge of coarse alluvium with apex merging with a mountain stream bed and the fan spreading out at a low angle slope onto an adjacent plain",
        ),
    )
    FARM = (
        "FRM",
        pgettext_lazy(
            "LocationType description",
            "a tract of land with associated buildings devoted to agriculture",
        ),
    )
    FARM_VILLAGE = (
        "PPLF",
        pgettext_lazy(
            "LocationType description",
            "a populated place where the population is largely engaged in agricultural activities",
        ),
    )
    FARMS = (
        "FRMS",
        pgettext_lazy(
            "LocationType description",
            "tracts of land with associated buildings devoted to agriculture",
        ),
    )
    FARMSTEAD = (
        "FRMT",
        pgettext_lazy(
            "LocationType description",
            "the buildings and adjacent service areas of a farm",
        ),
    )
    FERRY = (
        "FY",
        pgettext_lazy(
            "LocationType description",
            "a boat or other floating conveyance and terminal facilities regularly used to transport people and vehicles across a waterbody",
        ),
    )
    FERRY_TERMINAL = (
        "FYT",
        pgettext_lazy(
            "LocationType description",
            "a place where ferries pick-up and discharge passengers, vehicles and or cargo",
        ),
    )
    FIELD_S_ = (
        "FLD",
        pgettext_lazy(
            "LocationType description",
            "an open as opposed to wooded area",
        ),
    )
    FIRE_STATION = (
        "FIRE",
        pgettext_lazy(
            "LocationType description",
            "building housing firefighters and/or fire fighting equipment",
        ),
    )
    FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM1",
        pgettext_lazy(
            "LocationType description",
            "a primary administrative division of a country, such as a state in the United States",
        ),
    )
    FISHING_AREA = (
        "FISH",
        pgettext_lazy(
            "LocationType description",
            "a fishing ground, bank or area where fishermen go to catch fish",
        ),
    )
    FISHPONDS = (
        "PNDSF",
        pgettext_lazy(
            "LocationType description",
            "ponds or enclosures in which fish are kept or raised",
        ),
    )
    FISSURE = (
        "FSR",
        pgettext_lazy(
            "LocationType description",
            "a crack associated with volcanism",
        ),
    )
    FJORD = (
        "FJD",
        pgettext_lazy(
            "LocationType description",
            "a long, narrow, steep-walled, deep-water arm of the sea at high latitudes, usually along mountainous coasts",
        ),
    )
    FJORDS = (
        "FJDS",
        pgettext_lazy(
            "LocationType description",
            "long, narrow, steep-walled, deep-water arms of the sea at high latitudes, usually along mountainous coasts",
        ),
    )
    FORD = (
        "FORD",
        pgettext_lazy(
            "LocationType description",
            "a shallow part of a stream which can be crossed on foot or by land vehicle",
        ),
    )
    FOREST_RESERVE = (
        "RESF",
        pgettext_lazy(
            "LocationType description",
            "a forested area set aside for preservation or controlled use",
        ),
    )
    FOREST_STATION = (
        "STNF",
        pgettext_lazy(
            "LocationType description",
            "a collection of buildings and facilities for carrying out forest management",
        ),
    )
    FOREST_S_ = (
        "FRST",
        pgettext_lazy(
            "LocationType description",
            "an area dominated by tree vegetation",
        ),
    )
    FORMER_INLET = (
        "INLTQ",
        pgettext_lazy(
            "LocationType description",
            "an inlet which has been filled in, or blocked by deposits",
        ),
    )
    FORMER_SUGAR_MILL = (
        "MLSGQ",
        pgettext_lazy(
            "LocationType description",
            "a sugar mill no longer used as a sugar mill",
        ),
    )
    FORT = (
        "FT",
        pgettext_lazy(
            "LocationType description",
            "a defensive structure or earthworks",
        ),
    )
    FOSSILIZED_FOREST = (
        "FRSTF",
        pgettext_lazy(
            "LocationType description",
            "a forest fossilized by geologic processes and now exposed at the earth's surface",
        ),
    )
    FOUNDRY = (
        "FNDY",
        pgettext_lazy(
            "LocationType description",
            "a building or works where metal casting is carried out",
        ),
    )
    FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM4",
        pgettext_lazy(
            "LocationType description",
            "a subdivision of a third-order administrative division",
        ),
    )
    FREE_TRADE_ZONE = (
        "ZNF",
        pgettext_lazy(
            "LocationType description",
            "an area, usually a section of a port, where goods may be received and shipped free of customs duty and of most customs regulations",
        ),
    )
    FREELY_ASSOCIATED_STATE = (
        "PCLF",
        pgettext_lazy("LocationType description", "freely associated state"),
    )
    FUEL_DEPOT = (
        "DPOF",
        pgettext_lazy("LocationType description", "an area where fuel is stored"),
    )
    GAP = (
        "GAP",
        pgettext_lazy(
            "LocationType description",
            "a low place in a ridge, not used for transportation",
        ),
    )
    GARDEN_S_ = (
        "GDN",
        pgettext_lazy(
            "LocationType description",
            "an enclosure for displaying selected plant or animal life",
        ),
    )
    GAS_OIL_SEPARATOR_PLANT = (
        "GOSP",
        pgettext_lazy(
            "LocationType description",
            "a facility for separating gas from oil",
        ),
    )
    GASFIELD = (
        "GASF",
        pgettext_lazy(
            "LocationType description",
            "an area containing a subterranean store of natural gas of economic value",
        ),
    )
    GATE = (
        "GATE",
        pgettext_lazy(
            "LocationType description",
            "a controlled access entrance or exit",
        ),
    )
    GEYSER = (
        "GYSR",
        pgettext_lazy(
            "LocationType description",
            "a type of hot spring with intermittent eruptions of jets of hot water and steam",
        ),
    )
    GHĀT = (
        "GHAT",
        pgettext_lazy(
            "LocationType description",
            "a set of steps leading to a river, which are of religious significance, and at their base is usually a platform for bathing",
        ),
    )
    GLACIER_S_ = (
        "GLCR",
        pgettext_lazy(
            "LocationType description",
            "a mass of ice, usually at high latitudes or high elevations, with sufficient thickness to flow away from the source area in lobes, tongues, or masses",
        ),
    )
    GOLD_MINE_S_ = (
        "MNAU",
        pgettext_lazy(
            "LocationType description",
            "a mine where gold ore, or alluvial gold is extracted",
        ),
    )
    GOLF_COURSE = (
        "RECG",
        pgettext_lazy(
            "LocationType description",
            "a recreation field where golf is played",
        ),
    )
    GORGE_S_ = (
        "GRGE",
        pgettext_lazy(
            "LocationType description",
            "a short, narrow, steep-sided section of a stream valley",
        ),
    )
    GRASSLAND = (
        "GRSLD",
        pgettext_lazy(
            "LocationType description",
            "an area dominated by grass vegetation",
        ),
    )
    GRAVE = (
        "GRVE",
        pgettext_lazy("LocationType description", "a burial site"),
    )
    GRAVEL_AREA = (
        "GVL",
        pgettext_lazy("LocationType description", "an area covered with gravel"),
    )
    GRAZING_AREA = (
        "GRAZ",
        pgettext_lazy(
            "LocationType description",
            "an area of grasses and shrubs used for grazing",
        ),
    )
    GUEST_HOUSE = (
        "GHSE",
        pgettext_lazy(
            "LocationType description",
            "a house used to provide lodging for paying guests",
        ),
    )
    GULF = (
        "GULF",
        pgettext_lazy(
            "LocationType description",
            "a large recess in the coastline, larger than a bay",
        ),
    )
    HALTING_PLACE = (
        "HLT",
        pgettext_lazy(
            "LocationType description",
            "a place where caravans stop for rest",
        ),
    )
    HAMMOCK_S_ = (
        "HMCK",
        pgettext_lazy(
            "LocationType description",
            "a patch of ground, distinct from and slightly above the surrounding plain or wetland. Often occurs in groups",
        ),
    )
    HANGAR = (
        "AIRG",
        pgettext_lazy(
            "LocationType description",
            "a covered and usually enclosed area for housing and repairing aircraft",
        ),
    )
    HANGING_VALLEY = (
        "VALG",
        pgettext_lazy(
            "LocationType description",
            "a valley the floor of which is notably higher than the valley or shore to which it leads; most common in areas that have been glaciated",
        ),
    )
    HARBOR_S_ = (
        "HBR",
        pgettext_lazy(
            "LocationType description",
            "a haven or space of deep water so sheltered by the adjacent land as to afford a safe anchorage for ships",
        ),
    )
    HEADLAND = (
        "HDLD",
        pgettext_lazy(
            "LocationType description",
            "a high projection of land extending into a large body of water beyond the line of the coast",
        ),
    )
    HEADWATERS = (
        "STMH",
        pgettext_lazy(
            "LocationType description",
            "the source and upper part of a stream, including the upper drainage basin",
        ),
    )
    HEATH = (
        "HTH",
        pgettext_lazy(
            "LocationType description",
            "an upland moor or sandy area dominated by low shrubby vegetation including heather",
        ),
    )
    HELIPORT = (
        "AIRH",
        pgettext_lazy(
            "LocationType description",
            "a place where helicopters land and take off",
        ),
    )
    HERMITAGE = (
        "HERM",
        pgettext_lazy(
            "LocationType description",
            "a secluded residence, usually for religious sects",
        ),
    )
    HILL = (
        "HLL",
        pgettext_lazy(
            "LocationType description",
            "a rounded elevation of limited extent rising above the surrounding land with local relief of less than 300m",
        ),
    )
    HILLS = (
        "HLLS",
        pgettext_lazy(
            "LocationType description",
            "rounded elevations of limited extent rising above the surrounding land with local relief of less than 300m",
        ),
    )
    HISTORICAL_ADMINISTRATIVE_DIVISION = (
        "ADMDH",
        pgettext_lazy(
            "LocationType description",
            "a former administrative division of a political entity, undifferentiated as to administrative level",
        ),
    )
    HISTORICAL_FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM1H",
        pgettext_lazy(
            "LocationType description",
            "a former first-order administrative division",
        ),
    )
    HISTORICAL_FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM4H",
        pgettext_lazy(
            "LocationType description",
            "a former fourth-order administrative division",
        ),
    )
    HISTORICAL_POLITICAL_ENTITY = (
        "PCLH",
        pgettext_lazy("LocationType description", "a former political entity"),
    )
    HISTORICAL_POPULATED_PLACE = (
        "PPLH",
        pgettext_lazy(
            "LocationType description",
            "a populated place that no longer exists",
        ),
    )
    HISTORICAL_RAILROAD = (
        "RRH",
        pgettext_lazy(
            "LocationType description",
            "a former permanent twin steel-rail track on which freight and passenger cars move long distances",
        ),
    )
    HISTORICAL_RAILROAD_STATION = (
        "RSTNH",
        pgettext_lazy(
            "LocationType description",
            "a former facility comprising ticket office, platforms, etc. for loading and unloading train passengers and freight",
        ),
    )
    HISTORICAL_REGION = (
        "RGNH",
        pgettext_lazy(
            "LocationType description",
            "a former area distinguished by one or more observable physical or cultural characteristics",
        ),
    )
    HISTORICAL_SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM2H",
        pgettext_lazy(
            "LocationType description",
            "a former second-order administrative division",
        ),
    )
    HISTORICAL_SITE = (
        "HSTS",
        pgettext_lazy("LocationType description", "a place of historical importance"),
    )
    HISTORICAL_THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM3H",
        pgettext_lazy(
            "LocationType description",
            "a former third-order administrative division",
        ),
    )
    HISTORICAL_UNDERSEA_FEATURE = (
        "UFHU",
        pgettext_lazy(
            "LocationType description",
            "an undersea feature whose existence has been subsequently disproved",
        ),
    )
    HOMESTEAD = (
        "HMSD",
        pgettext_lazy(
            "LocationType description",
            "a residence, owner's or manager's, on a sheep or cattle station, woolshed, outcamp, or Aboriginal outstation, specific to Australia and New Zealand",
        ),
    )
    HOSPITAL = (
        "HSP",
        pgettext_lazy(
            "LocationType description",
            "a building in which sick or injured, especially those confined to bed, are medically treated",
        ),
    )
    HOT_SPRING_S_ = (
        "SPNT",
        pgettext_lazy(
            "LocationType description",
            "a place where hot ground water flows naturally out of the ground",
        ),
    )
    HOTEL = (
        "HTL",
        pgettext_lazy(
            "LocationType description",
            "a building providing lodging and/or meals for the public",
        ),
    )
    HOUSE_S_ = (
        "HSE",
        pgettext_lazy(
            "LocationType description",
            "a building used as a human habitation",
        ),
    )
    HOUSING_DEVELOPMENT = (
        "DEVH",
        pgettext_lazy(
            "LocationType description",
            "a tract of land on which many houses of similar design are built according to a development plan",
        ),
    )
    HUNTING_RESERVE = (
        "RESH",
        pgettext_lazy(
            "LocationType description",
            "a tract of land used primarily for hunting",
        ),
    )
    HUT = (
        "HUT",
        pgettext_lazy("LocationType description", "a small primitive house"),
    )
    HUTS = (
        "HUTS",
        pgettext_lazy("LocationType description", "small primitive houses"),
    )
    HYDROELECTRIC_POWER_STATION = (
        "PSH",
        pgettext_lazy(
            "LocationType description",
            "a building where electricity is generated from water power",
        ),
    )
    ICECAP = (
        "CAPG",
        pgettext_lazy(
            "LocationType description",
            "a dome-shaped mass of glacial ice covering an area of mountain summits or other high lands; smaller than an ice sheet",
        ),
    )
    ICECAP_DEPRESSION = (
        "DPRG",
        pgettext_lazy(
            "LocationType description",
            "a comparatively depressed area on an icecap",
        ),
    )
    ICECAP_DOME = (
        "DOMG",
        pgettext_lazy(
            "LocationType description",
            "a comparatively elevated area on an icecap",
        ),
    )
    ICECAP_RIDGE = (
        "RDGG",
        pgettext_lazy("LocationType description", "a linear elevation on an icecap"),
    )
    INDEPENDENT_POLITICAL_ENTITY = (
        "PCLI",
        pgettext_lazy("LocationType description", "independent political entity"),
    )
    INDUSTRIAL_AREA = (
        "INDS",
        pgettext_lazy(
            "LocationType description",
            "an area characterized by industrial activity",
        ),
    )
    INLET = (
        "INLT",
        pgettext_lazy(
            "LocationType description",
            "a narrow waterway extending into the land, or connecting a bay or lagoon with a larger body of water",
        ),
    )
    INSPECTION_STATION = (
        "STNI",
        pgettext_lazy(
            "LocationType description",
            "a station at which vehicles, goods, and people are inspected",
        ),
    )
    INTERDUNE_TROUGH_S_ = (
        "TRGD",
        pgettext_lazy(
            "LocationType description",
            "a long wind-swept trough between parallel longitudinal dunes",
        ),
    )
    INTERFLUVE = (
        "INTF",
        pgettext_lazy(
            "LocationType description",
            "a relatively undissected upland between adjacent stream valleys",
        ),
    )
    INTERMITTENT_LAKE = (
        "LKI",
        pgettext_lazy("LocationType description", "intermittent lake"),
    )
    INTERMITTENT_LAKES = (
        "LKSI",
        pgettext_lazy("LocationType description", "intermittent lakes"),
    )
    INTERMITTENT_OXBOW_LAKE = (
        "LKOI",
        pgettext_lazy("LocationType description", "intermittent oxbow lake"),
    )
    INTERMITTENT_POND = (
        "PNDI",
        pgettext_lazy("LocationType description", "intermittent pond"),
    )
    INTERMITTENT_PONDS = (
        "PNDSI",
        pgettext_lazy("LocationType description", "intermittent ponds"),
    )
    INTERMITTENT_POOL = (
        "POOLI",
        pgettext_lazy("LocationType description", "intermittent pool"),
    )
    INTERMITTENT_RESERVOIR = (
        "RSVI",
        pgettext_lazy("LocationType description", "intermittent reservoir"),
    )
    INTERMITTENT_SALT_LAKE = (
        "LKNI",
        pgettext_lazy("LocationType description", "intermittent salt lake"),
    )
    INTERMITTENT_SALT_LAKES = (
        "LKSNI",
        pgettext_lazy("LocationType description", "intermittent salt lakes"),
    )
    INTERMITTENT_SALT_POND_S_ = (
        "PNDNI",
        pgettext_lazy("LocationType description", "intermittent salt pond(s)"),
    )
    INTERMITTENT_STREAM = (
        "STMI",
        pgettext_lazy("LocationType description", "intermittent stream"),
    )
    INTERMITTENT_WETLAND = (
        "WTLDI",
        pgettext_lazy("LocationType description", "intermittent wetland"),
    )
    INTERSECTION = (
        "RDIN",
        pgettext_lazy(
            "LocationType description",
            "a junction of two or more highways by a system of separate levels that permit traffic to pass from one to another without the crossing of traffic streams",
        ),
    )
    IRON_MINE_S_ = (
        "MNFE",
        pgettext_lazy(
            "LocationType description",
            "a mine where iron ore is extracted",
        ),
    )
    IRRIGATED_FIELD_S_ = (
        "FLDI",
        pgettext_lazy(
            "LocationType description",
            "a tract of level or terraced land which is irrigated",
        ),
    )
    IRRIGATION_CANAL = (
        "CNLI",
        pgettext_lazy(
            "LocationType description",
            "a canal which serves as a main conduit for irrigation water",
        ),
    )
    IRRIGATION_DITCH = (
        "DTCHI",
        pgettext_lazy(
            "LocationType description",
            "a ditch which serves to distribute irrigation water",
        ),
    )
    IRRIGATION_SYSTEM = (
        "SYSI",
        pgettext_lazy(
            "LocationType description",
            "a network of ditches and one or more of the following elements: water supply, reservoir, canal, pump, well, drain, etc.",
        ),
    )
    ISLAND = (
        "ISL",
        pgettext_lazy(
            "LocationType description",
            "a tract of land, smaller than a continent, surrounded by water at high water",
        ),
    )
    ISLANDS = (
        "ISLS",
        pgettext_lazy(
            "LocationType description",
            "tracts of land, smaller than a continent, surrounded by water at high water",
        ),
    )
    ISRAELI_SETTLEMENT = (
        "STLMT",
        pgettext_lazy("LocationType description", "Israeli settlement"),
    )
    ISTHMUS = (
        "ISTH",
        pgettext_lazy(
            "LocationType description",
            "a narrow strip of land connecting two larger land masses and bordered by water",
        ),
    )
    JETTY = (
        "JTY",
        pgettext_lazy(
            "LocationType description",
            "a structure built out into the water at a river mouth or harbor entrance to regulate currents and silting",
        ),
    )
    KARST_AREA = (
        "KRST",
        pgettext_lazy(
            "LocationType description",
            "a distinctive landscape developed on soluble rock such as limestone characterized by sinkholes, caves, disappearing streams, and underground drainage",
        ),
    )
    LABOR_CAMP = (
        "CMPLA",
        pgettext_lazy(
            "LocationType description",
            "a camp used by migrant or temporary laborers",
        ),
    )
    LAGOON = (
        "LGN",
        pgettext_lazy(
            "LocationType description",
            "a shallow coastal waterbody, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature",
        ),
    )
    LAGOONS = (
        "LGNS",
        pgettext_lazy(
            "LocationType description",
            "shallow coastal waterbodies, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature",
        ),
    )
    LAKE = (
        "LK",
        pgettext_lazy(
            "LocationType description",
            "a large inland body of standing water",
        ),
    )
    LAKE_BED_S_ = (
        "LBED",
        pgettext_lazy(
            "LocationType description",
            "a dried up or drained area of a former lake",
        ),
    )
    LAKE_CHANNEL_S_ = (
        "CHNL",
        pgettext_lazy(
            "LocationType description",
            "that part of a lake having water deep enough for navigation between islands, shoals, etc.",
        ),
    )
    LAKE_REGION = (
        "RGNL",
        pgettext_lazy(
            "LocationType description",
            "a tract of land distinguished by numerous lakes",
        ),
    )
    LAKES = (
        "LKS",
        pgettext_lazy(
            "LocationType description",
            "large inland bodies of standing water",
        ),
    )
    LAND_TIED_ISLAND = (
        "ISLT",
        pgettext_lazy(
            "LocationType description",
            "a coastal island connected to the mainland by barrier beaches, levees or dikes",
        ),
    )
    LANDFILL = (
        "LNDF",
        pgettext_lazy(
            "LocationType description",
            "a place for trash and garbage disposal in which the waste is buried between layers of earth to build up low-lying land",
        ),
    )
    LANDING = (
        "LDNG",
        pgettext_lazy(
            "LocationType description",
            "a place where boats receive or discharge passengers and freight, but lacking most port facilities",
        ),
    )
    LAVA_AREA = (
        "LAVA",
        pgettext_lazy("LocationType description", "an area of solidified lava"),
    )
    LEAD_MINE_S_ = (
        "MNPB",
        pgettext_lazy(
            "LocationType description",
            "a mine where lead ore is extracted",
        ),
    )
    LEASED_AREA = (
        "LTER",
        pgettext_lazy(
            "LocationType description",
            "a tract of land leased by the United Kingdom from the People's Republic of China to form part of Hong Kong",
        ),
    )
    LEPER_COLONY = (
        "LEPC",
        pgettext_lazy(
            "LocationType description",
            "a settled area inhabited by lepers in relative isolation",
        ),
    )
    LEPROSARIUM = (
        "HSPL",
        pgettext_lazy("LocationType description", "an asylum or hospital for lepers"),
    )
    LEVEE = (
        "LEV",
        pgettext_lazy(
            "LocationType description",
            "a natural low embankment bordering a distributary or meandering stream; often built up artificially to control floods",
        ),
    )
    LIGHTHOUSE = (
        "LTHSE",
        pgettext_lazy(
            "LocationType description",
            "a distinctive structure exhibiting a major navigation light",
        ),
    )
    LIMEKILN = (
        "MFGLM",
        pgettext_lazy(
            "LocationType description",
            "a furnace in which limestone is reduced to lime",
        ),
    )
    LOCAL_GOVERNMENT_OFFICE = (
        "GOVL",
        pgettext_lazy(
            "LocationType description",
            "a facility housing local governmental offices, usually a city, town, or village hall",
        ),
    )
    LOCALITY = (
        "LCTY",
        pgettext_lazy(
            "LocationType description",
            "a minor area or place of unspecified or mixed character and indefinite boundaries",
        ),
    )
    LOCK_S_ = (
        "LOCK",
        pgettext_lazy(
            "LocationType description",
            "a basin in a waterway with gates at each end by means of which vessels are passed from one water level to another",
        ),
    )
    LOGGING_CAMP = (
        "CMPL",
        pgettext_lazy("LocationType description", "a camp used by loggers"),
    )
    LOST_RIVER = (
        "STMSB",
        pgettext_lazy(
            "LocationType description",
            "a surface stream that disappears into an underground channel, or dries up in an arid area",
        ),
    )
    MANEUVER_AREA = (
        "MVA",
        pgettext_lazy(
            "LocationType description",
            "a tract of land where military field exercises are carried out",
        ),
    )
    MANGROVE_ISLAND = (
        "ISLM",
        pgettext_lazy(
            "LocationType description",
            "a mangrove swamp surrounded by a waterbody",
        ),
    )
    MANGROVE_SWAMP = (
        "MGV",
        pgettext_lazy(
            "LocationType description",
            "a tropical tidal mud flat characterized by mangrove vegetation",
        ),
    )
    MARINA = (
        "MAR",
        pgettext_lazy(
            "LocationType description",
            "a harbor facility for small boats, yachts, etc.",
        ),
    )
    MARINE_CHANNEL = (
        "CHNM",
        pgettext_lazy(
            "LocationType description",
            "that part of a body of water deep enough for navigation through an area otherwise not suitable",
        ),
    )
    MARITIME_SCHOOL = (
        "SCHN",
        pgettext_lazy(
            "LocationType description",
            "a school at which maritime sciences form the core of the curriculum",
        ),
    )
    MARKET = (
        "MKT",
        pgettext_lazy(
            "LocationType description",
            "a place where goods are bought and sold at regular intervals",
        ),
    )
    MARSH_ES_ = (
        "MRSH",
        pgettext_lazy(
            "LocationType description",
            "a wetland dominated by grass-like vegetation",
        ),
    )
    MEADOW = (
        "MDW",
        pgettext_lazy(
            "LocationType description",
            "a small, poorly drained area dominated by grassy vegetation",
        ),
    )
    MEANDER_NECK = (
        "NKM",
        pgettext_lazy(
            "LocationType description",
            "a narrow strip of land between the two limbs of a meander loop at its narrowest point",
        ),
    )
    MEDICAL_CENTER = (
        "CTRM",
        pgettext_lazy(
            "LocationType description",
            "a complex of health care buildings including two or more of the following: hospital, medical school, clinic, pharmacy, doctor's offices, etc.",
        ),
    )
    MESA_S_ = (
        "MESA",
        pgettext_lazy(
            "LocationType description",
            "a flat-topped, isolated elevation with steep slopes on all sides, less extensive than a plateau",
        ),
    )
    METEOROLOGICAL_STATION = (
        "STNM",
        pgettext_lazy(
            "LocationType description",
            "a station at which weather elements are recorded",
        ),
    )
    MILITARY_BASE = (
        "MILB",
        pgettext_lazy(
            "LocationType description",
            "a place used by an army or other armed service for storing arms and supplies, and for accommodating and training troops, a base from which operations can be initiated",
        ),
    )
    MILITARY_INSTALLATION = (
        "INSM",
        pgettext_lazy(
            "LocationType description",
            "a facility for use of and control by armed forces",
        ),
    )
    MILITARY_SCHOOL = (
        "SCHM",
        pgettext_lazy(
            "LocationType description",
            "a school at which military science forms the core of the curriculum",
        ),
    )
    MILL_S_ = (
        "ML",
        pgettext_lazy(
            "LocationType description",
            "a building housing machines for transforming, shaping, finishing, grinding, or extracting products",
        ),
    )
    MINE_S_ = (
        "MN",
        pgettext_lazy(
            "LocationType description",
            "a site where mineral ores are extracted from the ground by excavating surface pits and subterranean passages",
        ),
    )
    MINING_AREA = (
        "MNA",
        pgettext_lazy(
            "LocationType description",
            "an area of mine sites where minerals and ores are extracted",
        ),
    )
    MINING_CAMP = (
        "CMPMN",
        pgettext_lazy("LocationType description", "a camp used by miners"),
    )
    MISSION = (
        "MSSN",
        pgettext_lazy(
            "LocationType description",
            "a place characterized by dwellings, school, church, hospital and other facilities operated by a religious group for the purpose of providing charitable services and to propagate religion",
        ),
    )
    MOLE = (
        "MOLE",
        pgettext_lazy(
            "LocationType description",
            "a massive structure of masonry or large stones serving as a pier or breakwater",
        ),
    )
    MONASTERY = (
        "MSTY",
        pgettext_lazy(
            "LocationType description",
            "a building and grounds where a community of monks lives in seclusion",
        ),
    )
    MONUMENT = (
        "MNMT",
        pgettext_lazy(
            "LocationType description",
            "a commemorative structure or statue",
        ),
    )
    MOOR_S_ = (
        "MOOR",
        pgettext_lazy(
            "LocationType description",
            "an area of open ground overlaid with wet peaty soils",
        ),
    )
    MORAINE = (
        "MRN",
        pgettext_lazy(
            "LocationType description",
            "a mound, ridge, or other accumulation of glacial till",
        ),
    )
    MOSQUE = (
        "MSQE",
        pgettext_lazy(
            "LocationType description",
            "a building for public Islamic worship",
        ),
    )
    MOUND_S_ = (
        "MND",
        pgettext_lazy("LocationType description", "a low, isolated, rounded hill"),
    )
    MOUNTAIN = (
        "MT",
        pgettext_lazy(
            "LocationType description",
            "an elevation standing high above the surrounding area with small summit area, steep slopes and local relief of 300m or more",
        ),
    )
    MOUNTAINS = (
        "MTS",
        pgettext_lazy(
            "LocationType description",
            "a mountain range or a group of mountains or high ridges",
        ),
    )
    MUD_FLAT_S_ = (
        "FLTM",
        pgettext_lazy(
            "LocationType description",
            "a relatively level area of mud either between high and low tide lines, or subject to flooding",
        ),
    )
    MUNITIONS_PLANT = (
        "MFGM",
        pgettext_lazy(
            "LocationType description",
            "a factory where ammunition is made",
        ),
    )
    MUSEUM = (
        "MUS",
        pgettext_lazy(
            "LocationType description",
            "a building where objects of permanent interest in one or more of the arts and sciences are preserved and exhibited",
        ),
    )
    NARROWS = (
        "NRWS",
        pgettext_lazy(
            "LocationType description",
            "a navigable narrow part of a bay, strait, river, etc.",
        ),
    )
    NATURAL_TUNNEL = (
        "TNLN",
        pgettext_lazy("LocationType description", "a cave that is open at both ends"),
    )
    NATURE_RESERVE = (
        "RESN",
        pgettext_lazy(
            "LocationType description",
            "an area reserved for the maintenance of a natural habitat",
        ),
    )
    NAVAL_BASE = (
        "NVB",
        pgettext_lazy(
            "LocationType description",
            "an area used to store supplies, provide barracks for troops and naval personnel, a port for naval vessels, and from which operations are initiated",
        ),
    )
    NAVIGATION_CANAL_S_ = (
        "CNLN",
        pgettext_lazy(
            "LocationType description",
            "a watercourse constructed for navigation of vessels",
        ),
    )
    NAVIGATION_CHANNEL = (
        "CHNN",
        pgettext_lazy(
            "LocationType description",
            "a buoyed channel of sufficient depth for the safe navigation of vessels",
        ),
    )
    NICKEL_MINE_S_ = (
        "MNNI",
        pgettext_lazy(
            "LocationType description",
            "a mine where nickel ore is extracted",
        ),
    )
    NOVITIATE = (
        "NOV",
        pgettext_lazy(
            "LocationType description",
            "a religious house or school where novices are trained",
        ),
    )
    NUCLEAR_POWER_STATION = (
        "PSN",
        pgettext_lazy("LocationType description", "nuclear power station"),
    )
    NUNATAK = (
        "NTK",
        pgettext_lazy(
            "LocationType description",
            "a rock or mountain peak protruding through glacial ice",
        ),
    )
    NUNATAKS = (
        "NTKS",
        pgettext_lazy(
            "LocationType description",
            "rocks or mountain peaks protruding through glacial ice",
        ),
    )
    NURSERY__IES_ = (
        "NSY",
        pgettext_lazy(
            "LocationType description",
            "a place where plants are propagated for transplanting or grafting",
        ),
    )
    OASIS__ES_ = (
        "OAS",
        pgettext_lazy(
            "LocationType description",
            "an area in a desert made productive by the availability of water",
        ),
    )
    OBSERVATION_POINT = (
        "OBPT",
        pgettext_lazy(
            "LocationType description",
            "a wildlife or scenic observation point",
        ),
    )
    OBSERVATORY = (
        "OBS",
        pgettext_lazy(
            "LocationType description",
            "a facility equipped for observation of atmospheric or space phenomena",
        ),
    )
    OCEAN = (
        "OCN",
        pgettext_lazy(
            "LocationType description",
            "one of the major divisions of the vast expanse of salt water covering part of the earth",
        ),
    )
    OFFICE_BUILDING = (
        "BLDO",
        pgettext_lazy(
            "LocationType description",
            "commercial building where business and/or services are conducted",
        ),
    )
    OIL_CAMP = (
        "CMPO",
        pgettext_lazy("LocationType description", "a camp used by oilfield workers"),
    )
    OIL_PALM_PLANTATION = (
        "ESTO",
        pgettext_lazy(
            "LocationType description",
            "an estate specializing in the cultivation of oil palm trees",
        ),
    )
    OIL_PIPELINE = (
        "OILP",
        pgettext_lazy(
            "LocationType description",
            "a pipeline used for transporting oil",
        ),
    )
    OIL_PIPELINE_JUNCTION = (
        "OILJ",
        pgettext_lazy(
            "LocationType description",
            "a section of an oil pipeline where two or more pipes join together",
        ),
    )
    OIL_PIPELINE_TERMINAL = (
        "TRMO",
        pgettext_lazy(
            "LocationType description",
            "a tank farm or loading facility at the end of an oil pipeline",
        ),
    )
    OIL_PUMPING_STATION = (
        "PMPO",
        pgettext_lazy(
            "LocationType description",
            "a facility for pumping oil through a pipeline",
        ),
    )
    OIL_REFINERY = (
        "OILR",
        pgettext_lazy(
            "LocationType description",
            "a facility for converting crude oil into refined petroleum products",
        ),
    )
    OIL_WELL = (
        "OILW",
        pgettext_lazy(
            "LocationType description",
            "a well from which oil may be pumped",
        ),
    )
    OILFIELD = (
        "OILF",
        pgettext_lazy(
            "LocationType description",
            "an area containing a subterranean store of petroleum of economic value",
        ),
    )
    OLIVE_GROVE = (
        "GRVO",
        pgettext_lazy("LocationType description", "a planting of olive trees"),
    )
    OLIVE_OIL_MILL = (
        "MLO",
        pgettext_lazy(
            "LocationType description",
            "a mill where oil is extracted from olives",
        ),
    )
    ORCHARD_S_ = (
        "OCH",
        pgettext_lazy("LocationType description", "a planting of fruit or nut trees"),
    )
    ORE_TREATMENT_PLANT = (
        "MLM",
        pgettext_lazy(
            "LocationType description",
            "a facility for improving the metal content of ore by concentration",
        ),
    )
    OVERFALLS = (
        "OVF",
        pgettext_lazy(
            "LocationType description",
            "an area of breaking waves caused by the meeting of currents or by waves moving against the current",
        ),
    )
    OXBOW_LAKE = (
        "LKO",
        pgettext_lazy(
            "LocationType description",
            "a crescent-shaped lake commonly found adjacent to meandering streams",
        ),
    )
    PAGODA = (
        "PGDA",
        pgettext_lazy(
            "LocationType description",
            "a tower-like storied structure, usually a Buddhist shrine",
        ),
    )
    PALACE = (
        "PAL",
        pgettext_lazy(
            "LocationType description",
            "a large stately house, often a royal or presidential residence",
        ),
    )
    PALM_GROVE = (
        "GRVP",
        pgettext_lazy("LocationType description", "a planting of palm trees"),
    )
    PALM_TREE_RESERVE = (
        "RESP",
        pgettext_lazy(
            "LocationType description",
            "an area of palm trees where use is controlled",
        ),
    )
    PAN = (
        "PAN",
        pgettext_lazy(
            "LocationType description",
            "a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool",
        ),
    )
    PANS = (
        "PANS",
        pgettext_lazy(
            "LocationType description",
            "a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool",
        ),
    )
    PARISH = (
        "PRSH",
        pgettext_lazy("LocationType description", "an ecclesiastical district"),
    )
    PARK = (
        "PRK",
        pgettext_lazy(
            "LocationType description",
            "an area, often of forested land, maintained as a place of beauty, or for recreation",
        ),
    )
    PARK_GATE = (
        "PRKGT",
        pgettext_lazy("LocationType description", "a controlled access to a park"),
    )
    PARK_HEADQUARTERS = (
        "PRKHQ",
        pgettext_lazy("LocationType description", "a park administrative facility"),
    )
    PARKING_GARAGE = (
        "GARG",
        pgettext_lazy(
            "LocationType description",
            "a building or underground facility used exclusively for parking vehicles",
        ),
    )
    PARKING_LOT = (
        "PKLT",
        pgettext_lazy(
            "LocationType description",
            "an area used for parking vehicles",
        ),
    )
    PASS = (
        "PASS",
        pgettext_lazy(
            "LocationType description",
            "a break in a mountain range or other high obstruction, used for transportation from one side to the other [See also gap]",
        ),
    )
    PATROL_POST = (
        "PSTP",
        pgettext_lazy(
            "LocationType description",
            "a post from which patrols are sent out",
        ),
    )
    PEAK = (
        "PK",
        pgettext_lazy(
            "LocationType description",
            "a pointed elevation atop a mountain, ridge, or other hypsographic feature",
        ),
    )
    PEAKS = (
        "PKS",
        pgettext_lazy(
            "LocationType description",
            "pointed elevations atop a mountain, ridge, or other hypsographic features",
        ),
    )
    PEAT_CUTTING_AREA = (
        "PEAT",
        pgettext_lazy("LocationType description", "an area where peat is harvested"),
    )
    PENINSULA = (
        "PEN",
        pgettext_lazy(
            "LocationType description",
            "an elongate area of land projecting into a body of water and nearly surrounded by water",
        ),
    )
    PETROLEUM_BASIN = (
        "BSNP",
        pgettext_lazy(
            "LocationType description",
            "an area underlain by an oil-rich structural basin",
        ),
    )
    PHOSPHATE_WORKS = (
        "MFGPH",
        pgettext_lazy(
            "LocationType description",
            "a facility for producing fertilizer",
        ),
    )
    PIER = (
        "PIER",
        pgettext_lazy(
            "LocationType description",
            "a structure built out into navigable water on piles providing berthing for ships and recreation",
        ),
    )
    PINE_GROVE = (
        "GRVPN",
        pgettext_lazy("LocationType description", "a planting of pine trees"),
    )
    PLACER_MINE_S_ = (
        "MNPL",
        pgettext_lazy(
            "LocationType description",
            "a place where heavy metals are concentrated and running water is used to extract them from unconsolidated sediments",
        ),
    )
    PLAIN_S_ = (
        "PLN",
        pgettext_lazy(
            "LocationType description",
            "an extensive area of comparatively level to gently undulating land, lacking surface irregularities, and usually adjacent to a higher area",
        ),
    )
    PLATEAU = (
        "PLAT",
        pgettext_lazy(
            "LocationType description",
            "an elevated plain with steep slopes on one or more sides, and often with incised streams",
        ),
    )
    POINT = (
        "PT",
        pgettext_lazy(
            "LocationType description",
            "a tapering piece of land projecting into a body of water, less prominent than a cape",
        ),
    )
    POINTS = (
        "PTS",
        pgettext_lazy(
            "LocationType description",
            "tapering pieces of land projecting into a body of water, less prominent than a cape",
        ),
    )
    POLDER = (
        "PLDR",
        pgettext_lazy(
            "LocationType description",
            "an area reclaimed from the sea by diking and draining",
        ),
    )
    POLICE_POST = (
        "PP",
        pgettext_lazy(
            "LocationType description",
            "a building in which police are stationed",
        ),
    )
    POLITICAL_ENTITY = (
        "PCL",
        pgettext_lazy("LocationType description", "political entity"),
    )
    POND = (
        "PND",
        pgettext_lazy("LocationType description", "a small standing waterbody"),
    )
    PONDS = (
        "PNDS",
        pgettext_lazy("LocationType description", "small standing waterbodies"),
    )
    POOL_S_ = (
        "POOL",
        pgettext_lazy(
            "LocationType description",
            "a small and comparatively still, deep part of a larger body of water such as a stream or harbor; or a small body of standing water",
        ),
    )
    POPULATED_LOCALITY = (
        "PPLL",
        pgettext_lazy(
            "LocationType description",
            "an area similar to a locality but with a small group of dwellings or other buildings",
        ),
    )
    POPULATED_PLACE = (
        "PPL",
        pgettext_lazy(
            "LocationType description",
            "a city, town, village, or other agglomeration of buildings where people live and work",
        ),
    )
    POPULATED_PLACES = (
        "PPLS",
        pgettext_lazy(
            "LocationType description",
            "cities, towns, villages, or other agglomerations of buildings where people live and work",
        ),
    )
    PORT = (
        "PRT",
        pgettext_lazy(
            "LocationType description",
            "a place provided with terminal and transfer facilities for loading and discharging waterborne cargo or passengers, usually located in a harbor",
        ),
    )
    PORTAGE = (
        "PTGE",
        pgettext_lazy(
            "LocationType description",
            "a place where boats, goods, etc., are carried overland between navigable waters",
        ),
    )
    POST_OFFICE = (
        "PO",
        pgettext_lazy(
            "LocationType description",
            "a public building in which mail is received, sorted and distributed",
        ),
    )
    POWER_STATION = (
        "PS",
        pgettext_lazy(
            "LocationType description",
            "a facility for generating electric power",
        ),
    )
    PRISON = (
        "PRN",
        pgettext_lazy(
            "LocationType description",
            "a facility for confining prisoners",
        ),
    )
    PROMENADE = (
        "PRMN",
        pgettext_lazy(
            "LocationType description",
            "a place for public walking, usually along a beach front",
        ),
    )
    PROMONTORY__IES_ = (
        "PROM",
        pgettext_lazy(
            "LocationType description",
            "a bluff or prominent hill overlooking or projecting into a lowland",
        ),
    )
    PYRAMID = (
        "PYR",
        pgettext_lazy(
            "LocationType description",
            "an ancient massive structure of square ground plan with four triangular faces meeting at a point and used for enclosing tombs",
        ),
    )
    PYRAMIDS = (
        "PYRS",
        pgettext_lazy(
            "LocationType description",
            "ancient massive structures of square ground plan with four triangular faces meeting at a point and used for enclosing tombs",
        ),
    )
    QUARRY__IES_ = (
        "MNQR",
        pgettext_lazy(
            "LocationType description",
            "a surface mine where building stone or gravel and sand, etc. are extracted",
        ),
    )
    QUAY = (
        "QUAY",
        pgettext_lazy(
            "LocationType description",
            "a structure of solid construction along a shore or bank which provides berthing for ships and which generally provides cargo handling facilities",
        ),
    )
    QUICKSAND = (
        "QCKS",
        pgettext_lazy(
            "LocationType description",
            "an area where loose sand with water moving through it may become unstable when heavy objects are placed at the surface, causing them to sink",
        ),
    )
    RACETRACK = (
        "RECR",
        pgettext_lazy("LocationType description", "a track where races are held"),
    )
    RADIO_OBSERVATORY = (
        "OBSR",
        pgettext_lazy(
            "LocationType description",
            "a facility equipped with an array of antennae for receiving radio waves from space",
        ),
    )
    RADIO_STATION = (
        "STNR",
        pgettext_lazy(
            "LocationType description",
            "a facility for producing and transmitting information by radio waves",
        ),
    )
    RAILROAD = (
        "RR",
        pgettext_lazy(
            "LocationType description",
            "a permanent twin steel-rail track on which freight and passenger cars move long distances",
        ),
    )
    RAILROAD_JUNCTION = (
        "RJCT",
        pgettext_lazy(
            "LocationType description",
            "a place where two or more railroad tracks join",
        ),
    )
    RAILROAD_SIDING = (
        "RSD",
        pgettext_lazy(
            "LocationType description",
            "a short track parallel to and joining the main track",
        ),
    )
    RAILROAD_SIGNAL = (
        "RSGNL",
        pgettext_lazy(
            "LocationType description",
            "a signal at the entrance of a particular section of track governing the movement of trains",
        ),
    )
    RAILROAD_STATION = (
        "RSTN",
        pgettext_lazy(
            "LocationType description",
            "a facility comprising ticket office, platforms, etc. for loading and unloading train passengers and freight",
        ),
    )
    RAILROAD_STOP = (
        "RSTP",
        pgettext_lazy(
            "LocationType description",
            "a place lacking station facilities where trains stop to pick up and unload passengers and freight",
        ),
    )
    RAILROAD_TUNNEL = (
        "TNLRR",
        pgettext_lazy(
            "LocationType description",
            "a tunnel through which a railroad passes",
        ),
    )
    RAILROAD_YARD = (
        "RYD",
        pgettext_lazy(
            "LocationType description",
            "a system of tracks used for the making up of trains, and switching and storing freight cars",
        ),
    )
    RANCH_ES_ = (
        "RNCH",
        pgettext_lazy(
            "LocationType description",
            "a large farm specializing in extensive grazing of livestock",
        ),
    )
    RAPIDS = (
        "RPDS",
        pgettext_lazy(
            "LocationType description",
            "a turbulent section of a stream associated with a steep, irregular stream bed",
        ),
    )
    RAVINE_S_ = (
        "RVN",
        pgettext_lazy(
            "LocationType description",
            "a small, narrow, deep, steep-sided stream channel, smaller than a gorge",
        ),
    )
    REACH = (
        "RCH",
        pgettext_lazy(
            "LocationType description",
            "a straight section of a navigable stream or channel between two bends",
        ),
    )
    REEF_S_ = (
        "RF",
        pgettext_lazy(
            "LocationType description",
            "a surface-navigation hazard composed of consolidated material",
        ),
    )
    REFORMATORY = (
        "PRNJ",
        pgettext_lazy(
            "LocationType description",
            "a facility for confining, training, and reforming young law offenders",
        ),
    )
    REFUGEE_CAMP = (
        "CMPRF",
        pgettext_lazy("LocationType description", "a camp used by refugees"),
    )
    REGION = (
        "RGN",
        pgettext_lazy(
            "LocationType description",
            "an area distinguished by one or more observable physical or cultural characteristics",
        ),
    )
    RELIGIOUS_CENTER = (
        "CTRR",
        pgettext_lazy(
            "LocationType description",
            "a facility where more than one religious activity is carried out, e.g., retreat, school, monastery, worship",
        ),
    )
    RELIGIOUS_POPULATED_PLACE = (
        "PPLR",
        pgettext_lazy(
            "LocationType description",
            "a populated place whose population is largely engaged in religious occupations",
        ),
    )
    RELIGIOUS_SITE = (
        "RLG",
        pgettext_lazy(
            "LocationType description",
            "an ancient site of significant religious importance",
        ),
    )
    RESEARCH_INSTITUTE = (
        "ITTR",
        pgettext_lazy(
            "LocationType description",
            "a facility where research is carried out",
        ),
    )
    RESERVATION = (
        "RESV",
        pgettext_lazy(
            "LocationType description",
            "a tract of land set aside for aboriginal, tribal, or native populations",
        ),
    )
    RESERVE = (
        "RES",
        pgettext_lazy(
            "LocationType description",
            "a tract of public land reserved for future use or restricted as to use",
        ),
    )
    RESERVOIR_S_ = (
        "RSV",
        pgettext_lazy("LocationType description", "an artificial pond or lake"),
    )
    RESORT = (
        "RSRT",
        pgettext_lazy(
            "LocationType description",
            "a specialized facility for vacation, health, or participation sports activities",
        ),
    )
    RESTHOUSE = (
        "RHSE",
        pgettext_lazy(
            "LocationType description",
            "a structure maintained for the rest and shelter of travelers",
        ),
    )
    RETREAT = (
        "RLGR",
        pgettext_lazy(
            "LocationType description",
            "a place of temporary seclusion, especially for religious groups",
        ),
    )
    RIDGE_S_ = (
        "RDGE",
        pgettext_lazy(
            "LocationType description",
            "a long narrow elevation with steep sides, and a more or less continuous crest",
        ),
    )
    ROAD = (
        "RD",
        pgettext_lazy(
            "LocationType description",
            "an open way with improved surface for transportation of animals, people and vehicles",
        ),
    )
    ROAD_BEND = (
        "RDB",
        pgettext_lazy(
            "LocationType description",
            "a conspicuously curved or bent section of a road",
        ),
    )
    ROAD_CUT = (
        "RDCUT",
        pgettext_lazy(
            "LocationType description",
            "an excavation cut through a hill or ridge for a road",
        ),
    )
    ROAD_JUNCTION = (
        "RDJCT",
        pgettext_lazy(
            "LocationType description",
            "a place where two or more roads join",
        ),
    )
    ROAD_TUNNEL = (
        "TNLRD",
        pgettext_lazy(
            "LocationType description",
            "a tunnel through which a road passes",
        ),
    )
    ROADSTEAD = (
        "RDST",
        pgettext_lazy(
            "LocationType description",
            "an open anchorage affording less protection than a harbor",
        ),
    )
    ROCK = (
        "RK",
        pgettext_lazy(
            "LocationType description",
            "a conspicuous, isolated rocky mass",
        ),
    )
    ROCK_DESERT = (
        "HMDA",
        pgettext_lazy(
            "LocationType description",
            "a relatively sand-free, high bedrock plateau in a hot desert, with or without a gravel veneer",
        ),
    )
    ROCKFALL = (
        "RKFL",
        pgettext_lazy(
            "LocationType description",
            "an irregular mass of fallen rock at the base of a cliff or steep slope",
        ),
    )
    ROCKS = (
        "RKS",
        pgettext_lazy(
            "LocationType description",
            "conspicuous, isolated rocky masses",
        ),
    )
    ROOKERY = (
        "RKRY",
        pgettext_lazy(
            "LocationType description",
            "a breeding place of a colony of birds or seals",
        ),
    )
    RUBBER_PLANTATION = (
        "ESTR",
        pgettext_lazy(
            "LocationType description",
            "an estate which specializes in growing and tapping rubber trees",
        ),
    )
    RUIN_S_ = (
        "RUIN",
        pgettext_lazy(
            "LocationType description",
            "a destroyed or decayed structure which is no longer functional",
        ),
    )
    RUINED_BRIDGE = (
        "BDGQ",
        pgettext_lazy(
            "LocationType description",
            "a destroyed or decayed bridge which is no longer functional",
        ),
    )
    RUINED_DAM = (
        "DAMQ",
        pgettext_lazy(
            "LocationType description",
            "a destroyed or decayed dam which is no longer functional",
        ),
    )
    SABKHA_S_ = (
        "SBKH",
        pgettext_lazy(
            "LocationType description",
            "a salt flat or salt encrusted plain subject to periodic inundation from flooding or high tides",
        ),
    )
    SADDLE = (
        "SDL",
        pgettext_lazy(
            "LocationType description",
            "a broad, open pass crossing a ridge or between hills or mountains",
        ),
    )
    SALT_AREA = (
        "SALT",
        pgettext_lazy(
            "LocationType description",
            "a shallow basin or flat where salt accumulates after periodic inundation",
        ),
    )
    SALT_EVAPORATION_PONDS = (
        "MFGN",
        pgettext_lazy(
            "LocationType description",
            "diked salt ponds used in the production of solar evaporated salt",
        ),
    )
    SALT_LAKE = (
        "LKN",
        pgettext_lazy(
            "LocationType description",
            "an inland body of salt water with no outlet",
        ),
    )
    SALT_LAKES = (
        "LKSN",
        pgettext_lazy(
            "LocationType description",
            "inland bodies of salt water with no outlet",
        ),
    )
    SALT_MARSH = (
        "MRSHN",
        pgettext_lazy(
            "LocationType description",
            "a flat area, subject to periodic salt water inundation, dominated by grassy salt-tolerant plants",
        ),
    )
    SALT_MINE_S_ = (
        "MNN",
        pgettext_lazy(
            "LocationType description",
            "a mine from which salt is extracted",
        ),
    )
    SALT_POND = (
        "PNDN",
        pgettext_lazy(
            "LocationType description",
            "a small standing body of salt water often in a marsh or swamp, usually along a seacoast",
        ),
    )
    SALT_PONDS = (
        "PNDSN",
        pgettext_lazy(
            "LocationType description",
            "small standing bodies of salt water often in a marsh or swamp, usually along a seacoast",
        ),
    )
    SANATORIUM = (
        "SNTR",
        pgettext_lazy(
            "LocationType description",
            "a facility where victims of physical or mental disorders are treated",
        ),
    )
    SAND_AREA = (
        "SAND",
        pgettext_lazy(
            "LocationType description",
            "a tract of land covered with sand",
        ),
    )
    SANDY_DESERT = (
        "ERG",
        pgettext_lazy(
            "LocationType description",
            "an extensive tract of shifting sand and sand dunes",
        ),
    )
    SATELLITE_STATION = (
        "STNS",
        pgettext_lazy(
            "LocationType description",
            "a facility for tracking and communicating with orbiting satellites",
        ),
    )
    SAWMILL = (
        "MLSW",
        pgettext_lazy(
            "LocationType description",
            "a mill where logs or lumber are sawn to specified shapes and sizes",
        ),
    )
    SCHOOL = (
        "SCH",
        pgettext_lazy(
            "LocationType description",
            "building(s) where instruction in one or more branches of knowledge takes place",
        ),
    )
    SCHOOL_DISTRICT = (
        "ADMS",
        pgettext_lazy("LocationType description", "school district"),
    )
    SCIENTIFIC_RESEARCH_BASE = (
        "STNB",
        pgettext_lazy(
            "LocationType description",
            "a scientific facility used as a base from which research is carried out or monitored",
        ),
    )
    SCRUBLAND = (
        "SCRB",
        pgettext_lazy(
            "LocationType description",
            "an area of low trees, bushes, and shrubs stunted by some environmental limitation",
        ),
    )
    SEA = (
        "SEA",
        pgettext_lazy(
            "LocationType description",
            "a large body of salt water more or less confined by continuous land or chains of islands forming a subdivision of an ocean",
        ),
    )
    SEACHANNEL = (
        "SCNU",
        pgettext_lazy(
            "LocationType description",
            "a continuously sloping, elongated depression commonly found in fans or plains and customarily bordered by levees on one or two sides",
        ),
    )
    SEACHANNELS = (
        "SCSU",
        pgettext_lazy(
            "LocationType description",
            "continuously sloping, elongated depressions commonly found in fans or plains and customarily bordered by levees on one or two sides",
        ),
    )
    SEAMOUNT = (
        "SMU",
        pgettext_lazy(
            "LocationType description",
            "an elevation rising generally more than 1,000 meters and of limited extent across the summit",
        ),
    )
    SEAMOUNTS = (
        "SMSU",
        pgettext_lazy(
            "LocationType description",
            "elevations rising generally more than 1,000 meters and of limited extent across the summit",
        ),
    )
    SEAPLANE_LANDING_AREA = (
        "AIRS",
        pgettext_lazy(
            "LocationType description",
            "a place on a waterbody where floatplanes land and take off",
        ),
    )
    SEAT_OF_A_FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA",
        pgettext_lazy(
            "LocationType description",
            "seat of a first-order administrative division (PPLC takes precedence over PPLA)",
        ),
    )
    SEAT_OF_A_FOURTH_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA4",
        pgettext_lazy(
            "LocationType description",
            "seat of a fourth-order administrative division",
        ),
    )
    SEAT_OF_A_SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA2",
        pgettext_lazy(
            "LocationType description",
            "seat of a second-order administrative division",
        ),
    )
    SEAT_OF_A_THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "PPLA3",
        pgettext_lazy(
            "LocationType description",
            "seat of a third-order administrative division",
        ),
    )
    SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM2",
        pgettext_lazy(
            "LocationType description",
            "a subdivision of a first-order administrative division",
        ),
    )
    SECTION_OF_BANK = (
        "BNKX",
        pgettext_lazy("LocationType description", "section of bank"),
    )
    SECTION_OF_CANAL = (
        "CNLX",
        pgettext_lazy("LocationType description", "section of canal"),
    )
    SECTION_OF_ESTATE = (
        "ESTX",
        pgettext_lazy("LocationType description", "section of estate"),
    )
    SECTION_OF_HARBOR = (
        "HBRX",
        pgettext_lazy("LocationType description", "section of harbor"),
    )
    SECTION_OF_INDEPENDENT_POLITICAL_ENTITY = (
        "PCLIX",
        pgettext_lazy(
            "LocationType description",
            "section of independent political entity",
        ),
    )
    SECTION_OF_INTERMITTENT_STREAM = (
        "STMIX",
        pgettext_lazy("LocationType description", "section of intermittent stream"),
    )
    SECTION_OF_ISLAND = (
        "ISLX",
        pgettext_lazy("LocationType description", "section of island"),
    )
    SECTION_OF_LAGOON = (
        "LGNX",
        pgettext_lazy("LocationType description", "section of lagoon"),
    )
    SECTION_OF_LAKE = (
        "LKX",
        pgettext_lazy("LocationType description", "section of lake"),
    )
    SECTION_OF_PENINSULA = (
        "PENX",
        pgettext_lazy("LocationType description", "section of peninsula"),
    )
    SECTION_OF_PLAIN = (
        "PLNX",
        pgettext_lazy("LocationType description", "section of plain"),
    )
    SECTION_OF_PLATEAU = (
        "PLATX",
        pgettext_lazy("LocationType description", "section of plateau"),
    )
    SECTION_OF_POPULATED_PLACE = (
        "PPLX",
        pgettext_lazy("LocationType description", "section of populated place"),
    )
    SECTION_OF_REEF = (
        "RFX",
        pgettext_lazy("LocationType description", "section of reef"),
    )
    SECTION_OF_STREAM = (
        "STMX",
        pgettext_lazy("LocationType description", "section of stream"),
    )
    SECTION_OF_VALLEY = (
        "VALX",
        pgettext_lazy("LocationType description", "section of valley"),
    )
    SECTION_OF_WADI = (
        "WADX",
        pgettext_lazy("LocationType description", "section of wadi"),
    )
    SECTION_OF_WATERFALL_S_ = (
        "FLLSX",
        pgettext_lazy("LocationType description", "section of waterfall(s)"),
    )
    SEMI_INDEPENDENT_POLITICAL_ENTITY = (
        "PCLS",
        pgettext_lazy(
            "LocationType description",
            "semi-independent political entity",
        ),
    )
    SEWAGE_TREATMENT_PLANT = (
        "SWT",
        pgettext_lazy(
            "LocationType description",
            "facility for the processing of sewage and/or wastewater",
        ),
    )
    SHEEPFOLD = (
        "SHPF",
        pgettext_lazy(
            "LocationType description",
            "a fence or wall enclosure for sheep and other small herd animals",
        ),
    )
    SHOAL_S_ = (
        "SHOL",
        pgettext_lazy(
            "LocationType description",
            "a surface-navigation hazard composed of unconsolidated material",
        ),
    )
    SHOPPING_CENTER_OR_MALL = (
        "SHOPC",
        pgettext_lazy(
            "LocationType description",
            "an urban shopping area featuring a variety of shops surrounding a usually open-air concourse reserved for pedestrian traffic; or a large suburban building or group of buildings containing various shops with associated passageways",
        ),
    )
    SHORE = (
        "SHOR",
        pgettext_lazy(
            "LocationType description",
            "a narrow zone bordering a waterbody which covers and uncovers at high and low water, respectively",
        ),
    )
    SHRINE = (
        "SHRN",
        pgettext_lazy(
            "LocationType description",
            "a structure or place memorializing a person or religious concept",
        ),
    )
    SILL = (
        "SILL",
        pgettext_lazy(
            "LocationType description",
            "the low part of a gap or saddle separating basins",
        ),
    )
    SINKHOLE = (
        "SINK",
        pgettext_lazy(
            "LocationType description",
            "a small crater-shape depression in a karst area",
        ),
    )
    SISAL_PLANTATION = (
        "ESTSL",
        pgettext_lazy(
            "LocationType description",
            "an estate that specializes in growing sisal",
        ),
    )
    SLIDE = (
        "SLID",
        pgettext_lazy(
            "LocationType description",
            "a mound of earth material, at the base of a slope and the associated scoured area",
        ),
    )
    SLOPE_S_ = (
        "SLP",
        pgettext_lazy(
            "LocationType description",
            "a surface with a relatively uniform slope angle",
        ),
    )
    SLUICE = (
        "SLCE",
        pgettext_lazy(
            "LocationType description",
            "a conduit or passage for carrying off surplus water from a waterbody, usually regulated by means of a sluice gate",
        ),
    )
    SNOWFIELD = (
        "SNOW",
        pgettext_lazy(
            "LocationType description",
            "an area of permanent snow and ice forming the accumulation area of a glacier",
        ),
    )
    SOUND = (
        "SD",
        pgettext_lazy(
            "LocationType description",
            "a long arm of the sea forming a channel between the mainland and an island or islands; or connecting two larger bodies of water",
        ),
    )
    SPA = (
        "SPA",
        pgettext_lazy(
            "LocationType description",
            "a resort area usually developed around a medicinal spring",
        ),
    )
    SPACE_CENTER = (
        "CTRS",
        pgettext_lazy(
            "LocationType description",
            "a facility for launching, tracking, or controlling satellites and space vehicles",
        ),
    )
    SPILLWAY = (
        "SPLY",
        pgettext_lazy(
            "LocationType description",
            "a passage or outlet through which surplus water flows over, around or through a dam",
        ),
    )
    SPIT = (
        "SPIT",
        pgettext_lazy(
            "LocationType description",
            "a narrow, straight or curved continuation of a beach into a waterbody",
        ),
    )
    SPRING_S_ = (
        "SPNG",
        pgettext_lazy(
            "LocationType description",
            "a place where ground water flows naturally out of the ground",
        ),
    )
    SPUR_S_ = (
        "SPUR",
        pgettext_lazy(
            "LocationType description",
            "a subordinate ridge projecting outward from a hill, mountain or other elevation",
        ),
    )
    SQUARE = (
        "SQR",
        pgettext_lazy(
            "LocationType description",
            "a broad, open, public area near the center of a town or city",
        ),
    )
    STABLE = (
        "STBL",
        pgettext_lazy(
            "LocationType description",
            "a building for the shelter and feeding of farm animals, especially horses",
        ),
    )
    STADIUM = (
        "STDM",
        pgettext_lazy(
            "LocationType description",
            "a structure with an enclosure for athletic games with tiers of seats for spectators",
        ),
    )
    STEPS = (
        "STPS",
        pgettext_lazy(
            "LocationType description",
            "stones or slabs placed for ease in ascending or descending a steep slope",
        ),
    )
    STOCK_ROUTE = (
        "STKR",
        pgettext_lazy("LocationType description", "a route taken by livestock herds"),
    )
    STONY_DESERT = (
        "REG",
        pgettext_lazy(
            "LocationType description",
            "a desert plain characterized by a surface veneer of gravel and stones",
        ),
    )
    STORE = (
        "RET",
        pgettext_lazy(
            "LocationType description",
            "a building where goods and/or services are offered for sale",
        ),
    )
    STOREHOUSE = (
        "SHSE",
        pgettext_lazy(
            "LocationType description",
            "a building for storing goods, especially provisions",
        ),
    )
    STRAIT = (
        "STRT",
        pgettext_lazy(
            "LocationType description",
            "a relatively narrow waterway, usually narrower and less extensive than a sound, connecting two larger bodies of water",
        ),
    )
    STREAM = (
        "STM",
        pgettext_lazy(
            "LocationType description",
            "a body of running water moving to a lower level in a channel on land",
        ),
    )
    STREAM_BANK = (
        "BNKR",
        pgettext_lazy(
            "LocationType description",
            "a sloping margin of a stream channel which normally confines the stream to its channel on land",
        ),
    )
    STREAM_BEND = (
        "STMB",
        pgettext_lazy(
            "LocationType description",
            "a conspicuously curved or bent segment of a stream",
        ),
    )
    STREAM_GAUGING_STATION = (
        "STMGS",
        pgettext_lazy(
            "LocationType description",
            "named place where a measuring station for a watercourse, reservoir or other water body exists",
        ),
    )
    STREAM_MOUTH_S_ = (
        "STMM",
        pgettext_lazy(
            "LocationType description",
            "a place where a stream discharges into a lagoon, lake, or the sea",
        ),
    )
    STREAMS = (
        "STMS",
        pgettext_lazy(
            "LocationType description",
            "bodies of running water moving to a lower level in a channel on land",
        ),
    )
    STREET = (
        "ST",
        pgettext_lazy("LocationType description", "a paved urban thoroughfare"),
    )
    SUB_SURFACE_DAM = (
        "DAMSB",
        pgettext_lazy(
            "LocationType description",
            "a dam put down to bedrock in a sand river",
        ),
    )
    SUBWAY = (
        "SUBW",
        pgettext_lazy(
            "LocationType description",
            "a railroad used for mass public transportation primarily in urban areas, all or part of the system may be located below, above, or at ground level",
        ),
    )
    SUBWAY_STATION = (
        "SUBS",
        pgettext_lazy(
            "LocationType description",
            "a facility comprising ticket office, platforms, etc. for loading and unloading subway passengers",
        ),
    )
    SUGAR_MILL = (
        "MLSG",
        pgettext_lazy(
            "LocationType description",
            "a facility where sugar cane is processed into raw sugar",
        ),
    )
    SUGAR_PLANTATION = (
        "ESTSG",
        pgettext_lazy(
            "LocationType description",
            "an estate that specializes in growing sugar cane",
        ),
    )
    SUGAR_REFINERY = (
        "MFGSG",
        pgettext_lazy(
            "LocationType description",
            "a facility for converting raw sugar into refined sugar",
        ),
    )
    SULPHUR_SPRING_S_ = (
        "SPNS",
        pgettext_lazy(
            "LocationType description",
            "a place where sulphur ground water flows naturally out of the ground",
        ),
    )
    SWAMP = (
        "SWMP",
        pgettext_lazy(
            "LocationType description",
            "a wetland dominated by tree vegetation",
        ),
    )
    SYNAGOGUE = (
        "SYG",
        pgettext_lazy(
            "LocationType description",
            "a place for Jewish worship and religious instruction",
        ),
    )
    TABLEMOUNT__OR_GUYOT_ = (
        "TMTU",
        pgettext_lazy(
            "LocationType description",
            "a seamount having a comparatively smooth, flat top",
        ),
    )
    TABLEMOUNTS__OR_GUYOTS_ = (
        "TMSU",
        pgettext_lazy(
            "LocationType description",
            "seamounts having a comparatively smooth, flat top",
        ),
    )
    TALUS_SLOPE = (
        "TAL",
        pgettext_lazy(
            "LocationType description",
            "a steep concave slope formed by an accumulation of loose rock fragments at the base of a cliff or steep slope",
        ),
    )
    TANK_FARM = (
        "OILT",
        pgettext_lazy(
            "LocationType description",
            "a tract of land occupied by large, cylindrical, metal tanks in which oil or liquid petrochemicals are stored",
        ),
    )
    TEA_PLANTATION = (
        "ESTT",
        pgettext_lazy(
            "LocationType description",
            "an estate which specializes in growing tea bushes",
        ),
    )
    TECHNICAL_SCHOOL = (
        "SCHT",
        pgettext_lazy(
            "LocationType description",
            "post-secondary school with a specifically technical or vocational curriculum",
        ),
    )
    TEMPLE_S_ = (
        "TMPL",
        pgettext_lazy(
            "LocationType description",
            "an edifice dedicated to religious worship",
        ),
    )
    TERMINAL = (
        "AIRT",
        pgettext_lazy(
            "LocationType description",
            "airport facilities for the handling of freight and passengers",
        ),
    )
    TERRACE = (
        "TRR",
        pgettext_lazy(
            "LocationType description",
            "a long, narrow alluvial platform bounded by steeper slopes above and below, usually overlooking a waterbody",
        ),
    )
    TERRITORY = (
        "TERR",
        pgettext_lazy("LocationType description", "territory"),
    )
    THIRD_ORDER_ADMINISTRATIVE_DIVISION = (
        "ADM3",
        pgettext_lazy(
            "LocationType description",
            "a subdivision of a second-order administrative division",
        ),
    )
    TIDAL_CREEK_S_ = (
        "CRKT",
        pgettext_lazy(
            "LocationType description",
            "a meandering channel in a coastal wetland subject to bi-directional tidal currents",
        ),
    )
    TIDAL_FLAT_S_ = (
        "FLTT",
        pgettext_lazy(
            "LocationType description",
            "a large flat area of mud or sand attached to the shore and alternately covered and uncovered by the tide",
        ),
    )
    TIN_MINE_S_ = (
        "MNSN",
        pgettext_lazy(
            "LocationType description",
            "a mine where tin ore is extracted",
        ),
    )
    TOLL_GATE_BARRIER = (
        "TOLL",
        pgettext_lazy("LocationType description", "highway toll collection station"),
    )
    TOMB_S_ = (
        "TMB",
        pgettext_lazy("LocationType description", "a structure for interring bodies"),
    )
    TOWER = (
        "TOWR",
        pgettext_lazy(
            "LocationType description",
            "a high conspicuous structure, typically much higher than its diameter",
        ),
    )
    TRAFFIC_CIRCLE = (
        "RDCR",
        pgettext_lazy(
            "LocationType description",
            "a road junction formed around a central circle about which traffic moves in one direction only",
        ),
    )
    TRAIL = (
        "TRL",
        pgettext_lazy(
            "LocationType description",
            "a path, track, or route used by pedestrians, animals, or off-road vehicles",
        ),
    )
    TRANSIT_TERMINAL = (
        "TRANT",
        pgettext_lazy(
            "LocationType description",
            "facilities for the handling of vehicular freight and passengers",
        ),
    )
    TREE_S_ = (
        "TREE",
        pgettext_lazy(
            "LocationType description",
            "a conspicuous tree used as a landmark",
        ),
    )
    TRIANGULATION_STATION = (
        "TRIG",
        pgettext_lazy(
            "LocationType description",
            "a point on the earth whose position has been determined by triangulation",
        ),
    )
    TRIBAL_AREA = (
        "TRB",
        pgettext_lazy(
            "LocationType description",
            "a tract of land used by nomadic or other tribes",
        ),
    )
    TUNDRA = (
        "TUND",
        pgettext_lazy(
            "LocationType description",
            "a marshy, treeless, high latitude plain, dominated by mosses, lichens, and low shrub vegetation under permafrost conditions",
        ),
    )
    TUNNEL = (
        "TNL",
        pgettext_lazy(
            "LocationType description",
            "a subterranean passageway for transportation",
        ),
    )
    TUNNELS = (
        "TNLS",
        pgettext_lazy(
            "LocationType description",
            "subterranean passageways for transportation",
        ),
    )
    UNDERGROUND_IRRIGATION_CANAL_S_ = (
        "CNLSB",
        pgettext_lazy(
            "LocationType description",
            "a gently inclined underground tunnel bringing water for irrigation from aquifers",
        ),
    )
    UNDERGROUND_LAKE = (
        "LKSB",
        pgettext_lazy(
            "LocationType description",
            "a standing body of water in a cave",
        ),
    )
    UNDERSEA_APRON = (
        "APNU",
        pgettext_lazy(
            "LocationType description",
            "a gentle slope, with a generally smooth surface, particularly found around groups of islands and seamounts",
        ),
    )
    UNDERSEA_ARCH = (
        "ARCU",
        pgettext_lazy(
            "LocationType description",
            "a low bulge around the southeastern end of the island of Hawaii",
        ),
    )
    UNDERSEA_ARRUGADO = (
        "ARRU",
        pgettext_lazy(
            "LocationType description",
            "an area of subdued corrugations off Baja California",
        ),
    )
    UNDERSEA_BANK = (
        "BNKU",
        pgettext_lazy(
            "LocationType description",
            "an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation",
        ),
    )
    UNDERSEA_BANKS = (
        "BKSU",
        pgettext_lazy(
            "LocationType description",
            "elevations, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation",
        ),
    )
    UNDERSEA_BASIN = (
        "BSNU",
        pgettext_lazy(
            "LocationType description",
            "a depression more or less equidimensional in plan and of variable extent",
        ),
    )
    UNDERSEA_BENCH = (
        "BNCU",
        pgettext_lazy("LocationType description", "a small terrace"),
    )
    UNDERSEA_BORDERLAND = (
        "BDLU",
        pgettext_lazy(
            "LocationType description",
            "a region adjacent to a continent, normally occupied by or bordering a shelf, that is highly irregular with depths well in excess of those typical of a shelf",
        ),
    )
    UNDERSEA_CANYON = (
        "CNYU",
        pgettext_lazy(
            "LocationType description",
            "a relatively narrow, deep depression with steep sides, the bottom of which generally has a continuous slope",
        ),
    )
    UNDERSEA_CANYONS = (
        "CNSU",
        pgettext_lazy(
            "LocationType description",
            "relatively narrow, deep depressions with steep sides, the bottom of which generally has a continuous slope",
        ),
    )
    UNDERSEA_CORDILLERA = (
        "CDAU",
        pgettext_lazy(
            "LocationType description",
            "an entire mountain system including the subordinate ranges, interior plateaus, and basins",
        ),
    )
    UNDERSEA_ESCARPMENT__OR_SCARP_ = (
        "ESCU",
        pgettext_lazy(
            "LocationType description",
            "an elongated and comparatively steep slope separating flat or gently sloping areas",
        ),
    )
    UNDERSEA_FAN = (
        "FANU",
        pgettext_lazy(
            "LocationType description",
            "a relatively smooth feature normally sloping away from the lower termination of a canyon or canyon system",
        ),
    )
    UNDERSEA_FLAT = (
        "FLTU",
        pgettext_lazy(
            "LocationType description",
            "a small level or nearly level area",
        ),
    )
    UNDERSEA_FORK = (
        "FRKU",
        pgettext_lazy("LocationType description", "a branch of a canyon or valley"),
    )
    UNDERSEA_FORKS = (
        "FRSU",
        pgettext_lazy("LocationType description", "a branch of a canyon or valley"),
    )
    UNDERSEA_FRACTURE_ZONE = (
        "FRZU",
        pgettext_lazy(
            "LocationType description",
            "an extensive linear zone of irregular topography of the sea floor, characterized by steep-sided or asymmetrical ridges, troughs, or escarpments",
        ),
    )
    UNDERSEA_FURROW = (
        "FURU",
        pgettext_lazy(
            "LocationType description",
            "a closed, linear, narrow, shallow depression",
        ),
    )
    UNDERSEA_GAP = (
        "GAPU",
        pgettext_lazy(
            "LocationType description",
            "a narrow break in a ridge or rise",
        ),
    )
    UNDERSEA_GULLY = (
        "GLYU",
        pgettext_lazy("LocationType description", "a small valley-like feature"),
    )
    UNDERSEA_HILL = (
        "HLLU",
        pgettext_lazy(
            "LocationType description",
            "an elevation rising generally less than 500 meters",
        ),
    )
    UNDERSEA_HILLS = (
        "HLSU",
        pgettext_lazy(
            "LocationType description",
            "elevations rising generally less than 500 meters",
        ),
    )
    UNDERSEA_HOLE = (
        "HOLU",
        pgettext_lazy(
            "LocationType description",
            "a small depression of the sea floor",
        ),
    )
    UNDERSEA_KNOLL = (
        "KNLU",
        pgettext_lazy(
            "LocationType description",
            "an elevation rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summit",
        ),
    )
    UNDERSEA_KNOLLS = (
        "KNSU",
        pgettext_lazy(
            "LocationType description",
            "elevations rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summits",
        ),
    )
    UNDERSEA_LEDGE = (
        "LDGU",
        pgettext_lazy(
            "LocationType description",
            "a rocky projection or outcrop, commonly linear and near shore",
        ),
    )
    UNDERSEA_LEVEE = (
        "LEVU",
        pgettext_lazy(
            "LocationType description",
            "an embankment bordering a canyon, valley, or seachannel",
        ),
    )
    UNDERSEA_MEDIAN_VALLEY = (
        "MDVU",
        pgettext_lazy(
            "LocationType description",
            "the axial depression of the mid-oceanic ridge system",
        ),
    )
    UNDERSEA_MESA = (
        "MESU",
        pgettext_lazy(
            "LocationType description",
            "an isolated, extensive, flat-topped elevation on the shelf, with relatively steep sides",
        ),
    )
    UNDERSEA_MOAT = (
        "MOTU",
        pgettext_lazy(
            "LocationType description",
            "an annular depression that may not be continuous, located at the base of many seamounts, islands, and other isolated elevations",
        ),
    )
    UNDERSEA_MOUND = (
        "MNDU",
        pgettext_lazy("LocationType description", "a low, isolated, rounded hill"),
    )
    UNDERSEA_MOUNTAIN = (
        "MTU",
        pgettext_lazy(
            "LocationType description",
            "a well-delineated subdivision of a large and complex positive feature",
        ),
    )
    UNDERSEA_MOUNTAINS = (
        "MTSU",
        pgettext_lazy(
            "LocationType description",
            "well-delineated subdivisions of a large and complex positive feature",
        ),
    )
    UNDERSEA_PEAK = (
        "PKU",
        pgettext_lazy(
            "LocationType description",
            "a prominent elevation, part of a larger feature, either pointed or of very limited extent across the summit",
        ),
    )
    UNDERSEA_PEAKS = (
        "PKSU",
        pgettext_lazy(
            "LocationType description",
            "prominent elevations, part of a larger feature, either pointed or of very limited extent across the summit",
        ),
    )
    UNDERSEA_PINNACLE = (
        "PNLU",
        pgettext_lazy(
            "LocationType description",
            "a high tower or spire-shaped pillar of rock or coral, alone or cresting a summit",
        ),
    )
    UNDERSEA_PLAIN = (
        "PLNU",
        pgettext_lazy(
            "LocationType description",
            "a flat, gently sloping or nearly level region",
        ),
    )
    UNDERSEA_PLATEAU = (
        "PLTU",
        pgettext_lazy(
            "LocationType description",
            "a comparatively flat-topped feature of considerable extent, dropping off abruptly on one or more sides",
        ),
    )
    UNDERSEA_PLATFORM = (
        "PLFU",
        pgettext_lazy(
            "LocationType description",
            "a flat or gently sloping underwater surface extending seaward from the shore",
        ),
    )
    UNDERSEA_PROVINCE = (
        "PRVU",
        pgettext_lazy(
            "LocationType description",
            "a region identifiable by a group of similar physiographic features whose characteristics are markedly in contrast with surrounding areas",
        ),
    )
    UNDERSEA_RAMP = (
        "RMPU",
        pgettext_lazy(
            "LocationType description",
            "a gentle slope connecting areas of different elevations",
        ),
    )
    UNDERSEA_RANGE = (
        "RNGU",
        pgettext_lazy(
            "LocationType description",
            "a series of associated ridges or seamounts",
        ),
    )
    UNDERSEA_RAVINE = (
        "RAVU",
        pgettext_lazy("LocationType description", "a small canyon"),
    )
    UNDERSEA_REEF = (
        "RFU",
        pgettext_lazy(
            "LocationType description",
            "a surface-navigation hazard composed of consolidated material",
        ),
    )
    UNDERSEA_REEFS = (
        "RFSU",
        pgettext_lazy(
            "LocationType description",
            "surface-navigation hazards composed of consolidated material",
        ),
    )
    UNDERSEA_RIDGE = (
        "RDGU",
        pgettext_lazy(
            "LocationType description",
            "a long narrow elevation with steep sides",
        ),
    )
    UNDERSEA_RIDGES = (
        "RDSU",
        pgettext_lazy(
            "LocationType description",
            "long narrow elevations with steep sides",
        ),
    )
    UNDERSEA_RISE = (
        "RISU",
        pgettext_lazy(
            "LocationType description",
            "a broad elevation that rises gently, and generally smoothly, from the sea floor",
        ),
    )
    UNDERSEA_SADDLE = (
        "SDLU",
        pgettext_lazy(
            "LocationType description",
            "a low part, resembling in shape a saddle, in a ridge or between contiguous seamounts",
        ),
    )
    UNDERSEA_SHELF = (
        "SHFU",
        pgettext_lazy(
            "LocationType description",
            "a zone adjacent to a continent (or around an island) that extends from the low water line to a depth at which there is usually a marked increase of slope towards oceanic depths",
        ),
    )
    UNDERSEA_SHELF_EDGE = (
        "EDGU",
        pgettext_lazy(
            "LocationType description",
            "a line along which there is a marked increase of slope at the outer margin of a continental shelf or island shelf",
        ),
    )
    UNDERSEA_SHELF_VALLEY = (
        "SHVU",
        pgettext_lazy(
            "LocationType description",
            "a valley on the shelf, generally the shoreward extension of a canyon",
        ),
    )
    UNDERSEA_SHOAL = (
        "SHLU",
        pgettext_lazy(
            "LocationType description",
            "a surface-navigation hazard composed of unconsolidated material",
        ),
    )
    UNDERSEA_SHOALS = (
        "SHSU",
        pgettext_lazy(
            "LocationType description",
            "hazards to surface navigation composed of unconsolidated material",
        ),
    )
    UNDERSEA_SILL = (
        "SILU",
        pgettext_lazy(
            "LocationType description",
            "the low part of an underwater gap or saddle separating basins, including a similar feature at the mouth of a fjord",
        ),
    )
    UNDERSEA_SLOPE = (
        "SLPU",
        pgettext_lazy(
            "LocationType description",
            "the slope seaward from the shelf edge to the beginning of a continental rise or the point where there is a general reduction in slope",
        ),
    )
    UNDERSEA_SPUR = (
        "SPRU",
        pgettext_lazy(
            "LocationType description",
            "a subordinate elevation, ridge, or rise projecting outward from a larger feature",
        ),
    )
    UNDERSEA_TERRACE = (
        "TERU",
        pgettext_lazy(
            "LocationType description",
            "a relatively flat horizontal or gently inclined surface, sometimes long and narrow, which is bounded by a steeper ascending slope on one side and by a steep descending slope on the opposite side",
        ),
    )
    UNDERSEA_TONGUE = (
        "TNGU",
        pgettext_lazy(
            "LocationType description",
            "an elongate (tongue-like) extension of a flat sea floor into an adjacent higher feature",
        ),
    )
    UNDERSEA_TRENCH = (
        "TRNU",
        pgettext_lazy(
            "LocationType description",
            "a long, narrow, characteristically very deep and asymmetrical depression of the sea floor, with relatively steep sides",
        ),
    )
    UNDERSEA_TROUGH = (
        "TRGU",
        pgettext_lazy(
            "LocationType description",
            "a long depression of the sea floor characteristically flat bottomed and steep sided, and normally shallower than a trench",
        ),
    )
    UNDERSEA_VALLEY = (
        "VALU",
        pgettext_lazy(
            "LocationType description",
            "a relatively shallow, wide depression, the bottom of which usually has a continuous gradient",
        ),
    )
    UNDERSEA_VALLEYS = (
        "VLSU",
        pgettext_lazy(
            "LocationType description",
            "a relatively shallow, wide depression, the bottom of which usually has a continuous gradient",
        ),
    )
    UNITED_STATES_GOVERNMENT_ESTABLISHMENT = (
        "USGE",
        pgettext_lazy(
            "LocationType description",
            "a facility operated by the United States Government in Panama",
        ),
    )
    UPLAND = (
        "UPLD",
        pgettext_lazy(
            "LocationType description",
            "an extensive interior region of high land with low to moderate surface relief",
        ),
    )
    VALLEY = (
        "VAL",
        pgettext_lazy(
            "LocationType description",
            "an elongated depression usually traversed by a stream",
        ),
    )
    VALLEYS = (
        "VALS",
        pgettext_lazy(
            "LocationType description",
            "elongated depressions usually traversed by a stream",
        ),
    )
    VETERINARY_FACILITY = (
        "VETF",
        pgettext_lazy(
            "LocationType description",
            "a building or camp at which veterinary services are available",
        ),
    )
    VINEYARD = (
        "VIN",
        pgettext_lazy("LocationType description", "a planting of grapevines"),
    )
    VINEYARDS = (
        "VINS",
        pgettext_lazy("LocationType description", "plantings of grapevines"),
    )
    VOLCANO = (
        "VLC",
        pgettext_lazy(
            "LocationType description",
            "a conical elevation composed of volcanic materials with a crater at the top",
        ),
    )
    WADI = (
        "WAD",
        pgettext_lazy(
            "LocationType description",
            "a valley or ravine, bounded by relatively steep banks, which in the rainy season becomes a watercourse; found primarily in North Africa and the Middle East",
        ),
    )
    WADI_BEND = (
        "WADB",
        pgettext_lazy(
            "LocationType description",
            "a conspicuously curved or bent segment of a wadi",
        ),
    )
    WADI_JUNCTION = (
        "WADJ",
        pgettext_lazy(
            "LocationType description",
            "a place where two or more wadies join",
        ),
    )
    WADI_MOUTH = (
        "WADM",
        pgettext_lazy(
            "LocationType description",
            "the lower terminus of a wadi where it widens into an adjoining floodplain, depression, or waterbody",
        ),
    )
    WADIES = (
        "WADS",
        pgettext_lazy(
            "LocationType description",
            "valleys or ravines, bounded by relatively steep banks, which in the rainy season become watercourses; found primarily in North Africa and the Middle East",
        ),
    )
    WALL = (
        "WALL",
        pgettext_lazy(
            "LocationType description",
            "a thick masonry structure, usually enclosing a field or building, or forming the side of a structure",
        ),
    )
    WATER_MILL = (
        "MLWTR",
        pgettext_lazy("LocationType description", "a mill powered by running water"),
    )
    WATER_PUMPING_STATION = (
        "PMPW",
        pgettext_lazy(
            "LocationType description",
            "a facility for pumping water from a major well or through a pipeline",
        ),
    )
    WATER_TANK = (
        "RSVT",
        pgettext_lazy(
            "LocationType description",
            "a contained pool or tank of water at, below, or above ground level",
        ),
    )
    WATERCOURSE = (
        "WTRC",
        pgettext_lazy(
            "LocationType description",
            "a natural, well-defined channel produced by flowing water, or an artificial channel designed to carry flowing water",
        ),
    )
    WATERFALL_S_ = (
        "FLLS",
        pgettext_lazy(
            "LocationType description",
            "a perpendicular or very steep descent of the water of a stream",
        ),
    )
    WATERHOLE_S_ = (
        "WTRH",
        pgettext_lazy(
            "LocationType description",
            "a natural hole, hollow, or small depression that contains water, used by man and animals, especially in arid areas",
        ),
    )
    WATERWORKS = (
        "WTRW",
        pgettext_lazy(
            "LocationType description",
            "a facility for supplying potable water through a water source and a system of pumps and filtration beds",
        ),
    )
    WEIR_S_ = (
        "WEIR",
        pgettext_lazy(
            "LocationType description",
            "a small dam in a stream, designed to raise the water level or to divert stream flow through a desired channel",
        ),
    )
    WELL = (
        "WLL",
        pgettext_lazy(
            "LocationType description",
            "a cylindrical hole, pit, or tunnel drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface",
        ),
    )
    WELLS = (
        "WLLS",
        pgettext_lazy(
            "LocationType description",
            "cylindrical holes, pits, or tunnels drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface",
        ),
    )
    WETLAND = (
        "WTLD",
        pgettext_lazy(
            "LocationType description",
            "an area subject to inundation, usually characterized by bog, marsh, or swamp vegetation",
        ),
    )
    WHALING_STATION = (
        "STNW",
        pgettext_lazy(
            "LocationType description",
            "a facility for butchering whales and processing train oil",
        ),
    )
    WHARF__VES_ = (
        "WHRF",
        pgettext_lazy(
            "LocationType description",
            "a structure of open rather than solid construction along a shore or a bank which provides berthing for ships and cargo-handling facilities",
        ),
    )
    WHIRLPOOL = (
        "WHRL",
        pgettext_lazy(
            "LocationType description",
            "a turbulent, rotating movement of water in a stream",
        ),
    )
    WILDLIFE_RESERVE = (
        "RESW",
        pgettext_lazy(
            "LocationType description",
            "a tract of public land reserved for the preservation of wildlife",
        ),
    )
    WINDMILL = (
        "MLWND",
        pgettext_lazy(
            "LocationType description",
            "a mill or water pump powered by wind",
        ),
    )
    WRECK = (
        "WRCK",
        pgettext_lazy(
            "LocationType description",
            "the site of the remains of a wrecked vessel",
        ),
    )
    ZONE = (
        "ZN",
        pgettext_lazy("LocationType description", "zone"),
    )
    ZOO = (
        "ZOO",
        pgettext_lazy(
            "LocationType description",
            "a zoological garden or park where wild animals are kept for exhibition",
        ),
    )
