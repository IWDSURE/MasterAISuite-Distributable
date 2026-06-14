# HWR_PROJECT_TASK_XREF

This cross reference (xref) table stores the relation between project and tasks in the project.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprojecttaskxref-20973.html#hwrprojecttaskxref-20973](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprojecttaskxref-20973.html#hwrprojecttaskxref-20973)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PROJECT_TASK_XREF_PK | PROJECT_ID, TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROJECT_ID | NUMBER |  | 18 | Yes | This is the primary key for the project table. |
| TASK_ID | NUMBER |  | 18 | Yes | This is the primary key for the task table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PROJECT_TASK_XREF_N1 | Non Unique | FUSION_TS_TX_DATA | TASK_ID |
| HWR_PROJECT_TASK_XREF_U1 | Unique | FUSION_TS_TX_DATA | PROJECT_ID, TASK_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
