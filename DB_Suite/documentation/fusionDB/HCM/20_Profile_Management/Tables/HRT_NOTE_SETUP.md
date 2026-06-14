# HRT_NOTE_SETUP

This table stores the list of setup for Notes.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtnotesetup-17135.html#hrtnotesetup-17135](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtnotesetup-17135.html#hrtnotesetup-17135)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_NOTE_SETUP_PK | NOTE_SETUP_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTE_SETUP_ID | NUMBER |  | 18 | Yes | Primary Key. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Source Object Type of the object against which the note is created. |
| CONTEXT_TYPE | VARCHAR2 | 30 |  |  | CONTEXT_TYPE |
| OBJECT_CONTEXT_LOOKUP_CODE | VARCHAR2 | 30 |  |  | OBJECT_CONTEXT_LOOKUP_CODE |
| DEFAULT_NOTE_VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Default Note Visibility code.  Null or blank indicates that there is no default visibility code. |
| ALL_FLAG | VARCHAR2 | 1 |  |  | Flag to include ALL in the visibility code. |
| MANAGERS_FLAG | VARCHAR2 | 1 |  |  | Flag to include Manager Only in the visibility code. |
| MANAGERS_AND_SUBJECT_FLAG | VARCHAR2 | 1 |  |  | Flag to include Managers and Subject in the visibility code. |
| PRIVATE_FLAG | VARCHAR2 | 1 |  |  | Flag to include Private in the visibility code. |
| SUBJECT_FLAG | VARCHAR2 | 1 |  |  | Flag to include Subject in the visibility code. |
| MANAGERS_SUBJECT_PEERS_FLAG | VARCHAR2 | 1 |  |  | Flag to include Managers,Subject and Peers in the visibility code. |
| NOTIFICATION_MANAGER_TYPE_LIST | VARCHAR2 | 1000 |  |  | List of manager types to be notified for anytime feedback. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_NOTE_SETUP_U1 | Unique | FUSION_TS_TX_DATA | NOTE_SETUP_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRT_NOTE_SETUP_U11 | Unique | FUSION_TS_TX_DATA | NOTE_SETUP_ID, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
