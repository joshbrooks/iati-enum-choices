from django.db import models
from django.utils.translation import pgettext_lazy


class OrganisationTypeDescription(models.IntegerChoices):
    LOCAL_GOVERNMENT = (
        11,
        pgettext_lazy(
            "IATI codelist OrganisationType description",
            "Any local (sub national) government organisation in either donor or recipient country.",
        ),
    )
    PARTNER_COUNTRY_BASED_NGO = (
        24,
        pgettext_lazy(
            "IATI codelist OrganisationType description",
            "Local and National NGO / CSO based in aid/assistance recipient country",
        ),
    )
    PRIVATE_SECTOR_IN_PROVIDER_COUNTRY = (
        71,
        pgettext_lazy(
            "IATI codelist OrganisationType description",
            "Is in provider / donor country.",
        ),
    )
    PRIVATE_SECTOR_IN_AID_RECIPIENT_COUNTRY = (
        72,
        pgettext_lazy(
            "IATI codelist OrganisationType description", "Is in aid recipient country."
        ),
    )
    PRIVATE_SECTOR_IN_THIRD_COUNTRY = (
        73,
        pgettext_lazy(
            "IATI codelist OrganisationType description",
            "Is not in either a donor or aid recipient country.",
        ),
    )
