# HWR_VLTR_GOAL_TL

The translation table for goal table

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoaltl-3618.html#hwrvltrgoaltl-3618](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoaltl-3618.html#hwrvltrgoaltl-3618)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_GOAL_TL_PK | GOAL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | GOAL_ID |
| GOAL_METRIC | VARCHAR2 | 50 |  | Yes | GOAL_METRIC |
| UNITS | VARCHAR2 | 50 |  |  | UNITS |
| FREQUENCY | VARCHAR2 | 50 |  |  | FREQUENCY |
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
| HWR_VLTR_GOAL_TL_U1 | Unique | FUSION_TS_TX_IDX | GOAL_ID, LANGUAGE |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
