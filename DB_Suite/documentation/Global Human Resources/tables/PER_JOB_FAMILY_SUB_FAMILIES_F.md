# PER_JOB_FAMILY_SUB_FAMILIES_F

PER_JOB_FAMILY_SUB_FAMILIES_F holds the association between Job Families and their Sub Job Families.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobfamilysubfamiliesf-26739.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobfamilysubfamiliesf-26739.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_FAMILY_SB_FAMILIES_PK | SUB_FAMILY_ASSOCIATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUB_FAMILY_ASSOCIATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Indicates if a Sub Job Family is active or inactive. |
| JOB_FAMILY_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_JOB_FAMILY_F table. |
| JOB_SUB_FAMILY | VARCHAR2 | 30 |  | Yes | Sub Job Family that the Job is grouped in. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_JOB_FAMILY_SB_FAMILIES_N1 | Non Unique | PER_JOB_FAMILY_SB_FAMILIES_N1 | JOB_FAMILY_ID |
| PER_JOB_FAMILY_SB_FAMILIES_N2 | Non Unique | PER_JOB_FAMILY_SB_FAMILIES_N2 | JOB_SUB_FAMILY |
| PER_JOB_FAMILY_SB_FAMILIES_PK | Unique | PER_JOB_FAMILY_SB_FAMILIES_PK | SUB_FAMILY_ASSOCIATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_JOB_FAMILY_SB_FAMILIES_UK1 | Unique | PER_JOB_FAMILY_SB_FAMILIES_UK1 | BUSINESS_GROUP_ID, EFFECTIVE_START_DATE, JOB_FAMILY_ID, JOB_SUB_FAMILY |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
