# PER_EXT_ACTIONS

Captures Actions for Data Elements or Records.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextactions-24463.html#perextactions-24463](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextactions-24463.html#perextactions-24463)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_ACTIONS_PK | EXT_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_ACTION_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MSG_APPLICATION_ID | NUMBER |  | 18 |  | The id of the message |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| EXT_DATA_ELEMENT_ID | NUMBER |  | 18 |  | Data Element id for which the action is created |
| REPORT_RECORD_ID | NUMBER |  | 18 |  | Record Id for whicch the action is created |
| SEQUENCE_NUMBER | NUMBER |  | 18 |  | Sequence of the action |
| ACTION_CODE | VARCHAR2 | 30 |  |  | Type of action |
| ACTION_FORMULA_ID | NUMBER |  | 18 |  | Fast Formula Id of the action |
| ACTION_MESSAGE | VARCHAR2 | 30 |  |  | Message used in the action |
| ACTION_CONDITION | VARCHAR2 | 2000 |  |  | The condition expression for the action |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EXT_ACTIONS_N20 | Non Unique | Default | SGUID |
| PER_EXT_ACTIONS_PK | Unique | Default | EXT_ACTION_ID, ORA_SEED_SET1 |
| PER_EXT_ACTIONS_PK1 | Unique | Default | EXT_ACTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
