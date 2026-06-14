# WLF_LMC_PERFORMANCES

Summarized status for a user's achievement for a content object

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcperformances-9731.html#wlflmcperformances-9731](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcperformances-9731.html#wlflmcperformances-9731)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_PERFORMANCES_PK | PERFORMANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERFORMANCE_ID | NUMBER |  | 18 | Yes | PERFORMANCE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to the PER_PERSONS table |
| USER_ID | NUMBER |  | 18 |  | Obsolete.  Replaced by PERSON_ID |
| CONTENT_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
| STATUS | VARCHAR2 | 20 |  | Yes | STATUS |
| SCORE | NUMBER |  |  | Yes | SCORE |
| TOTAL_TIME | NUMBER |  |  | Yes | TOTAL_TIME |
| LOCATION | VARCHAR2 | 2000 |  |  | LOCATION |
| COMPLETED_DATE | DATE |  |  |  | COMPLETED_DATE |
| ATTEMPT_ID | NUMBER |  | 18 |  | ATTEMPT_ID |
| LAST_UPDATE_METHOD | VARCHAR2 | 1 |  |  | LAST_UPDATE_METHOD |
| EXTERNAL_ID | VARCHAR2 | 30 |  |  | EXTERNAL_ID |
| EXTERNAL_SRC | VARCHAR2 | 30 |  |  | EXTERNAL_SRC |
| EXTRA_INFO | VARCHAR2 | 4000 |  |  | EXTRA_INFO |
| RCO_VERSION | VARCHAR2 | 200 |  |  | RCO_VERSION |
| COMMENTS | VARCHAR2 | 255 |  |  | COMMENTS |
| SUCCESS_STATUS | VARCHAR2 | 1 |  |  | SUCCESS_STATUS |
| COMPLETION_STATUS | VARCHAR2 | 1 |  |  | COMPLETION_STATUS |
| SCORM_TIMESTAMP | DATE |  |  |  | SCORM_TIMESTAMP |
| ILA_FILE_ID | NUMBER |  | 18 |  | ILA_FILE_ID |
| SATISFIED_BY_MEASURE | VARCHAR2 | 1 |  | Yes | SATISFIED_BY_MEASURE |
| SCALED_PASSING_SCORE | NUMBER |  |  |  | SCALED_PASSING_SCORE |
| MASTERY_SCORE | NUMBER |  |  |  | MASTERY_SCORE |
| PROGRESS_MEASURE | NUMBER |  |  |  | PROGRESS_MEASURE |
| NEEDS_STATUS_ROLLUP | VARCHAR2 | 1 |  | Yes | NEEDS_STATUS_ROLLUP |
| NEEDS_TIME_ROLLUP | VARCHAR2 | 1 |  | Yes | NEEDS_TIME_ROLLUP |
| AVAILABLE_CHILDREN | CLOB |  |  |  | AVAILABLE_CHILDREN |
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
| WLF_LMC_PERFORMANCES_PK | Unique | FUSION_TS_TX_DATA | PERFORMANCE_ID |
| WLF_LMC_PERFORMANCES_U1 | Unique | Default | PERSON_ID, CONTENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
