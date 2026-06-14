# CMP_CWB_PERSON_ELEMENTS

Stores person's element entry details for a compensation plan period. For example, 'Worksheet Rate' can be posted to 'Bonus' element and 'Custom Segment 20' can be posted to an information element.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersonelements-23454.html#cmpcwbpersonelements-23454](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersonelements-23454.html#cmpcwbpersonelements-23454)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PERSON_ELEMENTS_PK | PERSON_RUN_ID, ROW_TYPE, COMPONENT_ID, PLAN_ATTRIBUTE_ID, ATTRIBUTE_ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_RUN_ID | NUMBER |  | 18 | Yes | PERSON_RUN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ROW_TYPE | VARCHAR2 | 30 |  | Yes | ROW_TYPE |
| COMPONENT_ID | NUMBER |  | 18 | Yes | COMPONENT_ID |
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | PLAN_ATTRIBUTE_ID |
| ATTRIBUTE_ELEMENT_ID | NUMBER |  | 18 | Yes | ATTRIBUTE_ELEMENT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_NAME |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| DATE_BEHAVIOR | VARCHAR2 | 30 |  |  | DATE_BEHAVIOR |
| STATIC_DATE | DATE |  |  |  | STATIC_DATE |
| ELEMENT_POSTING_DATE | DATE |  |  |  | ELEMENT_POSTING_DATE |
| POSTED_DATE | DATE |  |  |  | POSTED_DATE |
| ELEMENT_SCREEN_ENTRY_TXT | VARCHAR2 | 150 |  |  | ELEMENT_SCREEN_ENTRY_TXT |
| ELEMENT_SCREEN_ENTRY_NUM | NUMBER |  |  |  | ELEMENT_SCREEN_ENTRY_NUM |
| POSTED_SCREEN_ENTRY | VARCHAR2 | 60 |  |  | POSTED_SCREEN_ENTRY |
| ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 |  | ELEMENT_ENTRY_VALUE_ID |
| ELEMENT_CREATION_DATE | DATE |  |  |  | ELEMENT_CREATION_DATE |
| RUN_ID | NUMBER |  | 18 | Yes | RUN_ID |
| PAY_INPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | PAY_INPUT_CURRENCY_CODE |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| SALARY_COMPONENT_ID | NUMBER |  | 18 |  | SALARY_COMPONENT_ID |
| SALARY_COMPONENT | VARCHAR2 | 30 |  |  | SALARY_COMPONENT |
| POSTED_SALARY_INCREASE_AMOUNT | NUMBER |  |  |  | POSTED_SALARY_INCREASE_AMOUN |
| SALARY_RATES_WS_VAL | NUMBER |  |  |  | SALARY_RATES_WS_VAL |
| SALARY_POSTED | NUMBER |  |  |  | SALARY_POSTED |
| SALARY_PREV | NUMBER |  |  |  | SALARY_PREV |
| SALARY_NEW | NUMBER |  |  |  | Salary New |
| ELEMENT_TYPE | VARCHAR2 | 32 |  |  | ELEMENT_TYPE |
| ELEMENT_ENTRY_POSTED | VARCHAR2 | 60 |  |  | ELEMENT_ENTRY_POSTED |
| ELEMENT_ENTRY_PREV | VARCHAR2 | 60 |  |  | ELEMENT_ENTRY_PREV |
| ELEMENT_ENTRY_NEW | VARCHAR2 | 60 |  |  | ELEMENT_ENTRY_NEW |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PERSON_ELEMENTS_N1 | Non Unique | Default | ELEMENT_ENTRY_VALUE_ID, RUN_ID |
| CMP_CWB_PERSON_ELEMENTS_N3 | Non Unique | Default | RUN_ID, PERSON_RUN_ID |
| CMP_CWB_PERSON_ELEMENTS_PK | Unique | Default | PERSON_RUN_ID, ROW_TYPE, COMPONENT_ID, PLAN_ATTRIBUTE_ID, ATTRIBUTE_ELEMENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
