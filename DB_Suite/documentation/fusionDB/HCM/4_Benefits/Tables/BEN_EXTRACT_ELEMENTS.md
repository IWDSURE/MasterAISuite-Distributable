# BEN_EXTRACT_ELEMENTS

This tbale holds basic data strcuture elements for the extract process for benefix.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractelements-24632.html#benextractelements-24632](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextractelements-24632.html#benextractelements-24632)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_ID | NUMBER |  | 18 | Yes | ELEMENT_ID |
| LAYOUT_ID | NUMBER |  | 18 | Yes | LAYOUT_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PARENT_ELEMENT_ID | NUMBER |  | 18 |  | PARENT_ELEMENT_ID |
| NAME | VARCHAR2 | 90 |  |  | NAME |
| LOOKUP_TYPE | VARCHAR2 | 60 |  |  | Identifies the lookup type that maps to this element. |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| SEQUENCE_NUM | NUMBER |  | 9 |  | SEQUENCE_NUM |
| REQUIRED_FLAG | VARCHAR2 | 30 |  |  | REQUIRED_FLAG |
| DEFAULT_FLAG | VARCHAR2 | 30 |  |  | DEFAULT_FLAG |
| POPULATE_FLAG | VARCHAR2 | 30 |  |  | POPULATE_FLAG |
| SEEDED_FLAG | VARCHAR2 | 30 |  |  | SEEDED_FLAG |
| DEFAULT_VALUE | VARCHAR2 | 60 |  |  | DEFAULT_VALUE |
| XML_TAG_NAME | VARCHAR2 | 60 |  |  | XML_TAG_NAME |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
