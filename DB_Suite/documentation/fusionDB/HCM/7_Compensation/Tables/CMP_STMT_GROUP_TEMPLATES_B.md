# CMP_STMT_GROUP_TEMPLATES_B

Table stores statement group templates record.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstmtgrouptemplatesb-4406.html#cmpstmtgrouptemplatesb-4406](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstmtgrouptemplatesb-4406.html#cmpstmtgrouptemplatesb-4406)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_STMT_GROUP_TEMPLATES_B_PK | STMT_GROUP_TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_GROUP_TEMPLATE_ID | NUMBER |  | 18 | Yes | STMT_GROUP_TEMPLATE_ID |
| STMT_WORKER_ACK_TIMING | VARCHAR2 | 1 |  |  | STMT_WORKER_ACK_TIMING |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| STMT_GROUP_ID | NUMBER |  | 18 | Yes | STMT_GROUP_ID |
| STMT_TEMPLATE_ID | NUMBER |  | 18 | Yes | STMT_TEMPLATE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| STMT_WORKER_ACK_ACTION | VARCHAR2 | 30 |  |  | STMT_WORKER_ACK_ACTION |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_STMT_GRP_TEMPLATES_B_UK1 | Unique | Default | STMT_GROUP_TEMPLATE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
