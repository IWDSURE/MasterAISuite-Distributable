# PER_REP_PREFERENCES

HCM Reporting document delivery preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perreppreferences-21584.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perreppreferences-21584.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_REP_PREFERENCES_PK | REP_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REP_PREFERENCE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| DOCUMENT_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_REP_DOCUMENTS_B table. |
| LEVEL_CODE | VARCHAR2 | 40 |  |  | Level Code. |
| LEVEL_ID | NUMBER |  | 18 |  | Level ID. |
| PREFERENCE_TYPE | VARCHAR2 | 20 |  |  | Preference Type. |
| PREFERENCE_VALUE | VARCHAR2 | 20 |  |  | Preference Value |
| ALLOW_NEXT_OVERRIDE | VARCHAR2 | 20 |  |  | Indicates whether to allow next level override. |
| ALLOW_WORKER_OVERRIDE | VARCHAR2 | 20 |  |  | Indicates whether to allow worker override. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_REP_PREFERENCES_FK1 | Non Unique | Default | DOCUMENT_ID |
| PER_REP_PREFERENCES_FK2 | Non Unique | Default | LEVEL_CODE |
| PER_REP_PREFERENCES_PK | Unique | Default | REP_PREFERENCE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
