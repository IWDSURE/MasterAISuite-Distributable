# PER_NUDGE_PLANS_B

This table records the nudge plans.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplansb-26993.html#pernudgeplansb-26993](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplansb-26993.html#pernudgeplansb-26993)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLANS_B_PK | NUDGE_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NUDGE_PLAN_ID | NUMBER |  | 18 | Yes | NUDGE_PLAN_ID |
| NUDGE_PLAN_CODE | VARCHAR2 | 240 |  | Yes | NUDGE_PLAN_CODE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| CRITERIA_CONDITION1 | VARCHAR2 | 4000 |  |  | CRITERIA_CONDITION1 |
| CRITERIA_CONDITION2 | VARCHAR2 | 4000 |  |  | CRITERIA_CONDITION2 |
| CRITERIA_CONDITION3 | VARCHAR2 | 4000 |  |  | CRITERIA_CONDITION3 |
| CRITERIA_CONDITION4 | VARCHAR2 | 4000 |  |  | CRITERIA_CONDITION4 |
| CRITERIA_CONDITION5 | VARCHAR2 | 4000 |  |  | CRITERIA_CONDITION5 |
| ENABLE_SCHEDULE | VARCHAR2 | 4 |  | Yes | Enable schedule flag for nudge plan |
| CRITERIA_TYPE | VARCHAR2 | 30 |  |  | Type of criteria |
| LIST_ID | NUMBER |  | 18 |  | Foreign Key to HR_VBCS_LISTS
The hcm list for which the criteria is specified |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | OBJECT_TYPE |
| SUBSCRIBER_CODE | VARCHAR2 | 30 |  | Yes | SUBSCRIBER_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | ELIGIBILITY_PROFILE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_NUDGE_PLANS_B_PK | Unique | Default | NUDGE_PLAN_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
