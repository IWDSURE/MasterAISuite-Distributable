# PER_CHECKLISTS_TL_

PER_CHECKLISTS_TL holds translated information for Checklist Templates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percheckliststl-15022.html#percheckliststl-15022](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percheckliststl-15022.html#percheckliststl-15022)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLISTS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, CHECKLIST_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| MESSAGE_SUB_TITLE | VARCHAR2 | 720 |  |  | MESSAGE_SUB_TITLE |
| COMPLETION_MESSAGE | VARCHAR2 | 720 |  |  | COMPLETION_MESSAGE |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 240 |  |  | Translated name of Checklist Template |
| DESCRIPTION | VARCHAR2 | 360 |  |  | Translated description of Checklist Template |
| DISPLAY_NAME_FORMAT | VARCHAR2 | 240 |  |  | DISPLAY_NAME_FORMAT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CHECKLIST_DETAILS | CLOB |  |  |  | Checklist Details |
| MESSAGE_TITLE | VARCHAR2 | 400 |  |  | Checklist Message Title |
| MESSAGE_TEXT | VARCHAR2 | 400 |  |  | Checklist MessageText |
| USER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | USER_DISPLAY_NAME |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PCTN1_ | Non Unique | Default | CHECKLIST_ID, LANGUAGE, LAST_UPDATE_DATE |
| PER_CHECKLISTS_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, CHECKLIST_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
