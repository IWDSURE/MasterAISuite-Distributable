# WLF_POPULAR_LI_RECOM_DN

This table stores the details of popular learning items in a given recommendation category for all learners.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpopularlirecomdn-17924.html#wlfpopularlirecomdn-17924](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpopularlirecomdn-17924.html#wlfpopularlirecomdn-17924)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_POPULAR_LI_RECOM_DN_PK | POPULAR_LI_RECOM_DN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POPULAR_LI_RECOM_DN_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| RECOMMENDATION_NUMBER | VARCHAR2 | 30 |  | Yes | System generated unique identifier for the recommendation |
| LEARNER_ID | NUMBER |  | 18 | Yes | Specifies identifier of the learner |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Specifies identifier of the learning item |
| RECOM_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies category of the recommendation |
| RECOM_RANK | NUMBER |  |  | Yes | Specifies the order of the recommendation in a given recommendation category |
| METRIC_DATE | DATE |  |  |  | Specifies the effective date of the recommendation |
| PROCESSED_FLAG | VARCHAR2 | 30 |  |  | Specifies if the recommendation is processed or not |
| WITHDRAWN_FLAG | VARCHAR2 | 30 |  |  | Specifies if the recommendation is withdrawn by the learner |
| WITHDRAWN_DATE | TIMESTAMP |  |  |  | Specifies the date and time when the recommendation is withdrawn |
| REASON_CODE | VARCHAR2 | 30 |  |  | Specifies the reason for status change for the recommendation |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_POPULAR_LI_RECOM_DN_U1 | Unique | Default | POPULAR_LI_RECOM_DN_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
