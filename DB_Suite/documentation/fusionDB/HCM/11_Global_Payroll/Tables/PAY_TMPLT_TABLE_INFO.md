# PAY_TMPLT_TABLE_INFO

This holds the definition of an entity within the Template Solution. E.g. A Person entity or an object can be registered within this entity and as a result it can be used by any templates.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmplttableinfo-5509.html#paytmplttableinfo-5509](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmplttableinfo-5509.html#paytmplttableinfo-5509)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_TABLE_INFO_PK | TABLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TABLE_ID | NUMBER |  | 18 | Yes | TABLE_ID |
| BASE_TABLE_NAME | VARCHAR2 | 30 |  | Yes | BASE_TABLE_NAME |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TABLE_NAME | VARCHAR2 | 30 |  | Yes | TABLE_NAME |
| TABLE_VO | VARCHAR2 | 200 |  |  | TABLE_VO |
| TABLE_DESCRIPTION | VARCHAR2 | 200 |  |  | TABLE_DESCRIPTION |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| EVENT_OBJECT_NAME | VARCHAR2 | 240 |  |  | EVENT_OBJECT_NAME |
| EVENT_GROUP_FLAG | VARCHAR2 | 20 |  |  | EVENT_GROUP_FLAG |
| EVENT_DEFAULT_SQL | VARCHAR2 | 4000 |  |  | EVENT_DEFAULT_SQL |
| INST_NAME_REST_VO | VARCHAR2 | 512 |  |  | INST_NAME_REST_VO |
| INST_DESCR_REST_VO | VARCHAR2 | 512 |  |  | INST_DESCR_REST_VO |
| NAV_TYPE | VARCHAR2 | 30 |  |  | NAV_TYPE |
| NAV_URL | VARCHAR2 | 512 |  |  | NAV_URL |
| SECURING_RESOURCE_TYPE | VARCHAR2 | 30 |  |  | SECURING_RESOURCE_TYPE |
| SECURING_RESOURCE | VARCHAR2 | 512 |  |  | SECURING_RESOURCE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
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
| PAY_TMPLT_TABLE_INFO_PK | Unique | Default | TABLE_ID, ORA_SEED_SET1 |
| PAY_TMPLT_TABLE_INFO_PK1 | Unique | Default | TABLE_ID, ORA_SEED_SET2 |
| PAY_TMPLT_TABLE_INFO_U1 | Unique | Default | BASE_TABLE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_TMPLT_TABLE_INFO_U11 | Unique | Default | BASE_TABLE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
