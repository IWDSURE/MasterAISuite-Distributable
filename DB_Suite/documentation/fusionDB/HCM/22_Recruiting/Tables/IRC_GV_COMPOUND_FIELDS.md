# IRC_GV_COMPOUND_FIELDS

This table stores the fields which comprises of a compound field. For eg :- A Education Compound field can comprise of three fields - Degree , School and Major. This table will store that information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvcompoundfields-13929.html#ircgvcompoundfields-13929](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvcompoundfields-13929.html#ircgvcompoundfields-13929)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GV_COMPOUND_FIELDS_PK | COMPOUND_FIELD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPOUND_FIELD_ID | NUMBER |  | 18 | Yes | Primary key of table. System Generated. |
| COMPOUND_FIELD_CODE | VARCHAR2 | 100 |  | Yes | Foreign Key IRC_GV_FIELDS_B table which will point to FIELD_CODE where the FIELD_TYPE_CODE will be of Compound. |
| ASSOCIATED_FIELD_CODE | VARCHAR2 | 100 |  | Yes | Foreign Key IRC_GV_FIELDS_B table which will point to FIELD_CODE where the FIELD_TYPE_CODE will just be normal field. |
| FIELD_SEQUENCE | NUMBER |  | 2 | Yes | Stores the sequence of the field which is defined for a compound field. |
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
| IRC_GV_COMPOUND_FIELDS_PK | Unique | Default | COMPOUND_FIELD_ID, ORA_SEED_SET1 |
| IRC_GV_COMPOUND_FIELDS_PK1 | Unique | Default | COMPOUND_FIELD_ID, ORA_SEED_SET2 |
| IRC_GV_COMPOUND_FIELDS_U1 | Unique | Default | COMPOUND_FIELD_CODE, ASSOCIATED_FIELD_CODE, ORA_SEED_SET1 |
| IRC_GV_COMPOUND_FIELDS_U11 | Unique | Default | COMPOUND_FIELD_CODE, ASSOCIATED_FIELD_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
