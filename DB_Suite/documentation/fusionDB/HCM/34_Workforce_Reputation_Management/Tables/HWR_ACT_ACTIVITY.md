# HWR_ACT_ACTIVITY

This table stores the Simple Activities of a Wellness User

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwractactivity-21147.html#hwractactivity-21147](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwractactivity-21147.html#hwractactivity-21147)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ACT_ACTIVITY_PK | ACTIVITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTIVITY_ID | NUMBER |  | 18 | Yes | This column defines the id of the activity |
| SOURCE_ID | NUMBER |  | 18 | Yes | source ID of the EHW source connector |
| USER_ID | VARCHAR2 | 500 |  | Yes | This stores the User Id to whom the Simple Activity Belongs. |
| URI | VARCHAR2 | 500 |  | Yes | This stores the URI of the simple Activity |
| START_TIME | TIMESTAMP |  |  | Yes | This stores the time when the activity was started |
| STOP_TIME | TIMESTAMP |  |  | Yes | This indicates when the activity is completed |
| ACTIVE_TIME | NUMBER |  |  |  | Active time associated with user activity |
| DISTANCE | NUMBER |  |  |  | Distance in miles associated with user activity |
| STEPS | NUMBER |  |  |  | Step count associated with user activity |
| ENERGY_BURNED | NUMBER |  |  |  | Energy burned in Calories |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| TIME_PERIOD | VARCHAR2 | 50 |  | Yes | This stores the Time Period of the acti |
| ACTIVITY_NAME | VARCHAR2 | 80 |  |  | This is the Custom Name of Activity being identified in this record. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ACT_ACTIVITY_N1 | Non Unique | FUSION_TS_TX_DATA | USER_ID |
| HWR_ACT_ACTIVITY_N2 | Non Unique | FUSION_TS_TX_DATA | SOURCE_ID |
| HWR_ACT_ACTIVITY_U1 | Unique | FUSION_TS_TX_DATA | ACTIVITY_ID |
| HWR_ACT_ACTIVITY_U2 | Unique | FUSION_TS_TX_DATA | START_TIME, URI, USER_ID, SOURCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
