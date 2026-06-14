# HWM_TIMECARDS

Table where time card data retrieved from related REST services are stored. These time cards display in the Visual Builder Cloud Service time card grid component.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtimecards-9293.html#hwmtimecards-9293](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtimecards-9293.html#hwmtimecards-9293)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TIMECARDS_PK | TIMECARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIMECARD_ID | NUMBER |  | 18 | Yes | Time card identifier |
| TIMECARD_VERSION | NUMBER |  | 9 | Yes | Time card version |
| STATUS | VARCHAR2 | 30 |  |  | Time card status |
| PERSON_ID | NUMBER |  | 18 |  | Person identifier for the time card |
| START_TIME | TIMESTAMP |  |  |  | Time card period start |
| STOP_TIME | TIMESTAMP |  |  |  | Time card period end |
| SOURCE | VARCHAR2 | 30 |  |  | Source of the time card request |
| COMMENT_TEXT | VARCHAR2 | 2000 |  |  | Comments on the time card |
| PROCESS_MODE | VARCHAR2 | 30 |  |  | Code of the process applied to the time card |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAYOUT_SET_ID | VARCHAR2 | 18 |  |  | LAYOUT_SET_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TIMECARDS_PK | Unique | DEFAULT | TIMECARD_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
