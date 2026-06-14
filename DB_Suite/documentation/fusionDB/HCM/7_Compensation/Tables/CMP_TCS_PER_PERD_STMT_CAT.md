# CMP_TCS_PER_PERD_STMT_CAT

Table holds Cmp Tcs Per Perd Stmt Cat records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdstmtcat-22542.html#cmptcsperperdstmtcat-22542](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdstmtcat-22542.html#cmptcsperperdstmtcat-22542)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_PER_PERD_STMT_CAT_PK | PER_PERD_STMT_CAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PERD_STMT_CAT_ID | NUMBER |  | 18 | Yes | PER_PERD_STMT_CAT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PER_PERD_STMT_ID | NUMBER |  | 18 | Yes | PER_PERD_STMT_ID |
| CAT_ID | NUMBER |  | 18 | Yes | CAT_ID |
| ORDR_NUM | NUMBER |  | 18 |  | ORDR_NUM |
| ZERO_VALUE_OPTIONS | VARCHAR2 | 30 |  |  | ZERO_VALUE_OPTIONS |
| HISTORY_DATA_FLAG | VARCHAR2 | 1 |  |  | HISTORY_DATA_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_STMT_CAT_UK1 | Unique | Default | PER_PERD_STMT_CAT_ID |
| CMP_TCS_PER_STMT_CAT_UK2 | Unique | Default | PER_PERD_STMT_ID, CAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
