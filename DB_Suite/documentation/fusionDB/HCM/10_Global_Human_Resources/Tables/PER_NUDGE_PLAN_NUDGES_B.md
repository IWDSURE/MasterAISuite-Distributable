# PER_NUDGE_PLAN_NUDGES_B

This table stores the nudge plan details.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplannudgesb-12572.html#pernudgeplannudgesb-12572](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeplannudgesb-12572.html#pernudgeplannudgesb-12572)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_PLAN_NUDGES_B_PK | PLAN_NUDGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_NUDGE_ID | NUMBER |  | 18 | Yes | PLAN_NUDGE_ID |
| PLAN_NUDGE_CODE | VARCHAR2 | 240 |  | Yes | PLAN_NUDGE_CODE |
| NUDGE_PLAN_ID | NUMBER |  | 18 | Yes | NUDGE_PLAN_ID |
| PRODUCT_CODE | VARCHAR2 | 30 |  | Yes | PRODUCT_CODE |
| NUDGE_TYPE_CODE | VARCHAR2 | 80 |  | Yes | NUDGE_TYPE_CODE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| INPUT_PARAMETER1 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER1 |
| INPUT_PARAMETER2 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER2 |
| INPUT_PARAMETER3 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER3 |
| INPUT_PARAMETER4 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER4 |
| INPUT_PARAMETER5 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER5 |
| INPUT_PARAMETER6 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER6 |
| INPUT_PARAMETER7 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER7 |
| INPUT_PARAMETER8 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER8 |
| INPUT_PARAMETER9 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER9 |
| INPUT_PARAMETER10 | VARCHAR2 | 400 |  |  | INPUT_PARAMETER10 |
| INPUT_PARAMETER_NUMBER1 | NUMBER |  |  |  | INPUT_PARAMETER_NUMBER1 |
| INPUT_PARAMETER_NUMBER2 | NUMBER |  |  |  | INPUT_PARAMETER_NUMBER2 |
| INPUT_PARAMETER_NUMBER3 | NUMBER |  |  |  | INPUT_PARAMETER_NUMBER3 |
| INPUT_PARAMETER_NUMBER4 | NUMBER |  |  |  | INPUT_PARAMETER_NUMBER4 |
| INPUT_PARAMETER_NUMBER5 | NUMBER |  |  |  | INPUT_PARAMETER_NUMBER5 |
| INPUT_PARAMETER_DATE1 | DATE |  |  |  | INPUT_PARAMETER_DATE1 |
| INPUT_PARAMETER_DATE2 | DATE |  |  |  | INPUT_PARAMETER_DATE2 |
| INPUT_PARAMETER_DATE3 | DATE |  |  |  | INPUT_PARAMETER_DATE3 |
| INPUT_PARAMETER_DATE4 | DATE |  |  |  | INPUT_PARAMETER_DATE4 |
| INPUT_PARAMETER_DATE5 | DATE |  |  |  | INPUT_PARAMETER_DATE5 |
| EXPIRY_FLAG | VARCHAR2 | 4 |  | Yes | EXPIRY_FLAG |
| EXPIRY_DURATION | NUMBER |  | 9 |  | EXPIRY_DURATION |
| EXPIRY_DURATION_UOM | VARCHAR2 | 30 |  |  | EXPIRY_DURATION_UOM |
| EXPIRY_RELATIVE_TO | VARCHAR2 | 30 |  |  | EXPIRY_RELATIVE_TO |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_NUDGE_PLAN_NUDGES_B_N1 | Non Unique | Default | NUDGE_PLAN_ID, NUDGE_TYPE_CODE |
| PER_NUDGE_PLAN_NUDGES_B_PK | Unique | Default | PLAN_NUDGE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
