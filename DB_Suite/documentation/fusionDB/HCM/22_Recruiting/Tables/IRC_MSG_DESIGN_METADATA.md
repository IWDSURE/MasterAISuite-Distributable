# IRC_MSG_DESIGN_METADATA

Stores the design metadata of the email design.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmsgdesignmetadata-23747.html#ircmsgdesignmetadata-23747](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmsgdesignmetadata-23747.html#ircmsgdesignmetadata-23747)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MSG_DESIGN_METADATA_PK | MESSAGE_DESIGN_ID, MESSAGE_LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_DESIGN_ID | NUMBER |  | 18 | Yes | Part of the primary Key of the table. System Generated. |
| MESSAGE_LANGUAGE | VARCHAR2 | 4 |  | Yes | Part of the primary key of the table. Stores the language in which the email is designed |
| DEFAULT_LANGUAGE_FLAG | VARCHAR2 | 1 |  |  | Stores whether this design is the design for the default language. |
| SUBJECT | VARCHAR2 | 1000 |  |  | Stores the subject of the email |
| DESCRIPTION | CLOB |  |  |  | Stores description for the landing page |
| IMAGE_URL | VARCHAR2 | 1000 |  |  | Stores location of the thumbnail url for the landing page |
| DESIGN_METADATA | CLOB |  |  |  | Stores the email design metadata in JSON format. |
| HTML_TEMPLATE | CLOB |  |  |  | Stores the HTML template that should be used for sending emails |
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
| IRC_MSG_DESIGN_METADATA_U1 | Unique | Default | MESSAGE_DESIGN_ID, MESSAGE_LANGUAGE, ORA_SEED_SET1 |
| IRC_MSG_DESIGN_METADATA_U11 | Unique | Default | MESSAGE_DESIGN_ID, MESSAGE_LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
