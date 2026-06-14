# HWM_RULE_FF_WORK_LOG

Contains the logs created for OTL Time Calculation, Time Entry and Time Audit rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleffworklog-5002.html#hwmruleffworklog-5002](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleffworklog-5002.html#hwmruleffworklog-5002)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_FF_WORK_LOG_PK | LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOG_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FFS_ID | NUMBER |  | 18 | Yes | Unique Fast Formula Session id used for one ruleset processing |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| LOG_TYPE | VARCHAR2 | 30 |  |  | LOG_TYPE |
| LOG_GROUP_TYPE | VARCHAR2 | 30 |  |  | LOG_GROUP_TYPE |
| APP_NAME | VARCHAR2 | 30 |  |  | APP_NAME |
| LOG_SEVERITY | VARCHAR2 | 30 |  |  | LOG_SEVERITY |
| LOG_TEXT | VARCHAR2 | 2000 |  |  | LOG_TEXT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_FF_WORK_LOG_N1 | Non Unique | Default | FFS_ID |
| HWM_RULE_FF_WORK_LOG_N2 | Non Unique | Default | RULE_ID |
| HWM_RULE_FF_WORK_LOG_N3 | Non Unique | Default | TRUNC("CREATION_DATE") |
| HWM_RULE_FF_WORK_LOG_PK | Unique | FUSION_TS_TX_DATA | LOG_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
