# HWM_RULE_RUN_INFO_LINE

Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleruninfoline-17712.html#hwmruleruninfoline-17712](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleruninfoline-17712.html#hwmruleruninfoline-17712)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_RUN_INFO_LINE_PK | RUN_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_LINE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| RUN_SEQ | NUMBER |  | 9 |  | RUN_SEQ |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RUN_ID | NUMBER |  | 18 | Yes | RUN_ID |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| RULE_NAME | VARCHAR2 | 80 |  |  | Name of the Rule |
| RULE_TYPE | VARCHAR2 | 30 |  |  | RULE_TYPE |
| PROCESS_TYPE | VARCHAR2 | 30 |  |  | PROCESS_TYPE |
| PROCESS_ID | NUMBER |  | 18 |  | PROCESS_ID |
| PRS_EFFECTIVE_START_DATE | DATE |  |  |  | PRS_EFFECTIVE_START_DATE |
| PRS_EFFECTIVE_END_DATE | DATE |  |  |  | PRS_EFFECTIVE_END_DATE |
| TCAT_ID_RULE_SET | NUMBER |  | 18 |  | TCAT_ID_RULE_SET |
| TCAT_ID_CONDITION | NUMBER |  | 18 |  | TCAT_ID_CONDITION |
| RULE_EXCLUDED | VARCHAR2 | 1 |  |  | RULE_EXCLUDED |
| EXCLUDE_REASON | VARCHAR2 | 80 |  |  | EXCLUDE_REASON |
| EXCLUDE_COMMENT | VARCHAR2 | 240 |  |  | EXCLUDE_COMMENT |
| FF_LOG_DATA | CLOB |  |  |  | FF_LOG_DATA |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_RUN_INFO_LINE_N1 | Non Unique | Default | LOWER("RULE_NAME") |
| HWM_RULE_RUN_INFO_LINE_N2 | Non Unique | Default | TRUNC("CREATION_DATE") |
| HWM_RULE_RUN_INFO_LINE_N3 | Non Unique | Default | RULE_ID |
| HWM_RULE_RUN_INFO_LINE_PK | Unique | FUSION_TS_TX_DATA | RUN_LINE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
