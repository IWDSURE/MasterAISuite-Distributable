# HWR_WLNS_NEWS_TL

This table stores the tasks and their descriptions

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsnewstl-10820.html#hwrwlnsnewstl-10820](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsnewstl-10820.html#hwrwlnsnewstl-10820)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_NEWS_TL_PK | NEWS_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NEWS_ID | NUMBER |  | 18 | Yes | This column holds the news id |
| NEWS_TITLE | VARCHAR2 | 100 |  | Yes | This column stores the new s title |
| NEWS_DESC | CLOB |  |  | Yes | This column stores description of the news |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_NEWS_TL_U1 | Unique | FUSION_TS_TX_DATA | NEWS_ID, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
