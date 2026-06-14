# BEN_STAGE_INFO

BEN_STAGE_INFO contains staging information related to benefits.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** ben_stage_info

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benstageinfo-19130.html#benstageinfo-19130](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benstageinfo-19130.html#benstageinfo-19130)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_STAGE_INFO_PK | STAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAGE_ID | NUMBER |  | 22 | Yes | System generated primary key column. |
| RECEIVED_DATE | TIMESTAMP |  |  | Yes | Date when the request was made to the agent. |
| SOURCE | VARCHAR2 | 4000 |  |  | Source of the document. |
| STATUS | VARCHAR2 | 30 |  |  | Status of the record. |
| STATUS_DATE | DATE |  |  |  | Date when the status was changed on this table. |
| FEED_TYPE | VARCHAR2 | 500 |  |  | Type of the message. |
| FEED_NAME | VARCHAR2 | 500 |  |  | Message name. |
| FEED_VAL | VARCHAR2 | 4000 |  |  | Content of the message. |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | Number assigned to the person, to identify the person uniquely in any context, not dependent on being an employee, contingent worker, etc. |
| FULL_NAME | VARCHAR2 | 400 |  |  | System constructed version of name, used in more formal display purposes. |
| CON_PERSON_NUM | VARCHAR2 | 30 |  |  | Contact person number. |
| CON_FULL_NAME | VARCHAR2 | 400 |  |  | System constructed version of name of a contact, used in more formal display purposes |
| PERSON_ID | NUMBER |  | 22 | Yes | This column holds Foreign Key to PER_PEOPLE_F. |
| PGM_NAME | VARCHAR2 | 240 |  |  | Name of the program. |
| PLAN_NAME | VARCHAR2 | 240 |  |  | Name of the plan. |
| PLAN_CD | VARCHAR2 | 240 |  |  | Plan usage. |
| OPTION_NAME | VARCHAR2 | 240 |  |  | Name of the option. |
| EVENT_NAME | VARCHAR2 | 240 |  |  | Name of the Event. |
| EVENT_DATE | DATE |  |  |  | Date of the Event. |
| CTFN_NAME | VARCHAR2 | 240 |  |  | Certification Name. |
| DOC_TYPE | VARCHAR2 | 240 |  |  | Document Type. |
| IDENT_TYPE | VARCHAR2 | 4000 |  |  | Identifier Type. |
| IDENT_VAL | VARCHAR2 | 4000 |  |  | Identifier Value. |
| START_DATE | DATE |  |  |  | Enrollment coverage start date. |
| END_DATE | DATE |  |  |  | Enrollment coverage end date. |
| SUBMITTED_BY | VARCHAR2 | 240 |  |  | Indicates the user who submitted the action. |
| SUBMITTED_DATE | DATE |  |  |  | Date of Submission. |
| CONFIG_CHAR_1 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_6 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_7 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_8 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_9 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_10 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_11 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_12 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_13 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_14 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_15 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_16 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_17 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_18 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_19 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_20 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_21 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_22 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_23 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_24 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_25 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_26 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_27 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_28 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_29 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_30 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_NUM_1 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_6 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_7 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_8 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_9 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_10 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_11 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_12 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_13 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_14 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_15 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_16 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_17 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_18 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_19 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_NUM_20 | NUMBER |  | 22 |  | Template number field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_6 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_7 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_8 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_9 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_10 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_11 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_12 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_13 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_14 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_15 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_16 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_17 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_18 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_19 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_20 | DATE |  |  |  | Template date field for future use. |
| DATA_LOB1 | CLOB |  |  |  | Enrollment information in JSON format. |
| DATA_LOB2 | CLOB |  |  |  | Enrollment information in JSON format. |
| DATA_LOB3 | BLOB |  |  |  | Enrollment information in binary format. |
| BUSINESS_GROUP_ID | NUMBER |  | 22 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_STAGE_INFO_N1 | Non Unique | BEN_STAGE_INFO_N1 | PERSON_NUMBER, FEED_TYPE, FEED_NAME |
| BEN_STAGE_INFO_N2 | Non Unique | BEN_STAGE_INFO_N2 | CREATION_DATE |
| BEN_STAGE_INFO_N3 | Non Unique | BEN_STAGE_INFO_N3 | PERSON_ID, RECEIVED_DATE |
| BEN_STAGE_INFO_PK | Unique | BEN_STAGE_INFO_PK | STAGE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
