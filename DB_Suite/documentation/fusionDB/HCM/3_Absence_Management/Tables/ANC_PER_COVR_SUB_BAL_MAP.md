# ANC_PER_COVR_SUB_BAL_MAP

Table to capture mapping values from carryover table and accrual entry dts

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpercovrsubbalmap-11975.html#ancpercovrsubbalmap-11975](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpercovrsubbalmap-11975.html#ancpercovrsubbalmap-11975)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_COVR_SUB_BAL_MAP_PK | ANC_PER_COVR_SUB_BAL_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANC_PER_COVR_SUB_BAL_MAP_ID | NUMBER |  | 18 | Yes | Primary key |
| PER_ACRL_ENTRY_DTL_ID | NUMBER |  | 18 | Yes | Ref of the transaction in accrual entry details table |
| ANC_PER_COVR_SUB_BAL_ID | NUMBER |  | 18 | Yes | Ref to the carryover sub balance bucket that is consumed from. |
| VALUE | NUMBER |  |  | Yes | Value consumed by the transaction |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_COVR_SUB_BAL_MAP_N1 | Non Unique | Default | ANC_PER_COVR_SUB_BAL_ID |
| ANC_PER_COVR_SUB_BAL_MAP_N2 | Non Unique | Default | PER_ACRL_ENTRY_DTL_ID |
| ANC_PER_COVR_SUB_BAL_MAP_U1 | Unique | Default | ANC_PER_COVR_SUB_BAL_MAP_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
