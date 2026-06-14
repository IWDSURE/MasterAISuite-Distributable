# IRC_ROUTING_STEPS_B

This table stores all the routing steps involved in a process

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircroutingstepsb-25797.html#ircroutingstepsb-25797](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircroutingstepsb-25797.html#ircroutingstepsb-25797)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ROUTING_STEPS_B_PK | ROUTING_STEP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROUTING_STEP_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the type of the routing as a a lookup code. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_PROCESSES_B table. |
| SEQUENCE_NUMBER | NUMBER |  | 9 |  | Determine the sequence number of the step whitin the immediate parent process |
| SUB_PROCESS_ID | NUMBER |  | 18 |  | Foreign keyto IRC_PROCESSES_B table. Stores the reference to the sub process within a process. |
| PHASE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PHASES_B table. |
| STATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_STATES_B table. |
| PUBLIC_STATE_ID | NUMBER |  | 18 |  | PUBLIC_STATE_ID |
| IS_INITIAL_FLAG | VARCHAR2 | 1 |  | Yes | Indicates that this routing step it's the initial one (used for routing of type state) |
| IS_COMPLETION_FLAG | VARCHAR2 | 1 |  | Yes | Indicates that this routing step marks phase as completed (used for routing of type state) |
| LAST_ACTIVATION_DATE | TIMESTAMP |  |  |  | Date when the step has been activated |
| LAST_DEACTIVATION_DATE | TIMESTAMP |  |  |  | Date when a step has been deactivated |
| STEP_STATUS | VARCHAR2 | 30 |  |  | Value from FND lookup, will determinate the status of the step (Active / Inactive ... ) |
| STEP_TEMPLATE_ID | NUMBER |  | 18 |  | Field used by the instance to know from which step it has been instantiated. |
| SETTING_ID | NUMBER |  | 18 |  | Points to a setting id when needed, this value will be the same for the step instance and for the step template. |
| CODE | VARCHAR2 | 60 |  |  | Identifies a step uniquely among all other steps sharing a same processId |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_ROUTING_STEPS_B_FK1 | Non Unique | FUSION_TS_SEED | PROCESS_ID |  |
| IRC_ROUTING_STEPS_B_FK2 | Non Unique | FUSION_TS_SEED | SUB_PROCESS_ID | Obsolete |
| IRC_ROUTING_STEPS_B_FK3 | Non Unique | FUSION_TS_SEED | PHASE_ID |  |
| IRC_ROUTING_STEPS_B_FK4 | Non Unique | FUSION_TS_SEED | STATE_ID |  |
| IRC_ROUTING_STEPS_B_FK5 | Non Unique | FUSION_TS_SEED | SETTING_ID |  |
| IRC_ROUTING_STEPS_B_N1 | Non Unique | FUSION_TS_SEED | SUB_PROCESS_ID, PROCESS_ID |  |
| IRC_ROUTING_STEPS_B_PK | Unique | FUSION_TS_SEED | ROUTING_STEP_ID, ORA_SEED_SET1 |  |
| IRC_ROUTING_STEPS_B_PK1 | Unique | FUSION_TS_SEED | ROUTING_STEP_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
