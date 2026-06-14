# BEN_RPTG_GRP_TL

BEN_RPTG_GRP_TL hold MLS translated data from the main table,BEN_RPTG_GRP..

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benrptggrptl-28320.html#benrptggrptl-28320](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benrptggrptl-28320.html#benrptggrptl-28320)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_RPTG_GRP_TL_PK | RPTG_GRP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RPTG_GRP_ID | NUMBER |  | 18 | Yes | Reporting Group Id |
| NAME | VARCHAR2 | 240 |  | Yes | Name |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_RPTG_GRP_TL_N1 | Non Unique | Default | UPPER("NAME") |
| BEN_RPTG_GRP_TL_PK | Unique | Default | RPTG_GRP_ID, LANGUAGE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
