# HWM_RULE_FF_WORKAREA

Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleffworkarea-3800.html#hwmruleffworkarea-3800](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleffworkarea-3800.html#hwmruleffworkarea-3800)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_FF_WORKAREA_PK | WORKAREA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKAREA_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FFS_ID | NUMBER |  | 18 | Yes | Unique Fast Formula Session id used for one ruleset processing |
| PARM_TYPE | VARCHAR2 | 10 |  | Yes | Values 'WRK', 'LOG', 'RULE' |
| PARM_NAME | VARCHAR2 | 30 |  | Yes | PARM_NAME |
| PARM_SEQ | NUMBER |  | 9 | Yes | PARM_SEQ |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| PARM_VALUE_ID | NUMBER |  | 18 |  | PARM_VALUE_ID |
| PARM_VALUE_NUMBER | NUMBER |  |  |  | PARM_VALUE_NUMBER |
| PARM_VALUE_DATE | DATE |  |  |  | PARM_VALUE_DATE |
| PARM_VALUE_TEXT | VARCHAR2 | 250 |  |  | PARM_VALUE_TEXT |
| PARM_VALUE_LOG | VARCHAR2 | 250 |  |  | PARM_VALUE_LOG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_FF_WORKAREA_N1 | Non Unique | Default | WORKAREA_ID, LAST_UPDATE_DATE |
| HWM_RULE_FF_WORKAREA_N2 | Non Unique | Default | TRUNC("CREATION_DATE") |
| HWM_RULE_FF_WORKAREA_PK | Unique | FUSION_TS_TX_DATA | WORKAREA_ID |
| HWM_RULE_FF_WORKAREA_U1 | Unique | FUSION_TS_TX_DATA | FFS_ID, PARM_TYPE, PARM_NAME, PARM_SEQ |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
