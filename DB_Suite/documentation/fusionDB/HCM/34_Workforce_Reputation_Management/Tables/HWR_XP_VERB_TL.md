# HWR_XP_VERB_TL

This is the table for the experience store verbs translation.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpverbtl-9227.html#hwrxpverbtl-9227](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpverbtl-9227.html#hwrxpverbtl-9227)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_VERB_TL_PK | VERB_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VERB_ID | NUMBER |  | 18 | Yes | This is the column verb_id on table HWR_XP_VERB_TL. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| NAME | VARCHAR2 | 255 |  |  | The human readable representation of the Verb. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_VERB_TL_U1 | Unique | Default | VERB_ID, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
