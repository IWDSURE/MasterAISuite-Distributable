# HWR_ACT_MSR_ACTIVE

This stores the Information on the activity Measure of a Simple Activity

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwractmsractive-16067.html#hwractmsractive-16067](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwractmsractive-16067.html#hwractmsractive-16067)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ACT_MSR_ACTIVE_PK | ACTIVITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTIVITY_ID | NUMBER |  | 18 | Yes | ACTIVITY_ID which maps back to it's parent activity |
| UNITS | VARCHAR2 | 500 |  |  | This stores the type of Unit to be used for the activity measure |
| VALUE | NUMBER |  |  | Yes | This stores the values of the activity measure |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ACT_MSR_ACTIVE_U1 | Unique | FUSION_TS_TX_DATA | ACTIVITY_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
