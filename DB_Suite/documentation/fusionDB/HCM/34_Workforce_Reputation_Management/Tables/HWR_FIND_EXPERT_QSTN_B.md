# HWR_FIND_EXPERT_QSTN_B

This table will be used to store information regardding OSN conversations used in Ask a Question feature.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrfindexpertqstnb-20265.html#hwrfindexpertqstnb-20265](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrfindexpertqstnb-20265.html#hwrfindexpertqstnb-20265)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FIND_EXPERT_QSTN_B_PK | QUESTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the Question Id associated with the OSN conversation for Ask a Question feature |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of  conversation. |
| OSN_ID | VARCHAR2 | 100 |  |  | ID of the OSN convesation linked to the Ask a Question feature |
| QUESTION_CATEGORY | VARCHAR2 | 500 |  |  | This is a comma separated list of Categories associated with a question |
| QUESTION_TOPICS | VARCHAR2 | 500 |  |  | This is a comma separated list of Topics associated with a question. |
| QUESTION_DESCRIPTION | VARCHAR2 | 4000 |  | Yes | This is the text of the question being asked. |
| QSTN_ATTR_1 | VARCHAR2 | 100 |  |  | QSTN_ATTR_1. This is the extra attribute in case if needed. |
| QSTN_ATTR_2 | VARCHAR2 | 100 |  |  | QSTN_ATTR_2. This is the extra attribute in case if needed. |
| QSTN_ATTR_3 | VARCHAR2 | 100 |  |  | QSTN_ATTR_3. This is the extra attribute in case if needed. |
| QSTN_ATTR_4 | VARCHAR2 | 100 |  |  | QSTN_ATTR_4. This is the extra attribute in case if needed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_FIND_EXPERT_QSTN_B_U1 | Unique | Default | QUESTION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
