# HRC_ALERT_FILTERS

Contains resource alert filter data.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertfilters-10354.html#hrcalertfilters-10354](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertfilters-10354.html#hrcalertfilters-10354)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_FILTERS_PK | FILTER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILTER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| OBJECT_GUID | VARCHAR2 | 32 |  | Yes | Specifies the object GUID. Primarily used for seed data framework. |
| ALERT_ID | NUMBER |  | 18 | Yes | Alert Identifier. Foreign Key to HRC_ALERT_FILTERS.ALERT_ID |
| RESOURCE_PATH | VARCHAR2 | 400 |  | Yes | Filter Resource Path Name. Example- workers/workRelationships/assignments |
| CONJUNCTION | VARCHAR2 | 30 |  | Yes | Filter conjunction. Valid Values - ORA_AND and ORA_OR |
| CREATED_FROM | VARCHAR2 | 64 |  | Yes | indicates the source from where the filter row created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| DELETED_FLAG | VARCHAR2 | 30 |  | Yes | Used to identify for soft delete on Seeded Rows. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_FILTERS_N1 | Non Unique | Default | ALERT_ID |
| HRC_ALERT_FILTERS_N20 | Non Unique | Default | SGUID |
| HRC_ALERT_FILTERS_PK | Unique | Default | FILTER_ID, ORA_SEED_SET1 |
| HRC_ALERT_FILTERS_PK1 | Unique | Default | FILTER_ID, ORA_SEED_SET2 |
| HRC_ALERT_FILTERS_U1 | Unique | Default | OBJECT_GUID, ORA_SEED_SET1 |
| HRC_ALERT_FILTERS_U11 | Unique | Default | OBJECT_GUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
