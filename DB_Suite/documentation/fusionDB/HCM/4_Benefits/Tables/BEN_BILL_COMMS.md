# BEN_BILL_COMMS

This table is used to store the communication details for bill

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillcomms-28645.html#benbillcomms-28645](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbillcomms-28645.html#benbillcomms-28645)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BILL_COMMS_PK | BILL_PERSON_COMM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BILL_PERSON_COMM_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| BILL_PRINTED | VARCHAR2 | 30 |  | Yes | This columns stores  Y or N to say Bill Printed or not. |
| BILL_SENT | VARCHAR2 | 30 |  |  | Thi column stores Y or N to say whether bill sent or not |
| BILL_SENT_DATE | DATE |  |  |  | This column storeds the date on which the Bill was sent |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_PEOPLE_F |
| BILL_RESENT_DATE | DATE |  |  |  | This column stores the Bill Resent date |
| BILL_RESENT_NUMBER | NUMBER |  | 18 |  | Number of times bill has been resent |
| BILL_CHARGE_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BILL_CHARGES |
| BILL_CAL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_BILL_CALENDAR |
| BILL_PRINT_DATE | DATE |  |  |  | This column stores the date on which bill was printed |
| BILL_SENT_MODE | VARCHAR2 | 240 |  |  | Bill Sent Mode. Values could be email/mail/fax etc |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZAION_UNITS |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template Number Field for future use |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template Number Field for future use |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template Number Field for future use |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template Number Field for future use |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template Number Field for future use |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character Field for future use |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character Field for future use |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character Field for future use |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character Field for future use |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character Field for future use |
| CONFIG_DATE_1 | DATE |  |  |  | Template date Field for future use |
| CONFIG_DATE_2 | DATE |  |  |  | Template date Field for future use |
| CONFIG_DATE_3 | DATE |  |  |  | Template date Field for future use |
| CONFIG_DATE_4 | DATE |  |  |  | Template date Field for future use |
| CONFIG_DATE_5 | DATE |  |  |  | Template date Field for future use |
| BCM_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column |
| BCM_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield segment column |
| BCM_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield segment column |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BILL_COMMS_FK1 | Non Unique | FUSION_TS_TX_IDX | PERSON_ID |
| BEN_BILL_COMMS_FK2 | Non Unique | FUSION_TS_TX_IDX | BILL_CHARGE_ID |
| BEN_BILL_COMMS_FK3 | Non Unique | FUSION_TS_TX_IDX | BILL_CAL_ID |
| BEN_BILL_COMMS_PK1 | Unique | FUSION_TS_TX_IDX | BILL_PERSON_COMM_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
