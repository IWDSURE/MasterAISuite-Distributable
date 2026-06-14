# HWR_CAT_TOPIC_TL

The translation table for the topic table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcattopictl-30177.html#hwrcattopictl-30177](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcattopictl-30177.html#hwrcattopictl-30177)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CAT_TOPIC_TL_PK | TOPIC_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | This is a primary key from the hwr_topc_b table |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| DISPLAY_TEXT | VARCHAR2 | 400 |  | Yes | The topic value to be displayed. Stored mixed-case and including internal spaces, just as the user entered it. | Active |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | A description that allows space for more details than the display text. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CAT_TOPIC_TL_N1 | Non Unique | FUSION_TS_SEED | DISPLAY_TEXT |
| HWR_CAT_TOPIC_TL_U1 | Unique | FUSION_TS_SEED | TOPIC_ID, LANGUAGE, ORA_SEED_SET1 |
| HWR_CAT_TOPIC_TL_U11 | Unique | FUSION_TS_SEED | TOPIC_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
