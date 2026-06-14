# HRC_EVT_CONTEXT_RULES

A Context Rule is used to qualify a Subscription Set and defines the context value(s) that will cause the Subscription Set's event handlers to be processed. It is possible to define a context value as either Included or Excluded; if the value is included then if the Source Object's Context value matches the Context Rule the Event handler will be processed, whilst if the value is Excluded, then the Event handler will be processed as long as the event object's context does not match the excluded value.

When there are multiple context rules for a subscription set the Included values are combined using an OR clause and the Excluded values are combined using an AND clause
e.g. (Context = 'A' OR Context = 'B') AND (Context <> 'X' AND Context <> 'Y')

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtcontextrules-3373.html#hrcevtcontextrules-3373](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtcontextrules-3373.html#hrcevtcontextrules-3373)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_CONTEXT_RULES_PK | CONTEXT_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEXT_RULE_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| SUBSCRIPTION_SET_ID | NUMBER |  | 18 | Yes | Unique Identifier of Subscription Set |
| CONTEXT_TYPE | VARCHAR2 | 30 |  | Yes | Context Type |
| CONTEXT_VALUE_N | NUMBER |  | 18 |  | Numeric Context Value |
| CONTEXT_VALUE_D | DATE |  |  |  | Date Context Value |
| CONTEXT_VALUE_V | VARCHAR2 | 80 |  |  | Varchar Context Value |
| INCLUDE_EXCLUDE | VARCHAR2 | 30 |  | Yes | Indication of whether the context should be present or not |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_CONTEXT_RULES_N20 | Non Unique | Default | SGUID |
| HRC_EVT_CONTEXT_RULES_PK | Unique | FUSION_TS_TX_DATA | CONTEXT_RULE_ID, ORA_SEED_SET1 |
| HRC_EVT_CONTEXT_RULES_PK1 | Unique | FUSION_TS_TX_DATA | CONTEXT_RULE_ID, ORA_SEED_SET2 |
| HRC_EVT_CONTEXT_RULES_U1 | Unique | FUSION_TS_TX_DATA | SUBSCRIPTION_SET_ID, CONTEXT_TYPE, CONTEXT_VALUE_N, CONTEXT_VALUE_D, CONTEXT_VALUE_V, ORA_SEED_SET1 |
| HRC_EVT_CONTEXT_RULES_U11 | Unique | FUSION_TS_TX_DATA | SUBSCRIPTION_SET_ID, CONTEXT_TYPE, CONTEXT_VALUE_N, CONTEXT_VALUE_D, CONTEXT_VALUE_V, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
