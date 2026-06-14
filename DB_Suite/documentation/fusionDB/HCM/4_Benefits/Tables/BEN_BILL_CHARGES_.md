# BEN_BILL_CHARGES_

BEN_BILL_CHARGE contains information related to Master charge record for each month and Stores summary amounts.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillcharges-9661.html#benbillcharges-9661](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillcharges-9661.html#benbillcharges-9661)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_CHARGES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, BILL_CHARGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_CHARGE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to PER_ALL_PEOPLE_F. |
| BILLING_DATE | DATE |  |  |  | This column indicates the bill generation date. |
| HOLD_BILL_FLAG | VARCHAR2 | 30 |  |  | This column indicates that hold bill flag is set Y or N. |
| TOTAL_BILL_AMT | NUMBER |  |  |  | This column indicates the total outstanding bill amount which is the summation of CURRENT_BILL_AMT, PAST_AMT_DUE, OTHER_AMT_DUE. |
| BILL_YEAR | VARCHAR2 | 30 |  |  | This column indicates the year of bill generation which flows from BEN_BILL_CALENDAR. |
| BILL_PERIOD | VARCHAR2 | 120 |  |  | This column indicates the billing period which flows from BEN_BILL_CALENDAR. |
| STATUS | VARCHAR2 | 30 |  |  | This column indicates the billing status for which the possible values are Open, Unpaid, Partially-paid, and Fully-paid. |
| BILL_CAL_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_CALENDAR. |
| BILL_SOURCE | VARCHAR2 | 30 |  |  | This column determines if bill was generated manually or by batch process. |
| COMMENTS | VARCHAR2 | 4000 |  |  | This column indicates the comments which flows from BEN_BILL_CALENDAR. |
| BILL_GENERATED | VARCHAR2 | 30 |  |  | This column indicates that the bill is generated or not. It holds Y or N as value. |
| BILL_GENERATED_DATE | DATE |  |  |  | This column indicates the date on which bill was generated. |
| PAST_AMT_DUE | NUMBER |  |  |  | This column holds past due amount. From prior yet Unpaid, Partially-paid bill details / line items. |
| BILL_NUM | NUMBER |  | 18 |  | This column indicates the Generated ID, could be PK as well. |
| BILL_REASON | VARCHAR2 | 240 |  |  | This column is created for Future use. |
| OTHER_AMT_DUE | NUMBER |  |  |  | This column holds amount values from conversion. |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | This column indicates currency code as on program or plan. |
| PER_ACCT_NUM | NUMBER |  | 18 |  | This column indicates the Foreign Key to PER_ALL_PEOPLE_F. |
| CURRENT_BILL_AMT | NUMBER |  |  |  | This column indicates the holds bill for current period. |
| TOTAL_TAX_AMT | NUMBER |  |  |  | This column indicates total tax amount. This column is created for Future use. |
| PER_BILL_INFO_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PER_BILL_INFO_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to HR_ORGANIZATION_UNITS. |
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
| BCH_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| BCH_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCH_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_CHARGESN1_ | Non Unique | Default | BILL_CHARGE_ID, LAST_UPDATE_DATE |
| BEN_BILL_CHARGES_PK1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, BILL_CHARGE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
