# HWR_SOC_MED_ROLE_PRFL_B

This table stores the Global Profiles to be used in Social Media Role

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedroleprflb-28474.html#hwrsocmedroleprflb-28474](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedroleprflb-28474.html#hwrsocmedroleprflb-28474)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SOC_MED_ROLE_PRFL_B_PK | GBL_PRFL_ID, PRFL_TIMESTAMP |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | This stores the global profile Id of the consumer |
| PRFL_TIMESTAMP | TIMESTAMP |  |  | Yes | This stores the time stamp when the profile Id is created |
| DURATION | NUMBER |  |  |  | This stores the duration value of the profile. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SOC_MED_ROLE_PRFL_B_U1 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID, PRFL_TIMESTAMP |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
