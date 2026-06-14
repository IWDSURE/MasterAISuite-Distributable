# ANC_PER_ABS_TYPE_ENTRIES

This table holds information of  the person absence type entries.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabstypeentries-9702.html#ancperabstypeentries-9702](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabstypeentries-9702.html#ancperabstypeentries-9702)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_TYPE_ENTRIES_PK | PER_ABS_TYPE_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_TYPE_ENTRY_ID |
| END_DATETIME | TIMESTAMP |  |  |  | END_DATETIME |
| START_DATETIME | TIMESTAMP |  |  |  | START_DATETIME |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_ENTRY_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ABSENCE_STATUS | VARCHAR2 | 30 |  | Yes | ABSENCE_STATUS |
| START_DATE | DATE |  |  | Yes | START_DATE |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| QTY | NUMBER |  |  |  | QTY |
| END_DATE | DATE |  |  |  | END_DATE |
| START_TIME | VARCHAR2 | 30 |  |  | START_TIME |
| END_TIME | VARCHAR2 | 30 |  |  | END_TIME |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | ABSENCE_TYPE_ID |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | Obsolete.  Do not write to the column any longer. |
| EXPECTED_DT_CHILD_BIRTH | DATE |  |  |  | EXPECTED_DT_CHILD_BIRTH |
| PLANNED_ST_DT | DATE |  |  |  | PLANNED_ST_DT |
| INTEND_TO_WORK | VARCHAR2 | 30 |  |  | INTEND_TO_WORK |
| PLANNED_RETURN_DT | DATE |  |  |  | PLANNED_RETURN_DT |
| LEAVE_DURATION | NUMBER |  |  |  | LEAVE_DURATION |
| ACTUAL_CHILD_BIRTH_DT | DATE |  |  |  | ACTUAL_CHILD_BIRTH_DT |
| ACTUAL_ST_DT | DATE |  |  |  | ACTUAL_ST_DT |
| ACTUAL_RETURN_DT | DATE |  |  |  | ACTUAL_RETURN_DT |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| START_DATE_DURATION | NUMBER |  |  |  | Start time durtaion |
| END_DATE_DURATION | NUMBER |  |  |  | End time duration |
| ABSENCE_TYPE_REASON_ID | NUMBER |  | 18 |  | ABSENCE_TYPE_REASON_ID |
| ABS_AGGREGATION_ID | NUMBER |  | 18 |  | To map the aggregation id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_TYPE_ENTRIES_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_TYPE_ENTRIES_N2 | Non Unique | Default | ASSIGNMENT_ID, ABSENCE_TYPE_ID |
| ANC_PER_ABS_TYPE_ENTRIES_N3 | Non Unique | Default | PERSON_ID, ABSENCE_TYPE_ID |
| ANC_PER_ABS_TYPE_ENTRIES_N4 | Non Unique | Default | TM_REC_GRP_ID |
| ANC_PER_ABS_TYPE_ENTRIES_U1 | Unique | FUSION_TS_TX_DATA | PER_ABS_TYPE_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
