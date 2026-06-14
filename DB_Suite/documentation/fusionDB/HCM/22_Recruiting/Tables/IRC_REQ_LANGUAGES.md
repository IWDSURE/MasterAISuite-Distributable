# IRC_REQ_LANGUAGES

Stores all languages Requisition will be used in.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqlanguages-28685.html#ircreqlanguages-28685](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqlanguages-28685.html#ircreqlanguages-28685)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQ_LANGUAGES_PK | REQ_LANGUAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_LANGUAGE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B. |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Stores the code of the language. |
| IS_BASE_FLAG | VARCHAR2 | 1 |  |  | Y/N flag indicating whether the current language is the base language of the requisition. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQ_LANGUAGES_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_REQ_LANGUAGES_PK | Unique | Default | REQ_LANGUAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
