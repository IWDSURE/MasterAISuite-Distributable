# BEN_PTNL_LER_FOR_PER

BEN_PTNL_LER_FOR_PER for a person is an occurrence of data change detection in person indicative data for a person, an event that is detected as a result of the examination of the passage of time, or a scheduled event that is explicitly assigned to the person.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benptnllerforper-18274.html#benptnllerforper-18274](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benptnllerforper-18274.html#benptnllerforper-18274)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PTNL_LER_FOR_PER_PK | PTNL_LER_FOR_PER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PTNL_LER_FOR_PER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CLPSED_BY | VARCHAR2 | 240 |  |  | This column holds CLPSED_BY value |
| PTNL_ADDNL_CHAR1 | VARCHAR2 | 2000 |  |  | This column holds PTNL_ADDNL_CHAR1 |
| PTNL_ADDNL_CHAR2 | VARCHAR2 | 2000 |  |  | This column holds PTNL_ADDNL_CHAR2 |
| PTNL_ADDNL_CHAR3 | VARCHAR2 | 2000 |  |  | This column holds PTNL_ADDNL_CHAR3 |
| PTNL_ADDNL_DATE1 | DATE |  |  |  | This column holds PTNL_ADDNL_DATE1 |
| PTNL_ADDNL_DATE2 | DATE |  |  |  | This column holds PTNL_ADDNL_DATE2 |
| PTNL_ADDNL_DATE3 | DATE |  |  |  | This column holds PTNL_ADDNL_DATE3 |
| PTNL_ADDNL_NUMBER1 | NUMBER |  |  |  | This column holds PTNL_ADDNL_NUMBER1 |
| PTNL_ADDNL_NUMBER2 | NUMBER |  |  |  | This column holds PTNL_ADDNL_NUMBER2 |
| PTNL_ADDNL_NUMBER3 | NUMBER |  |  |  | This column holds PTNL_ADDNL_NUMBER3 |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LF_EVT_OCRD_DT | DATE |  |  | Yes | This column holds Life event occurred date. |
| LER_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to BEN_LER_F. |
| PTNL_LER_FOR_PER_STAT_CD | VARCHAR2 | 30 |  | Yes | Potential life event reason for person status. |
| PTNL_LER_FOR_PER_SRC_CD | VARCHAR2 | 30 |  |  | Potential life event reason for person source. |
| NTFN_DT | DATE |  |  |  | This column holds Notification date. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column holds Foreign Key to PER_PEOPLE_F. |
| DTCTD_DT | DATE |  |  |  | This column holds Detected date. |
| PROCD_DT | DATE |  |  |  | This column holds Processed date. |
| UNPROCD_DT | DATE |  |  |  | This column holds Unprocessed Date. |
| VOIDD_DT | DATE |  |  |  | This column holds Voided date value. |
| MNL_DT | DATE |  |  |  | This column holds Manual date value. |
| ENRT_PERD_ID | NUMBER |  | 18 |  | This column holds Foreign key to BEN_ENRT_PERD. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | Concurrent Program who column - date when a program last updated this row). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MNLO_DT | DATE |  |  |  | This column holds Manual override date. |
| CSD_BY_PTNL_LER_FOR_PER_ID | NUMBER |  | 18 |  | Foreign key to BEN_CSD_BY_PTNL_LER_FOR_PER_F. |
| TRGR_TABLE_PK_ID | NUMBER |  | 18 |  | This column holds Triggering table primary key. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | This column holds BENEFIT_RELATION_ID |
| LER_TYPE_CD | VARCHAR2 | 30 |  |  | This column holds LER_TYPE_CD value |
| PROD_CD | VARCHAR2 | 30 |  |  | This column holds PROD_CD value |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_APP_NAME |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column holds PROGRAM_NAME value |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This column holds Legal Entity Id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PTNL_LER_FOR_PER_FK1 | Non Unique |  | BENEFIT_RELATION_ID |
| BEN_PTNL_LER_FOR_PER_FK2 | Non Unique | Default | CSD_BY_PTNL_LER_FOR_PER_ID |
| BEN_PTNL_LER_FOR_PER_FK4 | Non Unique | Default | ENRT_PERD_ID |
| BEN_PTNL_LER_FOR_PER_N1 | Non Unique | Default | LER_ID |
| BEN_PTNL_LER_FOR_PER_N2 | Non Unique | Default | PERSON_ID |
| BEN_PTNL_LER_FOR_PER_N3 | Non Unique | Default | PTNL_LER_FOR_PER_STAT_CD, LF_EVT_OCRD_DT |
| BEN_PTNL_LER_FOR_PER_PK | Unique | Default | PTNL_LER_FOR_PER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
