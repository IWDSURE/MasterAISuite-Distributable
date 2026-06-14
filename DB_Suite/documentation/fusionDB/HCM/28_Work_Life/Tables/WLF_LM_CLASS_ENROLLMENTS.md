# WLF_LM_CLASS_ENROLLMENTS

An student booking (delegate booking) records an enrollment onto a scheduled, program or one time event.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmclassenrollments-26057.html#wlflmclassenrollments-26057](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmclassenrollments-26057.html#wlflmclassenrollments-26057)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_CLASS_ENROLLMENTS_PK | CLASS_ENROLLMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASS_ENROLLMENT_ID | NUMBER |  | 18 | Yes | CLASS_ENROLLMENT_ID |
| BOOKING_STATUS_TYPE_ID | NUMBER |  | 18 | Yes | BOOKING_STATUS_TYPE_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| CONTACT_ID | NUMBER |  | 18 |  | CONTACT_ID |
| CLASS_ID | NUMBER |  | 18 | Yes | CLASS_ID |
| PERSON_ADDRESS_ID | NUMBER |  | 18 |  | PERSON_ADDRESS_ID |
| LEARNER_CONTACT_ID | NUMBER |  | 18 |  | LEARNER_CONTACT_ID |
| LEARNER_CONTACT_EMAIL | VARCHAR2 | 240 |  |  | LEARNER_CONTACT_EMAIL |
| THIRD_PARTY_EMAIL | VARCHAR2 | 240 |  |  | THIRD_PARTY_EMAIL |
| PERSON_ADDRESS_TYPE | VARCHAR2 | 30 |  |  | PERSON_ADDRESS_TYPE |
| LEARNER_ASSIGNMENT_ID | NUMBER |  | 18 |  | LEARNER_ASSIGNMENT_ID |
| LAST_CONTENT_ID | NUMBER |  | 18 |  | LAST_CONTENT_ID |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |
| SPONSOR_PERSON_ID | NUMBER |  | 18 |  | SPONSOR_PERSON_ID |
| SPONSOR_ASSIGNMENT_ID | NUMBER |  | 18 |  | SPONSOR_ASSIGNMENT_ID |
| CUSTOMER_ID | NUMBER |  | 18 |  | CUSTOMER_ID |
| AUTHORIZER_PERSON_ID | NUMBER |  | 18 |  | AUTHORIZER_PERSON_ID |
| DATE_ENROLLMENT_PLACED | DATE |  |  | Yes | DATE_ENROLLMENT_PLACED |
| INTERNAL_ENROLLMENT_FLAG | VARCHAR2 | 30 |  | Yes | INTERNAL_ENROLLMENT_FLAG |
| NUMBER_OF_PLACES | NUMBER |  | 9 | Yes | NUMBER_OF_PLACES |
| ADMINISTRATOR | NUMBER |  | 9 |  | ADMINISTRATOR |
| ATTENDANCE_RESULT | VARCHAR2 | 256 |  |  | ATTENDANCE_RESULT |
| ENROLLMENT_PRIORITY | VARCHAR2 | 30 |  |  | ENROLLMENT_PRIORITY |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| CONTACT_ADDRESS_ID | NUMBER |  | 18 |  | CONTACT_ADDRESS_ID |
| CORESPONDENT | VARCHAR2 | 30 |  |  | CORESPONDENT |
| DATE_STATUS_CHANGED | DATE |  |  |  | DATE_STATUS_CHANGED |
| LEARNER_CONTACT_FAX | VARCHAR2 | 60 |  |  | LEARNER_CONTACT_FAX |
| LEARNER_CONTACT_PHONE | VARCHAR2 | 60 |  |  | LEARNER_CONTACT_PHONE |
| FAILURE_REASON | VARCHAR2 | 30 |  |  | FAILURE_REASON |
| LANGUAGE_ID | NUMBER |  | 18 |  | LANGUAGE_ID |
| SOURCE_OF_ENROLLMENT | VARCHAR2 | 30 |  |  | SOURCE_OF_ENROLLMENT |
| SPECIAL_ENROLLMENT_INSTRUCTION | VARCHAR2 | 2000 |  |  | SPECIAL_ENROLLMENT_INSTRUCTION |
| SUCCESSFUL_ATTENDANCE_FLAG | VARCHAR2 | 30 |  |  | SUCCESSFUL_ATTENDANCE_FLAG |
| THIRD_PARTY_ADDRESS_ID | NUMBER |  | 18 |  | THIRD_PARTY_ADDRESS_ID |
| THIRD_PARTY_CONTACT_FAX | VARCHAR2 | 30 |  |  | THIRD_PARTY_CONTACT_FAX |
| THIRD_PARTY_CONTACT_ID | NUMBER |  | 18 |  | THIRD_PARTY_CONTACT_ID |
| THIRD_PARTY_CONTACT_PHONE | VARCHAR2 | 30 |  |  | THIRD_PARTY_CONTACT_PHONE |
| THIRD_PARTY_CUSTOMER_ID | NUMBER |  | 18 |  | THIRD_PARTY_CUSTOMER_ID |
| LINE_ID | NUMBER |  | 18 |  | LINE_ID |
| ORG_ID | NUMBER |  | 18 |  | Indicates the identifier of the business unit associated to the row. |
| DAEMON_FLAG | VARCHAR2 | 30 |  |  | DAEMON_FLAG |
| DAEMON_TYPE | VARCHAR2 | 30 |  |  | DAEMON_TYPE |
| OLD_CLASS_ID | NUMBER |  | 18 |  | OLD_CLASS_ID |
| QUOTE_LINE_ID | NUMBER |  | 18 |  | QUOTE_LINE_ID |
| INTERFACE_SOURCE | VARCHAR2 | 30 |  |  | INTERFACE_SOURCE |
| TOTAL_TRAINING_TIME | VARCHAR2 | 10 |  |  | TOTAL_TRAINING_TIME |
| CONTENT_PLAYER_STATUS | VARCHAR2 | 30 |  |  | CONTENT_PLAYER_STATUS |
| SCORE | NUMBER |  |  |  | SCORE |
| COMPLETED_CONTENT | NUMBER |  |  |  | COMPLETED_CONTENT |
| TOTAL_CONTENT | NUMBER |  |  |  | TOTAL_CONTENT |
| ENROLLMENT_JUSTIFICATION_ID | NUMBER |  | 18 |  | ENROLLMENT_JUSTIFICATION_ID |
| IS_HISTORY_FLAG | VARCHAR2 | 30 |  |  | IS_HISTORY_FLAG |
| IS_MANDATORY_ENROLLMENT | VARCHAR2 | 30 |  |  | IS_MANDATORY_ENROLLMENT |
| SIGN_EVAL_STATUS | VARCHAR2 | 2 |  |  | SIGN_EVAL_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_CLASS_ENROLLMENTS_N50 | Non Unique | Default | CUSTOMER_ID |
| WLF_LM_CLASS_ENROLLMENTS_N51 | Non Unique | Default | CONTACT_ID |
| WLF_LM_CLASS_ENROLLMENTS_N52 | Non Unique | Default | CONTACT_ADDRESS_ID |
| WLF_LM_CLASS_ENROLLMENTS_N53 | Non Unique | Default | PERSON_ID |
| WLF_LM_CLASS_ENROLLMENTS_N54 | Non Unique | Default | THIRD_PARTY_CUSTOMER_ID |
| WLF_LM_CLASS_ENROLLMENTS_N55 | Non Unique | Default | THIRD_PARTY_CONTACT_ID |
| WLF_LM_CLASS_ENROLLMENTS_N56 | Non Unique | Default | THIRD_PARTY_ADDRESS_ID |
| WLF_LM_CLASS_ENROLLMENTS_N57 | Non Unique | Default | ORGANIZATION_ID |
| WLF_LM_CLASS_ENROLLMENTS_N58 | Non Unique | Default | SPONSOR_PERSON_ID |
| WLF_LM_CLASS_ENROLLMENTS_N59 | Non Unique | Default | SPONSOR_ASSIGNMENT_ID |
| WLF_LM_CLASS_ENROLLMENTS_N60 | Non Unique | Default | PERSON_ADDRESS_ID |
| WLF_LM_CLASS_ENROLLMENTS_N61 | Non Unique | Default | LEARNER_ASSIGNMENT_ID |
| WLF_LM_CLASS_ENROLLMENTS_N62 | Non Unique | Default | LEARNER_CONTACT_ID |
| WLF_LM_CLASS_ENROLLMENTS_N64 | Non Unique | Default | DAEMON_FLAG, DAEMON_TYPE |
| WLF_LM_CLASS_ENROLLMENTS_N65 | Non Unique | Default | ENROLLMENT_JUSTIFICATION_ID |
| WLF_LM_CLASS_ENROLLMENTS_N66 | Non Unique | Default | CLASS_ID, PERSON_ID |
| WLF_LM_CLASS_ENROLLMENTS_U1 | Unique | Default | CLASS_ENROLLMENT_ID |
| WLF_LM_CLASS_ENROLLMENTS_U2 | Unique | Default | LINE_ID |
| WLF_LM_CLASS_ENROLLMENTS_U3 | Unique | Default | QUOTE_LINE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
