# WLF_LEARN_EVT_CONSUMER

Table to store learn event consumer information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnevtconsumer-9664.html#wlflearnevtconsumer-9664](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnevtconsumer-9664.html#wlflearnevtconsumer-9664)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_EVT_CONSUMER_PK | EVENT_CONSUMER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_CONSUMER_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EVENT_ID | NUMBER |  | 18 | Yes | EVENT_ID |
| EVENT_CONSUMER_CLASS | VARCHAR2 | 500 |  |  | EVENT_CONSUMER_CLASS |
| EVENT_JOB_ID | NUMBER |  | 18 |  | EVENT_JOB_ID |
| EVENT_CONSUMER_START_TIME | TIMESTAMP |  |  |  | EVENT_CONSUMER_START_TIME |
| EVENT_CONSUMER_END_TIME | TIMESTAMP |  |  |  | EVENT_CONSUMER_END_TIME |
| EVENT_CONSUMER_STATUS | VARCHAR2 | 30 |  |  | EVENT_CONSUMER_STATUS |
| EVENT_PHASE | VARCHAR2 | 30 |  |  | EVENT_PHASE |
| EVENT_CONSUMER_FAILED_COUNT | NUMBER |  |  |  | EVENT_CONSUMER_FAILED_COUNT |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_EVT_CONSUMER_N1 | Non Unique | Default | EVENT_ID |
| WLF_LEARN_EVT_CONSUMER_U1 | Unique | Default | EVENT_CONSUMER_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
