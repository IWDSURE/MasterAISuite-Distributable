# CMP_TCS_STMT_RATING_TL

Stores Translatable data from Total Compensation Setup's Feedback Rating

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtratingtl-25537.html#cmptcsstmtratingtl-25537](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtratingtl-25537.html#cmptcsstmtratingtl-25537)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_RATING_TL_PK | STMT_RATING_ID, LANGUAGE, PERD_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_RATING_ID | NUMBER |  | 18 | Yes | STMT_RATING_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| RATING | VARCHAR2 | 80 |  |  | RATING |
| DESCRIPTION | VARCHAR2 | 300 |  |  | DESCRIPTION |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_RATING_TL_FK2 | Non Unique | Default | PERD_RUN_ID |
| CMP_TCS_STMT_RATING_TL_U1 | Unique | Default | STMT_RATING_ID, LANGUAGE, PERD_RUN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
