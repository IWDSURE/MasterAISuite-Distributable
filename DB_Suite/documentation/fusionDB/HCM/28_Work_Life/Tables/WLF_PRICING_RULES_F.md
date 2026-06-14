# WLF_PRICING_RULES_F

Table to store Pricing Rules information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpricingrulesf-22547.html#wlfpricingrulesf-22547](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpricingrulesf-22547.html#wlfpricingrulesf-22547)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PRICING_RULES_F_PK | PRICING_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRICING_RULE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PRICING_RULE_NUMBER | VARCHAR2 | 30 |  |  | PRICING_RULE_NUMBER |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| TOTAL_PRICE | NUMBER |  |  |  | Indicates the total cost of the pricing rule. |
| CURRENCY | VARCHAR2 | 30 |  |  | Indicates the currency type of the price. |
| LEARNING_ITEM_TYPE | VARCHAR2 | 32 |  |  | Indicates the type of learning item for which pricing is set. |
| DELIVERY_MODE | VARCHAR2 | 32 |  |  | Indicates the delivery mode of learning item for which pricing is set. |
| USAGE | VARCHAR2 | 32 |  |  | Polymorphic discriminator column {ORA_SETTINGS,ORA_COURSE... }. |
| USES_PRICING | VARCHAR2 | 1 |  |  | Indicates whether pricing is used or not. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PAYMENT_TYPE | VARCHAR2 | 30 |  |  | Indicates the payment typeof learning item. |
| REFUND_TYPE | VARCHAR2 | 30 |  |  | Indicates refund type for the payment. |
| REFUND_ON_WITHDRAWAL_ENABLED | VARCHAR2 | 1 |  |  | Indicates if refund on withdrawal is enabled. |
| IS_PO_REQUIRED | VARCHAR2 | 30 |  |  | Indicates if purchase order is required. |
| RFND_ON_WITHDRAW_ENA_SP | VARCHAR2 | 1 |  |  | Indicates if refund on withdrawal is enabled for self paced offering. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PRICING_RULES_F_N1 | Non Unique | Default | PRICING_RULE_NUMBER |
| WLF_PRICING_RULES_F_U1 | Unique | Default | PRICING_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
