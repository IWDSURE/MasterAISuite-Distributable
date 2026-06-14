# IRC_LC_ACTION_USAGES_B

IRC_STEP_ACTION_USAGES_B table stores all configured actions for the given step of lifecycle.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcactionusagesb-11017.html#irclcactionusagesb-11017](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcactionusagesb-11017.html#irclcactionusagesb-11017)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_ACTION_USAGES_B_PK | STEP_ACTION_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | STEP ACTION USAGE ID : Primary key for the table |  |
| TRACE_LOG | CLOB |  |  |  | Lifecycle API internal data for troubleshooting purposes. |  |
| LAST_EXECUTION_RESULT | VARCHAR2 | 128 |  |  | LAST_EXECUTION_RESULT : stores the result of last execution action |  |
| STEP_ACTION_USAGE_CODE | VARCHAR2 | 256 |  |  | ACTION_CODE : Action code corresponding to the action configured for given step |  |
| TRIGGER_EVENT_CODE | VARCHAR2 | 42 |  |  | Event that will trigger action execution |  |
| ROUTING_STEP_ID | NUMBER |  | 18 | Yes | Step ID : Step ID  corresponding to the  given step  configured |  |
| ACTION_ID | NUMBER |  | 18 | Yes | ACTION_ID: Action ID  corresponding to the action configured for given step |  |
| SETTING_ID | NUMBER |  | 18 |  | FK to IRC_LC_SETTINGS table. Setting object holding action configuration. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| LAST_EXECUTION_DATE | TIMESTAMP |  |  |  | LAST_EXECUTION_DATE : Timestamp of last triggered action for the given step |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_ACTION_USAGES_B_N1 | Non Unique | Default | ACTION_ID |
| IRC_LC_ACTION_USAGES_B_N2 | Non Unique | Default | ROUTING_STEP_ID |
| IRC_LC_ACTION_USAGES_B_N3 | Non Unique | Default | STEP_ACTION_USAGE_CODE |
| IRC_LC_ACTION_USAGES_B_N4 | Non Unique | Default | SETTING_ID |
| IRC_LC_ACTION_USAGES_B_U1 | Unique | Default | STEP_ACTION_USAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
