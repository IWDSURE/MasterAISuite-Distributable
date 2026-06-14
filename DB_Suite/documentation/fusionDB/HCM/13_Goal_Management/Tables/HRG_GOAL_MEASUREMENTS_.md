# HRG_GOAL_MEASUREMENTS_

Store the details of Goal single and multiple measurements.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalmeasurements-22653.html#hrggoalmeasurements-22653](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalmeasurements-22653.html#hrggoalmeasurements-22653)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_MEASUREMENTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, MEASUREMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEASUREMENT_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_ID | NUMBER |  | 18 |  | Goal id, a foreign key to HRG_GOALS table |
| MEASUREMENT_NAME | VARCHAR2 | 400 |  |  | Measurement Name |
| COMMENTS | VARCHAR2 | 4000 |  |  | Measurement comments |
| START_DATE | DATE |  |  |  | Measurement Start Date |
| END_DATE | DATE |  |  |  | Measurement End Date |
| DISPLAY_SEQUENCE | NUMBER |  | 9 |  | Display sequence of measurments |
| MIN_TARGET | NUMBER |  | 18 |  | Measurement field for MIN_TARGET |
| TARGET_PERCENTAGE | NUMBER |  | 18 |  | Measurement field for TARGET PERCENTAGE |
| MAX_TARGET | NUMBER |  | 18 |  | Measurement field for MAX TARGET |
| TARGET_VALUE | NUMBER |  | 18 |  | Measurement field for TARGET VALUE |
| ACTUAL_VALUE | NUMBER |  | 18 |  | Measurement field for ACTUAL VALUE |
| ACHIEVED_WEIGHT | NUMBER |  | 18 |  | Measurement field for ACHIEVED WEIGHT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MEASURE_TYPE_CODE | VARCHAR2 | 30 |  |  | MEASURE_TYPE_CODE |
| TARGET_TYPE | VARCHAR2 | 30 |  |  | TARGET_TYPE |
| UOM_CODE | VARCHAR2 | 30 |  |  | UOM_CODE |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_MEASUREMENTSN1_ | Non Unique | Default | MEASUREMENT_ID |
| HRG_GOAL_MEASUREMENTSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, MEASUREMENT_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
