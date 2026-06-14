# BEN_BILL_CHARGE_PAYMENTS

BEN_BILL_CHARGE_PAYMENTS table is a resolution table between payment to charges, which  is many to many relationship.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillchargepayments-28194.html#benbillchargepayments-28194](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillchargepayments-28194.html#benbillchargepayments-28194)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_CHARGE_PAYMENTS_PK | BILL_CHARGE_PAYMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_CHARGE_PAYMENT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_ID | NUMBER |  | 18 | Yes | This column indicates the  Foreign Key to PER_ALL_PEOPLE_F. |
| BILL_CHARGE_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_CHARGES. |
| BILL_NUM | NUMBER |  | 18 |  | This column indicates the bill number which flows from BEN_BILL_CHARGES. |
| BILL_PERIOD | VARCHAR2 | 120 |  |  | This column indicates the billing period which flows from BEN_BILL_CALENDER. |
| BILL_YEAR | VARCHAR2 | 30 |  |  | This column indicates the year of bill generation which flows from BEN_BILL_CALENDER. |
| PER_CREDIT_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_PER_CREDIT. |
| BILL_CAL_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_CALENDER. |
| BILL_PAYMENT_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_PAYMENTS. |
| AMT_PAID | NUMBER |  |  |  | This column indicates the Amt Paid. |
| AMT_DUE | NUMBER |  |  |  | This column indicates the Amt Due. |
| BILL_CHARGE_DTL_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_CHARGE_DETAILS. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
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
| BCP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| BCP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_CHARGE_PAYMENTS_PK1 | Unique | Default | BILL_CHARGE_PAYMENT_ID |
| BEN_BILL_CHARGE_PAYMENT_FK1 | Non Unique | Default | PERSON_ID |
| BEN_BILL_CHARGE_PAYMENT_FK2 | Non Unique | Default | BILL_CHARGE_ID |
| BEN_BILL_CHARGE_PAYMENT_FK3 | Non Unique | Default | BILL_CAL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
