# HWR_SRVY_TOPIC_PER_SRVY

This will store information regarding the topics associated with the survey being created. Table specific for meeting survey.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvytopicpersrvy-16391.html#hwrsrvytopicpersrvy-16391](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvytopicpersrvy-16391.html#hwrsrvytopicpersrvy-16391)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_TOPIC_PER_SRVY_PK | SURVEY_ID, TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_ID | NUMBER |  | 18 | Yes | This is the Survey Id identifying the Survey entry in this table. |
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the Topic ID associated with the Survey. |
| TOPIC_PER_SRVY_ATTR_1 | VARCHAR2 | 100 |  |  | TOPIC_PER_SRVY_ATTR_1. This is the extra attribute in case if needed. |
| TOPIC_PER_SRVY_ATTR_2 | VARCHAR2 | 100 |  |  | TOPIC_PER_SRVY_ATTR_2. This is the extra attribute in case if needed. |
| TOPIC_PER_SRVY_ATTR_3 | VARCHAR2 | 100 |  |  | TOPIC_PER_SRVY_ATTR_3. This is the extra attribute in case if needed. |
| TOPIC_PER_SRVY_ATTR_4 | VARCHAR2 | 100 |  |  | TOPIC_PER_SRVY_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_TOPIC_PER_SRVY_U1 | Unique | Default | SURVEY_ID, TOPIC_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
