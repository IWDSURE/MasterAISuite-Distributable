# IRC_DESCRIPTIONS_B

Base table for description library

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescriptionsb-16007.html#ircdescriptionsb-16007](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescriptionsb-16007.html#ircdescriptionsb-16007)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DESCRIPTIONS_B_PK | DESCRIPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESCRIPTION_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| USE_NO_REPLY_FLAG | VARCHAR2 | 1 |  |  | Stores the flag for whether no-reply or vanity email should be used for the category. |
| DESCRIPTION_CODE | VARCHAR2 | 30 |  |  | Unique code for the description. |
| DESCRIPTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Description type based on lookup. The corresponding lookup type is ORA_IRC_DESCRIPTION_TYPE. |
| VISIBILITY_CODE | VARCHAR2 | 30 |  | Yes | Visibility of this description based on lookup. The corresponding lookup type is ORA_IRC_PUBLISHED_JOB_TYPE. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Status of this description based on lookup. The corresponding lookup type is ORA_IRC_DESCRIPTION_STATUS. |
| COLLABORATOR_RESP_TYPE_LIST | VARCHAR2 | 1000 |  |  | Stores the list of all collaborator responsibility types (ORA_IRC_COLLABORATOR_RESP_TYPE lookup values) that are set on the template level. |
| CAPTURE_INTERACTION | VARCHAR2 | 1 |  | Yes | This field describes if the interaction will be captured for this content library item |
| MESSAGE_TRACKING_START_DATE | TIMESTAMP |  |  |  | The timestamp when the message tracking was enabled |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DESCRIPTIONS_B_N1 | Non Unique | Default | DESCRIPTION_TYPE_CODE, STATUS_CODE |
| IRC_DESCRIPTIONS_B_PK | Unique | FUSION_TS_SEED | DESCRIPTION_ID, ORA_SEED_SET1 |
| IRC_DESCRIPTIONS_B_PK1 | Unique | FUSION_TS_SEED | DESCRIPTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
