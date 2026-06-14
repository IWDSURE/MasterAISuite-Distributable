# FF_DBI_GROUPS

This table contains database item groups, which are collections of database items for a particular attribute.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffdbigroups-6860.html#ffdbigroups-6860](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffdbigroups-6860.html#ffdbigroups-6860)

## Primary Key

| Name | Columns |
|------|----------|
| FF_DBI_GROUPS_PK | DBI_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DBI_GROUP_ID | NUMBER |  | 18 | Yes | Unique identifiier for database item group. |
| BASE_GROUP_NAME | VARCHAR2 | 255 |  | Yes | Unique name for the database item group. |
| CONTEXT_ID | NUMBER |  | 18 |  | Foreign key to FF_CONTEXTS. |
| DEFAULT_XML_TAG | VARCHAR2 | 30 |  |  | This is the default Tag that will be used in XML when this DBI Group is used in a report. |
| ATTRIBUTE_TYPE | VARCHAR2 | 20 |  |  | ATTRIBUTE_TYPE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_DBI_GROUPS_N1 | Non Unique | Default | UPPER("BASE_GROUP_NAME") |
| FF_DBI_GROUPS_N2 | Non Unique | Default | BASE_GROUP_NAME |
| FF_DBI_GROUPS_PK | Unique | Default | DBI_GROUP_ID, ORA_SEED_SET1 |
| FF_DBI_GROUPS_PK1 | Unique | Default | DBI_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
