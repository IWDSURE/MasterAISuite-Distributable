# WLF_EVENT_ATTEMPT_INTERACTIONS

Stores a user attempt interaction on a learning item object.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventattemptinteractions-17459.html#wlfeventattemptinteractions-17459](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventattemptinteractions-17459.html#wlfeventattemptinteractions-17459)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ATTEMPT_INTERACTIONS_PK | ATTEMPT_INTERACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTEMPT_INTERACTION_ID | NUMBER |  | 18 | Yes | EVENT_ATTEMPT_INTERACTION_ID |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| TYPE | VARCHAR2 | 30 |  |  | TYPE |
| INTERACTION_CREATION_DATE | TIMESTAMP |  |  |  | INTERACTION_CREATION_DATE |
| RAW_OBJECTIVE_STATUS | VARCHAR2 | 1 |  |  | RAW_OBJECTIVE_STATUS |
| RAW_COMPLETION_STATUS | VARCHAR2 | 1 |  |  | RAW_COMPLETION_STATUS |
| INTERNAL_STATE | VARCHAR2 | 1 |  |  | INTERNAL_STATE |
| IS_INITIALIZED | VARCHAR2 | 1 |  | Yes | IS_INITIALIZED |
| CMI_LOCATION | VARCHAR2 | 4000 |  |  | CMI_LOCATION |
| CMI_EXIT | VARCHAR2 | 1 |  |  | CMI_EXIT |
| PROGRESS_MEASURE | NUMBER |  |  |  | PROGRESS_MEASURE |
| SESSION_TIME | NUMBER |  |  |  | SESSION_TIME |
| RAW_SCORE | NUMBER |  |  |  | RAW_SCORE |
| SCALED_SCORE | NUMBER |  |  |  | SCALED_SCORE |
| MIN_SCORE | NUMBER |  |  |  | MIN_SCORE |
| MAX_SCORE | NUMBER |  |  |  | MAX_SCORE |
| SUSPEND_DATA | CLOB |  |  |  | SUSPEND_DATA |
| ENGAGEMENT_TOKEN | VARCHAR2 | 4000 |  | Yes | ENGAGEMENT_TOKEN |
| PREVIOUS_EVENT_STATUS | VARCHAR2 | 1 |  |  | PREVIOUS_EVENT_STATUS |
| PREVIOUS_EVENT_SCORE | NUMBER |  |  |  | PREVIOUS_EVENT_SCORE |
| PREVIOUS_EVENT_SESSION_TIME | NUMBER |  |  |  | PREVIOUS_EVENT_SESSION_TIME |
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
| WLF_ATTEMPT_INTERACTIONS_N1 | Non Unique | Default | EVENT_ID |
| WLF_ATTEMPT_INTERACTIONS_N2 | Non Unique | Default | INTERACTION_CREATION_DATE |
| WLF_ATTEMPT_INTERACTIONS_PK | Unique | Default | ATTEMPT_INTERACTION_ID |
| WLF_ATTEMPT_INTERACTIONS_U1 | Unique | Default | ENGAGEMENT_TOKEN |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
