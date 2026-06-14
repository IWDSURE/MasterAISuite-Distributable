# HWM_TIMECARD_FIELDS

Table where time card field data retrieved from the time card field values REST service are stored. These values display in the Visual Builder Cloud Service time card.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtimecardfields-30774.html#hwmtimecardfields-30774](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtimecardfields-30774.html#hwmtimecardfields-30774)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TIMECARD_FIELDS_PK | TCF_ID, TIME_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIME_ENTRY_ID | NUMBER |  | 18 | Yes | Time card entry identifier |
| TCF_ID | NUMBER |  | 18 | Yes | Time card field identifier |
| VALUE | VARCHAR2 | 150 |  |  | Time card field value |
| DISPLAY_VALUE | VARCHAR2 | 300 |  |  | Display Value |
| DISPLAY_LANG | VARCHAR2 | 30 |  |  | Display language |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TIMECARD_ID | NUMBER |  | 18 |  | TIMECARD_ID |
| USER_CONTEXT | VARCHAR2 | 30 |  |  | USER_CONTEXT |
| ATTRIBUTE_TYPE | VARCHAR2 | 20 |  |  | ATTRIBUTE_TYPE |
| ATTRIBUTE_REF | NUMBER |  | 18 |  | ATTRIBUTE_REF |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TIMECARD_FIELDS_N1 | Non Unique | HWM_TIMECARD_FIELDS_N1 | TIMECARD_ID, USER_CONTEXT |
| HWM_TIMECARD_FIELDS_PK | Unique | DEFAULT | TCF_ID, TIME_ENTRY_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
