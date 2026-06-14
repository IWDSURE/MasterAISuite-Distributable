# HHR_VLTR_ABS_TYPE

This table is created to store the volunteering absence types

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrabstype-4486.html#hhrvltrabstype-4486](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrabstype-4486.html#hhrvltrabstype-4486)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_ABS_TYPE_PK | ABSENCE_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | ABSENCE_TYPE_ID |
| STATUS | VARCHAR2 | 10 |  | Yes | STATUS |
| TIME_OVERRIDEN | NUMBER |  | 1 | Yes | TIME_OVERRIDEN |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_ABS_TYPE_U1 | Unique | FUSION_TS_TX_DATA | ABSENCE_TYPE_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
