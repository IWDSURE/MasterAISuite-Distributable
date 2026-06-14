# BEN_CRT_ORDR

BEN_CRT_ORDR  identifies orders issued by legislative bodies for a person and a plan or  a plan type.  A person may have multiple orders for the same plan covering different  related persons.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencrtordr-8576.html#bencrtordr-8576](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencrtordr-8576.html#bencrtordr-8576)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CRT_ORDR_PK | CRT_ORDR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRT_ORDR_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CRT_ORDR_TYP_CD | VARCHAR2 | 30 |  | Yes | Court order type. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| APLS_PERD_ENDG_DT | DATE |  |  |  | Applies period ending date. |
| APLS_PERD_STRTG_DT | DATE |  |  |  | Applies period starting date. |
| CRT_IDENT | VARCHAR2 | 90 |  |  | Court identifier. |
| DESCRIPTION | VARCHAR2 | 600 |  |  | Description. |
| DETD_QLFD_ORDR_DT | DATE |  |  |  | Determined qualified court order date. |
| ISSUE_DT | DATE |  |  |  | Issue date. |
| QDRO_AMT | NUMBER |  |  |  | Qualified Domestic Relations Order amount. |
| QDRO_DSTR_MTHD_CD | VARCHAR2 | 30 |  |  | Qualified Domestic Relations Order distribution method. |
| QDRO_PCT | NUMBER |  | 18 |  | Qualified Domestic Relations Order percent. |
| QDRO_NUM_PYMT_VAL | NUMBER |  | 18 |  | Qualified Domestic Relations Order  payment value. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PEOPLE_F. |
| QDRO_PER_PERD_CD | VARCHAR2 | 30 |  |  | Qualified Domestic Relations Order person period. |
| RCVD_DT | DATE |  |  |  | Received date. |
| UOM | VARCHAR2 | 30 |  |  | Unit of measure. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| CRT_ISSNG | VARCHAR2 | 180 |  |  | Issuing court. |
| CRT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| CRT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| CRT_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PL_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_TYP_F. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_CRT_ORDR_N1 | Non Unique | PERSON_ID |
| BEN_CRT_ORDR_N2 | Non Unique | PL_ID |
| BEN_CRT_ORDR_N3 | Non Unique | PL_TYP_ID |
| BEN_CRT_ORDR_PK1 | Unique | CRT_ORDR_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
