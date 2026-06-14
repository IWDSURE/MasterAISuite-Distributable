# PER_CHECKLISTS_TL

PER_CHECKLISTS_TL holds translated information for Checklist Templates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percheckliststl-28853.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percheckliststl-28853.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLISTS_TL_PK | CHECKLIST_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| MESSAGE_SUB_TITLE | VARCHAR2 | 720 |  |  | MESSAGE_SUB_TITLE |
| COMPLETION_MESSAGE | VARCHAR2 | 720 |  |  | COMPLETION_MESSAGE |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 240 |  | Yes | Translated name of Checklist Template |
| DESCRIPTION | VARCHAR2 | 360 |  |  | Translated description of Checklist Template |
| DISPLAY_NAME_FORMAT | VARCHAR2 | 240 |  |  | DISPLAY_NAME_FORMAT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CHECKLIST_DETAILS | CLOB |  |  |  | Checklist Details |
| MESSAGE_TITLE | VARCHAR2 | 400 |  |  | Checklist Message Title |
| MESSAGE_TEXT | VARCHAR2 | 400 |  |  | Checklist MessageText |
| USER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | USER_DISPLAY_NAME |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLISTS_TL_PK | Unique | Default | CHECKLIST_ID, LANGUAGE, ORA_SEED_SET1 |
| PER_CHECKLISTS_TL_PK1 | Unique | Default | CHECKLIST_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
