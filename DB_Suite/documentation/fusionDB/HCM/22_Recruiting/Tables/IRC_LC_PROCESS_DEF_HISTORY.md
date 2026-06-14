# IRC_LC_PROCESS_DEF_HISTORY

Stores the process history tracking data.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcprocessdefhistory-27382.html#irclcprocessdefhistory-27382](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcprocessdefhistory-27382.html#irclcprocessdefhistory-27382)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_PROCESS_DEF_HISTORY_PK | PROCESS_DEF_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_DEF_HISTORY_ID | NUMBER |  | 18 | Yes | The primary key for this table |
| PROCESS_ID | NUMBER |  | 18 | Yes | The process Id associated with the History Event. Foreign Key to IRC_PROCESSES_B table |
| SUB_PROCESS_ID | NUMBER |  | 18 |  | The sub process Id associated with the History Event. Foreign Key to IRC_PROCESSES_B table |
| EVENT_TYPE_ID | NUMBER |  | 18 | Yes | The event type id of the History Event. Foreign Key to IRC_HIST_EVENT_B table |
| EVENT_DATE | TIMESTAMP |  |  | Yes | The event date of the History Event |
| PERSON_ID | NUMBER |  | 18 | Yes | The person Id who performed the History Event. Foreign Key to PER_PERSONS table |
| ROUTING_STEP_ID | NUMBER |  | 18 |  | The routing step Id associated with the History Event. Foreign Key to IRC_ROUTING_STEPS_B table |
| TYPE_CODE | VARCHAR2 | 30 |  |  | The routing step type code associated with the History Event |
| SEQUENCE_NUMBER | NUMBER |  | 9 |  | The routing step sequence number associated with the History Event |
| PHASE_ID | NUMBER |  | 18 |  | The routing step phase Id associated with the History Event. Foreign Key to IRC_PHASES_B table |
| STATE_ID | NUMBER |  | 18 |  | The routing step state Id associated with the History Event. Foreign Key to IRC_STATES_B table |
| ACTION_USAGE_ID | NUMBER |  | 18 |  | The action usage Id associated with the History Event. Foreign Key to IRC_LC_ACTION_USAGES_B table |
| TRIGGER_EVENT_CODE | VARCHAR2 | 42 |  |  | The action usage trigger event code associated with the History Event. |
| SETTING_ID | NUMBER |  | 18 |  | The setting Id associated with the History Event. Foreign Key to IRC_LC_SETTINGS_B table |
| ITEM_KEY_NAME | VARCHAR2 | 50 |  |  | The setting item key name associated with the History Event |
| REF_TYPE_CODE | VARCHAR2 | 60 |  |  | The function expression ref type code associated with the History Event |
| EXPRESSION_REF_ID | NUMBER |  | 18 |  | The expression ref id associated with the History Event. Foreign Key to IRC_FN_EXPRESSION_REFS table |
| VALUE | VARCHAR2 | 1000 |  |  | The value modified by the History Event |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_PROCESS_DEF_HISTORY_FK1 | Non Unique | Default | PROCESS_ID |
| IRC_LC_PROCESS_DEF_HISTORY_PK | Unique | Default | PROCESS_DEF_HISTORY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
