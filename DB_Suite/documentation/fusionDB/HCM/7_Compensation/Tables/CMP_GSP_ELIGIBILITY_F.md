# CMP_GSP_ELIGIBILITY_F

CMP_GSP_ELIGIBILITY_F holds details of CMP eligibility for salary progression.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgspeligibilityf-8361.html#cmpgspeligibilityf-8361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgspeligibilityf-8361.html#cmpgspeligibilityf-8361)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_PROGRESSION_ELI_PK | GSP_ELIGIBILITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GSP_ELIGIBILITY_ID | NUMBER |  | 18 | Yes | GSP_ELIGIBILITY_ID |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | GRADE_LADDER_ID |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| GRADE_STEP_ID | NUMBER |  | 18 |  | GRADE_STEP_ID |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 | Yes | ELIGIBILITY_PROFILE_ID |
| REQUIRED_FLAG | VARCHAR2 | 1 |  | Yes | REQUIRED_FLAG |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_GSP_ELIGIBILITY_F_U1 | Unique | Default | GSP_ELIGIBILITY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
