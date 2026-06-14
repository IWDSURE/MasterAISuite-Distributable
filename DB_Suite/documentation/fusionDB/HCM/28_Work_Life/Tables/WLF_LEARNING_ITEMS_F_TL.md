# WLF_LEARNING_ITEMS_F_TL

Table to store language-dependent information of learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningitemsftl-19777.html#wlflearningitemsftl-19777](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningitemsftl-19777.html#wlflearningitemsftl-19777)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARNING_ITEMS_F_TL_PK | LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| XML_KEYWORDS | CLOB |  |  |  | This is a XML CLOB object to store info about the learningItem to be used in OracleText queries |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 250 |  |  | Name of the content object. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of the content object. |
| DESCRIPTION_SHORT | VARCHAR2 | 4000 |  |  | Short Description of the content object. |
| DESCRIPTION_LONG | CLOB |  |  |  | Long description of the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CAT_SEARCH_TERMS | CLOB |  |  |  | To be used by Self-Service Users to search catalog learning items |
| CAT_SEARCH_TITLE | VARCHAR2 | 250 |  |  | To be used to populate title of learning item only for required records |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_F_TL_CTX1 | Non Unique | Default | NAME |
| WLF_LI_F_TL_N2 | Non Unique | Default | NAME |
| WLF_LI_F_TL_N3 | Non Unique | Default | UPPER("NAME") |
| WLF_LI_F_TL_U1 | Unique | Default | LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
