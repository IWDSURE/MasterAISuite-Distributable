# IRC_DESC_VERSIONS_TL_

Translation table for versions of description library items

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescversionstl-11668.html#ircdescversionstl-11668](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdescversionstl-11668.html#ircdescversionstl-11668)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DESC_VERSIONS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DESC_VERSION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESC_VERSION_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| DESCRIPTION | CLOB |  |  |  | The actual html text content of this description library item. |
| QUALIFICATIONS | CLOB |  |  |  | The actual html text content of qualifications of this description library item. |
| RESPONSIBILITIES | CLOB |  |  |  | The actual html text content of responsibilities of this description library item. |
| SHORT_DESCRIPTION | CLOB |  |  |  | The alternate html text content of this library item |
| TXT_DESCRIPTION | CLOB |  |  |  | The alternate raw text content of this library item |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DESC_VERSIONS_TLN1_ | Non Unique | FUSION_TS_SEED | DESC_VERSION_ID, LANGUAGE, LAST_UPDATE_DATE |
| IRC_DESC_VERSIONS_TL_U1_ | Unique | FUSION_TS_SEED | LAST_UPDATE_DATE, LAST_UPDATED_BY, DESC_VERSION_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
