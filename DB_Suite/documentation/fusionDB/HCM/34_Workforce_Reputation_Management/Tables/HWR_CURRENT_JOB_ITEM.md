# HWR_CURRENT_JOB_ITEM

This is HWR table to store current job item details.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcurrentjobitem-19792.html#hwrcurrentjobitem-19792](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcurrentjobitem-19792.html#hwrcurrentjobitem-19792)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CURRENT_JOB_ITEM_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | This is the primary key job id for this table | Active |
| JOB_RUN_ID | NUMBER |  | 18 | Yes | This is the job run id column for current job item table. | Active |
| PARENT_JOB_ID | NUMBER |  | 18 |  | This is the parent job id column for the current job item table. | Active |
| STATUS | VARCHAR2 | 20 |  | Yes | This is the status column on current job item table. | Active |
| HAS_STARTED | VARCHAR2 | 1 |  |  | This is the has started column on current job item table. | Active |
| SCHEDULER_ID | VARCHAR2 | 255 |  |  | This is the scheduler id column on current job item table. | Active |
| JOB | CLOB |  |  |  | This is the job column on current job item table. | Active |
| APPLICATION_CODE | VARCHAR2 | 10 |  | Yes | This is the application of the current job item. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_CURRENT_JOB_ITEM_U1 | Unique | FUSION_TS_TX_DATA | JOB_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
