# WLF_CLASS_ASSIGNMENT_RECORDS_F

An student booking (delegate booking) records an enrollment onto a scheduled, program or one time event.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfclassassignmentrecordsf-27457.html#wlfclassassignmentrecordsf-27457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfclassassignmentrecordsf-27457.html#wlfclassassignmentrecordsf-27457)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CLASS_ASSIGN_RECS_F_PK | CLASS_ASSIGNMENT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASS_ASSIGNMENT_RECORD_ID | NUMBER |  | 18 | Yes | CLASS_ENROLLMENT_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 |  | ASSIGNMENT_RECORD_ID |
| ATTENDANCE_RESULT | VARCHAR2 | 256 |  |  | ATTENDANCE_RESULT |
| FAILURE_REASON | VARCHAR2 | 30 |  |  | FAILURE_REASON |
| SUCCESSFUL_ATTENDANCE_FLAG | VARCHAR2 | 30 |  |  | SUCCESSFUL_ATTENDANCE_FLAG |
| SIGN_EVAL_STATUS | VARCHAR2 | 2 |  |  | SIGN_EVAL_STATUS |
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
| WLF_CLASS_ASSIGN_RECS_F_N1 | Non Unique | Default | ASSIGNMENT_RECORD_ID |
| WLF_CLASS_ASSIGN_RECS_F_U1 | Unique | Default | CLASS_ASSIGNMENT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
