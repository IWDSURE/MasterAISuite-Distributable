# HR_GEN_AI_TOOLS_TL_

This table stores the seeded Gen AI Tools name and description.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaitoolstl-16059.html#hrgenaitoolstl-16059](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaitoolstl-16059.html#hrgenaitoolstl-16059)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_TOOLS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TOOL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOOL_ID | NUMBER |  | 18 | Yes | The Unique Identifier of the Gen AI Tool in the Agentic Workflow |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 200 |  |  | Name of the Gen AI Tool in the Agentic Workflow |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the Gen AI Tool in the Agentic Workflow |
| USER_INPUT_MSG | VARCHAR2 | 1000 |  |  | User message when the tool requires input from user. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_GEN_AI_TOOLS_TLN1_ | Non Unique | Default | TOOL_ID, LANGUAGE |
| HR_GEN_AI_TOOLS_TLU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TOOL_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
