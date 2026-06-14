# PER_ALLOC_TASK_COMMENTS

PER_ALLOC_TASK_COMMENTS : Allocated Task Comments

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peralloctaskcomments-19357.html#peralloctaskcomments-19357](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peralloctaskcomments-19357.html#peralloctaskcomments-19357)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOC_TASK_COMMENTS_PK | ALLOC_TASK_COMMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOC_TASK_COMMENT_ID | NUMBER |  | 18 | Yes | ALLOC_TASK_COMMENT_ID |
| ALLOCATED_TASK_ID | NUMBER |  | 18 | Yes | ALLOCATED_TASK_ID |
| COMMENT_USER_GUID | VARCHAR2 | 64 |  | Yes | COMMENT_USER_GUID |
| COMMENT_TYPE | VARCHAR2 | 30 |  | Yes | COMMENT_TYPE |
| COMMENT_TEXT | VARCHAR2 | 1000 |  | Yes | COMMENT_TEXT |
| COMMENT_DATE | DATE |  |  | Yes | COMMENT_DATE |
| COMMENT_STATUS | VARCHAR2 | 30 |  | Yes | COMMENT_STATUS |
| COMMENT_CONTEXT | VARCHAR2 | 1000 |  |  | COMMENT_CONTEXT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MESSAGE_NAME | VARCHAR2 | 30 |  |  | MESSAGE_NAME |
| RUN_ID | NUMBER |  | 18 |  | RUN_ID |
| COMMENT_DETAILS_1 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS_1 |
| COMMENT_DETAILS_2 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS_2 |
| COMMENT_DETAILS_3 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS_3 |
| COMMENT_DETAILS_4 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS_4 |
| COMMENT_DETAILS_5 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS_5 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALLOC_TASK_COMMENTS_N1 | Non Unique | FUSION_TS_TX_DATA | ALLOCATED_TASK_ID |
| PER_ALLOC_TASK_COMMENTS_PK | Unique | FUSION_TS_TX_DATA | ALLOC_TASK_COMMENT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
