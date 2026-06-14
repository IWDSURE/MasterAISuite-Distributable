# HRT_PROFILE_SRCH_KEYWORDS

This table is used to save Profile data for Person and Model Profiles collected by the keyword search crawler.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesrchkeywords-11166.html#hrtprofilesrchkeywords-11166](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesrchkeywords-11166.html#hrtprofilesrchkeywords-11166)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_SRCH_KEYWORDS_PK | PROFILE_SEARCH_KEYWORD_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_SEARCH_KEYWORD_ID | NUMBER |  | 18 | Yes | Unique identifier for Profile Search Keywords |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Profile ID of a Person or Model Profile |
| PERSON_ID | NUMBER |  | 18 |  | Person ID for a Person Profile |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| PROFILE_XML_KEYWORDS | CLOB |  |  |  | This is a XML CLOB object to store info about the person to be used in OracleText queries |
| PROFILE_TYPE_ID | NUMBER |  | 18 |  | Profile Type ID for a Person or Model Profile |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_SRCH_CTX1 | Non Unique | Default | PROFILE_XML_KEYWORDS |
| HRT_PROFILE_SRCH_KEYWORDS_N1 | Non Unique | Default | PROFILE_ID, LANGUAGE |
| HRT_PROFILE_SRCH_KEYWORDS_PK | Unique | Default | PROFILE_SEARCH_KEYWORD_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
