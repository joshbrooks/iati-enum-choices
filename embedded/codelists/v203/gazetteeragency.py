from django.db import models
from django.utils.translation import pgettext_lazy


class GazetteerAgency(models.IntegerChoices):
    """
    An online resource that holds coordinates and descriptions of geographic locations
    """

    GEONAMES_ORG = (
        1,
        pgettext_lazy("GazetteerAgency", "Geonames.org"),
    )
    NATIONAL_GEOSPATIAL_INTELLIGENCE_AGENCY = (
        2,
        pgettext_lazy("GazetteerAgency", "National Geospatial-Intelligence Agency"),
    )
    OPEN_STREET_MAP = (
        3,
        pgettext_lazy("GazetteerAgency", "Open Street Map"),
    )
