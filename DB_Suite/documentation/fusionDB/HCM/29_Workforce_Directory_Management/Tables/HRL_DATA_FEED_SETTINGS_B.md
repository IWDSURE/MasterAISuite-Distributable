# HRL_DATA_FEED_SETTINGS_B

This table stores the Spotlight data feed settings.

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedsettingsb-18182.html#hrldatafeedsettingsb-18182](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedsettingsb-18182.html#hrldatafeedsettingsb-18182)

## Primary Key

| Name | Columns |
|------|----------|
| HRL_DATA_FEED_SETTINGS_B_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a data feed setting. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| FLOW_CODE | VARCHAR2 | 30 |  |  | Flow code of the data feed setting. |
| SECTION_CODE | VARCHAR2 | 30 |  |  | Section code of the data feed setting. |
| CATEGORY_CODE | VARCHAR2 | 30 |  |  | Category code of the data feed setting. |
| SOURCE_CODE | VARCHAR2 | 30 |  |  | Source code of the data feed setting. |
| DATA_SOURCE_TYPE | VARCHAR2 | 400 |  |  | Data soure type of the data feed setting. |
| DATA_SOURCE_VALUE | VARCHAR2 | 4000 |  |  | Data source value of the data feed setting. |
| DATA_PRIV_NAME | VARCHAR2 | 400 |  |  | Data privilege name of the data feed setting. |
| DATA_PRIV_OBJ | VARCHAR2 | 400 |  |  | Data privilege object name of the data feed setting. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Active flag of the data feed setting. |
| VISIBILITY_CODE | VARCHAR2 | 200 |  |  | Visibility code of the data feed setting. |
| DISPLAY_SEQUENCE | NUMBER |  | 5 |  | Display sequence of the data feed setting. |
| IMAGE_NAME | VARCHAR2 | 400 |  |  | Image name of the data feed setting. |
| COLOR_CODE | VARCHAR2 | 30 |  |  | Color code of the data feed setting. |
| LINK_TYPE | VARCHAR2 | 30 |  |  | Link type of the data feed setting. |
| LINK_TEXT | VARCHAR2 | 2000 |  |  | Link text of the data feed setting. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRL_DATA_FEED_SETTINGS_B_PK | Unique | FUSION_TS_TX_IDX | SETTING_ID, ORA_SEED_SET1 |
| HRL_DATA_FEED_SETTINGS_B_PK1 | Unique | FUSION_TS_TX_IDX | SETTING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../29_Workforce_Directory_Management_Tables_Index.md)
