# HWR_WLNS_GBL_SCORE

This table stores the wellness global score for each user per topic.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsgblscore-25085.html#hwrwlnsgblscore-25085](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsgblscore-25085.html#hwrwlnsgblscore-25085)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_GBL_SCORE_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| FUS_PROFILE_ID | NUMBER |  | 18 | Yes | This is the fusion profile ID of the employee. |
| TOPIC_ID | NUMBER |  | 18 | Yes | The wellness topic id. |
| RAW_SCORE | NUMBER |  |  |  | Raw score of the specific wellness topic across all sources. |
| PERCENTILE | NUMBER |  | 3 |  | Percentile rank of the user score compared with others. |
| STATUS | NUMBER |  |  | Yes | Indicates the status of score calculation. 2 score calculated, 1 obsolete record. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_GBL_SCORE_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
