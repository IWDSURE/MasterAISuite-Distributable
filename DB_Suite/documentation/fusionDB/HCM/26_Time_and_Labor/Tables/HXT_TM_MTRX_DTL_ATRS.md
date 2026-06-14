# HXT_TM_MTRX_DTL_ATRS

This table is designed to store the reverse orientation of data stored in HXT_TM_MTRX_DLY_ATRS to allow configuration on the two types of details dialog layout.  The extra copy of data exists for performance reasons.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxdtlatrs-28232.html#hxttmmtrxdtlatrs-28232](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxdtlatrs-28232.html#hxttmmtrxdtlatrs-28232)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_MTRX_DTL_ATRS_PK | TM_MTRX_DTL_ATR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_MTRX_DTL_ATR_ID | NUMBER |  | 18 | Yes | HXT_TM_MTRX_DTL_ATRS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_MTRX_ROW_ID | NUMBER |  | 18 |  | HXT_TM_MTRX_ROW_ID |
| DAY1 | VARCHAR2 | 32 |  |  | DAY1 |
| DAY1_VALUE | VARCHAR2 | 32 |  |  | DAY1_VALUE |
| DAY2 | VARCHAR2 | 32 |  |  | DAY2 |
| DAY2_VALUE | VARCHAR2 | 32 |  |  | DAY2_VALUE |
| DAY3 | VARCHAR2 | 32 |  |  | DAY3 |
| DAY3_VALUE | VARCHAR2 | 32 |  |  | DAY3_VALUE |
| DAY4 | VARCHAR2 | 32 |  |  | DAY4 |
| DAY4_VALUE | VARCHAR2 | 32 |  |  | DAY4_VALUE |
| DAY5 | VARCHAR2 | 32 |  |  | DAY5 |
| DAY5_VALUE | VARCHAR2 | 32 |  |  | DAY5_VALUE |
| DAY6 | VARCHAR2 | 32 |  |  | DAY6 |
| DAY6_VALUE | VARCHAR2 | 32 |  |  | DAY6_VALUE |
| DAY7 | VARCHAR2 | 32 |  |  | DAY7 |
| DAY7_VALUE | VARCHAR2 | 32 |  |  | DAY7_VALUE |
| DAY8 | VARCHAR2 | 32 |  |  | DAY8 |
| DAY9 | VARCHAR2 | 32 |  |  | DAY9 |
| DAY10 | VARCHAR2 | 32 |  |  | DAY10 |
| DAY11 | VARCHAR2 | 32 |  |  | DAY11 |
| DAY12 | VARCHAR2 | 32 |  |  | DAY12 |
| DAY13 | VARCHAR2 | 32 |  |  | DAY13 |
| DAY14 | VARCHAR2 | 32 |  |  | DAY14 |
| DAY15 | VARCHAR2 | 32 |  |  | DAY15 |
| DAY16 | VARCHAR2 | 32 |  |  | DAY16 |
| DAY17 | VARCHAR2 | 32 |  |  | DAY17 |
| DAY18 | VARCHAR2 | 32 |  |  | DAY18 |
| DAY19 | VARCHAR2 | 32 |  |  | DAY19 |
| DAY20 | VARCHAR2 | 32 |  |  | DAY20 |
| DAY21 | VARCHAR2 | 32 |  |  | DAY21 |
| DAY22 | VARCHAR2 | 32 |  |  | DAY22 |
| DAY23 | VARCHAR2 | 32 |  |  | DAY23 |
| DAY24 | VARCHAR2 | 32 |  |  | DAY24 |
| DAY25 | VARCHAR2 | 32 |  |  | DAY25 |
| DAY26 | VARCHAR2 | 32 |  |  | DAY26 |
| DAY27 | VARCHAR2 | 32 |  |  | DAY27 |
| DAY28 | VARCHAR2 | 32 |  |  | DAY28 |
| DAY29 | VARCHAR2 | 32 |  |  | DAY29 |
| DAY30 | VARCHAR2 | 32 |  |  | DAY30 |
| DAY31 | VARCHAR2 | 32 |  |  | DAY31 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_MTRX_DTL_ATRS_U1 | Unique | Default | TM_MTRX_DTL_ATR_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
