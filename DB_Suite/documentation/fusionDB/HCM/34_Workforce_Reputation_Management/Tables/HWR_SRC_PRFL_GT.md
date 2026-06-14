# HWR_SRC_PRFL_GT

This is a global temporary table for sourceId and profileId.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrcprflgt-31322.html#hwrsrcprflgt-31322](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrcprflgt-31322.html#hwrsrcprflgt-31322)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the source id from the HWR_SRC_SOURCE_B table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the source profile id from the HWR_PER_PROFILE_B table. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
