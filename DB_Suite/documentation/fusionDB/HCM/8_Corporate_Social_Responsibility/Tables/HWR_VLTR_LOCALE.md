# HWR_VLTR_LOCALE

This table stores locale specific information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrlocale-15248.html#hwrvltrlocale-15248](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrlocale-15248.html#hwrvltrlocale-15248)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_LOCALE_PK | KEY |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| KEY | VARCHAR2 | 6 | Yes | KEY |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | LANGUAGE_CODE |
| COUNTRY_CODE | VARCHAR2 | 4 |  | COUNTRY_CODE |
| DESCRIPTION | VARCHAR2 | 255 | Yes | DESCRIPTION |
| OEBS_LANGUAGE_CODE | VARCHAR2 | 6 | Yes | OEBS_LANGUAGE_CODE |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_LOCALE_U1 | Unique | FUSION_TS_TX_IDX | KEY |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
