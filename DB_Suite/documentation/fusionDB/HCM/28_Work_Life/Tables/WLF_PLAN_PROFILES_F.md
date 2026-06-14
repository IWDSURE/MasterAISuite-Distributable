# WLF_PLAN_PROFILES_F

Table to store  learning plan profiles.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfplanprofilesf-6501.html#wlfplanprofilesf-6501](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfplanprofilesf-6501.html#wlfplanprofilesf-6501)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PLAN_PROFILES_F_PK | PLAN_PROFILE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_PROFILE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_ID | NUMBER |  | 18 | Yes | EVENT_ID |
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | EVENT_ASSIGNMENT_ID |
| LEARNING_PLAN_ID | NUMBER |  | 18 | Yes | LEARNING_PLAN_ID |
| PLAN_PROFILE_TYPE | VARCHAR2 | 30 |  | Yes | Plan profile type {NEW,EXISTING} |
| INITIAL_PLAN_RECORD_STATUS | VARCHAR2 | 30 |  |  | Initial plan record status |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PLAN_PROFILES_F_N1 | Non Unique | Default | LEARNING_PLAN_ID |
| WLF_PLAN_PROFILES_F_U1 | Unique | Default | PLAN_PROFILE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| WLF_PLAN_PROFILES_F_N2 | Non Unique | Default | EVENT_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
