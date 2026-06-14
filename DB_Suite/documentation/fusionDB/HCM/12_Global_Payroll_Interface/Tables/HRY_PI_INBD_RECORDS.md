# HRY_PI_INBD_RECORDS

Stores summary information from third-party payroll providers, such as the name and payroll period of the processed payroll.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiinbdrecords-30219.html#hrypiinbdrecords-30219](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiinbdrecords-30219.html#hrypiinbdrecords-30219)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_INBD_RECORDS_PK | INBD_RECORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INBD_RECORD_ID | NUMBER |  | 18 | Yes | Primary Key for Inbound Record |
| RECORD_IDENTIFIER | VARCHAR2 | 30 |  |  | Uniquely identifies the record |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Type of Entity |
| SOURCE_ID | NUMBER |  | 18 |  | Primary key of Inbound Record Owner |
| FUNCTIONAL_CATEGORY | VARCHAR2 | 30 |  | Yes | Functional Category of Inbound Record |
| RECORD_TYPE | VARCHAR2 | 30 |  | Yes | Type of Inbound Record |
| START_DATE | DATE |  |  | Yes | Start date of the Inbound Record |
| BATCH_CODE | VARCHAR2 | 100 |  | Yes | Batch or file identifier |
| ENTITY_IDENTIFIER | VARCHAR2 | 30 |  | Yes | Number or name of entity |
| END_DATE | DATE |  |  |  | End date of Inbound Record |
| BATCH_DATE | DATE |  |  | Yes | Batch or file date |
| VENDOR_CODE | VARCHAR2 | 30 |  | Yes | Inbound Record Vendor Name |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to PAY_ALL_PAYROLLS_F |
| TIME_PERIOD_ID | NUMBER |  | 18 |  | Foreign key to PAY_TIME_PERIODS |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_PERSONS |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAY_RELATIONSHIPS_F |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLL_TERMS |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLL_ASSIGNMENTS |
| DOCUMENTS_OF_RECORD_ID | NUMBER |  | 18 |  | Foreign key to HR_DOCUMENTS_OF_RECORD |
| CATEGORY_CODE | VARCHAR2 | 80 |  | Yes | Foreign key to FND_EF_CATEGORIES_B |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRY_PI_INBD_RECORDS_N1 | Non Unique | FUSION_TS_TX_IDX | ENTITY_IDENTIFIER | Obsolete |
| HRY_PI_INBD_RECORDS_N2 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID |  |
| HRY_PI_INBD_RECORDS_N3 | Non Unique | FUSION_TS_TX_IDX | PAYROLL_RELATIONSHIP_ID |  |
| HRY_PI_INBD_RECORDS_N4 | Non Unique | FUSION_TS_TX_IDX | PAYROLL_TERM_ID |  |
| HRY_PI_INBD_RECORDS_N5 | Non Unique | FUSION_TS_TX_IDX | PAYROLL_ASSIGNMENT_ID |  |
| HRY_PI_INBD_RECORDS_N6 | Non Unique | FUSION_TS_TX_IDX | PAYROLL_ID, TIME_PERIOD_ID |  |
| HRY_PI_INBD_RECORDS_PK | Unique | FUSION_TS_TX_IDX | INBD_RECORD_ID |  |
| HRY_PI_INBD_RECORDS_U1 | Unique | FUSION_TS_TX_IDX | ENTITY_IDENTIFIER, SOURCE_TYPE, START_DATE, FUNCTIONAL_CATEGORY, RECORD_TYPE, BATCH_CODE, RECORD_IDENTIFIER |  |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
