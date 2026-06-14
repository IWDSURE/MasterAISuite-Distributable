# HWR_VLTR_ADDRESS_TL

The translation table for the address table

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltraddresstl-14067.html#hwrvltraddresstl-14067](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltraddresstl-14067.html#hwrvltraddresstl-14067)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_ADDRESS_TL_PK | ADDRESS_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADDRESS_ID | NUMBER |  | 18 | Yes | ADDRESS_ID |
| ADDRESS_LINE_1 | VARCHAR2 | 100 |  |  | ADDRESS_LINE_1 |
| ADDRESS_LINE_2 | VARCHAR2 | 100 |  |  | ADDRESS_LINE_2 |
| CITY | VARCHAR2 | 100 |  |  | CITY |
| STATE | VARCHAR2 | 100 |  |  | STATE |
| COUNTRY | VARCHAR2 | 100 |  |  | COUNTRY |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_ADDRESS_TL_U2 | Unique | FUSION_TS_TX_IDX | ADDRESS_ID, LANGUAGE |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
