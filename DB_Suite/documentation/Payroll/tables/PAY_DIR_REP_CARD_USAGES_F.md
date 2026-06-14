# PAY_DIR_REP_CARD_USAGES_F

This table contains mappings of deduction components to employment terms or assignments within a reporting card.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydirrepcardusagesf-30503.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydirrepcardusagesf-30503.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_REP_CARD_USAGES_F_PK | DIR_REP_CARD_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_REP_CARD_USAGE_ID | NUMBER |  | 18 | Yes | DIR_REP_CARD_USAGE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DIR_REP_CARD_ID | NUMBER |  | 18 |  | DIR_REP_CARD_ID |
| RELATIONSHIP_GROUP_ID | NUMBER |  | 18 | Yes | RELATIONSHIP_GROUP_ID |
| DIR_CARD_COMP_ID | NUMBER |  | 18 |  | DIR_CARD_COMP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_DIR_REP_CARD_USAGES_F_N1 | Non Unique | Default | DIR_REP_CARD_ID |
| PAY_DIR_REP_CARD_USAGES_F_N2 | Non Unique | Default | RELATIONSHIP_GROUP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_REP_CARD_USAGES_F_N3 | Non Unique | Default | DIR_CARD_COMP_ID |
| PAY_DIR_REP_CARD_USAGES_F_PK | Unique | Default | DIR_REP_CARD_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
