# HRL_DATA_FEED_SETTINGS_TL

This is the translation table for HRL_DATA_FEED_SETTINGS_B

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedsettingstl-23286.html#hrldatafeedsettingstl-23286](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedsettingstl-23286.html#hrldatafeedsettingstl-23286)

## Primary Key

| Name | Columns |
|------|----------|
| HRL_DATA_FEED_SETTINGS_TL_PK | SETTING_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Foreign key to HRL_DATA_FEED_SETTINGS_B. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SOURCE_NAME | VARCHAR2 | 200 |  | Yes | Source name of the data feed setting. |
| SOURCE_DESCRIPTION | VARCHAR2 | 4000 |  |  | Source description of the data feed setting. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRL_DATA_FEED_SETTINGS_TL_PK | Unique | FUSION_TS_TX_DATA | SETTING_ID, LANGUAGE, ORA_SEED_SET1 |
| HRL_DATA_FEED_SETTINGS_TL_U1 | Unique | FUSION_TS_TX_DATA | SETTING_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../29_Workforce_Directory_Management_Tables_Index.md)
