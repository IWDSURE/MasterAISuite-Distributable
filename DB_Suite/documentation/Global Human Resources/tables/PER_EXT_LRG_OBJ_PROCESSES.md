# PER_EXT_LRG_OBJ_PROCESSES

EXTRACT LARGE OBJECT PROCESSES TABLE

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextlrgobjprocesses-7041.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextlrgobjprocesses-7041.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_LRG_OBJ_PROCESSES_PK | FLOW_INSTANCE_ID, PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_INSTANCE_ID |
| PROCESS_ID | NUMBER |  | 18 | Yes | PROCESS_ID |
| PARENT_PROCESS_ID | NUMBER |  | 18 |  | PARENT_PROCESS_ID |
| PROCESS_TYPE | VARCHAR2 | 100 |  |  | PROCESS_TYPE |
| ABS_PROCESS_ID | NUMBER |  | 18 |  | ABS_PROCESS_ID |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | EXT_DEFINITION_ID |
| START_DATE_TIME | TIMESTAMP |  |  |  | START_DATE_TIME |
| END_DATE_TIME | TIMESTAMP |  |  |  | END_DATE_TIME |
| STATUS | VARCHAR2 | 100 |  |  | STATUS |
| ONGOING_STATUS | VARCHAR2 | 100 |  |  | ONGOING_STATUS |
| IDENTIFIED_OBJECTS | NUMBER |  | 38 |  | IDENTIFIED_OBJECTS |
| ERRORED_OBJECTS | NUMBER |  | 38 |  | ERRORED_OBJECTS |
| PROCESSED_OBJECTS | NUMBER |  | 38 |  | PROCESSED_OBJECTS |
| FILE_LIST_SENT | VARCHAR2 | 4000 |  |  | FILE_LIST_SENT |
| COMMENTS | VARCHAR2 | 4000 |  |  | COMMENTS |
| COMMENTS1 | VARCHAR2 | 4000 |  |  | COMMENTS1 |
| COMMENTS2 | VARCHAR2 | 4000 |  |  | COMMENTS2 |
| COMMENTS3 | VARCHAR2 | 4000 |  |  | COMMENTS3 |
| COMMENTS4 | VARCHAR2 | 4000 |  |  | COMMENTS4 |
| COMMENTS5 | VARCHAR2 | 4000 |  |  | COMMENTS5 |
| COMMENTS6 | VARCHAR2 | 4000 |  |  | COMMENTS6 |
| COMMENTS7 | VARCHAR2 | 4000 |  |  | COMMENTS6 |
| COMMENTS8 | VARCHAR2 | 4000 |  |  | COMMENTS8 |
| COMMENTS9 | VARCHAR2 | 4000 |  |  | COMMENTS9 |
| COMMENTS10 | VARCHAR2 | 4000 |  |  | COMMENTS10 |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_LRG_OBJ_PROCESSES_N1 | Non Unique | Default | EXT_DEFINITION_ID |
| PER_EXT_LRG_OBJ_PROCESSES_N2 | Non Unique | Default | ABS_PROCESS_ID |
| PER_EXT_LRG_OBJ_PROCESSES_PK | Unique | Default | FLOW_INSTANCE_ID, PROCESS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
