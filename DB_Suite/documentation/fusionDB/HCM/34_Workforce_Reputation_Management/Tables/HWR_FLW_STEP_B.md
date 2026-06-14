# HWR_FLW_STEP_B

The step table is used to store steps.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwstepb-29873.html#hwrflwstepb-29873](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwstepb-29873.html#hwrflwstepb-29873)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FLW_STEP_B_PK | STEP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| STEP_ID | NUMBER |  | 18 | Yes | This is the primary key of the step table. | Active |
| FLOW_ID | NUMBER |  | 18 | Yes | The flow id of the flow containing this step. | Active |
| UUID | VARCHAR2 | 255 |  | Yes | This is the generated instance identifier associated to this step. | Active |
| NAME | VARCHAR2 | 255 |  | Yes | The display name value for the step. | Active |
| FLOW_COMP_UUID | VARCHAR2 | 255 |  |  | The flow component identifier of this step. | Active |
| STEP_CONFIG | CLOB |  |  | Yes | This is the serialized step configuration. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_FLW_STEP_B_U1 | Unique | FUSION_TS_TX_DATA | STEP_ID | Active |
| HWR_FLW_STEP_B_U2 | Unique | FUSION_TS_TX_DATA | UUID | Active |
| HWR_FLW_STEP_B_U3 | Unique | FUSION_TS_TX_DATA | STEP_ID, FLOW_ID | Active |
| HWR_FLW_STEP_B_U4 | Unique | FUSION_TS_TX_DATA | FLOW_ID, NAME | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
