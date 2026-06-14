# WLF_SEARCH_STOPWORDS

Table to store the stopwords that will not be indexed for keyword searches.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfsearchstopwords-12666.html#wlfsearchstopwords-12666](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfsearchstopwords-12666.html#wlfsearchstopwords-12666)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SEARCH_STOPWORDS_PK | STOPWORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STOPWORD_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LANG_CODE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language for a given stopword. |
| CATEGORY | VARCHAR2 | 30 |  | Yes | Category of data for which the stopword applies. |
| STOPWORD | VARCHAR2 | 255 |  | Yes | The word that will not be indexed for keyword searches. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | When this stopword was used for keyword search stopword processing. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STATUS | VARCHAR2 | 30 |  |  | Indicates status for a given stopword. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SEARCH_STOPWORDS_U1 | Unique | Default | STOPWORD_ID, ORA_SEED_SET1 |
| WLF_SEARCH_STOPWORDS_U11 | Unique | Default | STOPWORD_ID, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
