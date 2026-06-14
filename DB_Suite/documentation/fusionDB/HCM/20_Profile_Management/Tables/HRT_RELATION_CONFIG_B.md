# HRT_RELATION_CONFIG_B

Relation Config Base table stores the relations that can be associated to model profiles.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtrelationconfigb-4966.html#hrtrelationconfigb-4966](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtrelationconfigb-4966.html#hrtrelationconfigb-4966)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_RELATION_CONFIG_B_PK | RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RELATION_ID | NUMBER |  | 18 | Yes | Relation ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| RELATION_CODE | VARCHAR2 | 30 |  | Yes | Relation Code |
| RELATION_TYPE_CODE | VARCHAR2 | 30 |  |  | Relation Type Code |
| RELATION_SEQ_NUMBER | NUMBER |  | 18 |  | Relation Sequence Number |
| KEY_TABLE_NAME | VARCHAR2 | 240 |  | Yes | Key Table Name |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENABLED_FLAG | VARCHAR2 | 30 |  |  | Enabled Flag |
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
| HRT_RELATION_CONFIG_B_U1 | Unique | Default | RELATION_ID, ORA_SEED_SET1 |
| HRT_RELATION_CONFIG_B_U11 | Unique | Default | RELATION_ID, ORA_SEED_SET2 |
| HRT_RELATION_CONFIG_B_U2 | Unique | Default | RELATION_CODE, ORA_SEED_SET1 |
| HRT_RELATION_CONFIG_B_U21 | Unique | Default | RELATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
