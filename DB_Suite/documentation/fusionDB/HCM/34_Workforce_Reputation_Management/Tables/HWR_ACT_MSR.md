# HWR_ACT_MSR

This stores the Information on the activity Measure of a Simple Activity

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwractmsr-17315.html#hwractmsr-17315](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwractmsr-17315.html#hwractmsr-17315)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ACT_MSR_PK | ACTIVITY_MEASURE_TYPE, ACTIVITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTIVITY_ID | NUMBER |  | 18 | Yes | id which uniquely identifies specific activity |
| VALUE | NUMBER |  |  | Yes | This stores the values of the activity measure |
| UNITS | VARCHAR2 | 500 |  |  | This stores the type of Unit to be used for the activity measure |
| ACTIVITY_MEASURE_TYPE | VARCHAR2 | 500 |  | Yes | This stores the type of activity measure |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ACT_MSR_N1 | Non Unique | FUSION_TS_TX_DATA | ACTIVITY_ID |
| HWR_ACT_MSR_U1 | Unique | FUSION_TS_TX_DATA | ACTIVITY_MEASURE_TYPE, ACTIVITY_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
