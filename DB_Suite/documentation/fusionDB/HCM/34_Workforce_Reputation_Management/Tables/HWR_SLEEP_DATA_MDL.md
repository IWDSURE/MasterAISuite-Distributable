# HWR_SLEEP_DATA_MDL

The sleep data model table stores sleep model data for groups of users.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsleepdatamdl-21423.html#hwrsleepdatamdl-21423](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsleepdatamdl-21423.html#hwrsleepdatamdl-21423)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SLEEP_DATA_MDL_PK | KEY, TYPE |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| KEY | VARCHAR2 | 500 | Yes | This is the primary key for the sleep data model table. |
| TYPE | VARCHAR2 | 40 | Yes | This is the type of the sleep model data. |
| SLEEP_COUNT | NUMBER |  |  | This is the total sleep count of the sleep model data. |
| SLEEP_SCORE | NUMBER |  |  | This is the total sleep score of the sleep model data. |
| BED_TIME | NUMBER |  |  | This is the total bed time of the sleep model data. |
| SLEEP_TIME | NUMBER |  |  | This is the total sleep time of the sleep model data. |
| AWAKE_TIME | NUMBER |  |  | This is the total awake time of the sleep model data. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SLEEP_DATA_MDL_U1 | Unique | FUSION_TS_TX_DATA | KEY, TYPE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
