# HWR_PER_PRFL_SYNC

The configuration table stores information about Social Network User required for IConnector queries for applications used in HWR project.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprflsync-27289.html#hwrperprflsync-27289](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperprflsync-27289.html#hwrperprflsync-27289)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_PRFL_SYNC_PK | PRFL_ID, SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the ID of the profile for which profile sync info is stored. |
| SOURCE_ID | NUMBER |  | 18 | Yes | This represents the data source. |
| AUTH_TOKEN | VARCHAR2 | 2500 |  |  | This is the authentication token for the profile. |
| REFRESH_TOKEN | VARCHAR2 | 2500 |  |  | This is the refresh token for the profile. |
| TOKEN_TYPE | VARCHAR2 | 800 |  |  | This is the token type for the profile. |
| AUTH_SECRET | VARCHAR2 | 800 |  |  | This is the authentication secret for the profile. |
| AUTH_EXPIRATION_DATE | TIMESTAMP |  |  |  | This is authentication expiration date. |
| STATE_DATA | VARCHAR2 | 4000 |  |  | This identifies the state of profile synchronization. |
| META_DATA | VARCHAR2 | 4000 |  |  | This is additional metadata that may be used for the connector. |
| STATE | NUMBER |  |  |  | This is an enumeration describing registered or unregistered state. |
| LAST_DWNLD_DT_PRFL_CORE | TIMESTAMP |  |  |  | This is the last download date of the profile core. |
| LAST_DWNLD_DT_PRFL_RLTNS | TIMESTAMP |  |  |  | This is the last download date of the profile relations. |
| LAST_DWNLD_DT_PRFL_POSTS | TIMESTAMP |  |  |  | This is the last download date of the profile posts. |
| GBL_PRFL_ID | NUMBER |  | 18 |  | This is the global profile Id associated with the profile sync. |
| LINKED_PRFL_ID | VARCHAR2 | 500 |  |  | This is the ID of the profile with which profile sync info is linked. |
| LINKED_SOURCE_ID | NUMBER |  | 18 |  | This is the ID of the source with which profile sync info is linked. |
| HWR_SHARING_ENABLED | NUMBER |  | 18 | Yes | This indicates whether user has opted in for sharing of HWR updates or not. 0 --> False, 1--> True. Default is False; |
| HHR_SHARING_ENABLED | NUMBER |  | 18 | Yes | This indicates whether user has opted in for sharing of HHR updates or not. 0 --> False, 1--> True. Default is False; |
| EHW_SHARING_ENABLED | NUMBER |  | 18 | Yes | This indicates whether user has opted in for sharing of EHW updates or not. 0 --> False, 1--> True. Default is False; |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PER_PRFL_SYNC_N1 | Non Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID |
| HWR_PER_PRFL_SYNC_U1 | Unique | FUSION_TS_TX_DATA | PRFL_ID, SOURCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
