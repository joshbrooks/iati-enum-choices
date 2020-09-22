from django.db import models
from django.utils.translation import pgettext_lazy


class GeographicVocabularyDescription(models.TextChoices):
    UN_SECOND_ADMINISTRATIVE_LEVEL_BOUNDARY_PROJECT = (
        "A2",
        pgettext_lazy(
            "GeographicVocabulary description",
            "Note: the unsalb.org website is no longer accessible, and public access to the boundaries resources has been removed http://www.ungiwg.org/content/united-nations-international-and-administrative-boundaries-resources",
        ),
    )
    OPENSTREETMAP = (
        "G2",
        pgettext_lazy(
            "GeographicVocabulary description",
            "Note: the code should be formed by prefixing the relevant OpenStreetMap ID with node/ way/ or relation/ as appropriate, e.g. node/1234567",
        ),
    )
