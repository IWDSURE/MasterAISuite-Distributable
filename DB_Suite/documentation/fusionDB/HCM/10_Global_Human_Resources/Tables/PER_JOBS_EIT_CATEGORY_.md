# PER_JOBS_EIT_CATEGORY_

Jobs intermediate table storing  Extensible Flexfield  Category Code for each job

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobseitcategory-31274.html#perjobseitcategory-31274](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobseitcategory-31274.html#perjobseitcategory-31274)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_EIT_CATEGORY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | JOB_ID |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Extensible Flexfield Category Code |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_JOBS_EIT_CATEGORYN1_ | Non Unique | Default | JOB_ID |
| PER_JOBS_EIT_CATEGORY_U1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, JOB_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
