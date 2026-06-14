# BEN_PL_COPY_LOGS

This table stores the log data created while exporting or importing the plan or program.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcopylogs-16834.html#benplcopylogs-16834](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplcopylogs-16834.html#benplcopylogs-16834)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_COPY_LOGS_PK | PL_COPY_LOG_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_COPY_LOG_ID | NUMBER |  | 18 | Yes | PL_COPY_LOG_ID |
| PL_COPY_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_COPY_PARAMS Table. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| MESSAGE_TYPE | VARCHAR2 | 240 |  |  | MESSAGE_TYPE |
| MESSAGE | VARCHAR2 | 4000 |  |  | MESSAGE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LOG_ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | LOG_ATTRIBUTE1 |
| LOG_ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | LOG_ATTRIBUTE2 |
| LOG_ATTRIBUTE3 | VARCHAR2 | 4000 |  |  | LOG_ATTRIBUTE3 |
| LOG_ATTRIBUTE4 | VARCHAR2 | 4000 |  |  | LOG_ATTRIBUTE4 |
| LOG_ATTRIBUTE5 | VARCHAR2 | 4000 |  |  | LOG_ATTRIBUTE5 |
| LOG_ATTRIBUTE_DATE1 | DATE |  |  |  | LOG_ATTRIBUTE_DATE1 |
| LOG_ATTRIBUTE_DATE2 | DATE |  |  |  | LOG_ATTRIBUTE_DATE2 |
| LOG_ATTRIBUTE_DATE3 | DATE |  |  |  | LOG_ATTRIBUTE_DATE3 |
| LOG_ATTRIBUTE_DATE4 | DATE |  |  |  | LOG_ATTRIBUTE_DATE4 |
| LOG_ATTRIBUTE_DATE5 | DATE |  |  |  | LOG_ATTRIBUTE_DATE5 |
| LOG_ATTRIBUTE_NUMBER1 | NUMBER |  | 22 |  | LOG_ATTRIBUTE_NUMBER1 |
| LOG_ATTRIBUTE_NUMBER2 | NUMBER |  | 22 |  | LOG_ATTRIBUTE_NUMBER2 |
| LOG_ATTRIBUTE_NUMBER3 | NUMBER |  | 22 |  | LOG_ATTRIBUTE_NUMBER3 |
| LOG_ATTRIBUTE_NUMBER4 | NUMBER |  | 22 |  | LOG_ATTRIBUTE_NUMBER4 |
| LOG_ATTRIBUTE_NUMBER5 | NUMBER |  | 22 |  | LOG_ATTRIBUTE_NUMBER5 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_COPY_LOGS_N1 | Non Unique | Default | PL_COPY_ID |
| BEN_PL_COPY_LOGS_PK | Unique | Default | PL_COPY_LOG_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
