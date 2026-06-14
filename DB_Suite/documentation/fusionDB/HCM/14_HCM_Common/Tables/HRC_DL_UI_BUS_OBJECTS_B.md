# HRC_DL_UI_BUS_OBJECTS_B

HRC_DL_BUS_OBJECTS_B is seeded as a base Standard MLS table

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdluibusobjectsb-6309.html#hrcdluibusobjectsb-6309](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdluibusobjectsb-6309.html#hrcdluibusobjectsb-6309)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_UI_BUS_OBJECTS_B_PK | UI_BUSINESS_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UI_BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | UI_BUSINESS_OBJECT_ID |
| UI_BUSINESS_OBJECT_GUID | VARCHAR2 | 64 |  | Yes | UI_BUSINESS_OBJECT_GUID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_UI_BUS_OBJECTS_B_PK | Unique | Default | UI_BUSINESS_OBJECT_ID, ORA_SEED_SET1 |
| HRC_DL_UI_BUS_OBJECTS_B_PK1 | Unique | Default | UI_BUSINESS_OBJECT_ID, ORA_SEED_SET2 |
| HRC_DL_UI_BUS_OBJECTS_B_U1 | Unique | Default | UI_BUSINESS_OBJECT_GUID, ORA_SEED_SET1 |
| HRC_DL_UI_BUS_OBJECTS_B_U11 | Unique | Default | UI_BUSINESS_OBJECT_GUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
