# PER_CHECKLIST_EXCEPTIONS

This table records exceptions occurring at customer side

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistexceptions-29207.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistexceptions-29207.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_EXCEPTIONS_PK | EXCEPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXCEPTION_ID | NUMBER |  | 18 | Yes | EXCEPTION_ID |
| REFERENCE_OBJECT_NAME | VARCHAR2 | 30 |  |  | REFERENCE_OBJECT_NAME |
| REFERENCE_OBJECT_ID | NUMBER |  | 18 |  | REFERENCE_OBJECT_ID |
| PROGRAM_NAME | VARCHAR2 | 240 |  | Yes | PROGRAM_NAME |
| PROGRAM_PARAMETERS | VARCHAR2 | 4000 |  |  | PROGRAM_PARAMETERS |
| EXCEPTION_MESSAGE | VARCHAR2 | 4000 |  |  | EXCEPTION_MESSAGE |
| EXECUTION_CONTEXT | VARCHAR2 | 240 |  |  | EXECUTION_CONTEXT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_EXCEPTIONS_PK | Unique | DEFAULT | EXCEPTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
