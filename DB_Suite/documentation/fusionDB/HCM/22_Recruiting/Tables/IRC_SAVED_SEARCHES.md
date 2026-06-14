# IRC_SAVED_SEARCHES

This table stores all the saved searches for candidates.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsavedsearches-16428.html#ircsavedsearches-16428](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsavedsearches-16428.html#ircsavedsearches-16428)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SAVED_SEARCHES_PK | SEARCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| NAME | VARCHAR2 | 240 |  | Yes | User entered name for this saved search. |
| SEARCH_QUERY | CLOB |  |  | Yes | Saved search stored in XML format. |
| SAVED_SEARCH_TYPE | VARCHAR2 | 32 |  |  | Stores the type of the saved search. |
| OWNER_PERSON_ID | NUMBER |  | 18 | Yes | Indicates the owner of the saved search. |
| SEARCH_CONTEXT | VARCHAR2 | 32 |  |  | The context from which search is triggered. |
| LAST_EXECUTED_TIME | TIMESTAMP |  |  |  | The last time the search query was executed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SAVED_SEARCHES_FK1 | Non Unique | Default | OWNER_PERSON_ID |
| IRC_SAVED_SEARCHES_N1 | Non Unique | Default | SEARCH_CONTEXT, OWNER_PERSON_ID, NAME |
| IRC_SAVED_SEARCHES_PK | Unique | Default | SEARCH_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
