# HWP_DATA_INPUT_PROCESS

Data input process master table

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdatainputprocess-11528.html#hwpdatainputprocess-11528](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdatainputprocess-11528.html#hwpdatainputprocess-11528)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_DATA_INPUT_PROCESS_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Data Input process ID. |
| PROCESS_DATE | DATE |  |  |  | Data input process date. |
| MODEL_CODE | VARCHAR2 | 200 |  |  | Data input model code. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_DATA_INPUT_PROCESS_PK | Unique | Default | PROCESS_ID |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
