# PER_ASSIGNMENT_STATUS_TYPES_TL

This table holds the translated USER_STATUS definitions of statuses for a specific assignment or Set of Employment/Placement Terms. This table is kept as-is.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentstatustypestl-30640.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentstatustypestl-30640.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASG_STATUS_TYPES_TL_PK | ASSIGNMENT_STATUS_TYPE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ASSIGNMENT_STATUS_TYPES. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| USER_STATUS | VARCHAR2 | 80 |  | Yes | Translated user defined status name. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| EXTERNAL_STATUS | VARCHAR2 | 240 |  |  | User defined status for the applicant to see. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASG_STATUS_TYPES_TL_N2 | Non Unique | Default | LANGUAGE, USER_STATUS |
| PER_ASG_STATUS_TYPES_TL_PK | Unique | Default | ASSIGNMENT_STATUS_TYPE_ID, LANGUAGE, ORA_SEED_SET1 |
| PER_ASG_STATUS_TYPES_TL_PK1 | Unique | Default | ASSIGNMENT_STATUS_TYPE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
