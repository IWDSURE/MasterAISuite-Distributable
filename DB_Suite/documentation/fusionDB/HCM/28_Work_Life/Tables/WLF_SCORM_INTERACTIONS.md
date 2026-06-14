# WLF_SCORM_INTERACTIONS

Learning Management Interactions

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscorminteractions-31216.html#wlfscorminteractions-31216](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscorminteractions-31216.html#wlfscorminteractions-31216)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_INTERACTIONS_PK | INTERACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERACTION_ID | NUMBER |  | 18 | Yes | INTERACTION_ID |
| ATTEMPT_INTERACTION_ID | NUMBER |  | 18 | Yes | ATTEMPTINTERACTION_ID |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 4000 |  | Yes | EXTERNAL_IDENTIFIER |
| INTERACTION_TYPE | VARCHAR2 | 1 |  |  | INTERACTION_TYPE |
| INTERACTION_TIMESTAMP | VARCHAR2 | 120 |  |  | INTERACTION_TIMESTAMP |
| WEIGHTING | NUMBER |  |  |  | WEIGHTING |
| LEARNER_RESPONSE | CLOB |  |  |  | LEARNER_RESPONSE |
| RESULT | VARCHAR2 | 120 |  |  | RESULT |
| CORRECTNESS | NUMBER |  |  |  | CORRECTNESS |
| LATENCY | NUMBER |  |  |  | LATENCY |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SCORM_INTERACTIONS_N1 | Non Unique | Default | ATTEMPT_INTERACTION_ID |
| WLF_SCORM_INTERACTIONS_PK | Unique | FUSION_TS_TX_DATA | INTERACTION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
