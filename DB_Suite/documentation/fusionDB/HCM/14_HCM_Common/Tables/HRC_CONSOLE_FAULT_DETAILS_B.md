# HRC_CONSOLE_FAULT_DETAILS_B

Fault DetailsTable: This Table holds the fault details

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcconsolefaultdetailsb-25516.html#hrcconsolefaultdetailsb-25516](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcconsolefaultdetailsb-25516.html#hrcconsolefaultdetailsb-25516)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_CONSOLE_FAULT_DETAILS_PK | FAULT_DETAILS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FAULT_DETAILS_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ISSUE_TYPE_CODE | VARCHAR2 | 30 |  |  | Seeded Issue Type code matching corresponding column in ApplCore's FND_CONSOLE_ISSUE table |
| FAULT_CODE | VARCHAR2 | 100 |  |  | Seeded fault code matching corresponding column in ApplCore's FND_CONSOLE_ISSUE table |
| ERROR_CODE | VARCHAR2 | 100 |  |  | Seeded Error code matching corresponding column in ApplCore's FND_CONSOLE_ISSUE table |
| INTERNAL_CODE | VARCHAR2 | 100 |  |  | This column stores internal code and will be used in queries to fetch a row with fine tuned issue description and resolution |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning |
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
| HRC_CONSOLE_FAULT_DETAILS_N20 | Non Unique | Default | SGUID |
| HRC_CONSOLE_FAULT_DETS_B_PK | Unique | Default | FAULT_DETAILS_ID, ORA_SEED_SET1 |
| HRC_CONSOLE_FAULT_DETS_B_PK1 | Unique | Default | FAULT_DETAILS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
