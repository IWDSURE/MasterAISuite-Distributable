# PAY_DIR_REP_CARDS_F_

This table contains the association between a card, or a section of a card, and a tax reporting unit, thus forming a reporting card.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydirrepcardsf-23017.html#paydirrepcardsf-23017](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydirrepcardsf-23017.html#paydirrepcardsf-23017)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_REP_CARDS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DIR_REP_CARD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_REP_CARD_ID | NUMBER |  | 18 | Yes | DIR_REP_CARD_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| DIR_CARD_ID | NUMBER |  | 18 |  | DIR_CARD_ID |
| DIR_CARD_COMP_ID | NUMBER |  | 18 |  | DIR_CARD_COMP_ID |
| TRU_BATCH_ID | VARCHAR2 | 80 |  |  | TRU_BATCH_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIR_REP_CARDS_FN1_ | Non Unique | Default | DIR_REP_CARD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_REP_CARDS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DIR_REP_CARD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
