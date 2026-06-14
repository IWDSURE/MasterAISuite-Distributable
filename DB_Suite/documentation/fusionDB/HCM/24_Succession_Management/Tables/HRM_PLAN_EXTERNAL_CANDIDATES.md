# HRM_PLAN_EXTERNAL_CANDIDATES

Succession External Candidates created from Succession Plans.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanexternalcandidates-5114.html#hrmplanexternalcandidates-5114](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanexternalcandidates-5114.html#hrmplanexternalcandidates-5114)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_PLAN_EXTERNAL_CANDIDA_PK | EXTERNAL_CANDIDATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| EXTERNAL_CANDIDATE_ID | NUMBER |  | 18 | Yes | External candidate id is primary key for the table. |
| FIRST_NAME | VARCHAR2 | 150 |  |  | The first name of the candidate. |
| LAST_NAME | VARCHAR2 | 150 |  | Yes | The last name of the candidate. |
| DISPLAY_NAME | VARCHAR2 | 300 |  |  | The display name of the candidate. This is derived from first_name last_name. |
| CURRENT_EMPLOYER_NAME | VARCHAR2 | 64 |  |  | Current company name of the candidate. |
| CURRENT_JOB_TITLE | VARCHAR2 | 64 |  |  | Current job title of the candidate. |
| ADDRESS_LINE1 | VARCHAR2 | 240 |  |  | Address line 1 represents the first line for address description. |
| ADDRESS_LINE2 | VARCHAR2 | 240 |  |  | The second line of the address. |
| COUNTRY | VARCHAR2 | 60 |  |  | Country where this address belongs. |
| STATE | VARCHAR2 | 120 |  |  | State represents the name of the state for address. |
| TOWN_OR_CITY | VARCHAR2 | 30 |  |  | Town or city represents the name of city for address. |
| POSTAL_CODE | VARCHAR2 | 30 |  |  | National code to identify addresses in a specific country. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Email address represents the E-mail address of the candidate. |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | Phone number represents the telephone number of the candidate. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_PLAN_EXTERNAL_CANDIDA_PK | Unique | Default | EXTERNAL_CANDIDATE_ID |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
