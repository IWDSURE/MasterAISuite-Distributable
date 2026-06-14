# HR_API_HOOK_CALLS

Lists which extra logic, package procedures or formula, should be called from the API hook points. This table will contain rows created by legislation groups, legislation vertical market groups and customers.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapihookcalls-24480.html#hrapihookcalls-24480](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapihookcalls-24480.html#hrapihookcalls-24480)

## Primary Key

| Name | Columns |
|------|----------|
| HR_API_HOOK_CALLS_PK | API_HOOK_CALL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| API_HOOK_CALL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| API_HOOK_ID | NUMBER |  | 18 | Yes | Foreign key to HR_API_HOOKS. |
| API_HOOK_CALL_TYPE | VARCHAR2 | 30 |  | Yes | Type of hook call. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Indicates if the extra logic should be called every time the hook point is reached or when the data corresponds to a particular legislation. |
| SEQUENCE | NUMBER |  | 18 | Yes | When more than one row exists for the same API_HOOK_ID, SEQUENCE affects the order of the hook calls. |
| ENABLED_FLAG | VARCHAR2 | 30 |  | Yes | Indicates if the hook call should be generated. |
| CALL_PACKAGE | VARCHAR2 | 30 |  |  | Name of the database package which the hook package should call to carry out the legislation, legislation vertical market or customer specific logic |
| CALL_PROCEDURE | VARCHAR2 | 30 |  |  | Name of the procedure, within CALL_PACKAGE, which the hook package should call to carry out the legislation, legislation vertical market or customer specific logic. |
| PRE_PROCESSOR_DATE | DATE |  |  |  | The last time the API hook pre-processor program attempted (successfully or unsuccessfully) to create the package body code for this hook call. |
| ENCODED_ERROR | VARCHAR2 | 2000 |  |  | If the last time the API hook pre-processor program failed to make the source code for this hook call, the error details will be held in this column. |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of hook call code at pre-processor time (as of PRE_PROCESSOR_DATE). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| APPLICATION_ID | NUMBER |  |  |  | The APPLICATION_ID of Application as defined in the FND_APPLICATION table. |
| APP_INSTALL_STATUS | VARCHAR2 | 30 |  |  | Indicates for which installation statuses the hook call should be included in the user hook package body. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_API_HOOK_CALLS_PK | Unique | Default | API_HOOK_CALL_ID, ORA_SEED_SET1 |
| HR_API_HOOK_CALLS_PK1 | Unique | Default | API_HOOK_CALL_ID, ORA_SEED_SET2 |
| HR_API_HOOK_CALLS_U1 | Unique | Default | APPLICATION_ID, API_HOOK_ID, LEGISLATION_CODE, CALL_PACKAGE, CALL_PROCEDURE, ORA_SEED_SET1 |
| HR_API_HOOK_CALLS_U11 | Unique | Default | APPLICATION_ID, API_HOOK_ID, LEGISLATION_CODE, CALL_PACKAGE, CALL_PROCEDURE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
