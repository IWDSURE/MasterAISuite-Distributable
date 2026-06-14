# HWM_RULE_SET_MBRS

Contains members of Time Rule Set. Each row has a sequence of precessing the Rule or Rule set and Time category.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulesetmbrs-22459.html#hwmrulesetmbrs-22459](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulesetmbrs-22459.html#hwmrulesetmbrs-22459)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_SET_MBRS_PK | RULE_SET_MBRS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RULE_SET_MBRS_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |  |
| RULE_SET_ID | NUMBER |  | 18 | Yes | Foreign key to Ruleset Table |  |
| RULE_SET_UNQ_ID | NUMBER |  | 18 | Yes | Foreign key to Ruleset Table |  |
| PROCESSING_ORDER | NUMBER |  | 9 | Yes | The Order in which these rules, rulesets should be applied on the TBB. |  |
| TCAT_ID | NUMBER |  | 18 |  | Time category Run Condition, which determines if this member should be applied on TBB. |  |
| MEMBER_TYPE | VARCHAR2 | 30 |  | Yes | Lookup type - Determines if this member is a Rule, Conditional Rule or a Rule Set. |  |
| MBR_RULE_ID | NUMBER |  | 18 |  | MBR_RULE_ID |  |
| MBR_RULE_SET_ID | NUMBER |  | 18 |  | MBR_RULE_SET_ID |  |
| MBR_CNDL_RULE_ID | NUMBER |  | 18 |  | MBR_CNDL_RULE_ID |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_SET_MBRS_N1 | Non Unique | Default | MBR_RULE_ID |
| HWM_RULE_SET_MBRS_PK | Unique | FUSION_TS_TX_DATA | RULE_SET_MBRS_ID |
| HWM_RULE_SET_MBRS_U1 | Unique | FUSION_TS_TX_DATA | RULE_SET_UNQ_ID, PROCESSING_ORDER |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
