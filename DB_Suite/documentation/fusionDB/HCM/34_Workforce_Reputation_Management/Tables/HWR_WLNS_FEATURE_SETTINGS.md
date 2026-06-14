# HWR_WLNS_FEATURE_SETTINGS

This table stores the wellness feature settings

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsfeaturesettings-25871.html#hwrwlnsfeaturesettings-25871](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsfeaturesettings-25871.html#hwrwlnsfeaturesettings-25871)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_FEATURE_SETTINGS_PK | FEATURE_SETTINGS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEATURE_SETTINGS_ID | NUMBER |  | 18 | Yes | This column indicates the wellness feature settings Id |
| IS_ACTIVE | VARCHAR2 | 1 |  | Yes | This column indicates the active row of  Wellness feature settings table |
| IS_WELLNESS_POINTS_ENABLED | NUMBER |  | 18 | Yes | This is column indicates wellness points enabled/distabled. 0 is disabled and 1 is enabled |
| IS_RESET_POINTS_ENABLED | NUMBER |  | 18 | Yes | This is column indicates Reset enabled/distabled. 0 is disabled and 1 is enabled |
| IS_CT_INTEGRATION_ENABLED | NUMBER |  | 18 |  | This column indicates CT reward integration is enabled/disabled. 0 is disabled and 1 is enabled |
| POINTS_RESET_MONTH | VARCHAR2 | 20 |  | Yes | This column stores the month of the reset date |
| POINTS_RESET_DAY | VARCHAR2 | 20 |  | Yes | This column stores the day of the reset date |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_FEATURE_SETTINGS_U1 | Unique | FUSION_TS_TX_DATA | FEATURE_SETTINGS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
