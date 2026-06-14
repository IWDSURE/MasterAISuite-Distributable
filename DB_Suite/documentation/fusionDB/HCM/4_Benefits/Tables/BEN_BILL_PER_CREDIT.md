# BEN_BILL_PER_CREDIT

This table stores amounts from conversion or credits or adjustments

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillpercredit-9560.html#benbillpercredit-9560](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillpercredit-9560.html#benbillpercredit-9560)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_PER_CREDIT_PK | BILL_PER_CREDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_PER_CREDIT_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_PEOPLE_F |
| CREDIT_AMT | NUMBER |  |  |  | This column stores the credit amount |
| BILL_PAYMENT_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BILL_PAYMENTS to track if a payment result in credit |
| DEBIT_AMT | NUMBER |  |  |  | This column stores the debit amount |
| RECORDED_DATE | DATE |  |  |  | This column stores the Recorded Date |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | This column stores the Currency Code |
| COMMENTS | VARCHAR2 | 4000 |  |  | This column stores the Comments. User can enter. |
| NO_BILL_FLAG | VARCHAR2 | 30 |  |  | No Bill Flag Y or N. When payment made and no bills exist for allocation. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use |
| BPC_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column |
| BPC_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_MUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_MUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_MUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_MUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BPC_ATTRIBUTE_MUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_PER_CREDIT_FK1 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID |
| BEN_BILL_PER_CREDIT_FK2 | Non Unique | FUSION_TS_TX_IDX | BILL_PAYMENT_ID |
| BEN_BILL_PER_CREDIT_PK1 | Unique | FUSION_TS_TX_IDX | BILL_PER_CREDIT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
