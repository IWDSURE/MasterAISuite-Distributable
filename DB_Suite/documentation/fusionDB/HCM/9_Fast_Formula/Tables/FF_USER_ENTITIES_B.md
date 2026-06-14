# FF_USER_ENTITIES_B

This table contains table and selection criteria combinations used to define database items.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffuserentitiesb-22118.html#ffuserentitiesb-22118](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffuserentitiesb-22118.html#ffuserentitiesb-22118)

## Primary Key

| Name | Columns |
|------|----------|
| FF_USER_ENTITIES_PK | USER_ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ENTITY_ID | NUMBER |  | 18 | Yes | Unique identifier for the user entity. |
| ROUTE_ID | NUMBER |  | 18 | Yes | Identifier for route. Foreign key to FF_ROUTES. |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | An indication of what created the user entity. |
| CREATOR_ID | NUMBER |  | 18 |  | Foreign key to table identified by creator type |
| BASE_USER_ENTITY_NAME | VARCHAR2 | 240 |  | Yes | Unique name for user entity. |
| NOTFOUND_ALLOWED_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether no rows found is acceptable for the sql for the user entity. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_USER_ENTITIES_B_N1 | Non Unique | Default | CREATOR_TYPE, CREATOR_ID |
| FF_USER_ENTITIES_B_N2 | Non Unique | Default | UPPER("BASE_USER_ENTITY_NAME") |
| FF_USER_ENTITIES_B_N3 | Non Unique | Default | BASE_USER_ENTITY_NAME |
| FF_USER_ENTITIES_B_PK | Unique | Default | USER_ENTITY_ID, ORA_SEED_SET1 |
| FF_USER_ENTITIES_B_PK1 | Unique | Default | USER_ENTITY_ID, ORA_SEED_SET2 |
| FF_USER_ENTITIES_FK1 | Non Unique | Default | ROUTE_ID |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
