# WLF_LMC_ATTEMPTS

Stores a user attempt on a content object.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcattempts-11433.html#wlflmcattempts-11433](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcattempts-11433.html#wlflmcattempts-11433)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_ATTEMPTS_PK | ATTEMPT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTEMPT_ID | NUMBER |  | 18 | Yes | ATTEMPT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to the PER_PERSONS table. |
| CONTENT_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
| TARGET_CONTENT_ID | NUMBER |  | 18 | Yes | TARGET_CONTENT_ID |
| CLASS_ID | NUMBER |  | 18 |  | CLASS_ID |
| RESUMED_BY_ATTEMPT_ID | NUMBER |  | 18 |  | If this attempt is suspended, a new attempt is created when this attempt is resumed.  This new attempt id is the resumed_by_attempt_id.  A value in this field means this attempts is suspended. This is a foreign key into the ATTEMPT table. |
| SUSPENDED_ATTEMPT_ID | NUMBER |  | 18 |  | If this attempt is resumed, save the previous suspended attempt id. A value in this column means that this is a resumed attempt. This is a foreign key into the ATTEMPT table. |
| ATTEMPT_DATE | DATE |  |  | Yes | ATTEMPT_DATE |
| ATTEMPT_STATUS | VARCHAR2 | 1 |  | Yes | ATTEMPT_STATUS |
| RAW_STATUS | VARCHAR2 | 1 |  | Yes | RAW_STATUS |
| ATTEMPT_SCORE | NUMBER |  |  | Yes | ATTEMPT_SCORE |
| RAW_SCORE | NUMBER |  |  | Yes | RAW_SCORE |
| SESSION_TIME | NUMBER |  |  | Yes | SESSION_TIME |
| ATTEMPT_ORDER | NUMBER |  |  | Yes | ATTEMPT_ORDER |
| ATTEMPT_TYPE | VARCHAR2 | 240 |  |  | ATTEMPT_TYPE |
| TEST_ID | NUMBER |  | 18 |  | TEST_ID |
| IS_REVIEW | VARCHAR2 | 1 |  |  | IS_REVIEW |
| INTERNAL_STATE | VARCHAR2 | 1 |  |  | INTERNAL_STATE |
| IS_INITIALIZED | VARCHAR2 | 1 |  | Yes | IS_INITIALIZED |
| IS_AUTO_COMMIT | VARCHAR2 | 1 |  | Yes | IS_AUTO_COMMIT |
| CMI_LOCATION | VARCHAR2 | 4000 |  |  | CMI_LOCATION |
| CMI_EXIT | VARCHAR2 | 1 |  |  | CMI_EXIT |
| TIME_EXTENDED | NUMBER |  |  |  | TIME_EXTENDED |
| GRADE_TYPE | VARCHAR2 | 1 |  |  | GRADE_TYPE |
| MASTERY_SCORE | NUMBER |  |  |  | MASTERY_SCORE |
| IS_CERTIFICATION | VARCHAR2 | 1 |  | Yes | IS_CERTIFICATION |
| CONTENT_VERSION | VARCHAR2 | 200 |  |  | CONTENT_VERSION |
| CMI_COMMENTS | VARCHAR2 | 4000 |  |  | CMI_COMMENTS |
| PROCTOR_CODE_ID | NUMBER |  | 18 |  | PROCTOR_CODE_ID |
| SUCCESS_STATUS | VARCHAR2 | 1 |  |  | SUCCESS_STATUS |
| COMPLETION_STATUS | VARCHAR2 | 1 |  |  | COMPLETION_STATUS |
| SCALED_SCORE | NUMBER |  |  |  | SCALED_SCORE |
| MIN_SCORE | NUMBER |  |  |  | MIN_SCORE |
| MAX_SCORE | NUMBER |  |  |  | MAX_SCORE |
| PROGRESS_MEASURE | NUMBER |  |  |  | PROGRESS_MEASURE |
| PREVIOUS_ATTEMPT_STATUS | VARCHAR2 | 1 |  |  | PREVIOUS_ATTEMPT_STATUS |
| PREVIOUS_ATTEMPT_SCORE | NUMBER |  |  |  | PREVIOUS_ATTEMPT_SCORE |
| PREVIOUS_SESSION_TIME | NUMBER |  |  |  | PREVIOUS_SESSION_TIME |
| ATTEMPT_TOKEN | VARCHAR2 | 4000 |  | Yes | ATTEMPT_TOKEN |
| SUSPEND_DATA | CLOB |  |  |  | SUSPEND_DATA |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| USER_ID | NUMBER |  | 18 |  | Obsolete.  Replaced by PERSON_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LMC_ATTEMPTS_N1 | Non Unique | Default | PERSON_ID, CONTENT_ID, ATTEMPT_ID |
| WLF_LMC_ATTEMPTS_PK | Unique | Default | ATTEMPT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
