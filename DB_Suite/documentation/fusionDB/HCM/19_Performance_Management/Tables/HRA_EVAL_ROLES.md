# HRA_EVAL_ROLES

This table stores the evaluation roles

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalroles-16902.html#hraevalroles-16902](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalroles-16902.html#hraevalroles-16902)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_ROLES_PK | EVAL_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVAL_ROLE_ID | NUMBER |  | 18 | Yes | Primary key of  roles |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| EVALUATION_ID | NUMBER |  | 18 |  | Primary key of Evaluation. |
| TMPL_ROLE_ID | NUMBER |  | 18 |  | Foreign key to HRA_TMPL_ROLES |
| ROLE_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates the code to identify the type of role (MANAGER, WORKER or PARTICIPANT) |
| MINIMUM_NUM_PCPNS | NUMBER |  | 18 |  | Stores minimum number of participants required per role. Will be copied from setup when document is created. |
| MAXIMUM_NUM_PCPNS | NUMBER |  | 18 |  | Stores maximum number of participants required per role |
| MATRIX_PARTICIPANT_FLAG | VARCHAR2 | 30 |  |  | Indicates that role is matrix participant role. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_ROLES_N1 | Non Unique | Default | EVALUATION_ID, ROLE_TYPE_CODE |
| HRA_EVAL_ROLES_PK | Unique | Default | EVAL_ROLE_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
