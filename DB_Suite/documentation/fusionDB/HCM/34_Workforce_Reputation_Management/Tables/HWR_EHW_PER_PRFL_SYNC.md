# HWR_EHW_PER_PRFL_SYNC

The configuration table stores information about Social Network User required for applications used in EHW project.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrehwperprflsync-4414.html#hwrehwperprflsync-4414](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrehwperprflsync-4414.html#hwrehwperprflsync-4414)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_EHW_PER_PRFL_SYNC_PK | PRFL_ID, SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the ID of the profile for which profile sync info is stored. |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| AUTH_TOKEN | VARCHAR2 | 2048 |  | Yes | This is the authentication token for the profile. |
| REFRESH_TOKEN | VARCHAR2 | 2048 |  |  | This is the refresh token for the profile. |
| TOKEN_TYPE | VARCHAR2 | 2048 |  | Yes | This is the token type for the profile. |
| AUTH_SECRET | VARCHAR2 | 2048 |  |  | This is the authentication secret for the profile. |
| AUTH_EXPIRATION_DATE | TIMESTAMP |  |  |  | This is authentication expiration date. |
| STATE_DATA | VARCHAR2 | 4000 |  |  | This identifies the state of profile synchronization. |
| META_DATA | VARCHAR2 | 4000 |  |  | This is additional metadata that may be used for the connector. |
| STATE | NUMBER |  |  |  | This is an enumeration describing registered or unregistered state. |
| LAST_SYNC_ACTIVITY | TIMESTAMP |  |  |  | This is the last sync date of the profile. |
| LINKED_PRFL_ID | VARCHAR2 | 500 |  |  | This is the ID of the profile with which profile sync info is linked. |
| LINKED_SOURCE_ID | NUMBER |  | 18 |  | This is the ID of the source with which profile sync info is linked. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_EHW_PER_PRFL_SYNC_N1 | Non Unique | Default | SOURCE_ID, PRFL_ID |
| HWR_EHW_PER_PRFL_SYNC_U1 | Unique | Default | PRFL_ID, SOURCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
