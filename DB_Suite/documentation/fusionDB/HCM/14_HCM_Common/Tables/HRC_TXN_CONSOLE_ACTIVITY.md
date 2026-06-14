# HRC_TXN_CONSOLE_ACTIVITY

Table to store the activity details

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconsoleactivity-20588.html#hrctxnconsoleactivity-20588](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconsoleactivity-20588.html#hrctxnconsoleactivity-20588)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_CONSOLE_ACTIVITY_PK | ACTIVITYID |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| ACTIVITYID | NUMBER |  | Yes | Primary key |
| SOURCE | VARCHAR2 | 200 |  | COLUMN2 |
| COMPONENT | VARCHAR2 | 200 |  | COLUMN3 |
| ACTIVITY | VARCHAR2 | 200 |  | COLUMN4 |
| STATUS | VARCHAR2 | 100 |  | COLUMN5 |
| PARAM1 | VARCHAR2 | 200 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM2 | VARCHAR2 | 200 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM3 | VARCHAR2 | 200 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM4 | VARCHAR2 | 200 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM5 | VARCHAR2 | 200 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM6 | NUMBER |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM7 | NUMBER |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM8 | NUMBER |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM9 | NUMBER |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARMA10 | NUMBER |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM11 | TIMESTAMP |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM12 | TIMESTAMP |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM13 | TIMESTAMP |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM14 | TIMESTAMP |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM15 | TIMESTAMP |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| PARAM16 | CLOB |  |  | Descriptive Flexfield: segment of the user descriptive flexfield |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_CONSOLE_ACTIVITY_PK | Unique | HRC_TXN_CONSOLE_ACTIVITY_PK | ACTIVITYID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
