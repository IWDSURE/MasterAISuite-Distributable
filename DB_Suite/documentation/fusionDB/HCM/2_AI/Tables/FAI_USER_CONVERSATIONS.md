# FAI_USER_CONVERSATIONS

This table stores the user conversations

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiuserconversations-19510.html#faiuserconversations-19510](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiuserconversations-19510.html#faiuserconversations-19510)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_USER_CONVERSATIONS_PK | CONVERSATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONVERSATION_ID | VARCHAR2 | 500 |  | Yes | Uniquely identifies the user conversations |
| PERSON_ID | NUMBER |  | 18 | Yes | Stores the Person identifier associated with the conversation |
| OBJECT_CODE | VARCHAR2 | 1000 |  |  | Stores the object code |
| OBJECT_TYPE | VARCHAR2 | 1000 |  |  | Stores the object type |
| SPECIFICATION | CLOB |  |  |  | JSON specification for the user conversation |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_USER_CONVERSATIONS_U1 | Unique | FAI_USER_CONVERSATIONS_U1 | CONVERSATION_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
