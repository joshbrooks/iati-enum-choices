from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationType(models.IntegerChoices):
    GOVERNMENT = (
        10,
        pgettext_lazy("IATI codelist OrganisationType", "Government"),
    )
    LOCAL_GOVERNMENT = (
        11,
        pgettext_lazy("IATI codelist OrganisationType", "Local Government"),
    )
    OTHER_PUBLIC_SECTOR = (
        15,
        pgettext_lazy("IATI codelist OrganisationType", "Other Public Sector"),
    )
    INTERNATIONAL_NGO = (
        21,
        pgettext_lazy("IATI codelist OrganisationType", "International NGO"),
    )
    NATIONAL_NGO = (
        22,
        pgettext_lazy("IATI codelist OrganisationType", "National NGO"),
    )
    REGIONAL_NGO = (
        23,
        pgettext_lazy("IATI codelist OrganisationType", "Regional NGO"),
    )
    PARTNER_COUNTRY_BASED_NGO = (
        24,
        pgettext_lazy("IATI codelist OrganisationType", "Partner Country based NGO"),
    )
    PUBLIC_PRIVATE_PARTNERSHIP = (
        30,
        pgettext_lazy("IATI codelist OrganisationType", "Public Private Partnership"),
    )
    MULTILATERAL = (
        40,
        pgettext_lazy("IATI codelist OrganisationType", "Multilateral"),
    )
    FOUNDATION = (
        60,
        pgettext_lazy("IATI codelist OrganisationType", "Foundation"),
    )
    PRIVATE_SECTOR = (
        70,
        pgettext_lazy("IATI codelist OrganisationType", "Private Sector"),
    )
    PRIVATE_SECTOR_IN_PROVIDER_COUNTRY = (
        71,
        pgettext_lazy(
            "IATI codelist OrganisationType", "Private Sector in Provider Country"
        ),
    )
    PRIVATE_SECTOR_IN_AID_RECIPIENT_COUNTRY = (
        72,
        pgettext_lazy(
            "IATI codelist OrganisationType", "Private Sector in Aid Recipient Country"
        ),
    )
    PRIVATE_SECTOR_IN_THIRD_COUNTRY = (
        73,
        pgettext_lazy(
            "IATI codelist OrganisationType", "Private Sector in Third Country"
        ),
    )
    ACADEMIC__TRAINING_AND_RESEARCH = (
        80,
        pgettext_lazy(
            "IATI codelist OrganisationType", "Academic, Training and Research"
        ),
    )
    OTHER = (
        90,
        pgettext_lazy("IATI codelist OrganisationType", "Other"),
    )
