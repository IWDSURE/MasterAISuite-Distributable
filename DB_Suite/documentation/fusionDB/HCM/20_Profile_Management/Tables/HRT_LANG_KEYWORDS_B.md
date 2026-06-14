# HRT_LANG_KEYWORDS_B

Language Suggestion Keywords table stores the keywords that will trigger invocation of specific language suggestions.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtlangkeywordsb-11617.html#hrtlangkeywordsb-11617](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtlangkeywordsb-11617.html#hrtlangkeywordsb-11617)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_LANG_KEYWORDS_B_PK | KEYWORD_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEYWORD_ID | NUMBER |  | 18 | Yes | Unique identifier of Keywords for Language Suggestions. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This is the unique identifier for the enterprise. |
| KEYWORD_CODE | VARCHAR2 | 64 |  | Yes | Alternate unique alphanumeric code for the keyword. |
| SUGGESTION_ID | NUMBER |  | 18 | Yes | Foreign key to Language Suggestions table. |
| SUPPLIER_CODE | VARCHAR2 | 30 |  | Yes | Supplier code. This is used to store the information about which supplier supplied this data row, or it is user defined. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | The status of the item, Active or Inactive |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_LANG_KEYWORDS_B_U1 | Unique | FUSION_TS_TX_DATA | KEYWORD_ID, ENTERPRISE_ID |
| HRT_LANG_KEYWORDS_B_U2 | Unique | FUSION_TS_TX_DATA | KEYWORD_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
