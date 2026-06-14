# PER_PERSON_TYPES

Setup table defining the relationship between system person types and user variations of those.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersontypes-5917.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersontypes-5917.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERSON_TYPES_PK | PERSON_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_TYPE_ID | NUMBER |  | 18 | Yes | Unique key generated from sequence PER_PERSON_TYPES_S. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether the type is active[Y/N]. |
| DEFAULT_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether this USER_PERSON_TYPE is the default for the current SYSTEM_PERSON_TYPE [Y/N]. |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  | Yes | System name for the person type |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SEEDED_PERSON_TYPE_KEY | VARCHAR2 | 30 |  |  | Reserved for internal purpose |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERSON_TYPES_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_PERSON_TYPES_FK2 | Non Unique | Default | SEEDED_PERSON_TYPE_KEY |
| PER_PERSON_TYPES_N1 | Non Unique | Default | SYSTEM_PERSON_TYPE, BUSINESS_GROUP_ID |
| PER_PERSON_TYPES_N20 | Non Unique | Default | SGUID |
| PER_PERSON_TYPES_PK | Unique | Default | PERSON_TYPE_ID, ORA_SEED_SET1 |
| PER_PERSON_TYPES_PK1 | Unique | Default | PERSON_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
