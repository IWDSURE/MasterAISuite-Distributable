# WLF_SCORM_SEQ_CONDITIONS_F

SCORM sequencing rule expression in a condition

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormseqconditionsf-6457.html#wlfscormseqconditionsf-6457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormseqconditionsf-6457.html#wlfscormseqconditionsf-6457)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_SEQ_CONDS_PK | SEQUENCING_CONDITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQUENCING_CONDITION_ID | NUMBER |  | 18 | Yes | SEQUENCING_RULE_TERM_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SEQUENCING_RULE_ID | NUMBER |  | 18 | Yes | Foreign key into the WLF_SEQUENCING_RULES table. |
| CONDITION_SEQUENCE | NUMBER |  |  | Yes | TERM_SEQUENCE |
| OBJECTIVE_ID | NUMBER |  | 18 |  | OBJECTIVE_ID |
| MEASURE_THRESHOLD | NUMBER |  |  |  | MEASURE_THRESHOLD |
| CONDITION_OPERATOR | VARCHAR2 | 1 |  |  | OPERATOR |
| CONDITION_TYPE | VARCHAR2 | 1 |  | Yes | CONDITION_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SCORM_SEQ_CONDS_N1 | Non Unique | Default | SEQUENCING_RULE_ID, CONDITION_SEQUENCE |
| WLF_SCORM_SEQ_CONDS_PK | Unique | FUSION_TS_TX_DATA | SEQUENCING_CONDITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
