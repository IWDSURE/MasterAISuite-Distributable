# HWR_DI_ACC_ACCESS_POINT_B

The access point table is used to store access points.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiaccaccesspointb-8176.html#hwrdiaccaccesspointb-8176](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiaccaccesspointb-8176.html#hwrdiaccaccesspointb-8176)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_ACC_ACCESS_POINT_B_PK | ACCESS_POINT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ACCESS_POINT_ID | NUMBER |  | 18 | Yes | This is the primary key for the access point tables. The number should be generated from the sequence. | Active |
| SOURCE_ID | NUMBER |  | 18 | Yes | The social media source ID. | Active |
| NAME | VARCHAR2 | 500 |  | Yes | The display name of the access point. | Active |
| CONNECTION_SPEC | CLOB |  |  | Yes | The connection spec for the access point. | Active |
| ACCESS_POINT_TYPE | VARCHAR2 | 64 |  |  | This stores the type of Access Point. | Active |
| UUID | VARCHAR2 | 255 |  | Yes | This is the universal unique id. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_DI_ACC_ACCESS_POINT_B_U1 | Unique | FUSION_TS_TX_DATA | ACCESS_POINT_ID | Active |
| HWR_DI_ACC_ACCESS_POINT_B_U2 | Unique | FUSION_TS_TX_DATA | UUID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
