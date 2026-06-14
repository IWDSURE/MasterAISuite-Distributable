# HWR_CNST_METRIC_B

This table stores constest metrics

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstmetricb-15856.html#hwrcnstmetricb-15856](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstmetricb-15856.html#hwrcnstmetricb-15856)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_METRIC_B_PK | CONTEST_METRIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_METRIC_ID | NUMBER |  | 18 | Yes | This is the primary key for the table. |
| CONTEST_ID | NUMBER |  | 18 |  | This is the foreign key of the table pointing to hwr_contest_b. |
| POINTS | NUMBER |  | 18 |  | This is the point of the contest. |
| NAME | VARCHAR2 | 512 |  |  | This is the name of the contest. |
| GOAL_ID | NUMBER |  | 18 |  | This is the goal id reference to the hwr_goal_f table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_METRIC_B_N1 | Non Unique | FUSION_TS_TX_DATA | GOAL_ID |
| HWR_CNST_METRIC_B_N2 | Non Unique | FUSION_TS_TX_DATA | CONTEST_ID |
| HWR_CNST_METRIC_B_U1 | Unique | FUSION_TS_TX_DATA | CONTEST_METRIC_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
