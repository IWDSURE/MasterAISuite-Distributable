# PER_EXT_APP_IDENTIFIERS

Stores details of the Identifiers needed to be able for Fusion HCM systems to be able to intergrate with external third party applications

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextappidentifiers-31615.html#perextappidentifiers-31615](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextappidentifiers-31615.html#perextappidentifiers-31615)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_APP_IDENTIFIERS_PK | EXT_IDENTIFIER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_IDENTIFIER_ID | NUMBER |  | 18 | Yes | System generated primary key, surrogate key value |
| EXT_IDENTIFIER_TYPE | VARCHAR2 | 30 |  | Yes | Type of External Identifier |
| EXT_IDENTIFIER_NUMBER | VARCHAR2 | 256 |  | Yes | Numeric or character value of the External Identifier |
| EXT_IDENTIFIER_SEQ | NUMBER |  | 4 | Yes | A row number of Identifiers per person, used as a part of an alternate key for services |
| PERSON_ID | NUMBER |  | 18 | Yes | Idenfies person for whom this Identifier is recorded |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifies person's assignment for whom this Identifier is recorded |
| DATE_FROM | TIMESTAMP |  |  | Yes | Date and Time from when the Identifier is valid |
| DATE_TO | TIMESTAMP |  |  |  | Date and Time until when the identifier is valid |
| COMMENTS | VARCHAR2 | 2048 |  |  | Freeform comments |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EXT_APP_IDENTIFIERS_N1 | Non Unique | Default | PERSON_ID, EXT_IDENTIFIER_TYPE, EXT_IDENTIFIER_NUMBER |
| PER_EXT_APP_IDENTIFIERS_N2 | Non Unique | Default | ASSIGNMENT_ID, EXT_IDENTIFIER_TYPE, EXT_IDENTIFIER_NUMBER |
| PER_EXT_APP_IDENTIFIERS_N3 | Non Unique | Default | EXT_IDENTIFIER_NUMBER, DATE_FROM, DATE_TO |
| PER_EXT_APP_IDENTIFIERS_PK | Unique | Default | EXT_IDENTIFIER_ID |
| PER_EXT_APP_IDENTIFIERS_UK1 | Unique | Default | EXT_IDENTIFIER_SEQ, PERSON_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
