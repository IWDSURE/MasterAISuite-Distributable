# HWR_FLW_SYNC_STATE

The flow sync state stores serialized flow sync state information.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwsyncstate-4949.html#hwrflwsyncstate-4949](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwsyncstate-4949.html#hwrflwsyncstate-4949)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FLW_SYNC_STATE_PK | FLOW_ID, ENVIRONMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FLOW_ID | NUMBER |  | 18 | Yes | This is the primary key of the flow table. | Active |
| ENVIRONMENT_ID | NUMBER |  | 18 | Yes | This is the primary key of the environment table. | Active |
| LAST_RUN_DATE | TIMESTAMP |  |  |  | This represent the last time the flow last run | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_FLW_SYNC_STATE_N1 | Non Unique | FUSION_TS_TX_DATA | ENVIRONMENT_ID |  |
| HWR_FLW_SYNC_STATE_U1 | Unique | FUSION_TS_TX_DATA | FLOW_ID, ENVIRONMENT_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
