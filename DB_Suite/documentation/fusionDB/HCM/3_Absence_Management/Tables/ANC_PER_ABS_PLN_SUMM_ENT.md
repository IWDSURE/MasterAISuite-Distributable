# ANC_PER_ABS_PLN_SUMM_ENT

This table holds information of  the person absence plan summary entries.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsplnsumment-6403.html#ancperabsplnsumment-6403](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsplnsumment-6403.html#ancperabsplnsumment-6403)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_PLN_SUMM_ENT_PK | PER_ABS_PLN_SUMM_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_PLN_SUMM_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_PLN_SUMM_ENTRY_ID |
| CASE_ID | NUMBER |  | 18 |  | CASE_ID |
| SOURCE | VARCHAR2 | 255 |  |  | Source of this column value |
| CALC_DATE | TIMESTAMP |  |  |  | Calculation date of this record |
| PLAN_PERIOD_START_DATE | TIMESTAMP |  |  |  | Plan period start date |
| OVRRD_RSN_CD | VARCHAR2 | 255 |  |  | Override reason code |
| ACTIVITY_CD | VARCHAR2 | 255 |  |  | Plan activity code |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | Absence entry id |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 |  | PER_ABS_TYPE_ENTRY_ID |
| UNITS | NUMBER |  |  | Yes | absence units |
| UOM | VARCHAR2 | 30 |  | Yes | UOM |
| PAY_FACTOR | NUMBER |  |  | Yes | Pay factor |
| PERSON_ID | NUMBER |  | 18 | Yes | Person id |
| PLAN_ID | NUMBER |  | 18 |  | Plan id for the absence plan |
| START_DATETIME | TIMESTAMP |  |  | Yes | Start date timestamp |
| END_DATETIME | TIMESTAMP |  |  | Yes | End date timestamp |
| QUALIFICATION_DATE | DATE |  |  |  | Qualification date |
| ENTITLEMENT_DATE | DATE |  |  |  | Entitlement date |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_PLN_SUMM_ENT_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_PLN_SUMM_ENT_N2 | Non Unique | Default | PERSON_ID |
| ANC_PER_ABS_PLN_SUMM_ENT_N3 | Non Unique | Default | PER_ABS_TYPE_ENTRY_ID |
| ANC_PER_ABS_PLN_SUMM_ENT_N4 | Non Unique | Default | CASE_ID |
| ANC_PER_ABS_PLN_SUMM_ENT_U1 | Unique | FUSION_TS_TX_DATA | PER_ABS_PLN_SUMM_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
