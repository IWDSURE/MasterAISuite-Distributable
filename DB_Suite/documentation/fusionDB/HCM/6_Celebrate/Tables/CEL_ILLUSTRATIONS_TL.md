# CEL_ILLUSTRATIONS_TL

MLS translatable table to hold translatable attributes for illustrations

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celillustrationstl-29361.html#celillustrationstl-29361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celillustrationstl-29361.html#celillustrationstl-29361)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_ILLUSTRATIONS_TL_PK | ILLUSTRATION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ILLUSTRATION_ID | NUMBER |  | 18 | Yes | Illustration ID |
| ILLUSTRATION_NAME | VARCHAR2 | 80 |  |  | Name of the Illustration |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of the illustration |
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
| CEL_ILLUSTRATIONS_TL_PK | Unique | Default | ILLUSTRATION_ID, LANGUAGE |
| CEL_ILLUSTRATIONS_TL_UK1 | Unique | Default | LANGUAGE, ILLUSTRATION_NAME |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
