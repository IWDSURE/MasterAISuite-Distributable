# BEN_BILL_PAYMENTS

BEN_BILL_PAYMENTS contains information related to Benefits Billing Payments and Captures each payment made by person with necessary details.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillpayments-28467.html#benbillpayments-28467](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillpayments-28467.html#benbillpayments-28467)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_PAYMENTS_PK | BILL_PAYMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_PAYMENT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PAYMENT_DATE | DATE |  |  | Yes | This column indicates the payment instrument submission date like cheque submitted date. |
| PAYMENT_MODE | VARCHAR2 | 30 |  | Yes | This column indicates the payment mode. |
| PAYMENT_DOC_NUM | VARCHAR2 | 240 |  |  | This column indicates the payment document number. |
| PAYMENT_TYPE | VARCHAR2 | 30 |  |  | This column indicates that payment made is credit or debit. |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | This column holds currency code. |
| PAYEE_ORG_NAME | VARCHAR2 | 240 |  |  | For future use. This column indicates the payee organization name. |
| PAYEE_ORG_NUM | VARCHAR2 | 240 |  |  | For future use. This column indicates the payee organization number. |
| PAYEE_ORG_DETAILS | VARCHAR2 | 240 |  |  | For future use. This column indicates the payee organization details. |
| AMT_PAID | NUMBER |  |  | Yes | This column indicates the amount paid. |
| COMMENTS | VARCHAR2 | 4000 |  |  | This column indicates the comments entered by user. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column indicates the Foreign Key to PER_ALL_PEOPLE_F. |
| PAY_SEQ | NUMBER |  | 18 |  | For future use. This column indicates the pay sequence which is useful to track while handling multiple payments. |
| BILL_NUM | NUMBER |  | 18 |  | This column indicates the bill number which flows from BBEN_BILL_CHARGES. |
| PAYMENT_ENTRY_DATE | DATE |  |  |  | This column indicates the payment entry recorded date. |
| PER_ACCT_NUM | NUMBER |  | 18 | Yes | This column indicates Foreign Key to PER_ALL_PEOPLE_F. |
| ADJ_AMT | NUMBER |  |  |  | For future use. This column indicates the adjustment amount. |
| ADJ_DATE | DATE |  |  |  | For future use. This column indicates the adjustment date. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | This column indicates the Foreign Key to HR_ORGANIZATION_UNITS. |
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
| BPY_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flex field structure defining column. |
| BPY_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BPY_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_PAYMENTS_FK1 | Non Unique | Default | PERSON_ID |
| BEN_BILL_PAYMENTS_FK2 | Non Unique | Default | PER_ACCT_NUM |
| BEN_BILL_PAYMENTS_PK1 | Unique | Default | BILL_PAYMENT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
