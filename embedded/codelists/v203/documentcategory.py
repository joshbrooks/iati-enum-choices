from django.db import models
from django.utils.translation import pgettext_lazy


class DocumentCategory(models.TextChoices):
    PRE_AND_POST_PROJECT_IMPACT_APPRAISAL = (
        "A01",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Pre- and post-project impact appraisal"
        ),
    )
    OBJECTIVES___PURPOSE_OF_ACTIVITY = (
        "A02",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Objectives / Purpose of activity"
        ),
    )
    INTENDED_ULTIMATE_BENEFICIARIES = (
        "A03",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Intended ultimate beneficiaries"
        ),
    )
    CONDITIONS = (
        "A04",
        pgettext_lazy("IATI codelist DocumentCategory", "Conditions"),
    )
    BUDGET = (
        "A05",
        pgettext_lazy("IATI codelist DocumentCategory", "Budget"),
    )
    SUMMARY_INFORMATION_ABOUT_CONTRACT = (
        "A06",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Summary information about contract"
        ),
    )
    REVIEW_OF_PROJECT_PERFORMANCE_AND_EVALUATION = (
        "A07",
        pgettext_lazy(
            "IATI codelist DocumentCategory",
            "Review of project performance and evaluation",
        ),
    )
    RESULTS__OUTCOMES_AND_OUTPUTS = (
        "A08",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Results, outcomes and outputs"
        ),
    )
    MEMORANDUM_OF_UNDERSTANDING__IF_AGREED_BY_ALL_PARTIES_ = (
        "A09",
        pgettext_lazy(
            "IATI codelist DocumentCategory",
            "Memorandum of understanding (If agreed by all parties)",
        ),
    )
    TENDER = (
        "A10",
        pgettext_lazy("IATI codelist DocumentCategory", "Tender"),
    )
    CONTRACT = (
        "A11",
        pgettext_lazy("IATI codelist DocumentCategory", "Contract"),
    )
    ACTIVITY_WEB_PAGE = (
        "A12",
        pgettext_lazy("IATI codelist DocumentCategory", "Activity web page"),
    )
    ANNUAL_REPORT = (
        "B01",
        pgettext_lazy("IATI codelist DocumentCategory", "Annual report"),
    )
    INSTITUTIONAL_STRATEGY_PAPER = (
        "B02",
        pgettext_lazy("IATI codelist DocumentCategory", "Institutional Strategy paper"),
    )
    COUNTRY_STRATEGY_PAPER = (
        "B03",
        pgettext_lazy("IATI codelist DocumentCategory", "Country strategy paper"),
    )
    AID_ALLOCATION_POLICY = (
        "B04",
        pgettext_lazy("IATI codelist DocumentCategory", "Aid Allocation Policy"),
    )
    PROCUREMENT_POLICY_AND_PROCEDURE = (
        "B05",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Procurement Policy and Procedure"
        ),
    )
    INSTITUTIONAL_AUDIT_REPORT = (
        "B06",
        pgettext_lazy("IATI codelist DocumentCategory", "Institutional Audit Report"),
    )
    COUNTRY_AUDIT_REPORT = (
        "B07",
        pgettext_lazy("IATI codelist DocumentCategory", "Country Audit Report"),
    )
    EXCLUSIONS_POLICY = (
        "B08",
        pgettext_lazy("IATI codelist DocumentCategory", "Exclusions Policy"),
    )
    INSTITUTIONAL_EVALUATION_REPORT = (
        "B09",
        pgettext_lazy(
            "IATI codelist DocumentCategory", "Institutional Evaluation Report"
        ),
    )
    COUNTRY_EVALUATION_REPORT = (
        "B10",
        pgettext_lazy("IATI codelist DocumentCategory", "Country Evaluation Report"),
    )
    SECTOR_STRATEGY = (
        "B11",
        pgettext_lazy("IATI codelist DocumentCategory", "Sector strategy"),
    )
    THEMATIC_STRATEGY = (
        "B12",
        pgettext_lazy("IATI codelist DocumentCategory", "Thematic strategy"),
    )
    COUNTRY_LEVEL_MEMORANDUM_OF_UNDERSTANDING = (
        "B13",
        pgettext_lazy(
            "IATI codelist DocumentCategory",
            "Country-level Memorandum of Understanding",
        ),
    )
    EVALUATIONS_POLICY = (
        "B14",
        pgettext_lazy("IATI codelist DocumentCategory", "Evaluations policy"),
    )
    GENERAL_TERMS_AND_CONDITIONS = (
        "B15",
        pgettext_lazy("IATI codelist DocumentCategory", "General Terms and Conditions"),
    )
    ORGANISATION_WEB_PAGE = (
        "B16",
        pgettext_lazy("IATI codelist DocumentCategory", "Organisation web page"),
    )
    COUNTRY_REGION_WEB_PAGE = (
        "B17",
        pgettext_lazy("IATI codelist DocumentCategory", "Country/Region web page"),
    )
    SECTOR_WEB_PAGE = (
        "B18",
        pgettext_lazy("IATI codelist DocumentCategory", "Sector web page"),
    )
