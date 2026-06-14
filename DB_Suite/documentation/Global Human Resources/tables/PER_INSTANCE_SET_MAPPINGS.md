# PER_INSTANCE_SET_MAPPINGS

PER_INSTANCE_SET_MAPPINGS table to store mappings to FND Grants instance sets

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinstancesetmappings-28036.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinstancesetmappings-28036.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INSTANCE_SET_MAPPINGS_PK | INSTANCE_SET_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTANCE_SET_MAPPING_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SECURITY_PROFILE_TYPE | VARCHAR2 | 30 |  | Yes | SECURITY_PROFILE_TYPE |
| SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | SECURITY_PROFILE_ID |
| INSTANCE_SET_ID | NUMBER |  | 18 | Yes | INSTANCE_SET_ID |
| FUNCTION_ID | NUMBER |  | 18 |  | FUNCTION_ID |
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
|-------|------------|------------|----------|
| PER_INSTANCE_SET_MAPPINGS_N1 | Non Unique | Default | SECURITY_PROFILE_ID |
| PER_INSTANCE_SET_MAPPINGS_PK | Unique | Default | INSTANCE_SET_MAPPING_ID, ORA_SEED_SET1 |
| PER_INSTANCE_SET_MAPPINGS_PK1 | Unique | Default | INSTANCE_SET_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
