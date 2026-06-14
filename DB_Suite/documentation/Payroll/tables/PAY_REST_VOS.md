# PAY_REST_VOS

This table contains register VO names which can be accessed by generic rest webservice.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrestvos-14851.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrestvos-14851.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REST_VOS_PK | PAY_REST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_REST_ID | NUMBER |  | 18 | Yes | PAY_REST_ID |
| PAY_REST_NAME | VARCHAR2 | 512 |  | Yes | PAY_REST_NAME |
| VIEW_OBJECT_NAME | VARCHAR2 | 512 |  |  | Classpath for registered VO |
| SQL_QUERY | CLOB |  |  |  | SQL_QUERY |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| IS_SECURED | VARCHAR2 | 30 |  |  | IS_SECURED |
| REST_ADDITIONAL_CODE | VARCHAR2 | 64 |  |  | REST_ADDITIONAL_CODE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REST_VOS_U1 | Unique | Default | PAY_REST_ID, ORA_SEED_SET1 |
| PAY_REST_VOS_U11 | Unique | Default | PAY_REST_ID, ORA_SEED_SET2 |
| PAY_REST_VOS_U2 | Unique | Default | PAY_REST_NAME, ORA_SEED_SET1 |
| PAY_REST_VOS_U21 | Unique | Default | PAY_REST_NAME, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
