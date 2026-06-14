# IRC_AIMATCHING_TRK

Table used to store processing recruiting data for sending to AI for data ingestion.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaimatchingtrk-13667.html#ircaimatchingtrk-13667](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaimatchingtrk-13667.html#ircaimatchingtrk-13667)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AIMATCHING_TRK_PK | TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRACKING_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated |
| ENTITY_TYPE | VARCHAR2 | 64 |  |  | Candidates, submissions or requistions |
| CUTOFF_DATE | TIMESTAMP |  |  |  | Timestamp of last record processed |
| HTTP_STATUS_CODE | VARCHAR2 | 20 |  |  | HTTP_STATUS_CODE received after data push to AI rest service |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AIMATCHING_TRK_U1 | Unique | Default | TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
