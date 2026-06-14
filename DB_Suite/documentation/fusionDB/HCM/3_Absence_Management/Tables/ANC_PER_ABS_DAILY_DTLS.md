# ANC_PER_ABS_DAILY_DTLS

This table holds information of  the person absence daily details.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsdailydtls-27352.html#ancperabsdailydtls-27352](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsdailydtls-27352.html#ancperabsdailydtls-27352)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_CAL_ENTRIES_PK | PER_ABS_DAILY_DTL_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_DAILY_DTL_ID | NUMBER |  | 18 | Yes | Identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | References anc_per_abs_entries |
| ABS_DATE | DATE |  |  | Yes | Absence date |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment Id |
| ABS_HOURS | NUMBER |  |  |  | Number of absence hours |
| ABS_DAYS | NUMBER |  |  | Yes | Number absence days |
| SCHEDULED_UNITS | NUMBER |  |  |  | Scheduled duration |
| UOM | VARCHAR2 | 30 |  |  | Unit of measure |
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | Absence Type Id |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ABSENCE_TYPE_REASON_ID | NUMBER |  | 18 |  | Absence Type Reason Id |
| ABSENCE_PLAN_ID | NUMBER |  | 18 |  | Absence plan Identifier |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_DAILY_DTLS_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_DAILY_DTLS_N2 | Non Unique | Default | PERSON_ID |
| ANC_PER_ABS_DAILY_DTLS_N3 | Non Unique | Default | ASSIGNMENT_ID |
| ANC_PER_ABS_DAILY_DTLS_N4 | Non Unique | Default | ABSENCE_TYPE_ID |
| ANC_PER_ABS_DAILY_DTLS_N5 | Non Unique | Default | ABSENCE_TYPE_REASON_ID |
| ANC_PER_ABS_DAILY_DTLS_N6 | Non Unique | Default | ABSENCE_PLAN_ID |
| ANC_PER_ABS_DAILY_DTLS_UK1 | Unique | Default | PER_ABS_DAILY_DTL_ID, ENTERPRISE_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
