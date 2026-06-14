# HRC_ATOMPUB_EVT_USAGES

Stores mapping of hrc_evt_handlers and hrc_atompub_collections

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubevtusages-14576.html#hrcatompubevtusages-14576](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubevtusages-14576.html#hrcatompubevtusages-14576)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ATOMPUB_EVT_USAGES_PK | EVENT_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_USAGE_ID | NUMBER |  | 18 | Yes | Uniquely identifies an atom collection event usages row |
| EVENT_HANDLER_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_EVT_HANDLERS.EVENT_HANDLER_ID |
| COLLECTION_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_ATOMPUB_COLLECTIONS.COLLECTION_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| ENABLED_FLAG | VARCHAR2 | 30 |  | Yes | Determines if the Atompub Event Usages entry is enabled or disabled. Valid values are based on the lookup type YES_NO and the default value is Y. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ATOMPUB_EVT_USAGES_N1 | Non Unique | Default | ENTERPRISE_ID |
| HRC_ATOMPUB_EVT_USAGES_N20 | Non Unique | Default | SGUID |
| HRC_ATOMPUB_EVT_USAGES_U1 | Unique | Default | EVENT_USAGE_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_EVT_USAGES_U11 | Unique | Default | EVENT_USAGE_ID, ORA_SEED_SET2 |
| HRC_ATOMPUB_EVT_USAGES_U2 | Unique | Default | EVENT_HANDLER_ID, COLLECTION_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_EVT_USAGES_U21 | Unique | Default | EVENT_HANDLER_ID, COLLECTION_ID, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
