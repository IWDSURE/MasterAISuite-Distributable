# HWR_WLNS_QSTN_TL

The translation table for wellness question table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstntl-25330.html#hwrwlnsqstntl-25330](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstntl-25330.html#hwrwlnsqstntl-25330)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_QSTN_TL_PK | QUESTION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the primary key from the question table. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| QUESTION_TEXT | VARCHAR2 | 4000 |  | Yes | This is the text of the question being asked. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_WLNS_QSTN_TL_U1 | Unique | FUSION_TS_TX_DATA | QUESTION_ID, LANGUAGE | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
