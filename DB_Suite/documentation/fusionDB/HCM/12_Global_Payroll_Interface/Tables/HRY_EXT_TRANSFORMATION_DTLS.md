# HRY_EXT_TRANSFORMATION_DTLS

Stores detailed information related to transformation.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryexttransformationdtls-7265.html#hryexttransformationdtls-7265](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryexttransformationdtls-7265.html#hryexttransformationdtls-7265)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EXT_TRANSFORMATION_DTLS_PK | TRANSFORMATION_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSFORMATION_DETAIL_ID | NUMBER |  | 18 | Yes | Primary key for HRY_EXT_TRANSFORMATION_DTLS |
| REQUESTID | NUMBER |  | 18 |  | For storing the ess job request id that does the transformation. |
| TRANSFORMATION_ID | NUMBER |  | 18 | Yes | Primary key for HRY_EXT_TRANSFORMATION |
| PARSE_DETAIL_ID | NUMBER |  | 18 | Yes | Foreign key to HRY_EXT_PARSE_DETAIL |
| TRANSFORMED_XML | CLOB |  |  |  | For storing transformed sub xmls formed after DIAGNOSTICS Transformation or VALUE MAP Transformation |
| OBJECT_ACTION_ID | NUMBER |  | 18 |  | For storing the Object action id or Object Id |
| TRANSFORMATION_STATUS | VARCHAR2 | 80 |  |  | For storing transformation status.The values can be SUCCESS/ERROR/NOT PROCESSED |
| ERROR_DETAILS | VARCHAR2 | 4000 |  |  | For storing error text in case of any transformation error |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EXT_TRANSFORMATION_DTLS_N1 | Non Unique | Default | TRANSFORMATION_ID, TRANSFORMATION_STATUS |
| HRY_EXT_TRANSFORMATION_DTLS_PK | Unique | Default | TRANSFORMATION_DETAIL_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
