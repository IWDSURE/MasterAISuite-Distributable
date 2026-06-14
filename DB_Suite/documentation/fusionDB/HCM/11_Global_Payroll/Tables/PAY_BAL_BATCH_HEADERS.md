# PAY_BAL_BATCH_HEADERS

This table contains header information that defines the contents of a batch of balance initialisations to be  transferred into the live schema.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalbatchheaders-6281.html#paybalbatchheaders-6281](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalbatchheaders-6281.html#paybalbatchheaders-6281)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_BATCH_HEADERS_PK | BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | BATCH_ID |
| BATCH_NAME | VARCHAR2 | 100 |  |  | BATCH_NAME |
| BATCH_STATUS | VARCHAR2 | 30 |  |  | BATCH_STATUS |
| UPLOAD_DATE | DATE |  |  |  | UPLOAD_DATE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BAL_BATCH_HEADERS_N1 | Non Unique | Default | BATCH_NAME, LEGISLATIVE_DATA_GROUP_ID |
| PAY_BAL_BATCH_HEADERS_PK | Unique | Default | BATCH_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
