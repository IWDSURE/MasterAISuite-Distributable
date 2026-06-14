# IRC_PROCESSES_B

This table stores all the processes and their definitions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircprocessesb-27383.html#ircprocessesb-27383](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircprocessesb-27383.html#ircprocessesb-27383)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PROCESSES_B_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| PROCESS_TEMPLATE_ID | NUMBER |  | 18 |  | Id of the process template (for process instances) |
| GRAPH_TOPOLOGY | VARCHAR2 | 30 |  |  | Store process graph topology. Valaues for graphs automatically generated are :  FORWARD_ONLY and STRONGLY_CONNECTED.  CUSTOM to use for any module specific Process graph. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the status code of the process. |
| PHASE_ID | NUMBER |  | 18 |  | Used to store a PhaseId when needed. |
| CODE | VARCHAR2 | 256 |  |  | Stores the code for the process. |
| SETTING_ID | NUMBER |  | 18 |  | Used to point to a setting Id when needed. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the type of the process as a lookup code. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| USAGE_CODE | VARCHAR2 | 30 |  |  | Types the process "TEMPLATE", "TEMPLATE-SYSTEM"  or "INSTANCE" |
| IS_ACTIVE_FLAG | VARCHAR2 | 1 |  | Yes | Only an active process template can be used for submission progress (instance created from) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| TRACE_LOG | CLOB |  |  |  | Lifecycle API internal data for troubleshooting purposes |
| IMPORT_CONTROL_FLAG | VARCHAR2 | 1 |  |  | Used to discriminates a process currently being imported or already present in the database. |
| SUPPRESS_CANDIDATE_NOTIF_FLAG | VARCHAR2 | 1 |  |  | Suppress the candidate notifications associated with this Candidate Selection Process |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| SHOW_MOVE_FORWARD_FLAG | VARCHAR2 | 1 |  |  | Display the move forward action in the job application associated with this Candidate Selection Process |
| SHOW_QUICK_REJECT_FLAG | VARCHAR2 | 1 |  |  | Display the quick reject action in the job application associated with this Candidate Selection Process |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PROCESSES_B_FK1 | Non Unique | FUSION_TS_SEED | PHASE_ID |
| IRC_PROCESSES_B_FK2 | Non Unique | Default | SETTING_ID |
| IRC_PROCESSES_B_N1 | Non Unique | Default | USAGE_CODE, TYPE_CODE, STATUS_CODE |
| IRC_PROCESSES_B_N2 | Non Unique | FUSION_TS_SEED | IMPORT_CONTROL_FLAG |
| IRC_PROCESSES_B_PK | Unique | FUSION_TS_SEED | PROCESS_ID, ORA_SEED_SET1 |
| IRC_PROCESSES_B_PK1 | Unique | FUSION_TS_SEED | PROCESS_ID, ORA_SEED_SET2 |
| IRC_PROCESSES_B_U1 | Unique | FUSION_TS_SEED | CODE, TYPE_CODE, ORA_SEED_SET1 |
| IRC_PROCESSES_B_U11 | Unique | FUSION_TS_SEED | CODE, TYPE_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
