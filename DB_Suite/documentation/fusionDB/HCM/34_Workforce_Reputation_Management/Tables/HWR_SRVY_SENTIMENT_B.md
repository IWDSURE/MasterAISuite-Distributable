# HWR_SRVY_SENTIMENT_B

This will store the sentiments that will be used by sentiment analysis job.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysentimentb-31284.html#hwrsrvysentimentb-31284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysentimentb-31284.html#hwrsrvysentimentb-31284)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_SENTIMENT_B_PK | SENTIMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SENTIMENT_ID | NUMBER |  | 18 | Yes | This is the Sentiment Id identifying the Sentiment entry in this table. |
| SENTIMENT_URI | VARCHAR2 | 100 |  |  | This is the URI of the Sentiment. |
| SENTIMENT_ATTR_1 | VARCHAR2 | 100 |  |  | SENTIMENT_ATTR_1. This is the extra attribute in case if needed. |
| SENTIMENT_ATTR_2 | VARCHAR2 | 100 |  |  | SENTIMENT_ATTR_2. This is the extra attribute in case if needed. |
| SENTIMENT_ATTR_3 | VARCHAR2 | 100 |  |  | SENTIMENT_ATTR_3. This is the extra attribute in case if needed. |
| SENTIMENT_ATTR_4 | VARCHAR2 | 100 |  |  | SENTIMENT_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_SENTIMENT_B_U1 | Unique | Default | SENTIMENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
