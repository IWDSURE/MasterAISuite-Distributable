# WLF_EVENT_ATTEMPTS

Summarized status for a user's achievement for a learning item object.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventattempts-24901.html#wlfeventattempts-24901](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventattempts-24901.html#wlfeventattempts-24901)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_EVENT_ATTEMPTS_PK | EVENT_ATTEMPT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ATTEMPT_ID | NUMBER |  | 18 | Yes | EVENT_ATTEMPT_ID |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| LATEST_ATTEMPT_INTERACTION_ID | NUMBER |  | 18 |  | LATEST_EA_INTERACTION_ID |
| LOCATION | VARCHAR2 | 2000 |  |  | LOCATION |
| HWM_LOCATION | VARCHAR2 | 2000 |  |  | High Watermark Location. |
| TOTAL_TIME | NUMBER |  |  |  | TOTAL_TIME |
| PROGRESS_MEASURE | NUMBER |  |  |  | PROGRESS_MEASURE |
| OBJECTIVE_STATUS | VARCHAR2 | 30 |  |  | OBJECTIVE_STATUS |
| COMPLETION_STATUS | VARCHAR2 | 30 |  |  | COMPLETION_STATUS |
| COMPLETION_SCORE | NUMBER |  |  |  | COMPLETION_SCORE |
| OBJ_STATUS_CALC_METHOD | VARCHAR2 | 30 |  |  | OBJ_STATUS_CALC_METHOD |
| OBJECTIVE_MASTERY_SCORE | NUMBER |  |  |  | OBJECTIVE_MASTERY_SCORE |
| COMPLETION_MASTERY_SCORE | NUMBER |  |  |  | COMPLETION_MASTERY_SCORE |
| OBJECTIVE_SCORE | NUMBER |  |  |  | OBJECTIVE_SCORE |
| COMPLETED_UNITS | NUMBER |  | 18 |  | COMPLETED_UNITS |
| COMPLETION_DATE | TIMESTAMP |  |  |  | COMPLETION_DATE |
| RESET_DATE | TIMESTAMP |  |  |  | RESET_DATE |
| ATTEMPT_END_DATE | TIMESTAMP |  |  |  | ATTEMPT_END_DATE |
| ROOT_ATTEMPT_ID | NUMBER |  | 18 | Yes | ROOT_ATTEMPT_ID |
| LAST_UPDATE_METHOD | VARCHAR2 | 30 |  |  | LAST_UPDATE_METHOD |
| COMMENTS | VARCHAR2 | 255 |  |  | COMMENTS |
| NEEDS_STATUS_ROLLUP | VARCHAR2 | 30 |  | Yes | NEEDS_STATUS_ROLLUP |
| NEEDS_TIME_ROLLUP | VARCHAR2 | 30 |  | Yes | NEEDS_TIME_ROLLUP |
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
| WLF_EVENT_ATTEMPTS_N1 | Non Unique | Default | EVENT_ID |
| WLF_EVENT_ATTEMPTS_N2 | Non Unique | Default | ROOT_ATTEMPT_ID |
| WLF_EVENT_ATTEMPTS_N3 | Non Unique | Default | COMPLETION_DATE |
| WLF_EVENT_ATTEMPTS_N4 | Non Unique | Default | RESET_DATE |
| WLF_EVENT_ATTEMPTS_PK | Unique | Default | EVENT_ATTEMPT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
