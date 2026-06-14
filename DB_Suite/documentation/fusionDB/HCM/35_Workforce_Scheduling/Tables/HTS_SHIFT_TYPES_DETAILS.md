# HTS_SHIFT_TYPES_DETAILS

Shift definition extension to support shift types library in scheduling application

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshifttypesdetails-13970.html#htsshifttypesdetails-13970](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshifttypesdetails-13970.html#htsshifttypesdetails-13970)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHIFT_TYPE_ID | NUMBER |  |  | Yes | Shift identifier to uniquely identify a shift |
| SHIFT_SHORT_NAME | VARCHAR2 | 5 |  |  | Short name for each of the shifts for display purpose |
| SHIFT_COLOUR | VARCHAR2 | 20 |  |  | Shift color to be displayed on the UI |
| START_EARLY_GRACE | NUMBER |  | 18 |  | Clock integration Start Early grace period for violation |
| START_LATE_GRACE | NUMBER |  | 18 |  | Clock integration Start late grace period for violation |
| END_EARLY_GRACE | NUMBER |  | 18 |  | Clock integration End early grace period for violation |
| END_LATE_GRACE | NUMBER |  | 18 |  | Clock integration End late grace period for violation |
| TOLERANCE | NUMBER |  | 9 |  | Clock integration Threshold to ignore violation |
| START_EARLY_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration Start Early violation message |
| START_LATE_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration Start late violation message |
| END_EARLY_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration End Early violation message |
| END_LATE_VIOLATION | VARCHAR2 | 10 |  |  | Clock integration End late violation message |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SHIFT_CODE | VARCHAR2 | 64 |  |  | Shift unique Identifier code |
| TIME_NOT_WORKED | NUMBER |  | 18 |  | Column indicates time not worked for a shift |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SHIFT_TYPES_DETAILS_U1 | Unique | FUSION_TS_TX_DATA | SHIFT_TYPE_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
