# BEN_FF_EVAL_RSLT

BEN_FF_EVAL_RSLT contains statistical context name and its value or result name and its value of each formula that was run.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benffevalrslt-4041.html#benffevalrslt-4041](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benffevalrslt-4041.html#benffevalrslt-4041)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_FF_EVAL_RSLT_PK | DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| DATA_TYPE_CD | VARCHAR2 | 10 |  | Yes | Indicates the date type about context or result of formula run |
| NAME | VARCHAR2 | 32 |  |  | Indicates the context name or result name of formula run |
| VALUE | VARCHAR2 | 1024 |  |  | Indicates the context value or result value corresponding to the name of formula run |
| EVAL_REQ_ID | NUMBER |  | 18 | Yes | The Foreign Key to BEN_FF_EVAL table |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| ELIGY_PRFL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ELIGY_PRFL. Used to identify the eligibility profile that is evaluated. |
| MSG_TXT | VARCHAR2 | 4000 |  |  | Used to store the outcome of the evaluation. |
| MSG_DTLS | CLOB |  |  |  | Used to store the outcome of the evaluation. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_FF_EVAL_RSLT_FK1 | Non Unique | Default | EVAL_REQ_ID |
| BEN_FF_EVAL_RSLT_PK | Unique | Default | DATA_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
