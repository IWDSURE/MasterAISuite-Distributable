# PER_ALLOCATED_CHECKLISTS_TL_

PER_ALLOCATED_CHECKLISTS_TL : This is translation table for PER_ALLOCATED_CHECKLISTS

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocatedcheckliststl-15958.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocatedcheckliststl-15958.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOCATED_CHK_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ALLOCATED_CHECKLIST_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 | Yes | ALLOCATED_CHECKLIST_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| MESSAGE_SUB_TITLE | VARCHAR2 | 720 |  |  | MESSAGE_SUB_TITLE |
| COMPLETION_MESSAGE | VARCHAR2 | 720 |  |  | COMPLETION_MESSAGE |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CHECKLIST_NAME | VARCHAR2 | 240 |  |  | NAME |
| CHECKLIST_DISPLAY_NAME | VARCHAR2 | 4000 |  |  | CHECKLIST_DISPLAY_NAME |
| DESCRIPTION | VARCHAR2 | 360 |  |  | DESCRIPTION |
| MESSAGE_TITLE | VARCHAR2 | 400 |  |  | MESSAGE_TITLE |
| MESSAGE_TEXT | VARCHAR2 | 400 |  |  | MESSAGE_TEXT |
| USER_DISPLAY_NAME | VARCHAR2 | 240 |  |  | USER_DISPLAY_NAME |
| CHECKLIST_DETAILS | CLOB |  |  |  | CHECKLIST_DETAILS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ALLOCATED_CHECKLISTSN1_ | Non Unique | Default | ALLOCATED_CHECKLIST_ID, LANGUAGE, LAST_UPDATE_DATE |
| PER_ALLOCATED_CHK_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ALLOCATED_CHECKLIST_ID, LANGUAGE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
