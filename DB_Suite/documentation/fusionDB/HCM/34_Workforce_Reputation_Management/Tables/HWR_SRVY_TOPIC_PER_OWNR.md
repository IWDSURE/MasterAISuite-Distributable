# HWR_SRVY_TOPIC_PER_OWNR

This will store information regarding the topics associated with the Line Manager // owner of topics. Table specific for meeting survey.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvytopicperownr-13709.html#hwrsrvytopicperownr-13709](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvytopicperownr-13709.html#hwrsrvytopicperownr-13709)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_TOPIC_PER_OWNR_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | VARCHAR2 | 20 |  | Yes | This is the primary key for this table. |
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the Topic ID identifying the Topic entry in this table. |
| TOPIC_OWNER | VARCHAR2 | 500 |  | Yes | This is the FUSION id of the owner of this Topic. |
| QUESTIONAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID for which Topic is being added. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 |  | This is the Questionnaire Version associated with the Questionnaire ID of this Survey |
| TOPICS_PER_OWNER_ATTR_1 | VARCHAR2 | 100 |  |  | TOPICS_PER_OWNER_ATTR_1. This is the extra attribute in case if needed. |
| TOPICS_PER_OWNER_ATTR_2 | VARCHAR2 | 100 |  |  | TOPICS_PER_OWNER_ATTR_2. This is the extra attribute in case if needed. |
| TOPICS_PER_OWNER_ATTR_3 | VARCHAR2 | 100 |  |  | TOPICS_PER_OWNER_ATTR_3. This is the extra attribute in case if needed. |
| TOPICS_PER_OWNER_ATTR_4 | VARCHAR2 | 100 |  |  | TOPICS_PER_OWNER_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_TOPIC_PER_OWNR_N1 | Non Unique | Default | TOPIC_OWNER |
| HWR_SRVY_TOPIC_PER_OWNR_N2 | Non Unique | Default | QUESTIONAIRE_ID |
| HWR_SRVY_TOPIC_PER_OWNR_N3 | Non Unique | Default | TOPIC_ID |
| HWR_SRVY_TOPIC_PER_OWNR_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
