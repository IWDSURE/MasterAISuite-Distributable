# HRC_EVT_SOURCE_OBJECTS

A Source Object contains the details of object from which events can be raised and includes Entity Objects, Business Processes, HR Actions and PLSQL Row Handlers

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtsourceobjects-28111.html#hrcevtsourceobjects-28111](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtsourceobjects-28111.html#hrcevtsourceobjects-28111)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_SOURCE_OBJECTS_PK | SOURCE_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Unique identifier | Active |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the source object | Active |
| SOURCE_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of source object (e.g. EO, Business Process, HR Action, PLSQL Row Handler, CBP) | Active |
| DATE_EFFECTIVE | VARCHAR2 | 30 |  | Yes | Indication of whether the EO or Row Handler are based on a Date Effective Table | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| TRANSACTION_BASED | VARCHAR2 | 30 |  | Yes | Indication of whether the business process is based upon the HCM Transaction model | Active |
| VERIFICATION_DATE | TIMESTAMP |  |  |  | Date that the Source Object or any of its child entities was modified - used to ensure that the event cache is re-initialized correctly |  |
| TABLE_NAME | VARCHAR2 | 30 |  |  | Name of table that the entity object is based on |  |
| DISPLAY_NAME | VARCHAR2 | 30 |  |  | Display Name of the EO based source object |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_EVT_SOURCE_OBJECTS_F1 | Non Unique | FUSION_TS_TX_IDX | ENTERPRISE_ID | Active |
| HRC_EVT_SOURCE_OBJECTS_N20 | Non Unique | Default | SGUID |  |
| HRC_EVT_SOURCE_OBJECTS_PK | Unique | FUSION_TS_TX_IDX | SOURCE_OBJECT_ID, ORA_SEED_SET1 | Active |
| HRC_EVT_SOURCE_OBJECTS_PK1 | Unique | FUSION_TS_TX_IDX | SOURCE_OBJECT_ID, ORA_SEED_SET2 |  |
| HRC_EVT_SOURCE_OBJECTS_U1 | Unique | FUSION_TS_TX_IDX | NAME, ENTERPRISE_ID, ORA_SEED_SET1 | Active |
| HRC_EVT_SOURCE_OBJECTS_U11 | Unique | FUSION_TS_TX_IDX | NAME, ENTERPRISE_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
