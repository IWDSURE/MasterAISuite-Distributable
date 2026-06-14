# BEN_BATCH_PROC_INFO

BEN_BATCH_PROC_INFO  contains statistical data about each benefits concurrent manager process that was run.  It includes information such as the start and end time of the job, elapsed time, number of persons processed, and the number of errors generated.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchprocinfo-13662.html#benbatchprocinfo-13662](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchprocinfo-13662.html#benbatchprocinfo-13662)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_PROC_INFO_PK | BATCH_PROC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_PROC_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| STRT_DT | DATE |  |  |  | Start date. |
| END_DT | DATE |  |  |  | End date. |
| STRT_TM | VARCHAR2 | 90 |  |  | Start time. |
| END_TM | VARCHAR2 | 90 |  |  | End time. |
| ELPSD_TM | VARCHAR2 | 90 |  |  | Elapsed time. |
| PER_SLCTD | NUMBER |  | 18 |  | Number of persons selected. |
| PER_PROC | NUMBER |  | 18 |  | Number of persons processed. |
| PER_UNPROC | NUMBER |  | 18 |  | Number of persons un-processed. |
| PER_PROC_SUCC | NUMBER |  | 18 |  | Number of persons processed successfully. |
| PER_ERR | NUMBER |  | 18 |  | Number of persons with errors. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_PROC_INFO_FK1 | Non Unique |  | BENEFIT_RELATION_ID |
| BEN_BATCH_PROC_INFO_FK3 | Non Unique | Default | BENEFIT_ACTION_ID |
| BEN_BATCH_PROC_INFO_PK1 | Unique | Default | BATCH_PROC_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
