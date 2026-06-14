# HRW_RUN_DETAILS

Table to save run details of esc configuration.

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwrundetails-22166.html#hrwrundetails-22166](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwrundetails-22166.html#hrwrundetails-22166)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_RUN_DETAILS_PK | RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | RUN_ID |
| CONFIGURATION_ID | NUMBER |  | 18 |  | CONFIGURATION_ID |
| PROCESS_CODE | VARCHAR2 | 30 |  |  | PROCESS_CODE |
| PROCESS_STATUS | VARCHAR2 | 30 |  |  | PROCESS_STATUS |
| PROCESS_START_TIME | TIMESTAMP |  |  |  | PROCESS_START_TIME |
| PROCESS_END_TIME | TIMESTAMP |  |  |  | PROCESS_END_TIME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_RUN_DETAILS_U1 | Unique | Default | RUN_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
