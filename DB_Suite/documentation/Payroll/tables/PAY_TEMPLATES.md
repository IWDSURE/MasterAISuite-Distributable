# PAY_TEMPLATES

This Table Stores the Template Information Like its name etc

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemplates-14652.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemplates-14652.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TEMPLATES_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | TEMPLATE_ID |
| TEMPLATE_NAME | VARCHAR2 | 50 |  | Yes | TEMPLATE_NAME |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TEMPLATE_TYPE | VARCHAR2 | 30 |  | Yes | TEMPLATE_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| VERSION_NUMBER | NUMBER |  | 5 |  | VERSION_NUMBER |
| BASE_NAME | VARCHAR2 | 50 |  | Yes | BASE_NAME |
| BASE_PROCESSING_PRIORITY | NUMBER |  | 10 |  | BASE_PROCESSING_PRIORITY |
| MAX_BASE_NAME_LENGTH | NUMBER |  | 5 |  | MAX_BASE_NAME_LENGTH |
| VERSION | NUMBER |  | 5 |  | VERSION |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROGRESS | VARCHAR2 | 30 |  |  | PROGRESS |
| PROCESSING_STAGE | VARCHAR2 | 30 |  |  | PROCESSING_STAGE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| TEMPLATE_SEQUENCE_NUMBER | VARCHAR2 | 30 |  |  | TEMPLATE_SEQUENCE_NUMBER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| EXTRA_PARAM1 | VARCHAR2 | 300 |  |  | EXTRA_PARAM1 |
| EXTRA_PARAM2 | VARCHAR2 | 300 |  |  | EXTRA_PARAM2 |
| EXTRA_PARAM3 | VARCHAR2 | 4000 |  |  | EXTRA_PARAM3 |
| EXTRA_PARAM_NUMBER1 | NUMBER |  | 18 |  | EXTRA_PARAM_NUMBER1 |
| EXTRA_PARAM_NUMBER2 | NUMBER |  | 18 |  | EXTRA_PARAM_NUMBER2 |
| EXTRA_PARAM_DATE1 | DATE |  |  |  | EXTRA_PARAM_DATE1 |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TEMPLATES_PK | Unique | Default | TEMPLATE_ID, ORA_SEED_SET1 |
| PAY_TEMPLATES_PK1 | Unique | Default | TEMPLATE_ID, ORA_SEED_SET2 |
| PAY_TEMPLATES_U1 | Unique | Default | TEMPLATE_NAME, BASE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_TEMPLATES_U11 | Unique | Default | TEMPLATE_NAME, BASE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
