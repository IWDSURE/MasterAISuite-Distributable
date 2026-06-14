# HWM_CHANGE_EVENT_SET

The table stores metadata about event change sets, which represent a collection of changes made to specific objects (e.g., Absence, Assignment) within a particular time frame. This table tracks the processing of these change sets, including the status, consumer information, and relevant timestamps.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmchangeeventset-30133.html#hwmchangeeventset-30133](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmchangeeventset-30133.html#hwmchangeeventset-30133)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_CHANGE_EVENT_SET_PK | CHANGE_EVENT_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANGE_EVENT_SET_ID | NUMBER |  | 18 | Yes | A unique identifier of change event set |
| PUBLISH_START_DATE_TIME | TIMESTAMP |  |  | Yes | Event feed poll start date time |
| PUBLISH_END_DATE_TIME | TIMESTAMP |  |  | Yes | Event feed poll end date time |
| CONSUMER_CODE | VARCHAR2 | 30 |  | Yes | Object which listens to the change events or subscriber of the change events |
| CONSUMER_PROCESS_ID | NUMBER |  | 18 |  | Field indicating the ID of the consumer process that performed the feed event
poll. |
| JOB_REQUEST_ID | NUMBER |  | 18 | Yes | Request Id of the ess job |
| FEED_ENTRIES_COUNT | NUMBER |  |  |  | The number of feed entries read from the underlying feed |
| UPDATED_INSTANT | TIMESTAMP |  |  |  | The last time the underlying feed or one of its entries was modified |
| LATEST_FLAG | VARCHAR2 | 1 |  |  | Flag indicating whether this is the latest change set for the consumer code. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_CHANGE_EVENT_SET_N1 | Non Unique | Default | CONSUMER_CODE, LATEST_FLAG |
| HWM_CHANGE_EVENT_SET_PK | Unique | Default | CHANGE_EVENT_SET_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
