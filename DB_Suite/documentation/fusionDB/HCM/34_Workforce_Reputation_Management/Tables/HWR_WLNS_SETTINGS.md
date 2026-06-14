# HWR_WLNS_SETTINGS

This table stores wellness coach details.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnssettings-17249.html#hwrwlnssettings-17249](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnssettings-17249.html#hwrwlnssettings-17249)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_SETTINGS_PK | SETTINGS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETTINGS_ID | NUMBER |  | 18 | Yes | This is the primary key for the hwr_wlns_settings tables. |
| FEATURE | VARCHAR2 | 32 |  | Yes | This column indicated the feature enum for which the setting is stored. |
| IS_ACTIVE | VARCHAR2 | 5 |  | Yes | This column indicates the active status for the feature over wellness settings table. Y active or N not active. |
| EFFECTIVE_START_DATE | TIMESTAMP |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | TIMESTAMP |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SETTINGS_ATTR_1 | VARCHAR2 | 400 |  |  | This column stores extra wellness settings attribute 1. |
| SETTINGS_ATTR_2 | VARCHAR2 | 400 |  |  | This column stores extra wellness settings attribute 2. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_SETTINGS_U1 | Unique | Default | SETTINGS_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
