# HWR_FLW_FLOW_B

The flow table is used to store flows.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwflowb-21953.html#hwrflwflowb-21953](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwflowb-21953.html#hwrflwflowb-21953)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FLW_FLOW_B_PK | FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FLOW_ID | NUMBER |  | 18 | Yes | This is the primary key of the fow table. | Active |
| SOURCE_ID | NUMBER |  | 18 | Yes | The social media source ID. | Active |
| UUID | VARCHAR2 | 255 |  | Yes | This is the generated instance identifier associated to this flow. | Active |
| NAME | VARCHAR2 | 255 |  | Yes | The display name value for the flow. | Active |
| IS_SEEDED_DATA | VARCHAR2 | 1 |  | Yes | A flag to indicate the whether the flow is seeded: Y for yes; N for no. | Active |
| IS_INTERNAL | VARCHAR2 | 1 |  | Yes | A flag to indicate the internal state: Y for yes; N for no. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_FLW_FLOW_B_U1 | Unique | FUSION_TS_TX_DATA | FLOW_ID | Active |
| HWR_FLW_FLOW_B_U2 | Unique | FUSION_TS_TX_DATA | UUID | Active |
| HWR_FLW_FLOW_B_U4 | Unique | FUSION_TS_TX_DATA | NAME, SOURCE_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
