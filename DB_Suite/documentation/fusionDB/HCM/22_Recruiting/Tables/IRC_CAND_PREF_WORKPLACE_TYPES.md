# IRC_CAND_PREF_WORKPLACE_TYPES

Table used for storing Workplace type preferences for candidates

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandprefworkplacetypes-7010.html#irccandprefworkplacetypes-7010](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandprefworkplacetypes-7010.html#irccandprefworkplacetypes-7010)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_PREF_WPLC_TYPES_PK | PREF_WORKPLACE_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREF_WORKPLACE_TYPE_ID | NUMBER |  | 18 | Yes | This column represents primary key for the table "irc_cand_pref_workplace_types" |
| CAND_PREF_ID | NUMBER |  | 18 | Yes | Foreign Key to CAND_PREF_ID column of table 'irc_cand_preferences' |
| WORKPLACE_TYPE_CODE | VARCHAR2 | 32 |  |  | Used to store candidate workplace type preference. Contains Lookup codes of Look up Type "ORA_IRC_WORKPLACE_TYPE". |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_PREF_WPLC_TYPES_FK1 | Non Unique | Default | CAND_PREF_ID |
| IRC_CAND_PREF_WPLC_TYPES_PK | Unique | Default | PREF_WORKPLACE_TYPE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
