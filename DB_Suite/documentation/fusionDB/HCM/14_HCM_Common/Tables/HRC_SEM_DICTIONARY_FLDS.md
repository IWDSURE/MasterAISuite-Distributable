# HRC_SEM_DICTIONARY_FLDS

This table contains the field URIs for the dictionary.  The dictionary_id is the FK to hrc_dictionary_b table.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemdictionaryflds-14662.html#hrcsemdictionaryflds-14662](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemdictionaryflds-14662.html#hrcsemdictionaryflds-14662)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_DICTIONARY_FLDS_PK | DICTIONARYFIELD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DICTIONARYFIELD_ID | NUMBER |  | 18 | Yes | This column is the primary key for the dictionary field table. |
| DICTIONARY_ID | NUMBER |  | 18 | Yes | This column contains the dictionary id reference to hrc_dictionary_b table. |
| FIELDURI | VARCHAR2 | 1000 |  | Yes | This column contains the field uri for the dictionary. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_DICTIONARY_FLDS_N1 | Non Unique | FUSION_TS_TX_DATA | DICTIONARY_ID |
| HRC_SEM_DICTIONARY_FLDS_U1 | Unique | FUSION_TS_TX_DATA | DICTIONARYFIELD_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
