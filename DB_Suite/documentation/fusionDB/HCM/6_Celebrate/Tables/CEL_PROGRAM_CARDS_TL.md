# CEL_PROGRAM_CARDS_TL

MLS base table to hold base attributes for quick recognition card details

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramcardstl-30950.html#celprogramcardstl-30950](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramcardstl-30950.html#celprogramcardstl-30950)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_PROGRAM_CARDS_TL_PK | CARD_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CARD_ID | NUMBER |  | 18 | Yes | Quick recognition card identifier |
| CARD_HEADLINE | VARCHAR2 | 80 |  |  | Headline of quick recognition card |
| CARD_MESSAGE | VARCHAR2 | 2000 |  |  | Message for quick recognition card |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_PROGRAM_CARDS_TL_PK | Unique | Default | CARD_ID, LANGUAGE |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
