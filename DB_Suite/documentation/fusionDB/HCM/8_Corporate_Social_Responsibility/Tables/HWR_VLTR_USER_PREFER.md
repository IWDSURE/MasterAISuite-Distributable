# HWR_VLTR_USER_PREFER

this table stores user prefernce

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltruserprefer-19285.html#hwrvltruserprefer-19285](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltruserprefer-19285.html#hwrvltruserprefer-19285)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_USER_PREFER_PK | AG_USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AG_USER_ID | NUMBER |  | 18 | Yes | AG_USER_ID |
| LOCALE_LANGUAGE | VARCHAR2 | 63 |  |  | LOCALE_LANGUAGE |
| LOCALE_COUNTRY | VARCHAR2 | 63 |  |  | LOCALE_COUNTRY |
| LOCALE_COUNTRY_1 | VARCHAR2 | 63 |  |  | LOCALE_COUNTRY_1 |
| DATE_FORMAT | VARCHAR2 | 100 |  |  | DATE_FORMAT |
| TERRITORY | VARCHAR2 | 100 |  |  | TERRITORY |
| NUMBER_FORMAT | VARCHAR2 | 40 |  |  | NUMBER_FORMAT |
| TIME_FORMAT | VARCHAR2 | 40 |  |  | TIME_FORMAT |
| TIME_ZONE | VARCHAR2 | 40 |  |  | TIME_ZONE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_USER_PREFER_U1 | Unique | FUSION_TS_TX_IDX | AG_USER_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
