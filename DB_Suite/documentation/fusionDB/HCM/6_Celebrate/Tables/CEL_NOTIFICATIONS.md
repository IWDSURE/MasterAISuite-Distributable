# CEL_NOTIFICATIONS

Stores parameters for various notifications generated for rewards and recognition programs

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celnotifications-20885.html#celnotifications-20885](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celnotifications-20885.html#celnotifications-20885)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_NOTIFICATIONS_PK | NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTIFICATION_ID | NUMBER |  | 18 | Yes | Unique identifier for a notification |
| NOTIFICATION_TYPE | VARCHAR2 | 30 |  | Yes | Notification type |
| STATUS | VARCHAR2 | 30 |  |  | Status of the notification |
| PARAM1_VAL | VARCHAR2 | 240 |  |  | First parameter value |
| PARAM2_VAL | VARCHAR2 | 240 |  |  | Second parameter value |
| PARAM3_VAL | VARCHAR2 | 240 |  |  | Third parameter value |
| PARAM4_VAL | VARCHAR2 | 240 |  |  | Fourth parameter value |
| PARAM5_VAL | VARCHAR2 | 240 |  |  | Fifth parameter value |
| PARAM6_VAL | VARCHAR2 | 240 |  |  | Sixth parameter value |
| PARAM7_VAL | VARCHAR2 | 240 |  |  | Seventh parameter value |
| PARAM8_VAL | VARCHAR2 | 240 |  |  | Eighth parameter value |
| PARAM9_VAL | VARCHAR2 | 240 |  |  | Ninth parameter value |
| PARAM10_VAL | VARCHAR2 | 240 |  |  | Tenth parameter value |
| PARAM11_VAL | VARCHAR2 | 240 |  |  | Eleventh parameter value |
| PARAM12_VAL | VARCHAR2 | 240 |  |  | Twelfth parameter value |
| PARAM13_VAL | VARCHAR2 | 240 |  |  | Thirteenth parameter value |
| PARAM14_VAL | VARCHAR2 | 240 |  |  | Fourteenth parameter value |
| PARAM15_VAL | VARCHAR2 | 240 |  |  | Fifteenth parameter value |
| PARAM16_VAL | VARCHAR2 | 240 |  |  | Sixteenth parameter value |
| PARAM17_VAL | VARCHAR2 | 240 |  |  | Seventeenth parameter value |
| PARAM18_VAL | VARCHAR2 | 240 |  |  | Eighteenth parameter value |
| PARAM19_VAL | VARCHAR2 | 2000 |  |  | Nineteenth parameter value |
| PARAM20_VAL | VARCHAR2 | 2000 |  |  | Twentieth parameter value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_NOTIFICATIONS_N1 | Non Unique | Default | PARAM1_VAL, NOTIFICATION_TYPE |
| CEL_NOTIFICATIONS_PK | Unique | Default | NOTIFICATION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
