# CEL_GLOBAL_OPTIONS

Table to hold global preferences of recognition and award programs.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celglobaloptions-31781.html#celglobaloptions-31781](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celglobaloptions-31781.html#celglobaloptions-31781)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_GLOBAL_OPTIONS_PK | GLOBAL_OPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GLOBAL_OPTION_ID | NUMBER |  | 18 | Yes | Global Option Identifier |
| POINTS_TIME_UNIT_CODE | VARCHAR2 | 30 |  |  | Code that indicates the time unit of recurring points |
| USE_POINTS_FLAG | VARCHAR2 | 1 |  |  | Y/N to indicate if new program by default uses points |
| POINTS | NUMBER |  |  |  | Recurring points to allocate to persons |
| POINTS_START_DATE | DATE |  |  |  | Points start date |
| REDEEM_POINTS_CASH_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if points can be redeemed as cash |
| REDEEM_POINT_VALUE | NUMBER |  |  |  | Cash conversion rate per point |
| REDEEM_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Currency code used for points redemption to cash |
| ALLOW_VISIBILITY_CHANGE_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates if visibility options page is enabled for employees |
| NOMINATIONS_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates whether nominations are enabled |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_GLOBAL_OPTIONS_PK | Unique | Default | GLOBAL_OPTION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
