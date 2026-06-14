# HEX_RUN_CUST_OUTPUT

The table stores the final output for custom full extracts and seeded full extracts with retention period <= 90.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexruncustoutput-4547.html#hexruncustoutput-4547](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexruncustoutput-4547.html#hexruncustoutput-4547)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUN_CUST_OUTPUT_PK | CUSTRUN_XML_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CUSTRUN_XML_ID | NUMBER |  |  | Yes | The column indicates a unique sequence generated value. |
| EXT_RUN_ID | NUMBER |  |  |  | The column indicates the EXT_RUN_ID from HEX_RUNS table. |
| CONTENT_VALUE | CLOB |  |  |  | The column indicates the sub xml data. |
| CONTENT_TYPE | VARCHAR2 | 30 |  |  | The column indicates the source of the file like XML. |
| SEQ_NO | NUMBER |  |  |  | The column indicates the sequence of the XML |
| FRAGMENT_SEQ_NO | NUMBER |  | 18 |  | The column indicates the sequence number for each chunk created. |
| EXPIRY_DATE | TIMESTAMP |  |  |  | The column indicates the expiry date of the specific row of the XML generated. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HEX_RUN_CUST_OUTPUT_N1 | Non Unique | Default | EXT_RUN_ID, CONTENT_TYPE, SEQ_NO |  |
| HEX_RUN_CUST_OUTPUT_N2 | Non Unique | Default | EXT_RUN_ID, ATTRIBUTE_CATEGORY, ATTRIBUTE1 | Obsolete |
| HEX_RUN_CUST_OUTPUT_PK | Unique | Default | CUSTRUN_XML_ID |  |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
