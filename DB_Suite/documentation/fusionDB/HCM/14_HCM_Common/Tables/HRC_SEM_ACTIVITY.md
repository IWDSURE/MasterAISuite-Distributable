# HRC_SEM_ACTIVITY

Table to lock actity on semsearch server

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemactivity-13638.html#hrcsemactivity-13638](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemactivity-13638.html#hrcsemactivity-13638)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_ACTIVITY_PK | ACTIVITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTIVITY_ID | NUMBER |  |  | Yes | The ID of the activity ACTIVITY_ID |
| ACTIVITY | VARCHAR2 | 80 |  |  | The name of the activity running on the server. Unique |
| SERVER | VARCHAR2 | 80 |  |  | Name of the server where the activity in run |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_ACTIVITY_U1 | Unique | Default | ACTIVITY_ID |
| HRC_SEM_ACTIVITY_U2 | Unique | Default | ACTIVITY |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
