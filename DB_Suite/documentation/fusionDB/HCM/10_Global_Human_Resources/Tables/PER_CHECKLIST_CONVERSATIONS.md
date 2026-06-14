# PER_CHECKLIST_CONVERSATIONS

Table to store checklist conversations.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistconversations-20956.html#perchecklistconversations-20956](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistconversations-20956.html#perchecklistconversations-20956)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_CONVERSATIONS_PK | CONVERSATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONVERSATION_ID | NUMBER |  | 18 | Yes | CONVERSATION_ID |
| SOURCE_TYPE | VARCHAR2 | 64 |  | Yes | SOURCE_TYPE |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| CONTENT_TYPE | VARCHAR2 | 64 |  | Yes | CONTENT_TYPE |
| OBJECT_ID | NUMBER |  | 18 |  | OBJECT_ID |
| OBJECT_TYPE | VARCHAR2 | 64 |  |  | OBJECT_TYPE |
| PARENT_OBJECT_ID | NUMBER |  | 18 |  | PARENT_OBJECT_ID |
| PARENT_OBJECT_TYPE | VARCHAR2 | 64 |  |  | PARENT_OBJECT_TYPE |
| COMMENTS | VARCHAR2 | 4000 |  | Yes | COMMENTS |
| USER_TYPE | VARCHAR2 | 64 |  | Yes | USER_TYPE |
| USER_GUID | VARCHAR2 | 32 |  | Yes | USER_GUID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| COMMENT_DATETIME | TIMESTAMP |  |  | Yes | COMMENT_DATETIME |
| COMMENT_DETAILS1 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS1 |
| COMMENT_DETAILS2 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS2 |
| COMMENT_DETAILS3 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS3 |
| COMMENT_DETAILS4 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS4 |
| COMMENT_DETAILS5 | VARCHAR2 | 4000 |  |  | COMMENT_DETAILS5 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_CONVERSATIONS_PK | Unique | Default | CONVERSATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
