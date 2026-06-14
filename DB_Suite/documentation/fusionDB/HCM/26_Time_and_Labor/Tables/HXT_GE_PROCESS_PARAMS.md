# HXT_GE_PROCESS_PARAMS

The Input values collected from the UI to generate Time Entries. The Time Attributes and their Values that are selected for the creation of Time Entries.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeprocessparams-13219.html#hxtgeprocessparams-13219](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeprocessparams-13219.html#hxtgeprocessparams-13219)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_GE_PROCESS_PARAMS_PK | GE_PROCESS_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GE_PROCESS_PARAM_ID | NUMBER |  | 18 | Yes | GE_PROCESS_PARAM_ID |
| GE_PROCESS_ID | NUMBER |  |  | Yes | GE_PROCESS_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | TM_ATRB_FLD_ID |
| VALUE_TYPE | VARCHAR2 | 20 |  |  | VALUE_TYPE |
| NUMBER_VALUE | NUMBER |  | 18 |  | NUMBER_VALUE |
| STRING_VALUE | VARCHAR2 | 80 |  |  | STRING_VALUE |
| DATE_VALUE | DATE |  |  |  | DATE_VALUE |
| TIMESTAMP_VALUE | TIMESTAMP |  |  |  | TIMESTAMP_VALUE |
| PARAM_DISPLAY_VALUE | VARCHAR2 | 80 |  |  | PARAM_DISPLAY_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_GE_PROCESS_PARAMS_U1 | Unique | Default | GE_PROCESS_PARAM_ID |
| HXT_GE_PROCESS_PARAMS_U2 | Unique | Default | GE_PROCESS_ID, TM_ATRB_FLD_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
