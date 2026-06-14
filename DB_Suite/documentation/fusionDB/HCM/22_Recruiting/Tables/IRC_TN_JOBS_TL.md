# IRC_TN_JOBS_TL

Translation Table for storing flattened strings per Job

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobstl-3684.html#irctnjobstl-3684](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobstl-3684.html#irctnjobstl-3684)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOBS_TL_PK | TN_JOB_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| TITLE | VARCHAR2 | 240 |  |  | Stores the Title for this Requisition. This is the title that is published to external/internal candidates. |
| EXTERNAL_DESC | CLOB |  |  |  | Stores the html-free version of the External Description for this Requisition. |
| EXTERNAL_DESC_HTML | CLOB |  |  |  | Stores the html version of the External Description for this Requisition. |
| EXTERNAL_SHORT_DESC | CLOB |  |  |  | Stores the External Short Description for this Requisition. |
| EXTERNAL_RESP | CLOB |  |  |  | Stores the html-free version of the External Responsibilities for this Requisition. |
| EXTERNAL_RESP_HTML | CLOB |  |  |  | Stores the html version of the External Responsibilities for this Requisition. |
| EXTERNAL_QUAL | CLOB |  |  |  | Stores the html-free version of the External Qualifications for this Requisition |
| EXTERNAL_QUAL_HTML | CLOB |  |  |  | Stores the html version of the External Qualifications for this Requisition. |
| EXT_EMPLOYER_DESC | CLOB |  |  |  | Stores the  external employer description of the Requisition from IRC_DESCRIPTIONS_B.EXT_EMPLOYER_DESC_ID/IRC_DESCRIPTIONS_B/IRC_DESCRIPTIONS_TL Tables |
| EXT_ORGANIZATION_DESC | CLOB |  |  |  | Stores the external organization description of the Requisition from IRC_DESCRIPTIONS_B.EXT_ORGANIZATION_DESC_ID /IRC_DESCRIPTIONS_B/IRC_DESCRIPTIONS_TL Tables. |
| FULL_PART_TIME_MEANING | VARCHAR2 | 240 |  |  | Stores the full time part time meaning for the Requisition.Derived from  IRC_REQUISITIONS_B.FULL_PART_TIME and HCM_LOOKUPS(FULL_PART_TIME) |
| SALARY_FREQUENCY_MEANING | VARCHAR2 | 240 |  |  | Stores the salary frequency meaning . Derived from  IRC_REQUISITIONS_B.SALARY_FREQUENCY_CODE and HCM_LOOKUPS(CMP_SALARY_BASIS) |
| SALARY_CURRENCY_MEANING | VARCHAR2 | 240 |  |  | Stores the salary currency information. Derived from  IRC_REQUISITIONS_B.SALARY_CURRENCY_CODE and FND_CURRENCIES |
| ORGANIZATION_NAME | VARCHAR2 | 240 |  |  | Used to store the organization name of the requistion. |
| JOB_FAMILY_NAME | VARCHAR2 | 240 |  |  | Stores the name of the Job Family.Derived from  IRC_REQUISITIONS_B.JOB_FAMILY_ID, PER_JOB_FAMILY_F/PER_JOB_FAMILY_F_TL.JOB_FAMILY_NAME |
| JOB_FUNCTION_MEANING | VARCHAR2 | 240 |  |  | Stores the Job Function Meaning . Derived from  IRC_REQUISITIONS_B.JOB_FUNCTION_CODE and HCM_LOOKUPS(JOB_FUNCTION_CODE) |
| REGULAR_TEMPORARY_MEANING | VARCHAR2 | 240 |  |  | Stores whether the opening is for a regular or temporary job . Derived from  IRC_REQUISITIONS_B.REGULAR_TEMPORARY and HCM_LOOKUPS(REGULAR_TEMPORARY) |
| WORKPLACE_TYPE_MEANING | VARCHAR2 | 240 |  |  | Stores the Workplace type value of the Requisition . Derived from  IRC_REQUISITIONS_B.WORKPLACE_TYPE_CODE and HCM_LOOKUPS(ORA_IRC_WORKPLACE_TYPE) |
| TRAVEL_FREQUENCY_MEANING | VARCHAR2 | 240 |  |  | Stores the travel frequency value of the Requisition .Derived from   IRC_REQUISITIONS_B.PROFILE_ID and HRT_WORK_PREFERENCE_ITEMS_V.NAT_TRAVEL_FREQUENCY |
| WORK_HOURS_MEANING | VARCHAR2 | 240 |  |  | Stores the Work Hours of the  Requisition .Derived from   IRC_REQUISITIONS_B.PROFILE_ID , HRT_WORK_PREFERENCE_ITEMS_V.WORK_HOURS and HCM_LOOKUPS (HRT_WORK_HOURS) |
| WORK_DAYS_MEANING | VARCHAR2 | 240 |  |  | Stores the Work Hours of the  Requisition .Derived from   IRC_REQUISITIONS_B.PROFILE_ID , HRT_WORK_PREFERENCE_ITEMS_V.WORK_DAYS and HCM_LOOKUPS (HRT_WORK_DAYS) |
| STANDARD_WORKING_FREQ_MEANING | VARCHAR2 | 240 |  |  | Stores the Working Frequency of the Requisition  .Derived from   IRC_REQUISITIONS_B.POSITION_ID , HR_ALL_POSITIONS_F.STANDARD_WORKING_HOURS and HCM_LOOKUPS (FREQUENCY) |
| OVERTIME_STATUS_MEANING | VARCHAR2 | 240 |  |  | Stores the Overtime status of the Requisition  .Derived from   IRC_REQUISITIONS_B.PROFILE_ID , PER_JOB_LEG_F.INFORMATION1 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOBS_TL_PK | Unique | Default | TN_JOB_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
