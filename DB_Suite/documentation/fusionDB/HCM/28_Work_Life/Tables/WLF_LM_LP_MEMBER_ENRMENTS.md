# WLF_LM_LP_MEMBER_ENRMENTS

This table stores the learning path member enrollment objects

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmlpmemberenrments-25342.html#wlflmlpmemberenrments-25342](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmlpmemberenrments-25342.html#wlflmlpmemberenrments-25342)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_LP_MEMBER_ENRMENTS_PK | LP_MEMBER_ENROLLMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LP_MEMBER_ENROLLMENT_ID | NUMBER |  | 18 | Yes | LP_MEMBER_ENROLLMENT_ID |
| LP_ENROLLMENT_ID | NUMBER |  | 18 | Yes | LP_ENROLLMENT_ID |
| LEARNING_PATH_SECTION_ID | NUMBER |  | 18 | Yes | LEARNING_PATH_SECTION_ID |
| LEARNING_PATH_MEMBER_ID | NUMBER |  | 18 | Yes | LEARNING_PATH_MEMBER_ID |
| MEMBER_STATUS_CODE | VARCHAR2 | 30 |  | Yes | MEMBER_STATUS_CODE |
| COMPLETION_TARGET_DATE | DATE |  |  |  | COMPLETION_TARGET_DATE |
| COMPLETION_DATE | DATE |  |  |  | COMPLETION_DATE |
| CREATOR_PERSON_ID | NUMBER |  | 18 | Yes | CREATOR_PERSON_ID |
| CLASS_ID | NUMBER |  | 18 | Yes | CLASS_ID |
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
| WLF_LM_LP_MEMBER_ENRMENTS_PK1 | Unique | Default | LP_MEMBER_ENROLLMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
