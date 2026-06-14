# IRC_DESC_VERSIONS_B_

Base table for versions of description library items

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescversionsb-27110.html#ircdescversionsb-27110](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescversionsb-27110.html#ircdescversionsb-27110)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DESC_VERSIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DESC_VERSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESC_VERSION_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| DESCRIPTION_ID | NUMBER |  | 18 |  | Description library item to which this version is related. Foreign key to IRC_DESCRIPTIONS_B table. |
| VERSION_START_DATE | TIMESTAMP |  |  |  | Stores the date/time from which this description version is effective. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of this description version based on lookup. The corresponding lookup type is ORA_IRC_DESC_VERSION_STATUS. |
| WA_TEMPLATE_ID | NUMBER |  | 18 |  | Id of the WhatsApp template associated with the current content version. Foreign key to irc_whatsapp_template_b |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_ID | NUMBER |  | 18 |  | The primary key of the object to which the current content library item is related. |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | The type of object to which the current content library item is related. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DESC_VERSIONS_BN1_ | Non Unique | Default | DESC_VERSION_ID |
| IRC_DESC_VERSIONS_B_U1_ | Unique | FUSION_TS_SEED | LAST_UPDATE_DATE, LAST_UPDATED_BY, DESC_VERSION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
