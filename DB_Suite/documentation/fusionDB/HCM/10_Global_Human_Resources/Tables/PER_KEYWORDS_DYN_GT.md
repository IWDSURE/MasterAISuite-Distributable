# PER_KEYWORDS_DYN_GT

Global Temporary table to store dynamically calculated keywords during crawling with all people option.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perkeywordsdyngt-16562.html#perkeywordsdyngt-16562](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perkeywordsdyngt-16562.html#perkeywordsdyngt-16562)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | This column stores the Person Identifier. |
| ASSIGNMNET_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_ASSIGNMENTS_M table |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language code into which the contents of the translatable columns are used |
| DYN_XML_KEYWORDS | CLOB |  |  |  | This is a XML CLOB object to store dynamic keywords info about the person to be used in Oracle Text queries. |
| DATE_CAL | DATE |  |  |  | Date used for the dynamic keywords clob calculation. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
