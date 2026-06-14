# HRC_DL_AUDIT_LINES

This table holds data for each line of the audit output. Each row will be identified using AUDIT_LINE_ID

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlauditlines-11047.html#hrcdlauditlines-11047](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlauditlines-11047.html#hrcdlauditlines-11047)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_AUDIT_LINES_PK | AUDIT_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUDIT_LINE_ID | NUMBER |  | 18 | Yes | Primary Key. From sequence. |
| AUDIT_HEADER_ID | NUMBER |  | 18 | Yes | Foreign key to hrc_dl_audit_headers. The Audit Header Id of the business object component that this audit line reports. |
| AUDIT_LINE_NUMBER | NUMBER |  | 9 | Yes | Line number of the business object component audit line as it would be positioned within a standard file to enable correct output order during extract. |
| LINE_CONTENT | VARCHAR2 | 400 |  |  | Content of the business object component audit line as it would appear in a file based output. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise stripe identifier. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_AUDIT_LINES_U1 | Unique | Default | AUDIT_LINE_ID |
| HRC_DL_AUDIT_LINES_U2 | Unique | Default | AUDIT_HEADER_ID, AUDIT_LINE_NUMBER |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
