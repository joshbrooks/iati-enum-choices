from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicalPrecisionDescription(models.IntegerChoices):
    """
    A system for clarifying the accuracy and usage of geographical coordinates
    """

    EXACT_LOCATION = (
        1,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "The coordinates corresponds to an exact location, such as a populated place or a hill. The code is also used for locations that join a location which is a line (such as a road or railroad). Lines are not coded only the points that connect lines. All points that are mentioned in the source are coded.",
        ),
    )
    NEAR_EXACT_LOCATION = (
        2,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            'The location is mentioned in the source as being "near", in the "area" of, or up to 25 km away from an exact location. The coordinates refer to that adjacent, exact, location.',
        ),
    )
    SECOND_ORDER_ADMINISTRATIVE_DIVISION = (
        3,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "The location is, or lies in, a second order administrative division (ADM2), such as a district, municipality or commune",
        ),
    )
    FIRST_ORDER_ADMINISTRATIVE_DIVISION = (
        4,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "The location is, or lies in, a first order administrative division (ADM1), such as a province, state or governorate.",
        ),
    )
    ESTIMATED_COORDINATES = (
        5,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            'The location can only be related to estimated coordinates, such as when a location lies between populated places; along rivers, roads and borders; more than 25 km away from a specific location; or when sources refer to parts of a country greater than ADM1 (e.g. "northern Uganda").',
        ),
    )
    INDEPENDENT_POLITICAL_ENTITY = (
        6,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "The location can only be related to an independent political entity, meaning the pair of coordinates that represent a country.",
        ),
    )
    UNCLEAR_CAPITAL = (
        7,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "Unclear. The capital is assumed to be one of two possible locations. (The other option is the country level, with precision 9.)",
        ),
    )
    LOCAL_OR_NATIONAL_CAPITAL = (
        8,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "The location is estimated to be a seat of an administrative division (local capital) or the national capital. If aid goes to Luanda without further specification on the location, and there is an ADM1 and a capital called Luanda, then code the coordinates of the capital with precision 8. If it is not spelled out that aid goes to the capital; but if it is clear that it goes to a government ministry or to government financial institutions; and if those institutions are most likely located in the capital; then the coordinates of the capital are coded with precision 8. (However, if it can be verified that the recipient institution is located in the capital then precision 1 is used.)",
        ),
    )
    UNCLEAR_COUNTRY = (
        9,
        pgettext_lazy(
            "IATI codelist GeographicalPrecision description",
            "Unclear. The locations is estimated to be the country level (often paired with the capital, with precision 7)",
        ),
    )
