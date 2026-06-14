# PER_EMPL_DELETE_TXN_DATA

This table stores data of a deleted business object.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perempldeletetxndata-3580.html#perempldeletetxndata-3580](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perempldeletetxndata-3580.html#perempldeletetxndata-3580)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EMPL_DELETE_TXN_DATA_PK | EMPL_DELETE_TXN_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMPL_DELETE_TXN_DATA_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a record. |
| TRANSACTION_ID | NUMBER |  | 18 |  | Foreign Key to HRC_TXN_HEADER table. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Uniquely identifies an action occurrence record. Foreign Key to PER_ACTION_OCCURRENCES table. |
| ACTION_DATE | DATE |  |  |  | Effective date of the record being deleted. |
| ENTITY_TYPE | VARCHAR2 | 32 |  |  | Entity Type stores the object of a transactional entity. |
| ENTITY_ID | NUMBER |  | 18 |  | Stores surrogate key of the Entity Type. |
| PARENT_ENTITY_TYPE | VARCHAR2 | 32 |  |  | Parent Entity Type stores the parent object of a transactional entity. |
| PARENT_ENTITY_KEY_ID | NUMBER |  | 18 |  | Stores surrogate key of the Parent Entity Type. |
| EMPL_DELETE_TXN_DATA_XML | XMLTYPE |  |  |  | Stores the deleted object business data. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EMPL_DELETE_TXN_DATA_N1 | Non Unique | Default | ACTION_OCCURRENCE_ID |
| PER_EMPL_DELETE_TXN_DATA_N2 | Non Unique | Default | ENTITY_TYPE, ENTITY_ID |
| PER_EMPL_DELETE_TXN_DATA_PK | Unique | Default | EMPL_DELETE_TXN_DATA_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
