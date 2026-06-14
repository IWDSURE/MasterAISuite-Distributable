# BEN_BILL_ENRT_RSLT_

This table is used to store the enrollment details for bill

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillenrtrslt-30541.html#benbillenrtrslt-30541](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillenrtrslt-30541.html#benbillenrtrslt-30541)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_ENRT_RSLT_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, BILL_ENRT_RSLT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_ENRT_RSLT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign key to ben_benefit_relations_f. |
| ORGNL_PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | This column holds original enrollment result ID. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This column holds foreign Key LEGAL_ENTITY_ID. |
| ENRT_CVG_STRT_DT | DATE |  |  |  | This column holds  Enrollment Coverage Start Date |
| ORGNL_ENRT_DT | DATE |  |  |  | This column holds Original Enrollment Date. |
| ENRT_CVG_THRU_DT | DATE |  |  |  | This column holds Enrollment Coverage Thru date. |
| ELECTION_DATE | DATE |  |  |  | This column holds Elections made date. |
| BNFT_AMT | NUMBER |  |  |  | This column holds coverage amount. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to per_all_people_f. |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This is a foreign key to ben_per_in_ler. |
| LER_ID | NUMBER |  | 18 |  | This is a foreign key to ben_ler_f. |
| LER_TYP_CD | VARCHAR2 | 30 |  |  | This is a foreign key to ben_ler_f. |
| PGM_ID | NUMBER |  | 18 |  | This is a foreign key to ben_pgm_f. |
| PL_ID | NUMBER |  | 18 |  | This is a foreign key to ben_pl_f. |
| OIPL_ID | NUMBER |  | 18 |  | This is a foreign key to ben_oipl_f. |
| PTIP_ID | NUMBER |  | 18 |  | This is a foreign key to ben_ptip_f. |
| PL_TYP_ID | NUMBER |  | 18 |  | This is a foreign key to ben_pl_typ_f. |
| OPT_ID | NUMBER |  | 18 |  | This is a foreign key to ben_opt_f. |
| SRC_CD | VARCHAR2 | 240 |  |  | This column will hold source code. |
| BILL_START_DATE | DATE |  |  |  | This column holds bill start date. |
| BILL_END_DATE | DATE |  |  |  | This column holds bill end date. |
| PRORATE_TYPE | VARCHAR2 | 240 |  |  | This column holds prorate type. Daily/Rule |
| PRORATE_PERCENT | NUMBER |  |  |  | This column holds prorate percent. |
| PRORATE_DAYS | NUMBER |  |  |  | This column holds prorate days. |
| STOP_BILL_FLAG | VARCHAR2 | 30 |  |  | Hold Bill Flag. Y or N.Default value N. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to HR_ORGANIZATION_UNITS |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| BER_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| BER_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BER_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_ENRT_RSLTN1_ | Non Unique | Default | BILL_ENRT_RSLT_ID, LAST_UPDATE_DATE |
| BEN_BILL_ENRT_RSLT_PK1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, BILL_ENRT_RSLT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
