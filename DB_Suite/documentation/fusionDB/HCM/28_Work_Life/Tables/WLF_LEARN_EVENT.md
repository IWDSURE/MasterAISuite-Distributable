# WLF_LEARN_EVENT

Table to store learn event information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnevent-10970.html#wlflearnevent-10970](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnevent-10970.html#wlflearnevent-10970)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_EVENT_PK | EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EVENT_TYPE | VARCHAR2 | 30 |  | Yes | Type of the event, like LearningRecordCompletion. |
| EVENT_DATE | TIMESTAMP |  |  | Yes | Datetime when the event was raised. |
| EVENT_OWNER_ID | NUMBER |  | 18 | Yes | The person identifier who raised the event. |
| EVENT_PERSONA | VARCHAR2 | 30 |  |  | The persona who raised the event: (Learner, Manager, Specialist). |
| EVENT_SYSTEM_TYPE | VARCHAR2 | 30 |  | Yes | Even raised thru UI or through a background job. |
| EVENT_SOURCE | VARCHAR2 | 100 |  | Yes | EVENT_SOURCE |
| SUBJECT_ID | NUMBER |  | 18 | Yes | SUBJECT_ID |
| SUBJECT_TYPE | VARCHAR2 | 100 |  | Yes | SUBJECT_TYPE |
| EVENT_STATUS | VARCHAR2 | 30 |  |  | EVENT_STATUS |
| EVENT_PHASE | VARCHAR2 | 30 |  |  | EVENT_PHASE |
| EVENT_CONSUMERS_COUNT | NUMBER |  |  |  | EVENT_CONSUMERS_COUNT |
| EVENT_CONSUMERS | CLOB |  |  |  | EVENT_CONSUMERS |
| EVENT_PROCESSED_DATE | TIMESTAMP |  |  |  | EVENT_PROCESSED_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| OTHER_INFO | VARCHAR2 | 2000 |  |  | OTHER_INFO |
| EVENT_OWNER | VARCHAR2 | 20 |  |  | Represents owner of the event. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_EVENT_N1 | Non Unique | Default | EVENT_STATUS, EVENT_DATE |
| WLF_LEARN_EVENT_N2 | Non Unique | DEFAULT | EVENT_DATE, SUBJECT_ID, EVENT_TYPE |
| WLF_LEARN_EVENT_U1 | Unique | Default | EVENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
