from django.db import models
from django.utils.translation import pgettext_lazy


class Version(models.TextChoices):
    """
    Version of the IATI Standard
    """

    VERSION_1_01 = ("1.01",)
    VERSION_1_02 = ("1.02",)
    VERSION_1_03 = ("1.03",)
    VERSION_1_04 = ("1.04",)
    VERSION_1_05 = ("1.05",)
    VERSION_2_01 = ("2.01",)
    VERSION_2_02 = ("2.02",)
    VERSION_2_03 = ("2.03",)
