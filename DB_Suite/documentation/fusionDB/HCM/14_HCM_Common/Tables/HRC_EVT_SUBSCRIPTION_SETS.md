# HRC_EVT_SUBSCRIPTION_SETS

A Subscription Set groups a set of Internal Event handlers and associates them with one or more context rules for the purposes of determining whether the Event handler should actually be processed.
If an event handler is in a subscription set then the context rule must be satisfied before the event handler is processed.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtsubscriptionsets-17767.html#hrcevtsubscriptionsets-17767](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtsubscriptionsets-17767.html#hrcevtsubscriptionsets-17767)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_SUBSCRIP_SETS_PK | SUBSCRIPTION_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBSCRIPTION_SET_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| NAME | VARCHAR2 | 80 |  | Yes | Name of the Subscription Set |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| HRC_EVT_SUBSCRIPTION_SETS_N20 | Non Unique | Default | SGUID |
| HRC_EVT_SUBSCRIP_SETS_F1 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID |
| HRC_EVT_SUBSCRIP_SETS_N1 | Non Unique | Default | UPPER("NAME") |
| HRC_EVT_SUBSCRIP_SETS_PK | Unique | FUSION_TS_TX_DATA | SUBSCRIPTION_SET_ID, ORA_SEED_SET1 |
| HRC_EVT_SUBSCRIP_SETS_PK1 | Unique | FUSION_TS_TX_DATA | SUBSCRIPTION_SET_ID, ORA_SEED_SET2 |
| HRC_EVT_SUBSCRIP_SETS_U1 | Unique | FUSION_TS_TX_DATA | NAME, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_EVT_SUBSCRIP_SETS_U11 | Unique | FUSION_TS_TX_DATA | NAME, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
