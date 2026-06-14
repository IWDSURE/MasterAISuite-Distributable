# PER_POSITION_BUDGETS_TL_

Position Budgets table that stores the translatable position budget attributes.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionbudgetstl-22365.html#perpositionbudgetstl-22365](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionbudgetstl-22365.html#perpositionbudgetstl-22365)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POSITION_BUDGETS_TL_PK_ | POSITION_BUDGET_ID, LANGUAGE, LAST_UPDATED_BY, LAST_UPDATE_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_BUDGET_ID | NUMBER |  | 18 | Yes | Unique identifier of the position budget. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  |  | Name of the Position Budget. |
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
| PER_POSITION_BUDGETS_TL_PK_ | Unique | PER_POSITION_BUDGETS_TL_PK_ | POSITION_BUDGET_ID, LANGUAGE, LAST_UPDATED_BY, LAST_UPDATE_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
