# BEN_REGN_F_TL

BEN_REGN_F_TL holds MLS translated data from main table, BEN_REGN_F..

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benregnftl-15408.html#benregnftl-15408](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benregnftl-15408.html#benregnftl-15408)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_REGN_F_TL_PK | REGN_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REGN_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_REGN_F. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the translated regulation. |
| STTRY_CITN_NAME | VARCHAR2 | 240 |  | Yes | Statutory citation name. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_REGN_F_TL_N1 | Non Unique | Default | UPPER("NAME") |
| BEN_REGN_F_TL_PK | Unique | Default | REGN_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
