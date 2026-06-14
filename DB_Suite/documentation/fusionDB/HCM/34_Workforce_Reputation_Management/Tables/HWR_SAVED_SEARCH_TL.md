# HWR_SAVED_SEARCH_TL

The translation table for the SAVED_SEARCH table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsavedsearchtl-9254.html#hwrsavedsearchtl-9254](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsavedsearchtl-9254.html#hwrsavedsearchtl-9254)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SAVED_SEARCH_TL_PK | SEARCH_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_ID | NUMBER |  | 18 | Yes | This is the primary key for the SAVED_SEARCH tables. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| NAME | VARCHAR2 | 255 |  | Yes | The name that is used to identify the saved search info to the user. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SAVED_SEARCH_TL_U1 | Unique | FUSION_TS_TX_DATA | SEARCH_ID, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
