# BEN_BATCH_ACTN_ITEM_INFO

BEN_BATCH_ITEM_INFO  contains action item related data resulting from running concurrent manager processes. . BEN_BATCH tables store concurrent manager results so that this information is available for inclusion in reports, such as the activity summary report and audit log. This information is stored regardless of whether the process is run in validate (rollback) or commit mode.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchactniteminfo-13794.html#benbatchactniteminfo-13794](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchactniteminfo-13794.html#benbatchactniteminfo-13794)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_ACTN_ITEM_INFO_PK | BATCH_ACTN_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ACTN_ITEM_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PEOPLE_F. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| ACTN_TYP_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTN_TYP_F. |
| CMPLTD_DT | DATE |  |  |  | Completed date. |
| DUE_DT | DATE |  |  |  | Due date. |
| RQD_FLAG | VARCHAR2 | 30 |  |  | Required Y or N. |
| ACTN_CD | VARCHAR2 | 30 |  |  | Action code. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BATCH_ACTN_ITEM_INFO_N2 | Non Unique | Default | PERSON_ID |
| BEN_BATCH_ACTN_ITEM_INFO_PK1 | Unique | Default | BATCH_ACTN_ITEM_ID |
| BEN_BATCH_AC_ITM_INFO_FK1 | Non Unique | Default | BENEFIT_ACTION_ID |
| BEN_BATCH_AC_ITM_INFO_FK2 | Non Unique | Default | BENEFIT_RELATION_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
