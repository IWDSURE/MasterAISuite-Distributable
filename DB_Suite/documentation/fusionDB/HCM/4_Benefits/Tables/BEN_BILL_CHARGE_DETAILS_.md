# BEN_BILL_CHARGE_DETAILS_

BEN_BILL_CHARGE_DETAILS contains information related to Billing line item details and Keeps track of each enrt, EE rate etc.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillchargedetails-29468.html#benbillchargedetails-29468](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillchargedetails-29468.html#benbillchargedetails-29468)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_CHARGE_DETAILS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, BILL_CHARGE_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_CHARGE_DTL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BENEFIT_RELATIONS_F. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This column indicates the LEGAL_ENTITY_ID. |
| BILL_CHARGE_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_BILL_CHARGES. |
| PRTT_ENRT_RSLT_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PRTT_ENRT_RSLT_F. |
| PRTT_RT_VAL_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PRTT_RT_VAL. |
| PL_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PL_F. |
| PGM_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PGM_F. |
| OIPL_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_OIPL_F. |
| OPT_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_OPT_F. |
| PTIP_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PTIP_F. |
| ANN_RT_VAL | NUMBER |  |  |  | This column indicates the annual rate. |
| CMCD_RT_VAL | NUMBER |  |  |  | This column indicates the communicated rate value. |
| DFND_RT_VAL | NUMBER |  |  |  | This column indicates the defined rate value. |
| DFND_RT_FREQ | VARCHAR2 | 30 |  |  | This column indicates the defined rate frequency. |
| CMCD_RT_FREQ | VARCHAR2 | 30 |  |  | This column indicates the communicated rate frequency. |
| BILL_AMT | NUMBER |  |  |  | This column indicates the bill amount for enrollment result. |
| ORIGINAL_BILL_AMT | NUMBER |  |  |  | This column indicates the original bill amount for enrollment result. |
| STATUS | VARCHAR2 | 30 |  |  | This column indicates the bill status. |
| ADJ_PERCENT | NUMBER |  |  |  | For future use. This column indicates the adjustment percentage. |
| ADD_FLAT_AMT | NUMBER |  |  |  | For future use. Add flat amount for adjustment. |
| PL_TYP_ID | NUMBER |  | 18 |  | This column indicates the Foreign Key to BEN_PL_TYP_F. |
| CURRENCY_CD | VARCHAR2 | 30 |  |  | This column indicates the currency code. |
| AMT_PAID | NUMBER |  |  |  | This column indicates the amount paid. |
| ALLOC_SEQ_NUM | NUMBER |  | 18 |  | This column indicates the allocation sequence. |
| AMT_DUE | NUMBER |  |  |  | This column indicates the amount due for enrollment result. |
| ADJ_AMT | NUMBER |  |  |  | This column indicates the flat amount used for adjustment. |
| ADJ_DATE | DATE |  |  |  | This column indicates the adjustment date. |
| OVERRIDE_REASON | VARCHAR2 | 4000 |  |  | This column indicates the enrollment override reason. |
| OVERRIDE_DATE | DATE |  |  |  | This column indicates the bill overriden date. |
| RATE_START_DT | DATE |  |  |  | This column indicates the rate start date. |
| RATE_END_DT | DATE |  |  |  | This column indicates the rate end date. |
| DAILY_PROTN_FLAG | VARCHAR2 | 30 |  |  | This column indicates the daily proration is set to Y or N. |
| HOLD_FLAG | VARCHAR2 | 30 |  |  | This column indicates the hold is set to Y or N. |
| TAX_PERCENT | NUMBER |  |  |  | This column indicates the tax percentage. |
| TAX_AMT | NUMBER |  |  |  | This column indicates the tax amount. |
| TAX_TYPE | VARCHAR2 | 30 |  |  | This column indicates the tax type. |
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
| BCD_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| BCD_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| BCD_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_CHARGE_DETAILSN1_ | Non Unique | Default | BILL_CHARGE_DTL_ID, LAST_UPDATE_DATE |
| BEN_BILL_CHARGE_DETAILS_PK1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, BILL_CHARGE_DTL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
