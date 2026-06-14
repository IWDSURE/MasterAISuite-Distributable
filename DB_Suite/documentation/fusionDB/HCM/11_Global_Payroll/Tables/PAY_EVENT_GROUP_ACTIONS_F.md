# PAY_EVENT_GROUP_ACTIONS_F

This table links the Actions to the Event Groups to identify the Actions that will be performed when an Event is detected.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventgroupactionsf-23521.html#payeventgroupactionsf-23521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventgroupactionsf-23521.html#payeventgroupactionsf-23521)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_GROUP_ACTIONS_F_PK | EVENT_GROUP_ACTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_GROUP_ACTION_ID | NUMBER |  | 18 | Yes | EVENT_GROUP_ACTION_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to Pay Event Groups |
| EVENT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to Pay Event Actions |
| DEL_TIME_DEF_ID | NUMBER |  | 18 | Yes | Foreign Key to Time Definitions. This indicates how far back events need to be kept for. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_EVENT_GROUP_ACTIONS_F_PK | Unique | Default | EVENT_GROUP_ACTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_EVENT_GROUP_ACTIONS_F_PK1 | Unique | Default | EVENT_GROUP_ACTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_EVENT_GRP_ACTN_F_SGUID_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_EVT_GROUP_ACTIONS_F_N1 | Non Unique | Default | EVENT_GROUP_ID |
| PAY_EVT_GROUP_ACTIONS_F_N2 | Non Unique | Default | EVENT_ACTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
