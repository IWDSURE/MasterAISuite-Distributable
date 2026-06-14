# HWR_VLTR_NPROFIT_ORGFILE

This table stores non profit org file

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrnprofitorgfile-14087.html#hwrvltrnprofitorgfile-14087](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrnprofitorgfile-14087.html#hwrvltrnprofitorgfile-14087)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_NPROFIT_ORGFILE_PK | ORGFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORGFILE_ID | NUMBER |  | 18 | Yes | ORGFILE_ID |
| SOURCE | VARCHAR2 | 20 |  |  | SOURCE |
| ORGFILE | CLOB |  |  |  | ORGFILE |
| ORGFILE_NAME | VARCHAR2 | 100 |  |  | ORGFILE_NAME |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_NPROFIT_ORGFILE_U1 | Unique | FUSION_TS_TX_IDX | ORGFILE_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
