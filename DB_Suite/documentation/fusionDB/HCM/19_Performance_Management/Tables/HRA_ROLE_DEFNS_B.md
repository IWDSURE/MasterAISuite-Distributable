# HRA_ROLE_DEFNS_B

This table stores the configured participant roles that will be part of the evaluation process e.g. Manager, Employee, Peer etc

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraroledefnsb-30239.html#hraroledefnsb-30239](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraroledefnsb-30239.html#hraroledefnsb-30239)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_ROLE_DEFNS_B_PK | ROLE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_ID | NUMBER |  | 18 | Yes | Primary key of Role Definition. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| DATE_FROM | DATE |  |  | Yes | The date from which the role would be active |
| DATE_TO | DATE |  |  |  | The date untill which the role will be active |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Stores whether the role is active or inactive |
| ROLE_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates the type of role i.e manager or worker or participant etc. |
| MANAGER_TYPE | VARCHAR2 | 30 |  |  | Indicates the type of manager i.e line manager or product manager etc. |
| MATRIX_PARTICIPANT_FLAG | VARCHAR2 | 30 |  |  | Indicates that role is matrix participant role. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| HRA_ROLE_DEFNS_B_PK | Unique | Default | ROLE_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRA_ROLE_DEFNS_B_PK1 | Unique | Default | ROLE_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
