# FAI_MARKET_PLACE_WORKFLOWS

This table stores the marketplace workflows

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimarketplaceworkflows-29559.html#faimarketplaceworkflows-29559](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimarketplaceworkflows-29559.html#faimarketplaceworkflows-29559)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_MARKET_PLACE_WORKFLOWS_PK | MARKET_PLACE_WORKFLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MARKET_PLACE_WORKFLOW_ID | NUMBER |  | 18 | Yes | Uniquely identifies the marketplace workflow |
| WORKFLOW_NAME | VARCHAR2 | 200 |  | Yes | Name for the marketplace workflow |
| WORKFLOW_CODE | VARCHAR2 | 200 |  | Yes | Code for the marketplace workflow |
| FAMILY | VARCHAR2 | 80 |  | Yes | The product family associated to the marketplace workflow |
| PRODUCT | VARCHAR2 | 100 |  | Yes | The product associated to the marketplace workflow |
| SPECIFICATION | CLOB |  |  | Yes | JSON specification for the marketplace workflow |
| MKTPLACE_METADATA | CLOB |  |  |  | JSON metadata for the marketplace workflow |
| SEEDED_FLAG | VARCHAR2 | 1 |  | Yes | Indicates if the record was seeded by Oracle. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_MARKET_PLACE_WORKFLOWS_U1 | Unique | Default | MARKET_PLACE_WORKFLOW_ID, ORA_SEED_SET1 |
| FAI_MARKET_PLACE_WORKFLOWS_U2 | Unique | Default | MARKET_PLACE_WORKFLOW_ID, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
