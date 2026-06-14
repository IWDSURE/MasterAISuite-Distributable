# HRR_DASHBOARD_TMPLS_B

Talent Review Dashboard templates

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrdashboardtmplsb-21746.html#hrrdashboardtmplsb-21746](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrdashboardtmplsb-21746.html#hrrdashboardtmplsb-21746)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_DASHBOARD_TMPLS_B_PK | DASHBOARD_TMPL_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| DASHBOARD_TMPL_ID | NUMBER |  | 18 | Yes | Primary Key of Dashboard Templates |  |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Identifier of the questionnaire that should be used in the potential assessment in the meeting. |  |  |
| FILTER_DEPARTMENT | VARCHAR2 | 30 |  |  | Indicates whether department can be displayed as filter option in the dashboard |  |  |
| USE_NOTES_FLAG | VARCHAR2 | 30 |  |  | Indicates whether dashboard users can create notes for the participants |  |  |
| DISPLAY_PUBLIC_PERSON | VARCHAR2 | 30 |  |  | Indicates whether public person can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_CAREER_PLANNING | VARCHAR2 | 30 |  |  | Indicates whether career planning can be displayed in the detail on demand region. |  | Obsolete |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |  |
| SET_ID | NUMBER |  | 18 | Yes | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |  |  |
| TMPL_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Dashboard Template Status |  |  |
| OWNER_ID | NUMBER |  | 18 |  | OWNER_ID |  |  |
| DISPLAY_RISK_OF_LOSS | VARCHAR2 | 30 |  |  | Indicates whether Risk of Loss analytic overlay can be displayed or not. |  |  |
| DISPLAY_IMPACT_OF_LOSS | VARCHAR2 | 30 |  |  | Indicates whether Impact of Loss analytic overlay can be displayed or not. |  |  |
| DISPLAY_MOBILITY | VARCHAR2 | 30 |  |  | Indicates whether mobility analytic overlay can be displayed or not. |  |  |
| DISPLAY_GENDER | VARCHAR2 | 30 |  |  | Indicates whether gender analytic overlay can be displayed or not. |  |  |
| DISPLAY_AGE | VARCHAR2 | 30 |  |  | Indicates whether age analytic overlay can be displayed or not. |  |  |
| DISPLAY_ETHNICITY | VARCHAR2 | 30 |  |  | Indicates whether ethnicity analytic overlay can be displayed or not. |  |  |
| DISPLAY_RELIGIOUS_AFFLTN | VARCHAR2 | 30 |  |  | Indicates whether religious effiliation analytic overlay can be displayed or not. |  |  |
| DISPLAY_COMMENTS | VARCHAR2 | 30 |  |  | Indicates whether comments can be displayed in the detail on demand region. |  |  |
| DISPLAY_COMP_PLAN_DTLS | VARCHAR2 | 30 |  |  | Indicates whether compensation plan details can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_GOAL_DEVPLAN_DTLS | VARCHAR2 | 30 |  |  | Indicates whether foals and devlopment plan details can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_KUDOS | VARCHAR2 | 30 |  |  | Indicates whether kudos can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_EMPLOYMENT | VARCHAR2 | 30 |  |  | Indicates whether employment can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_PERFORMANCE_DTLS | VARCHAR2 | 30 |  |  | Indicates whether performance details can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_PERSON_ROFILE_DTLS | VARCHAR2 | 30 |  |  | Indicates whether person profile details can be displayed in the detail on demand region. |  | Obsolete |
| DISPLAY_SUCCESSION_DTLS | VARCHAR2 | 30 |  |  | Indicates if the succession tab on the person detail popup should be shown or not |  | Obsolete |
| DISPLAY_ADDITIONAL_INFORMATION | VARCHAR2 | 30 |  |  | Indicates whether to display additional custom content type data or not |  | Obsolete |
| INCLUDE_SUCCESSION_PLANS | VARCHAR2 | 30 |  |  | Indicates whether succession plans can be assocoiated with meetings using this template. |  |  |
| INCLUDE_TALENT_POOLS | VARCHAR2 | 30 |  |  | Indicates whether talent pools can be assocoiated with meetings using this template. |  |  |
| INCLUDE_MATRIX_MGMT | VARCHAR2 | 20 |  |  | INCLUDE_MATRIX_MGMT |  |  |
| FILTER_JOBROLE_ASSGN | VARCHAR2 | 30 |  |  | Indicates whether Job role or assignment can be displayed as filter option in the dashboard |  |  |
| FILTER_REVWR_PARTCPNT | VARCHAR2 | 30 |  |  | Filter workers  for those who are either a reviewer or participant in a  talent review meeting. |  |  |
| FILTER_LOCATION | VARCHAR2 | 30 |  |  | Indicates whether location can be displayed as filter option in the dashboard |  |  |
| FILTER_ORG_HIERARCHY | VARCHAR2 | 30 |  |  | Indicates whether Organisation hierarchy can be displayed as filter option in the dashboard |  |  |
| FILTER_LEVEL | VARCHAR2 | 30 |  |  | Indicates whether Level can be displayed as a filter option in the dashboard |  |  |
| FILTER_JOBGRADE | VARCHAR2 | 30 |  |  | FILTER_JOBGRADE |  |  |
| FILTER_COMPETENCY | VARCHAR2 | 30 |  |  | Indicates whether Competency can be displayed as a filter option in the dashboard |  |  |
| FILTER_PROFICIENCY | VARCHAR2 | 30 |  |  | Indicates whether Proficiency can be displayed as a filter option in the dashboard |  |  |
| FILTER_BUSINESSUNIT | VARCHAR2 | 30 |  |  | Indicates whether business unit can be displayed as filter option in the dashboard |  |  |
| FILTER_SUCCESSION_PLAN | VARCHAR2 | 30 |  |  | Indicates whether succession plan can be displayed as a filter option in the dashboard. |  |  |
| FILTER_TALENT_POOL | VARCHAR2 | 30 |  |  | Indicates whether talent pool can be displayed as a filter option in the dashboard. |  |  |
| COLOR_JOBROLE_ASSGN | VARCHAR2 | 30 |  |  | Indicates whether Job role or assignment can be displayed as a color option in the dashboard |  |  |
| COLOR_LOCATION | VARCHAR2 | 30 |  |  | Indicates whether Location can be displayed as a color option in the dashboard |  |  |
| COLOR_ORG_HIERARCHY | VARCHAR2 | 30 |  |  | Indicates whether Organization Hierarchy can be displayed as a color option in the dashboard |  |  |
| USE_TASKS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether dashboard users can created tasks for the participants |  |  |
| USE_POT_ASSESS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether Potential Assessment will be used or not. |  |  |
| USE_COMPARE_FLAG | VARCHAR2 | 30 |  |  | Indicates whether dashboard users can use Compare action. |  |  |
| USE_ORGCHART_FLAG | VARCHAR2 | 30 |  |  | Indicates whether dashboard users can use Orgchart action. |  |  |
| CREATE_GOALS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether dashboard users can assign goals |  |  |
| USE_HOLDING_AREA_FLAG | VARCHAR2 | 30 |  |  | Indicates whether dashboard can have holding area. |  |  |
| MAX_MARKERS_ALLOWED | NUMBER |  | 7 | Yes | Maximum number of markers to display in the box chart. |  |  |
| POPULATION_SIZE_FOR_ESS | NUMBER |  | 7 |  | Meeting population size for ESS |  |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE1 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE2 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE3 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE4 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE5 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE6 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE7 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE8 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE9 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE10 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE11 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE12 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE13 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE14 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE15 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE16 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE17 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE18 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE19 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE20 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE21 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE22 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE23 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE24 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE25 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE26 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE27 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE28 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE29 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE30 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Dashboard Template (HRR_DASHBOARD_TMPLS_B) |  |
| FILTER_JOB_FUNCTION | VARCHAR2 | 30 |  |  | Indicates whether job function can be displayed as filter option in the dashboard |  |  |
| FILTER_JOB_FAMILY | VARCHAR2 | 30 |  |  | Indicates whether job family can be displayed as filter option in the dashboard |  |  |
| FILTER_MGMT_LEVEL | VARCHAR2 | 30 |  |  | Indicates whether management level can be displayed as filter option in the dashboard |  |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  | Obsolete |
| ROL_DSPLY_OPTN_PREF | VARCHAR2 | 30 |  |  | Display option preference on the dashboard for risk of loss |  |  |
| IOL_DSPLY_OPTN_PREF | VARCHAR2 | 30 |  |  | Display option preference on the dashboard for impact of loss |  |  |
| MOBILITY_DSPLY_OPTN_PREF | VARCHAR2 | 30 |  |  | Display option preference on the dashboard for mobility |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRR_DASHBOARD_TMPLS_B_N1 | Non Unique | FUSION_TS_TX_DATA | SET_ID | Obsolete |
| HRR_DASHBOARD_TMPLS_B_U1 | Unique | FUSION_TS_TX_DATA | SET_ID, BUSINESS_GROUP_ID, DASHBOARD_TMPL_ID |  |
| HRR_DASHBOARD_TMPLS_B_U2 | Unique | FUSION_TS_TX_DATA | DASHBOARD_TMPL_ID, BUSINESS_GROUP_ID |  |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
