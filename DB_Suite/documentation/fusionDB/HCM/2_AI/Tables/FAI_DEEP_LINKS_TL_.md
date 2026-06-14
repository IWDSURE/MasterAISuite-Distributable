# FAI_DEEP_LINKS_TL_

This table stores the name, description and message of a deep link in different languages.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faideeplinkstl-4933.html#faideeplinkstl-4933](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faideeplinkstl-4933.html#faideeplinkstl-4933)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_DEEP_LINKS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DEEP_LINK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEEP_LINK_ID | NUMBER |  | 18 | Yes | Foreign Key to the base table FAI_DEEP_LINKS_B. Part of the primary key. |
| NAME | VARCHAR2 | 200 |  |  | The translatable name of the deep link. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The translatable description of the deep link. |
| MESSAGE | VARCHAR2 | 4000 |  |  | The translatable message of the deep link. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_DEEP_LINKS_TLN1_ | Non Unique | Default | DEEP_LINK_ID, LANGUAGE |
| FAI_DEEP_LINKS_TLU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DEEP_LINK_ID, LANGUAGE |

---

[← Back to Index](../2_AI_Tables_Index.md)
