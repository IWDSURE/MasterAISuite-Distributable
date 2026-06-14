# IRC_DESCRIPTIONS_TL_

Translation Table for Description Library

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescriptionstl-30064.html#ircdescriptionstl-30064](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescriptionstl-30064.html#ircdescriptionstl-30064)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DESCRIPTIONS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DESCRIPTION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESCRIPTION_ID | NUMBER |  | 18 | Yes | Primary key for this entity. System generated. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  |  | Name of the description, used when selecting a description within a LOV. |
| INTERACTION_CONTENT | CLOB |  |  |  | This field contains the interaction content to be captured |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | This column contains the Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DESCRIPTIONS_TLN1_ | Non Unique | FUSION_TS_SEED | DESCRIPTION_ID, LANGUAGE, LAST_UPDATE_DATE |
| IRC_DESCRIPTIONS_TL_PK_ | Unique | FUSION_TS_SEED | LAST_UPDATE_DATE, LAST_UPDATED_BY, DESCRIPTION_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
