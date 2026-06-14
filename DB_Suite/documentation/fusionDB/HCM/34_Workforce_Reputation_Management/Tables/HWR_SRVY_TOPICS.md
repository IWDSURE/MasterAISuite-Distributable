# HWR_SRVY_TOPICS

This table will be used to store the topics that are keyed in by the line manager and will
be used by sentiment analysis job for the meeting survey. Table specific for meeting survey

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvytopics-24561.html#hwrsrvytopics-24561](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvytopics-24561.html#hwrsrvytopics-24561)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_TOPICS_PK | TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the Topic Id identifying the Topic entry in this table. |
| TOPIC_NAME | VARCHAR2 | 500 |  | Yes | This is the name of the Topic being identified by Topic Id in this table. |
| TOPIC_DESCRIPTION | VARCHAR2 | 4000 |  |  | This is the description of the Topic being identified by Topic Id in this table. |
| TOPIC_URI | VARCHAR2 | 100 |  |  | This is the URI of the Topic. |
| TOPIC_ATTR_1 | VARCHAR2 | 100 |  |  | TOPIC_ATTR_1. This is the extra attribute in case if needed. |
| TOPIC_ATTR_2 | VARCHAR2 | 100 |  |  | TOPIC_ATTR_2. This is the extra attribute in case if needed. |
| TOPIC_ATTR_3 | VARCHAR2 | 100 |  |  | TOPIC_ATTR_3. This is the extra attribute in case if needed. |
| TOPIC_ATTR_4 | VARCHAR2 | 100 |  |  | TOPIC_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_TOPICS_U1 | Unique | Default | TOPIC_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
