# CEL_ILLUSTRATIONS_B

MLS base table to hold details of  illustrations

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celillustrationsb-30149.html#celillustrationsb-30149](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celillustrationsb-30149.html#celillustrationsb-30149)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_ILLUSTRATIONS_B_PK | ILLUSTRATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ILLUSTRATION_ID | NUMBER |  | 18 | Yes | Unique identifier for a Illustration |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if illustration is enabled |
| ILLUSTRATION | BLOB |  |  |  | Custom image uploaded by administrators |
| CONTENT_ID | VARCHAR2 | 30 |  |  | Universal content management identifier of stored illustration |
| ILLUSTRATION_URL | VARCHAR2 | 4000 |  |  | Uniform resource locator for stored illustration |
| ILLUSTRATION_CODE | VARCHAR2 | 30 |  |  | Lookup code for seeded image |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_ILLUSTRATIONS_B_PK | Unique | Default | ILLUSTRATION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
