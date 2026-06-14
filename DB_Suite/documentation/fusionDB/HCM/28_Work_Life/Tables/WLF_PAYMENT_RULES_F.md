# WLF_PAYMENT_RULES_F

Table to store Payment Type values for Pricing Rules.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpaymentrulesf-19935.html#wlfpaymentrulesf-19935](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpaymentrulesf-19935.html#wlfpaymentrulesf-19935)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PAYMENT_RULES_F_PK | PAYMENT_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYMENT_RULE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PAYMENT_TYPE | VARCHAR2 | 30 |  | Yes | Determines the type of payment for pricing rule. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REFUND_TYPE | VARCHAR2 | 30 |  |  | Indicates refund type for the payment. |
| REFUND_ON_WITHDRAWAL_ENABLED | VARCHAR2 | 1 |  |  | Indicates if refund on withdrawal is enabled. |
| IS_PO_REQUIRED | VARCHAR2 | 30 |  |  | Indicates if purchase order is required. |
| RFND_ON_WITHDRAW_ENA_SP | VARCHAR2 | 1 |  |  | Indicates if refund on withdrawal is enabled for self paced offering. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PAYMENT_RULES_F_U1 | Unique | Default | PAYMENT_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
