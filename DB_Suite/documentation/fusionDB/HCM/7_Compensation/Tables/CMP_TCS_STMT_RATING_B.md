# CMP_TCS_STMT_RATING_B

Stores data from Total Compensation Setup's Feedback Rating

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtratingb-10897.html#cmptcsstmtratingb-10897](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtratingb-10897.html#cmptcsstmtratingb-10897)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_RATING_B_PK | STMT_RATING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_RATING_ID | NUMBER |  | 18 | Yes | STMT_RATING_ID |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| RATING_CODE | VARCHAR2 | 30 |  |  | RATING_CODE |
| ORDER_NUM | NUMBER |  | 18 |  | ORDER_NUM |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_RATING_B_FK1 | Non Unique | Default | STMT_ID, STMT_PERD_ID |
| CMP_TCS_STMT_RATING_B_U1 | Unique | Default | STMT_RATING_ID |
| CMP_TCS_STMT_RATING_B_U2 | Unique | Default | PERD_RUN_ID, RATING_CODE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
