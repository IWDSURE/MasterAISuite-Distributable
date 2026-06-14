# BEN_POP_UP_MESSAGES

BEN_POP_UP_MESSAGES identify the messages associated with various steps in specific benefits forms.  . For example, display the message "First Time Enrollee" after the enrollment form has opened for a person who has no previous enrollment results.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpopupmessages-9458.html#benpopupmessages-9458](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpopupmessages-9458.html#benpopupmessages-9458)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_POP_UP_MESSSAGES_PK | POP_UP_MESSAGES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POP_UP_MESSAGES_ID | NUMBER |  |  | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  |  | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| POP_NAME | VARCHAR2 | 300 |  |  | Pop-up message name. |
| FORMULA_ID | NUMBER |  |  |  | Foreign key to FF_FORMULAS_F. |
| FUNCTION_NAME | VARCHAR2 | 2000 |  |  | This character field indicates function name. |
| BLOCK_NAME | VARCHAR2 | 2000 |  |  | This character field indicates block name. |
| FIELD_NAME | VARCHAR2 | 300 |  |  | This character field indicates field name. |
| EVENT_NAME | VARCHAR2 | 300 |  |  | This character field indicates event name. |
| MESSAGE | VARCHAR2 | 4000 |  |  | This character field indicates message text. |
| MESSAGE_TYPE | VARCHAR2 | 300 |  |  | This character field indicates message type. |
| NO_FORMULA_FLAG | VARCHAR2 | 30 |  |  | No Formula Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| START_DATE | DATE |  |  |  | Start Date. |
| END_DATE | DATE |  |  |  | End date. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| VAL | NUMBER |  |  |  | Template number field to hold numerical values. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | This field holds benefit relation id. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This field holds legal entity id. |
| TEXT | VARCHAR2 | 2000 |  |  | Template character field to hold text. |
| CNT_NUM | NUMBER |  | 38 |  | Template number field to hold numerical values. |
| ERROR_MESSAGE_CODE | VARCHAR2 | 240 |  |  | This field holds error message code. |
| LER_ID | NUMBER |  | 18 |  | This field holds foreign key to BEN_LER_F. |
| PERSON_ID | NUMBER |  | 18 |  | This field holds foreign key to PER_PEOPLE_F. |
| PGM_ID | NUMBER |  | 18 |  | This field holds foreign key to BEN_PGM_F. |
| PL_ID | NUMBER |  | 18 |  | This field holds foreign key to BEN_PL_F. |
| OIPL_ID | NUMBER |  | 18 |  | This field holds foreign key to BEN_OIPL_F. |
| FUNCTION_ID | NUMBER |  | 18 |  | Template ID field to hold ID values. |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 2000 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 2000 |  |  | Template character field for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_POP_UP_MESSAGES_N1 | Non Unique | Default | PERSON_ID |
| BEN_POP_UP_MESSAGES_N2 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_POP_UP_MESSAGES_N3 | Non Unique | Default | LER_ID |
| BEN_POP_UP_MESSAGES_N4 | Non Unique | Default | PGM_ID |
| BEN_POP_UP_MESSAGES_N5 | Non Unique | Default | PL_ID |
| BEN_POP_UP_MESSAGES_N6 | Non Unique | Default | FUNCTION_ID |
| BEN_POP_UP_MESSAGES_PK | Unique | Default | POP_UP_MESSAGES_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
