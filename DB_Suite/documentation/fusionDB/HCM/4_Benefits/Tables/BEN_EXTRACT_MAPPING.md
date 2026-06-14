# BEN_EXTRACT_MAPPING

This table holds the mapping values corresponding to the existing lookup values for extract purposes

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractmapping-23695.html#benextractmapping-23695](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractmapping-23695.html#benextractmapping-23695)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_EXTRACT_MAPPING_PK | MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MAPPING_ID | NUMBER |  | 18 | Yes | MAPPING_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LAYOUT_ID | NUMBER |  | 18 |  | LAYOUT_ID |
| ELEMENT_ID | NUMBER |  | 18 |  | ELEMENT_ID |
| LOOKUP_TYPE | VARCHAR2 | 60 |  |  | LOOKUP_TYPE |
| LOOKUP_CODE | VARCHAR2 | 60 |  |  | LOOKUP_CODE |
| LOOKUP_CODE_MAPPING | VARCHAR2 | 60 |  |  | LOOKUP_CODE_MAPPING |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| BEN_EXTRACT_MAPPING_U1 | Unique | Default | MAPPING_ID, ORA_SEED_SET1 |
| BEN_EXTRACT_MAPPING_U11 | Unique | Default | MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
