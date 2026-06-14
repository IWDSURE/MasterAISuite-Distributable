# IRC_LC_ACTIONS_B

IRC_LIFE_CYCLE_ACTIONS_B table stores all available actions for the process lifecycle.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcactionsb-10823.html#irclcactionsb-10823](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcactionsb-10823.html#irclcactionsb-10823)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_ACTIONS_B_PK | ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | Unique ACTION ID to identify a specific action in the table. Primary Key |
| OBJECT_STATUS | VARCHAR2 | 18 |  |  | OBJECT_STATUS : in order to support any soft delete of records in future |
| TYPE_CODE | VARCHAR2 | 120 |  | Yes | TYPE CODE : Configuration set up type code value |
| ACTION_CODE | VARCHAR2 | 256 |  | Yes | Unique ACTION CODE to identify a specific action |
| ACTION_TYPE | VARCHAR2 | 120 |  | Yes | ACTION TYPE : whether its manual or configured action |
| ACTION_SETUP_CLASS_NAME | VARCHAR2 | 120 |  |  | Class name of action setup that has the configuration code |
| ACTION_EXEC_CLASS_NAME | VARCHAR2 | 120 |  |  | Class name of consuming application that are called through external task flow |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ASYNC_ENABLED | VARCHAR2 | 1 |  |  | Indicates if the action is asynchronous. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_ACTIONS_B_U1 | Unique | FUSION_TS_SEED | ACTION_CODE, ORA_SEED_SET1 |
| IRC_LC_ACTIONS_B_U11 | Unique | FUSION_TS_SEED | ACTION_CODE, ORA_SEED_SET2 |
| IRC_LC_ACTIONS_B_U2 | Unique | FUSION_TS_SEED | ACTION_ID, ORA_SEED_SET1 |
| IRC_LC_ACTIONS_B_U21 | Unique | FUSION_TS_SEED | ACTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
