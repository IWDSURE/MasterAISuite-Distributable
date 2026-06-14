# PAY_DIR_CARDS_F

This table contains the header of a person's deduction card.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircardsf-7150.html#paydircardsf-7150](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircardsf-7150.html#paydircardsf-7150)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_CARDS_F_PK | DIR_CARD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_CARD_ID | NUMBER |  | 18 | Yes | DIR_CARD_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 | Yes | DIR_CARD_DEFINITION_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| CREATOR_ID | NUMBER |  | 18 |  | CREATOR_ID |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | CREATOR_TYPE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CARD_SEQUENCE | NUMBER |  | 18 |  | CARD_SEQUENCE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIR_CARDS_F_N1 | Non Unique | Default | DIR_CARD_DEFINITION_ID |
| PAY_DIR_CARDS_F_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID |
| PAY_DIR_CARDS_F_N3 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_DIR_CARDS_F_PK | Unique | Default | DIR_CARD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
