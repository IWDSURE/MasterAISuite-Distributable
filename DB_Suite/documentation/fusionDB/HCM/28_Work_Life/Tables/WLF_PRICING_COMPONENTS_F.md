# WLF_PRICING_COMPONENTS_F

Table to store Pricing Components.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpricingcomponentsf-17633.html#wlfpricingcomponentsf-17633](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpricingcomponentsf-17633.html#wlfpricingcomponentsf-17633)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PRICING_COMPONENTS_F_PK | PRICING_COMPONENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRICING_COMPONENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PRICING_COMPONENT_NUMBER | VARCHAR2 | 30 |  |  | PRICING_COMPONENT_NUMBER |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PRICING_RULE_ID | NUMBER |  | 18 | Yes | Identifier of pricing rule. Foreign key to WLF_PRICING_RULES_F. |
| PRICE | NUMBER |  |  |  | Indicates price of pricing component. |
| PRICING_TYPE | VARCHAR2 | 30 |  |  | Indicates pricing component type. |
| IS_REQUIRED | VARCHAR2 | 1 |  |  | Indicates if component is required when inherited. |
| USED_IN_CALC | VARCHAR2 | 1 |  |  | Indicates if component price should be used for price calculation. |
| IS_ADJUSTMENT | VARCHAR2 | 1 |  |  | Indicates whether component is adjusted. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PRICING_COMPONENTS_F_N1 | Non Unique | Default | PRICING_COMPONENT_NUMBER |
| WLF_PRICING_COMPONENTS_F_N2 | Non Unique | Default | PRICING_RULE_ID |
| WLF_PRICING_COMPONENTS_F_U1 | Unique | Default | PRICING_COMPONENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
