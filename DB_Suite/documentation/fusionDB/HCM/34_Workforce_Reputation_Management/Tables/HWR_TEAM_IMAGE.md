# HWR_TEAM_IMAGE

The HWR Team Image Details are stored in this

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamimage-19249.html#hwrteamimage-19249](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamimage-19249.html#hwrteamimage-19249)

## Primary Key

| Name | Columns |
|------|----------|
| SYS_C002629080 | TEAM_IMAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_IMAGE_ID | NUMBER |  | 19 | Yes | TEAM_IMAGE_ID |
| TEAM_ID | NUMBER |  | 19 | Yes | TEAM_ID |
| IMAGE | BLOB |  |  |  | IMAGE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_IMAGE_U1 | Unique | FUSION_TS_TX_DATA | TEAM_IMAGE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
