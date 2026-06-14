# HR_GEN_AI_TOOLS

This table stores the Gen AI Tools

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** HR_GEN_AI_TOOLS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaitools-3291.html#hrgenaitools-3291](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgenaitools-3291.html#hrgenaitools-3291)

## Primary Key

| Name | Columns |
|------|----------|
| HR_GEN_AI_TOOLS_PK | TOOL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOOL_ID | NUMBER |  | 18 | Yes | The Unique Identifier for the Gen AI Tool |
| NAME | VARCHAR2 | 200 |  |  | Name of the Gen AI Tool |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the Gen AI Tool |
| TYPE | VARCHAR2 | 20 |  |  | Type of the Gen AI Tool |
| TOOL_CREATED_DATE | DATE |  |  |  | Created Date of the Gen AI Tool |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Tool |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Name of the owner who created the Gen AI Tool |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_GEN_AI_TOOLS_PK | Unique | HR_GEN_AI_TOOLS_PK | TOOL_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
