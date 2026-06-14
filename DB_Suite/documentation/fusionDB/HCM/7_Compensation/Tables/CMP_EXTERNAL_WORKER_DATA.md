# CMP_EXTERNAL_WORKER_DATA

Stroes external data inforamtion entered by customer using Mana External Data UI or Spreadsheet Loader.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpexternalworkerdata-9157.html#cmpexternalworkerdata-9157](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpexternalworkerdata-9157.html#cmpexternalworkerdata-9157)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_EXTERNAL_WORKER_DATA_PK | EXTERNAL_WORKER_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTERNAL_WORKER_DATA_ID | NUMBER |  | 18 | Yes | EXTERNAL_WORKER_DATA_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity Id |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | Worker Number |
| RECORD_TYPE_CD | VARCHAR2 | 30 |  | Yes | Record Type Code |
| START_DATE | DATE |  |  | Yes | Start Date |
| END_DATE | DATE |  |  |  | End Date |
| SEQUENCE_NUMBER | NUMBER |  |  |  | Sequence Number |
| CURRENCY_CD | VARCHAR2 | 30 |  |  | Currency Code |
| VALUE1 | VARCHAR2 | 2000 |  |  | VALUE1 |
| VALUE2 | VARCHAR2 | 2000 |  |  | VALUE2 |
| VALUE3 | VARCHAR2 | 2000 |  |  | VALUE3 |
| VALUE4 | VARCHAR2 | 2000 |  |  | VALUE4 |
| VALUE5 | VARCHAR2 | 2000 |  |  | VALUE5 |
| VALUE6 | VARCHAR2 | 2000 |  |  | VALUE6 |
| VALUE7 | VARCHAR2 | 2000 |  |  | VALUE7 |
| VALUE8 | VARCHAR2 | 2000 |  |  | VALUE8 |
| VALUE9 | VARCHAR2 | 2000 |  |  | VALUE9 |
| VALUE10 | VARCHAR2 | 2000 |  |  | VALUE10 |
| VALUE11 | VARCHAR2 | 2000 |  |  | VALUE11 |
| VALUE12 | VARCHAR2 | 2000 |  |  | VALUE12 |
| VALUE13 | VARCHAR2 | 2000 |  |  | VALUE13 |
| VALUE14 | VARCHAR2 | 2000 |  |  | VALUE14 |
| VALUE15 | VARCHAR2 | 2000 |  |  | VALUE15 |
| VALUE16 | VARCHAR2 | 2000 |  |  | VALUE16 |
| VALUE17 | VARCHAR2 | 2000 |  |  | VALUE17 |
| VALUE18 | VARCHAR2 | 2000 |  |  | VALUE18 |
| VALUE19 | VARCHAR2 | 2000 |  |  | VALUE19 |
| VALUE20 | VARCHAR2 | 2000 |  |  | VALUE20 |
| VALUE21 | VARCHAR2 | 2000 |  |  | VALUE21 |
| VALUE22 | VARCHAR2 | 2000 |  |  | VALUE22 |
| VALUE23 | VARCHAR2 | 2000 |  |  | VALUE23 |
| VALUE24 | VARCHAR2 | 2000 |  |  | VALUE24 |
| VALUE25 | VARCHAR2 | 2000 |  |  | VALUE25 |
| VALUE26 | VARCHAR2 | 2000 |  |  | VALUE26 |
| VALUE27 | VARCHAR2 | 2000 |  |  | VALUE27 |
| VALUE28 | VARCHAR2 | 2000 |  |  | VALUE28 |
| VALUE29 | VARCHAR2 | 2000 |  |  | VALUE29 |
| VALUE30 | VARCHAR2 | 2000 |  |  | VALUE30 |
| VALUE31 | VARCHAR2 | 2000 |  |  | VALUE31 |
| VALUE32 | VARCHAR2 | 2000 |  |  | VALUE32 |
| VALUE33 | VARCHAR2 | 2000 |  |  | VALUE33 |
| VALUE34 | VARCHAR2 | 2000 |  |  | VALUE34 |
| VALUE35 | VARCHAR2 | 2000 |  |  | VALUE35 |
| VALUE36 | VARCHAR2 | 2000 |  |  | VALUE36 |
| VALUE37 | VARCHAR2 | 2000 |  |  | VALUE37 |
| VALUE38 | VARCHAR2 | 2000 |  |  | VALUE38 |
| VALUE39 | VARCHAR2 | 2000 |  |  | VALUE39 |
| VALUE40 | VARCHAR2 | 2000 |  |  | VALUE40 |
| VALUE41 | VARCHAR2 | 2000 |  |  | VALUE41 |
| VALUE42 | VARCHAR2 | 2000 |  |  | VALUE42 |
| VALUE43 | VARCHAR2 | 2000 |  |  | VALUE43 |
| VALUE44 | VARCHAR2 | 2000 |  |  | VALUE44 |
| VALUE45 | VARCHAR2 | 2000 |  |  | VALUE45 |
| VALUE46 | VARCHAR2 | 2000 |  |  | VALUE46 |
| VALUE47 | VARCHAR2 | 2000 |  |  | VALUE47 |
| VALUE48 | VARCHAR2 | 2000 |  |  | VALUE48 |
| VALUE49 | VARCHAR2 | 2000 |  |  | VALUE49 |
| VALUE50 | VARCHAR2 | 2000 |  |  | VALUE50 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_EXTERNAL_WORKER_DATA_N1 | Non Unique | Default | PERSON_ID, START_DATE, ASSIGNMENT_ID |
| CMP_EXTERNAL_WORKER_DATA_U1 | Unique | Default | EXTERNAL_WORKER_DATA_ID |
| CMP_EXTERNAL_WORKER_DATA_UK1 | Unique | Default | START_DATE, RECORD_TYPE_CD, PERSON_ID, LEGAL_ENTITY_ID, ASSIGNMENT_ID, SEQUENCE_NUMBER |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
