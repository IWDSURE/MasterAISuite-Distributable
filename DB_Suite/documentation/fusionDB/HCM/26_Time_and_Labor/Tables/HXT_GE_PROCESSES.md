# HXT_GE_PROCESSES

The Input values collected from the UI to generate Time Cards, Time Entries and Time Events.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeprocesses-26366.html#hxtgeprocesses-26366](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeprocesses-26366.html#hxtgeprocesses-26366)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_GE_PROCESSES_PK | GE_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GE_PROCESS_ID | NUMBER |  | 18 | Yes | GE_PROCESS_ID |
| STATUS | VARCHAR2 | 20 |  |  | STATUS |
| COMMENT_TEXT | VARCHAR2 | 400 |  |  | COMMENT_TEXT |
| GE_PROCESS_TYPE | VARCHAR2 | 20 |  | Yes | GE_PROCESS_TYPE |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | ESS_REQUEST_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REPORTER_ID | NUMBER |  | 18 |  | REPORTER_ID |
| FROM_DATE | DATE |  |  |  | FROM_DATE |
| TO_DATE | DATE |  |  |  | TO_DATE |
| MEASURE | NUMBER |  |  |  | MEASURE |
| UNIT_OF_MEASURE | VARCHAR2 | 150 |  |  | UNIT_OF_MEASURE |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| STOP_TIME | TIMESTAMP |  |  |  | STOP_TIME |
| SKIP_OFF_DAY | VARCHAR2 | 1 |  |  | SKIP_OFF_DAY |
| SKIP_PUBLIC_HOLIDAY | VARCHAR2 | 1 |  |  | SKIP_PUBLIC_HOLIDAY |
| REPLACE_EXISTING_VALUES | VARCHAR2 | 1 |  |  | REPLACE_EXISTING_VALUES |
| NEXT_TC_COUNT | NUMBER |  | 18 |  | NEXT_TC_COUNT |
| TIME_CARD_VALUE | VARCHAR2 | 20 |  |  | TIME_CARD_VALUE |
| EVENT | VARCHAR2 | 30 |  |  | EVENT |
| SEARCH_QUERY | BLOB |  |  |  | SEARCH_QUERY |
| PERSON_LIST | BLOB |  |  |  | PERSON_LIST |
| PERSON_LIST_TYPE | VARCHAR2 | 20 |  |  | PERSON_LIST_TYPE |
| SELECTED_ID_LIST | CLOB |  |  |  | SELECTED_ID_LIST |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TZ_AWARE | VARCHAR2 | 1 |  |  | TZ_AWARE |
| TC_PERIOD_OPTION | VARCHAR2 | 30 |  |  | Dedicated to Generate Time Cards processes, it indicates the inclusive periods
option for which time cards will be generated |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_GE_PROCESS_U1 | Unique | Default | GE_PROCESS_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
