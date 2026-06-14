# PER_BUSINESS_OBJECT_LIMIT

Stores the limit for business object

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perbusinessobjectlimit-18427.html#perbusinessobjectlimit-18427](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perbusinessobjectlimit-18427.html#perbusinessobjectlimit-18427)

## Primary Key

| Name | Columns |
|------|----------|
| PER_BUSINESS_OBJECT_LIMIT_PK | BO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| BO_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| BO_IDENTIFIER | VARCHAR2 | 80 |  | Yes | Identifier for the business object | Active |
| LIMIT | NUMBER |  | 18 | Yes | Numeric value indicating the limit | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_BUSINESS_OBJECT_LIMIT_PK | Unique | Default | BO_ID | Active |
| PER_BUSINESS_OBJECT_LIMIT_U1 | Unique | Default | BO_IDENTIFIER |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
