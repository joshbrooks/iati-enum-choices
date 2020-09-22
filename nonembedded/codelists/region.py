from django.db import models
from django.utils.translation import pgettext_lazy


class Region(models.IntegerChoices):
    STATES_EX_YUGOSLAVIA_UNSPECIFIED = (
        88,
        pgettext_lazy("Region", "States Ex-Yugoslavia unspecified"),
    )
    EUROPE__REGIONAL = (
        89,
        pgettext_lazy("Region", "Europe, regional"),
    )
    NORTH_OF_SAHARA__REGIONAL = (
        189,
        pgettext_lazy("Region", "North of Sahara, regional"),
    )
    SOUTH_OF_SAHARA__REGIONAL = (
        289,
        pgettext_lazy("Region", "South of Sahara, regional"),
    )
    AFRICA__REGIONAL = (
        298,
        pgettext_lazy("Region", "Africa, regional"),
    )
    WEST_INDIES__REGIONAL = (
        380,
        pgettext_lazy("Region", "West Indies, regional"),
    )
    NORTH___CENTRAL_AMERICA__REGIONAL = (
        389,
        pgettext_lazy("Region", "North & Central America, regional"),
    )
    SOUTH_AMERICA__REGIONAL = (
        489,
        pgettext_lazy("Region", "South America, regional"),
    )
    AMERICA__REGIONAL = (
        498,
        pgettext_lazy("Region", "America, regional"),
    )
    MIDDLE_EAST__REGIONAL = (
        589,
        pgettext_lazy("Region", "Middle East, regional"),
    )
    CENTRAL_ASIA__REGIONAL = (
        619,
        pgettext_lazy("Region", "Central Asia, regional"),
    )
    SOUTH_ASIA__REGIONAL = (
        679,
        pgettext_lazy("Region", "South Asia, regional"),
    )
    SOUTH___CENTRAL_ASIA__REGIONAL = (
        689,
        pgettext_lazy("Region", "South & Central Asia, regional"),
    )
    FAR_EAST_ASIA__REGIONAL = (
        789,
        pgettext_lazy("Region", "Far East Asia, regional"),
    )
    ASIA__REGIONAL = (
        798,
        pgettext_lazy("Region", "Asia, regional"),
    )
    OCEANIA__REGIONAL = (
        889,
        pgettext_lazy("Region", "Oceania, regional"),
    )
    DEVELOPING_COUNTRIES__UNSPECIFIED = (
        998,
        pgettext_lazy("Region", "Developing countries, unspecified"),
    )
    EASTERN_AFRICA__REGIONAL = (
        1027,
        pgettext_lazy("Region", "Eastern Africa, regional"),
    )
    MIDDLE_AFRICA__REGIONAL = (
        1028,
        pgettext_lazy("Region", "Middle Africa, regional"),
    )
    SOUTHERN_AFRICA__REGIONAL = (
        1029,
        pgettext_lazy("Region", "Southern Africa, regional"),
    )
    WESTERN_AFRICA__REGIONAL = (
        1030,
        pgettext_lazy("Region", "Western Africa, regional"),
    )
    CARIBBEAN__REGIONAL = (
        1031,
        pgettext_lazy("Region", "Caribbean, regional"),
    )
    CENTRAL_AMERICA__REGIONAL = (
        1032,
        pgettext_lazy("Region", "Central America, regional"),
    )
    MELANESIA__REGIONAL = (
        1033,
        pgettext_lazy("Region", "Melanesia, regional"),
    )
    MICRONESIA__REGIONAL = (
        1034,
        pgettext_lazy("Region", "Micronesia, regional"),
    )
    POLYNESIA__REGIONAL = (
        1035,
        pgettext_lazy("Region", "Polynesia, regional"),
    )
