from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicVocabulary(models.TextChoices):
    GLOBAL_ADMININISTRATIVE_UNIT_LAYERS = (
        "A1",
        pgettext_lazy("GeographicVocabulary", "Global Admininistrative Unit Layers"),
    )
    UN_SECOND_ADMINISTRATIVE_LEVEL_BOUNDARY_PROJECT = (
        "A2",
        pgettext_lazy(
            "GeographicVocabulary",
            "UN Second Administrative Level Boundary Project",
        ),
    )
    GLOBAL_ADMINISTRATIVE_AREAS = (
        "A3",
        pgettext_lazy("GeographicVocabulary", "Global Administrative Areas"),
    )
    ISO_COUNTRY__3166_1_ALPHA_2_ = (
        "A4",
        pgettext_lazy("GeographicVocabulary", "ISO Country (3166-1 alpha-2)"),
    )
    GEONAMES = (
        "G1",
        pgettext_lazy("GeographicVocabulary", "Geonames"),
    )
    OPENSTREETMAP = (
        "G2",
        pgettext_lazy("GeographicVocabulary", "OpenStreetMap"),
    )
