# IRC_BOT_JOB_KEYWORDS

This table contains data required for irc chatbot job keywords

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbotjobkeywords-21857.html#ircbotjobkeywords-21857](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbotjobkeywords-21857.html#ircbotjobkeywords-21857)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BOT_JOB_KEYWORDS_PK | KEYWORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEYWORD_ID | NUMBER |  | 18 | Yes | Primary key for this table. System Generated |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CANONICAL_NAME | VARCHAR2 | 512 |  | Yes | Stores the value for the keyword defined by the user |
| KEYWORD_CODE | VARCHAR2 | 64 |  | Yes | KEYWORD_CODE |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BOT_JOB_KEYWORDS_U1 | Unique | FUSION_TS_SEED | KEYWORD_ID, ORA_SEED_SET1 |
| IRC_BOT_JOB_KEYWORDS_U11 | Unique | FUSION_TS_SEED | KEYWORD_ID, ORA_SEED_SET2 |
| IRC_BOT_JOB_KEYWORDS_U2 | Unique | FUSION_TS_SEED | KEYWORD_CODE, ORA_SEED_SET1 |
| IRC_BOT_JOB_KEYWORDS_U21 | Unique | FUSION_TS_SEED | KEYWORD_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
