# IRC_LC_EVENT_MSG

Table for storing event messages the ESS Job will be processing.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclceventmsg-5082.html#irclceventmsg-5082](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclceventmsg-5082.html#irclceventmsg-5082)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_EVENT_MSG_PK | MSG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MSG_ID | NUMBER |  | 18 | Yes | Primary Key of the table |
| EVENT_CODE | VARCHAR2 | 256 |  | Yes | Predefined event code following the source of the event

Ex : Code identifying Assessment request updates, Background check result update etc. |
| CONTEXT_ID | NUMBER |  | 18 | Yes | References a lifecycle context object for which the event is applicable.

Relation component 1/2

Ex: SubmissionId, Requisition ID, pool member Id |
| CONTEXT_TYPE | VARCHAR2 | 30 |  | Yes | Lifecycle context type.

Relation component 2/2

Ex : 'CSW', 'POOL', 'REQUISITION' |
| TARGET_PROCESSING_DATE | TIMESTAMP |  |  |  | Date at which we want event to be processed

(For timer events typically) |
| ERROR_MESSAGE | VARCHAR2 | 250 |  |  | Error message in case message handling is failing. |
| ERROR_STACK | CLOB |  |  |  | Full error stack. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| EVENT_TYPE | VARCHAR2 | 32 |  |  | Defining the type of event. Possible values are EVENT or ASYNC_ACTION. |
| ACTION_PARAMS | VARCHAR2 | 4000 |  |  | Column storing the action parameters Map. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_EVENT_MSG_U1 | Unique | Default | MSG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
