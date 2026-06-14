# WLF_LM_LP_ENROLLMENTS

This table is used to store learning path enrollments objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmlpenrollments-12112.html#wlflmlpenrollments-12112](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmlpenrollments-12112.html#wlflmlpenrollments-12112)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_LP_ENROLLMENTS_PK | LP_ENROLLMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LP_ENROLLMENT_ID | NUMBER |  | 18 | Yes | LP_ENROLLMENT_ID |
| LEARNING_PATH_ID | NUMBER |  | 18 | Yes | LEARNING_PATH_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| CONTACT_ID | NUMBER |  | 18 |  | CONTACT_ID |
| PATH_STATUS_CODE | VARCHAR2 | 30 |  | Yes | PATH_STATUS_CODE |
| ENROLLMENT_SOURCE_CODE | VARCHAR2 | 30 |  | Yes | ENROLLMENT_SOURCE_CODE |
| NO_OF_MANDATORY_COURSES | NUMBER |  | 10 |  | NO_OF_MANDATORY_COURSES |
| NO_OF_COMPLETED_COURSES | NUMBER |  | 10 |  | NO_OF_COMPLETED_COURSES |
| COMPLETION_TARGET_DATE | DATE |  |  |  | COMPLETION_TARGET_DATE |
| COMPLETION_DATE | DATE |  |  |  | COMPLETION_DATE |
| CREATOR_PERSON_ID | NUMBER |  | 18 |  | CREATOR_PERSON_ID |
| IS_HISTORY_FLAG | VARCHAR2 | 30 |  |  | IS_HISTORY_FLAG |
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
| WLF_LM_LP_ENROLLMENTS_N1 | Non Unique | Default | CONTACT_ID |
| WLF_LM_LP_ENROLLMENTS_PK | Unique | Default | LP_ENROLLMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
