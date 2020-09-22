from django.db import models
from django.utils.translation import pgettext_lazy


class AidTypeDescription(models.TextChoices):
    GENERAL_BUDGET_SUPPORT = (
        "A01",
        pgettext_lazy(
            "AidType description",
            "Unearmarked contributions to the government budget including funding to support the implementation of macroeconomic reforms (structural adjustment programmes, poverty reduction strategies). Budget support is a method of financing a recipient country’s budget through a transfer of resources from an external financing agency to the recipient government’s national treasury. The funds thus transferred are managed in accordance with the recipient’s budgetary procedures. Funds transferred to the national treasury for financing programmes or projects managed according to different budgetary procedures from those of the recipient country, with the intention of earmarking the resources for specific uses, are therefore excluded.",
        ),
    )
    SECTOR_BUDGET_SUPPORT = (
        "A02",
        pgettext_lazy(
            "AidType description",
            "Sector budget support, like general budget support, is a financial contribution to a recipient government’s budget.  However, in sector budget support, the dialogue between donors and partner governments focuses on sector-specific concerns, rather than on overall policy and budget priorities.",
        ),
    )
    CORE_SUPPORT_TO_NGOS__OTHER_PRIVATE_BODIES__PPPS_AND_RESEARCH_INSTITUTES = (
        "B01",
        pgettext_lazy(
            "AidType description",
            "Funds are paid over to NGOs (local, national and international) for use at the latter’s discretion, and contribute to programmes and activities which NGOs have developed themselves, and which they implement on their own authority and responsibility. Core contributions to PPPs, funds paid over to foundations (e.g. philanthropic foundations), and contributions to research institutes (public and private) are also recorded here. Annex 2 of the DAC Directives provides a list of INGOs, PPPs and networks core contributions to which may be reported under B01. This list is not exclusive.",
        ),
    )
    CORE_CONTRIBUTIONS_TO_MULTILATERAL_INSTITUTIONS = (
        "B02",
        pgettext_lazy(
            "AidType description",
            "These funds are classified as multilateral ODA (all other categories fall under bilateral ODA). The recipient multilateral institution pools contributions so that they lose their identity and become an integral part of its financial assets. See Annex 2 of the DAC Directives for a comprehensive list of agencies core contributions to which may be reported under B02 (Section I. Multilateral institutions).",
        ),
    )
    CONTRIBUTIONS_TO_SPECIFIC_PURPOSE_PROGRAMMES_AND_FUNDS_MANAGED_BY_IMPLEMENTING_PARTNERS = (
        "B03",
        pgettext_lazy(
            "AidType description",
            "In addition to their core-funded operations, international organisations, NGOs, PPPs and networks, both in provider and in third countries, set up programmes and funds with a specific sectoral, thematic or geographical focus. Donors’ bilateral contributions to such programmes and funds are recorded here.",
        ),
    )
    BASKET_FUNDS_POOLED_FUNDING = (
        "B04",
        pgettext_lazy(
            "AidType description",
            "The donor contributes funds to an autonomous account, managed jointly with other donors and/or the recipient. The account will have specific purposes, modes of disbursement and accountability mechanisms, and a limited time frame. Basket funds are characterised by common project documents, common funding contracts and common reporting/audit procedures with all donors. Donors’ contributions to funds managed autonomously by international organisations are recorded under B03.",
        ),
    )
    PROJECT_TYPE_INTERVENTIONS = (
        "C01",
        pgettext_lazy(
            "AidType description",
            "A project is a set of inputs, activities and outputs, agreed with the partner country*, to reach specific objectives/outcomes within a defined time frame, with a defined budget and a  defined geographical area. Projects can vary significantly in terms of objectives, complexity, amounts involved and duration. There are smaller projects that might involve modest financial resources and last only a few months, whereas large projects might involve more significant amounts, entail successive phases and last for many years. A large project with a number of different components is sometimes referred to as a programme, but should nevertheless be recorded here. Feasibility studies, appraisals and evaluations are included (whether designed as part of projects/programmes or dedicated funding arrangements). Academic studies, research and development, trainings, scholarships, and other technical assistance activities not directly linked to development projects/programmes should instead be recorded under D02. Aid channelled through NGOs or multilaterals is also recorded here. This includes payments for NGOs and multilaterals to implement donors’ projects and programmes, and funding of specified NGOs projects. By contrast, core funding of NGOs and multilaterals as well as contributions to specific-purpose funds are recorded under B.* In the cases of equity investments, humanitarian aid or aid channelled through NGOs, projects are recorded here even if there was no direct agreement between the donor and the partner country.",
        ),
    )
    DONOR_COUNTRY_PERSONNEL = (
        "D01",
        pgettext_lazy(
            "AidType description",
            "Experts, consultants, teachers, academics, researchers, volunteers and contributions to public and private bodies for sending experts to developing countries.",
        ),
    )
    OTHER_TECHNICAL_ASSISTANCE = (
        "D02",
        pgettext_lazy(
            "AidType description",
            "Provision, outside projects as described in category C01, of technical assistance in recipient countries (excluding technical assistance performed by donor experts reported under D01, and scholarships/training in donor country reported under E01). This includes training and research; language training; south-south studies; research studies; collaborative research between donor and recipient universities and organisations); local scholarships; development-oriented social and cultural programmes. This category also covers ad hoc contributions such as conferences, seminars and workshops, exchange visits, publications, etc.",
        ),
    )
    SCHOLARSHIPS_TRAINING_IN_DONOR_COUNTRY = (
        "E01",
        pgettext_lazy(
            "AidType description",
            "Financial aid awards for individual students and contributions to trainees.",
        ),
    )
    IMPUTED_STUDENT_COSTS = (
        "E02",
        pgettext_lazy(
            "AidType description",
            "Indirect (“imputed”) costs of tuition in donor countries.",
        ),
    )
    DEBT_RELIEF = (
        "F01",
        pgettext_lazy(
            "AidType description",
            "Groups all actions relating to debt (forgiveness, conversions, swaps, buy-backs, rescheduling, refinancing).",
        ),
    )
    ADMINISTRATIVE_COSTS_NOT_INCLUDED_ELSEWHERE = (
        "G01",
        pgettext_lazy(
            "AidType description",
            "Administrative costs of development assistance programmes not already included under other ODA items as an integral part of the costs of delivering or implementing the aid provided. This category covers situation analyses and auditing activities.As regards the salaries component of administrative costs, it relates to  in-house agency staff and contractors only; costs associated with donor experts/consultants are to be reported under category C or D01.",
        ),
    )
    DEVELOPMENT_AWARENESS = (
        "H01",
        pgettext_lazy(
            "AidType description",
            "Funding of activities designed to increase public support, i.e. awareness in the donor country of development co-operation efforts, needs and issues.",
        ),
    )
    REFUGEES_ASYLUM_SEEKERS_IN_DONOR_COUNTRIES = (
        "H02",
        pgettext_lazy(
            "AidType description",
            "Costs incurred in donor countries for basic assistance to asylum seekers and refugees from developing countries, up to 12 months, when costs cannot be disaggregated. See section II.6 and Annex 17.",
        ),
    )
    ASYLUM_SEEKERS_ULTIMATELY_ACCEPTED = (
        "H03",
        pgettext_lazy(
            "AidType description",
            "Costs incurred in donor countries for basic assistance to asylum seekers, when these are ultimately accepted. This category includes only costs incurred prior to recognition.",
        ),
    )
    ASYLUM_SEEKERS_ULTIMATELY_REJECTED = (
        "H04",
        pgettext_lazy(
            "AidType description",
            "Costs incurred in donor countries for basic assistance to asylum seekers, when these are ultimately rejected. This category includes only costs incurred prior to rejection. Members may base their reporting on the first instance rejection, where a final decision on status is anticipated to occur after a 12-month period, and this facilitates the establishment of a conservative estimate. For further guidance on how to proceed with calculating costs related to rejected asylum seekers, see Clarification 5, third bullet in section II.6 of the Reporting Directives.",
        ),
    )
    RECOGNISED_REFUGEES = (
        "H05",
        pgettext_lazy(
            "AidType description",
            "Costs incurred in donor countries for basic assistance to refugees with a recognised status. This category only includes costs after recognition (or after date of entry into a country through a resettlement programme).",
        ),
    )
