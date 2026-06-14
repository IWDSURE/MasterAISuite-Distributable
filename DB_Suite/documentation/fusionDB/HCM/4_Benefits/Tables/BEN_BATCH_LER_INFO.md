# BEN_BATCH_LER_INFO

BEN_BATCH_LER_INFO contains life event reason related data resulting from running concurrent manager processes. . BEN_BATCH tables store concurrent manager results so that this information is available for inclusion in reports, such as the activity summary report and audit log. This information is stored regardless of whether the process is run in validate (rollback) or commit mode.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchlerinfo-14435.html#benbatchlerinfo-14435](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchlerinfo-14435.html#benbatchlerinfo-14435)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_LER_INFO_PK | BATCH_LER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PEOPLE_F. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_LER_F. |
| LF_EVT_OCRD_DT | DATE |  |  | Yes | Life event occurred date. |
| REPLCD_FLAG | VARCHAR2 | 30 |  | Yes | Replaced Y or N. |
| CRTD_FLAG | VARCHAR2 | 30 |  | Yes | Created Y or N. |
| TMPRL_FLAG | VARCHAR2 | 30 |  | Yes | Temporal Y or N. |
| DLTD_FLAG | VARCHAR2 | 30 |  | Yes | Deleted Y or N. |
| OPEN_AND_CLSD_FLAG | VARCHAR2 | 30 |  | Yes | Open And Closed Y or N. |
| CLSD_FLAG | VARCHAR2 | 30 |  | Yes | Closed Y or N. |
| NOT_CRTD_FLAG | VARCHAR2 | 30 |  | Yes | Not Created Y or N. |
| STL_ACTV_FLAG | VARCHAR2 | 30 |  | Yes | Still Active Y or N. |
| PER_IN_LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PER_IN_LER. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CLPSD_FLAG | VARCHAR2 | 30 |  | Yes | Collapsed Y or N. |
| CLSN_FLAG | VARCHAR2 | 30 |  | Yes | Collision Y or N. |
| NO_EFFECT_FLAG | VARCHAR2 | 30 |  | Yes | No Effect Y or N. |
| CVRGE_RT_PREM_FLAG | VARCHAR2 | 30 |  | Yes | Coverage rate premium Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_LER_INFO_FK1 | Non Unique |  | BENEFIT_RELATION_ID |
| BEN_BATCH_LER_INFO_FK4 | Non Unique | Default | BENEFIT_ACTION_ID |
| BEN_BATCH_LER_INFO_FK5 | Non Unique | Default | PER_IN_LER_ID |
| BEN_BATCH_LER_INFO_N1 | Non Unique | Default | PERSON_ID |
| BEN_BATCH_LER_INFO_N2 | Non Unique | Default | LER_ID |
| BEN_BATCH_LER_INFO_PK1 | Unique | Default | BATCH_LER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
