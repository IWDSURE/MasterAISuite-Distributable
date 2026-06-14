# HRC_ALERT_RUN_ERRORS

Contains alert run errors for a given run.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunerrors-12655.html#hrcalertrunerrors-12655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcalertrunerrors-12655.html#hrcalertrunerrors-12655)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ALERT_RUN_ERRORS_PK | ERROR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ERROR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ERROR_TYPE | VARCHAR2 | 30 |  |  | Error Type, possible values are ORA_E (Error),ORA_W (Warning),ORA_I(Info) and ORA_S (System Error) |
| PARENT_RUN_ID | NUMBER |  | 18 |  | Run Identifier of Parent. Foreign Key to HRC_ALERTS_RUNS.RUN_ID |
| RUN_ID | NUMBER |  | 18 | Yes | Run Identifier. Foreign Key to HRC_ALERT_RUNS.RUN_ID |
| ERROR_SOURCE | VARCHAR2 | 30 |  | Yes | Specifies the source of the error. Valid values are: R=Run,M=Message,R=Recipient |
| ERROR_SOURCE_ID | NUMBER |  | 18 | Yes | Specifies the source identifier and is dependent on the contents of the ERROR_SOURCE. If R (Run) then HRC_ALERT_RUNS.RUN_ID. If M (Message) then HRC_ALERT_RUN_MESSAGES.RUN_MESSAGE_ID. If R (Recipient) then HRC_ALERT_RUN_RECIPIENTS.RECIPIENT_ID. |
| ERROR_MSG_TEXT | VARCHAR2 | 2000 |  |  | Details of the error message. As we are using CLOB column, its taking time, instead going forward we can use this column which will have just the details. |
| ERROR_TEXT | CLOB |  |  |  | The error text of the Alert Run Error record. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SURROGATE_ID | NUMBER |  | 18 |  | SurrogateId of the record of the rest resource related table that is configured in the Alert. |
| PROP_NAME | VARCHAR2 | 80 |  |  | Property Name of the Alert Run Error record. |
| PROP_VALUE | VARCHAR2 | 200 |  |  | Property Value of the Alert Run Error record. |
| FUNC_NAME | VARCHAR2 | 80 |  |  | Function Name of the Alert Run Error record. |
| FUNC_ARG_NAME1 | VARCHAR2 | 80 |  |  | Function First Argument Name of the record. |
| FUNC_ARG_VAL1 | VARCHAR2 | 200 |  |  | Function First Argument Value of the record. |
| FUNC_ARG_NAME2 | VARCHAR2 | 80 |  |  | Function Second Argument Name of the record. |
| FUNC_ARG_VAL2 | VARCHAR2 | 200 |  |  | Function Second Argument Value of the record. |
| FUNC_ARG_NAME3 | VARCHAR2 | 80 |  |  | Function Third Argument Name of the record. |
| FUNC_ARG_VAL3 | VARCHAR2 | 200 |  |  | Function Third Argument Value of the record. |
| ERROR_SUBTYPE | VARCHAR2 | 30 |  |  | Error Subtype of the Alert Run Error record. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ALERT_RUN_ERRORS_N1 | Non Unique | Default | RUN_ID, ERROR_SOURCE, ERROR_SOURCE_ID |
| HRC_ALERT_RUN_ERRORS_N2 | Non Unique | Default | PARENT_RUN_ID |
| HRC_ALERT_RUN_ERRORS_N3 | Non Unique | Default | ERROR_TYPE, PARENT_RUN_ID |
| HRC_ALERT_RUN_ERRORS_N4 | Non Unique | Default | ERROR_TYPE, RUN_ID |
| HRC_ALERT_RUN_ERRORS_PK | Unique | Default | ERROR_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
