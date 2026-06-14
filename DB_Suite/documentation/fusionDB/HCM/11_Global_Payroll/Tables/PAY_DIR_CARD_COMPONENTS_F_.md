# PAY_DIR_CARD_COMPONENTS_F_

This table contains the details of a person's deduction card.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircardcomponentsf-11109.html#paydircardcomponentsf-11109](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircardcomponentsf-11109.html#paydircardcomponentsf-11109)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_CARD_COMPONENTS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DIR_CARD_COMP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_CARD_COMP_ID | NUMBER |  | 18 | Yes | DIR_CARD_COMP_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | DIR_CARD_COMP_DEF_ID |
| DIR_CARD_ID | NUMBER |  | 18 |  | DIR_CARD_ID |
| SUBPRIORITY | NUMBER |  | 9 |  | SUBPRIORITY |
| PARENT_DIR_CARD_COMP_ID | NUMBER |  | 18 |  | PARENT_DIR_CARD_COMP_ID |
| DEDUCTION_GROUP_ID | NUMBER |  | 18 |  | DEDUCTION_GROUP_ID |
| CREATOR_ID | NUMBER |  | 25 |  | CREATOR_ID |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | CREATOR_TYPE |
| CREATING_ACTION_ID | NUMBER |  | 18 |  | The Batch processing Action that created this component. |
| CONTEXT_VALUE1 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE1 |
| CONTEXT_VALUE2 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE2 |
| CONTEXT_VALUE3 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE3 |
| CONTEXT_VALUE4 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE4 |
| CONTEXT_VALUE5 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE5 |
| CONTEXT_VALUE6 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE6 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| COMPONENT_SEQUENCE | NUMBER |  | 18 |  | COMPONENT_SEQUENCE |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_CARD_COMPONENTS_FN1_ | Non Unique | Default | DIR_CARD_COMP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_CARD_COMPONENTS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DIR_CARD_COMP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
