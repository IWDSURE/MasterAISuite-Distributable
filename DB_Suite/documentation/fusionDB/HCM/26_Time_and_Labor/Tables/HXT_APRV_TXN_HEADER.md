# HXT_APRV_TXN_HEADER

Approval record group records for approval

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtaprvtxnheader-10258.html#hxtaprvtxnheader-10258](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtaprvtxnheader-10258.html#hxtaprvtxnheader-10258)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_APRV_TXN_HEADER_PK | APRV_TM_REC_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APRV_TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Approval Time Record Group Id |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| EXPEDITE | VARCHAR2 | 240 |  |  | EXPEDITE |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMB1 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB1 |
| ATTRIBUTE_NUMB2 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB2 |
| ATTRIBUTE_NUMB3 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB3 |
| ATTRIBUTE_NUMB4 | NUMBER |  | 18 |  | ATTRIBUTE_NUMBB4 |
| ATTRIBUTE_NUMB5 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB5 |
| HEADER_ATTRIBUTE_CHAR1 | VARCHAR2 | 150 |  |  | Generic header attribute of type Char. |
| HEADER_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | HEADER_ATTRIBUTE_NUMBER1 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ABSAPPROVALUSAGECD | VARCHAR2 | 240 |  |  | ABSAPPROVALUSAGECD |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_APRV_TXN_HEADER_U1 | Unique | Default | APRV_TM_REC_GRP_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
