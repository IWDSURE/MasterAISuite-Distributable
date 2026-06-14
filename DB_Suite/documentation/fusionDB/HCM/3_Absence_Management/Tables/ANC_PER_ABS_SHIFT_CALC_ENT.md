# ANC_PER_ABS_SHIFT_CALC_ENT

This table holds information of the earned date based calculated entries corresponding to the related shift breakdown.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsshiftcalcent-28236.html#ancperabsshiftcalcent-28236](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsshiftcalcent-28236.html#ancperabsshiftcalcent-28236)

## Primary Key

| Name | Columns |
|------|----------|
| anc_per_abs_shift_calc_en_PK | PER_ABS_SHIFT_CALC_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_SHIFT_CALC_ENTRY_ID | NUMBER |  | 18 | Yes | Key identifier for breakdown of calculated records. |
| PER_ABS_SHIFT_BREAKDOWN_ID | NUMBER |  | 18 | Yes | Key identifier of parent shift breakdown record. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise identifier. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person identifier. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment identifier. |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | Person absence entry identifier. |
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | Absence type identifier. |
| UOM | VARCHAR2 | 30 |  | Yes | Unit of measure. |
| START_DATETIME | TIMESTAMP |  |  | Yes | Start date and time of the shift calculate entry. |
| END_DATETIME | TIMESTAMP |  |  | Yes | End date and time of the shift calculated entry. |
| DURATION | NUMBER |  |  | Yes | Duration of the shift calculated entry. |
| DURATION_IN_MILLISECONDS | NUMBER |  |  |  | Duration of the shift calculated entry in milliseconds. |
| SCHEDULE_TYPE | VARCHAR2 | 30 |  | Yes | This denotes time or elapsed schedule type. |
| EARNED_DATE | DATE |  |  | Yes | This denotes the earned day. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_SHIFT_CALC_ENT_N1 | Non Unique | FUSION_TS_TX_IDX | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_SHIFT_CALC_ENT_U1 | Unique | Default | PER_ABS_SHIFT_CALC_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
