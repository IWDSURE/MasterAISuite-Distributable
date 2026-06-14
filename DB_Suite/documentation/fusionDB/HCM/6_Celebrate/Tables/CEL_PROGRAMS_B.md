# CEL_PROGRAMS_B

MLS base table to hold details of celebrate programs.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramsb-26745.html#celprogramsb-26745](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramsb-26745.html#celprogramsb-26745)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_PROGRAMS_B_PK | PROGRAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROGRAM_ID | NUMBER |  | 18 | Yes | Unique identifier for a celebrate program |
| TYPE_CODE | VARCHAR2 | 30 |  |  | Code that indicates type of program |
| SUBTYPE_CODE | VARCHAR2 | 30 |  |  | Code that indicates subtype of program |
| AWARD_TYPE_CODE | VARCHAR2 | 30 |  |  | Code that indicates type of award |
| VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Code that indicates visibility of the awards and recognitions through the program |
| TIME_UNIT_CODE | VARCHAR2 | 30 |  |  | Code that indicates time unit of program |
| TIME_UNIT_COUNT | NUMBER |  | 18 |  | Time unit count for recurring programs |
| TRIGGER_TIME_UNIT_COUNT | NUMBER |  | 18 |  | Trigger in advance time count |
| SENIORITY_DATE_CODE | VARCHAR2 | 30 |  |  | Code that indicates the start date for seniority |
| POINTS_RANGE_CODE | VARCHAR2 | 30 |  |  | Code that indicates range of points |
| POINTS_MINIMUM | NUMBER |  |  |  | Minimum value allowed for points |
| POINTS_MAXIMUM | NUMBER |  |  |  | Maximum value allowed for points |
| POINTS_INCREMENT | NUMBER |  |  |  | Increment allowed for points |
| OWNERS_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates if owners are enabled for the program |
| START_DATE | DATE |  |  |  | Program start date |
| END_DATE | DATE |  |  |  | Program end date |
| USE_POINTS_FLAG | VARCHAR2 | 1 |  |  | Flag that identifies if program uses points |
| SENDER_LIMIT_MAXIMUM | NUMBER |  | 18 |  | Maximum number of recognitions/awards per sender |
| RECEIVER_LIST_CODE | VARCHAR2 | 30 |  |  | Code that indicates the list of receivers |
| RECOGNITION_DATE | TIMESTAMP |  |  |  | Date on which recognition/award is to be sent |
| NOMINATION_END_DATE | DATE |  |  |  | End date for nominations |
| SELECTION_END_DATE | DATE |  |  |  | End date for selection of winners |
| WINNERS_TOTAL | NUMBER |  | 18 |  | Total number of winners |
| WINNERS_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates if winner selection is enabled for the program |
| ALLOW_VISIBILITY_CHANGE_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates if visibility options can be modified for a program by users |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Unique identifier for a questionnaire |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | Version number of the questionnaire |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_PROGRAMS_B_PK | Unique | Default | PROGRAM_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
