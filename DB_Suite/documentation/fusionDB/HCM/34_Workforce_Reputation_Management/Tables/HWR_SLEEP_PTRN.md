# HWR_SLEEP_PTRN

The sleep pattern table stores user sleep pattern data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsleepptrn-17959.html#hwrsleepptrn-17959](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsleepptrn-17959.html#hwrsleepptrn-17959)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SLEEP_PTRN_PK | USER_ID, SLEEP_PATTERN_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the wellness user table. |
| SLEEP_PATTERN_DATE | DATE |  |  | Yes | This is the date of the sleep pattern. |
| COLOR | VARCHAR2 | 20 |  |  | This is the color of the sleep pattern. |
| BED_TIME | NUMBER |  |  |  | This is the total bed time of the sleep pattern. |
| SLEEP_TIME | NUMBER |  |  |  | This is the total sleep time of the sleep pattern. |
| AWAKE_TIME | NUMBER |  |  |  | This is the total awake time of the sleep pattern. |
| SLEEP_NUMBER | NUMBER |  |  |  | This is the sleep number of the sleep pattern. |
| SCORE | NUMBER |  |  |  | This is the score of the sleep pattern. |
| WAKENINGS | NUMBER |  |  |  | This is the number of wakenings of the sleep pattern. |
| LOCATION | VARCHAR2 | 500 |  |  | This is the location of the sleep pattern. |
| SOURCE_ID | NUMBER |  | 18 |  | This is the source id of the sleep pattern. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SLEEP_PTRN_U1 | Unique | FUSION_TS_TX_DATA | USER_ID, SLEEP_PATTERN_DATE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
