# PAY_LEG_UPDATE_MERGE_ERRORS

PAY_LEG_UPDATE_MERGE_ERRORS - contains errors occurred during execution of pay_legislative_updates procedure.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** DEFAULT

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatemergeerrors-9137.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatemergeerrors-9137.html)

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| ORA_ERR_NUMBER$ | NUMBER |  |  | ORA_ERR_NUMBER$ |
| ORA_ERR_MESG$ | VARCHAR2 | 2000 |  | ORA_ERR_MESG$ |
| ORA_ERR_ROWID$ | ROWID |  |  | ORA_ERR_ROWID$ |
| ORA_ERR_OPTYP$ | VARCHAR2 | 2 |  | ORA_ERR_OPTYP$ |
| ORA_ERR_TAG$ | VARCHAR2 | 2000 |  | ORA_ERR_TAG$ |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
