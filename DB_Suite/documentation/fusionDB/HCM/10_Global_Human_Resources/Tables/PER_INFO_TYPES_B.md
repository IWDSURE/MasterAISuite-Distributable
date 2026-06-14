# PER_INFO_TYPES_B

This table stores the generic Info Types setup data.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinfotypesb-18197.html#perinfotypesb-18197](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinfotypesb-18197.html#perinfotypesb-18197)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INFO_TYPES_B_PK | CATEGORY, INFORMATION_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CATEGORY | VARCHAR2 | 240 |  | Yes | Discriminator column for the Extra Information Type. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| INFORMATION_TYPE | VARCHAR2 | 40 |  | Yes | Information type, maps to flexfield context. | Active |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | Flag showing if information_type is active or inactive | Active |
| MULTIPLE_OCCURRENCES_FLAG | VARCHAR2 | 30 |  | Yes | Flag showing whether multi-row entry is allowed for this info type. | Active |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_INFO_TYPES_B_PK | Unique | Default | CATEGORY, INFORMATION_TYPE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
