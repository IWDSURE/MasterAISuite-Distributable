# WLF_LMC_ROLLUP_RULES

Rollup Rules for a content object

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcrolluprules-21906.html#wlflmcrolluprules-21906](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcrolluprules-21906.html#wlflmcrolluprules-21906)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_ROLLUP_RULES_PK | ROLLUP_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLLUP_RULE_ID | NUMBER |  | 18 | Yes | ROLLUP_RULE_ID |
| SEQUENCING_INFO_ID | NUMBER |  | 18 | Yes | SEQUENCING_INFO_ID |
| RULE_SEQUENCE | NUMBER |  |  | Yes | RULE_SEQUENCE |
| CONDITION_COMBINATION | VARCHAR2 | 1 |  |  | CONDITION_COMBINATION |
| CHILD_ACTIVITY_SET | VARCHAR2 | 1 |  |  | CHILD_ACTIVITY_SET |
| MINIMUM_COUNT | NUMBER |  |  |  | MINIMUM_COUNT |
| MINIMUM_PERCENT | NUMBER |  |  |  | MINIMUM_PERCENT |
| ROLLUP_ACTION | VARCHAR2 | 1 |  | Yes | ROLLUP_ACTION |
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
| WLF_LMC_ROLLUP_RULES_N1 | Non Unique | Default | SEQUENCING_INFO_ID, RULE_SEQUENCE |
| WLF_LMC_ROLLUP_RULES_PK | Unique | FUSION_TS_TX_DATA | ROLLUP_RULE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
