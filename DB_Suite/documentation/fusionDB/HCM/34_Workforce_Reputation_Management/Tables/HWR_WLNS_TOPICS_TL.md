# HWR_WLNS_TOPICS_TL

The translation table for wellness topics table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstopicstl-30515.html#hwrwlnstopicstl-30515](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstopicstl-30515.html#hwrwlnstopicstl-30515)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_TOPICS_TL_PK | TOPIC_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the primary key for the wellness topics tables. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| TOPIC_NAME | VARCHAR2 | 400 |  | Yes | This is the name of the wellness topics displayed on UI. | Active |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | This is the description of the topic name. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_WLNS_TOPICS_TL_U1 | Unique | FUSION_TS_TX_DATA | TOPIC_ID, LANGUAGE, ORA_SEED_SET1 | Active |
| HWR_WLNS_TOPICS_TL_U11 | Unique | FUSION_TS_TX_DATA | TOPIC_ID, LANGUAGE, ORA_SEED_SET2 |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
