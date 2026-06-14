# FAI_WORKFLOWS_TL_

Translated attributes for Workflows.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowstl-21342.html#faiworkflowstl-21342](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowstl-21342.html#faiworkflowstl-21342)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_WORKFLOWS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORKFLOW_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKFLOW_ID | NUMBER |  | 18 | Yes | This column uniquely identifies workflow translations. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 200 |  |  | User readable name of the workflow |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | User readable description of the workflow |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_WORKFLOWS_TLN1_ | Non Unique | Default | WORKFLOW_ID, LANGUAGE |
| FAI_WORKFLOWS_TLU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, WORKFLOW_ID, LANGUAGE |

---

[← Back to Index](../2_AI_Tables_Index.md)
