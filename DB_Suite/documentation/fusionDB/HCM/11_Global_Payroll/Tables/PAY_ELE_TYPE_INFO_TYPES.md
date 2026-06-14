# PAY_ELE_TYPE_INFO_TYPES

This table contains additional flexfield structures to provide extra configuration for an element.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeletypeinfotypes-29328.html#payeletypeinfotypes-29328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeletypeinfotypes-29328.html#payeletypeinfotypes-29328)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_TYPE_INFO_TYPES_PK | INFORMATION_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INFORMATION_TYPE | VARCHAR2 | 40 |  | Yes | INFORMATION_TYPE |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | ACTIVE_INACTIVE_FLAG |
| MULTIPLE_OCCURENCES_FLAG | VARCHAR2 | 30 |  | Yes | MULTIPLE_OCCURENCES_FLAG |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | PROGRAM_UPDATE_DATE |
| PROGRAM_ID | NUMBER |  | 18 |  | PROGRAM_ID |
| PROGRAM_APPLICATION_ID | NUMBER |  | 18 |  | PROGRAM_APPLICATION_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ELE_TYPE_INFO_TYPES_PK | Unique | Default | INFORMATION_TYPE, ORA_SEED_SET1 |
| PAY_ELE_TYPE_INFO_TYPES_PK1 | Unique | Default | INFORMATION_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
