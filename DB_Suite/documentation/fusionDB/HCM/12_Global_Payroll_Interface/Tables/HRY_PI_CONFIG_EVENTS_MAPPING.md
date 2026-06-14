# HRY_PI_CONFIG_EVENTS_MAPPING

For Storing Configuration Events mapping Data

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiconfigeventsmapping-9643.html#hrypiconfigeventsmapping-9643](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiconfigeventsmapping-9643.html#hrypiconfigeventsmapping-9643)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_CONFIG_EVENTS_MAP_PK | CONFIG_EVENTS_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_EVENTS_MAPPING_ID | NUMBER |  | 18 | Yes | Primary Key for Configuration Events Mapping |
| CONFIGURATION_NAME | VARCHAR2 | 80 |  |  | Configuration Name for Payroll Interface |
| BUSINESS_EVENT_NAME | VARCHAR2 | 80 |  |  | Payroll Interface Business Event Name |
| SETUP_PAYLOAD_ID | NUMBER |  | 18 |  | Foreign key to HRY_PI_SETUP_PAYLOADS_B. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES_B. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | Unique row identification for seed data framework |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_CONFIG_EVENTS_MAP_N20 | Non Unique | Default | SGUID |
| HRY_PI_CONFIG_EVENTS_MAP_PK | Unique | Default | CONFIG_EVENTS_MAPPING_ID, ORA_SEED_SET1 |
| HRY_PI_CONFIG_EVENTS_MAP_PK1 | Unique | Default | CONFIG_EVENTS_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
