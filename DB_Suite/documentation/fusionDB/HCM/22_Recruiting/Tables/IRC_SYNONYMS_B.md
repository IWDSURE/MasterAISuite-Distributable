# IRC_SYNONYMS_B

Stores all the synonyms that can be used in chatbot.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsynonymsb-27866.html#ircsynonymsb-27866](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsynonymsb-27866.html#ircsynonymsb-27866)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SYNONYMS_B_PK | SYNONYM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SYNONYM_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| TYPE | VARCHAR2 | 100 |  | Yes | Stores a synonym type like locations acronyms of the synonym. |
| SYNONYM_CODE | VARCHAR2 | 200 |  | Yes | Stores a unique code of the synonym. |
| SYNONYM_NAME | VARCHAR2 | 1000 |  |  | Stores a fully qualified name of the synonym. |
| FA_REFERENCE | VARCHAR2 | 1000 |  |  | Stores comma separated fa reference codes of the synonym. |
| OBJECT_STATUS | VARCHAR2 | 120 |  |  | Stores a status code of the synonym. |
| ADDITIONAL_VALUE | VARCHAR2 | 1000 |  |  | Stores a any additional value of the synonym. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SYNONYMS_B_N1 | Non Unique | Default | TYPE, OBJECT_STATUS |
| IRC_SYNONYMS_B_PK | Unique | Default | SYNONYM_ID, ORA_SEED_SET1 |
| IRC_SYNONYMS_B_PK1 | Unique | Default | SYNONYM_ID, ORA_SEED_SET2 |
| IRC_SYNONYMS_B_U1 | Unique | Default | TYPE, SYNONYM_CODE, ORA_SEED_SET1 |
| IRC_SYNONYMS_B_U11 | Unique | Default | TYPE, SYNONYM_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
