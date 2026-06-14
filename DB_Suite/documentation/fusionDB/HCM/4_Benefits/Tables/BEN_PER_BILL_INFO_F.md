# BEN_PER_BILL_INFO_F

BEN_PER_BILL_INFO_F contains information related to Benefits Billing Information and it stores common billing info for person.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperbillinfof-14093.html#benperbillinfof-14093](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperbillinfof-14093.html#benperbillinfof-14093)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_BILL_INFO_F_PK | PER_BILL_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_BILL_INFO_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_PEOPLE_F. |
| PER_ACCT_NUM | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_PEOPLE_F. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| STOP_BILL_FLAG | VARCHAR2 | 30 |  | Yes | This column indicates the stop billing is set to Y or N. |
| ADDRESS_LINE1 | VARCHAR2 | 240 |  |  | This column indicates the first line of address. |
| ADDRESS_LINE2 | VARCHAR2 | 240 |  |  | This column indicates the second line of address. |
| ADDRESS_LINE3 | VARCHAR2 | 240 |  |  | This column indicates the third line of address. |
| ADDRESS_LINE4 | VARCHAR2 | 240 |  |  | This column indicates the fourth line of address. |
| STATE | VARCHAR2 | 240 |  |  | This column indicates the state of address. |
| CITY | VARCHAR2 | 240 |  |  | This column indicates the city of address. |
| COUNTRY | VARCHAR2 | 120 |  |  | This column indicates the country of the address. |
| ZIP_CODE | VARCHAR2 | 30 |  |  | This column indicates the postal code of the address. |
| COMMENTS | VARCHAR2 | 4000 |  |  | This column indicates the comments. |
| PRMRY_MAIL_ADDRESS_ID | NUMBER |  | 18 |  | Foreign key to PER_ADDRESSES. Identifies which address from PER_ADDRESSES is considered the mailing address for the person. |
| PRMRY_EMAIL_ID | NUMBER |  | 18 |  | Foreign key to PER_EMAIL_ADDRESSES. |
| PREF_COMM_MODE | VARCHAR2 | 240 |  |  | For future use. Values could be email/ mail / fax etc. |
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
| PBI_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| PBI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column. |
| PBI_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_BILL_INFO_FK1 | Non Unique | Default | PERSON_ID |
| BEN_PER_BILL_INFO_FK2 | Non Unique | Default | PER_ACCT_NUM |
| BEN_PER_BILL_INFO_PK1 | Unique | Default | PER_BILL_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
