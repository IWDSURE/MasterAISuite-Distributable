# HRC_SEM_DICTIONARY_ITEMS

This table contains the dictionary items.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemdictionaryitems-6655.html#hrcsemdictionaryitems-6655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemdictionaryitems-6655.html#hrcsemdictionaryitems-6655)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_DICTIONARY_ITEMS_PK | DICTIONARYITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DICTIONARYITEM_ID | NUMBER |  | 18 | Yes | This is the primary key of the dictionary item table. |
| DICTIONARY_ID | NUMBER |  | 18 | Yes | This is the foreign key to the dictionary table. |
| WORD | VARCHAR2 | 100 |  |  | This column contains the word of the dictionary item. |
| ASSOCIATION | VARCHAR2 | 100 |  |  | This column contains the association of a dictionary item. |
| SCORE_1 | NUMBER |  | 18 |  | This column contains score 1 for the dictionary item. |
| SCORE_2 | NUMBER |  | 18 |  | This column contains the score 2 for the dictionary item. |
| SCORE_3 | NUMBER |  | 18 |  | This column contains the score 3 for the dictionary item. |
| SCORE_4 | NUMBER |  | 18 |  | This column contains the score 4 for the dictionary item. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_DICTIONARY_ITEMS_N1 | Non Unique | FUSION_TS_TX_DATA | DICTIONARY_ID |
| HRC_SEM_DICTIONARY_ITEMS_U1 | Unique | FUSION_TS_TX_DATA | DICTIONARYITEM_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
