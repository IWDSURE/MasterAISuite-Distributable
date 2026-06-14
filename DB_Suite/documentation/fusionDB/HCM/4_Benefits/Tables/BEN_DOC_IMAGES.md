# BEN_DOC_IMAGES

BEN_DOC_IMAGES for documents and images

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendocimages-4410.html#bendocimages-4410](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bendocimages-4410.html#bendocimages-4410)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_DOC_IMAGES_PK | BEN_DOC_IMG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BEN_DOC_IMG_ID | NUMBER |  | 18 | Yes | BEN_DOC_IMG_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| MAPPING_TABLE_NAME | VARCHAR2 | 30 |  | Yes | MAPPING_TABLE_NAME |
| MAPPING_COLUMN_NAME | VARCHAR2 | 30 |  | Yes | MAPPING_COLUMN_NAME |
| MAPPING_TABLE_PK_ID | NUMBER |  | 18 | Yes | MAPPING_TABLE_PK_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| IMG_BLOB | BLOB |  |  |  | IMG_BLOB |
| DOC_CLOB | CLOB |  |  |  | DOC_CLOB |
| ADDNL_DESC1 | VARCHAR2 | 4000 |  |  | ADDNL_DESC1 |
| ADDNL_DESC2 | VARCHAR2 | 4000 |  |  | ADDNL_DESC2 |
| ADDNL_DESC3 | VARCHAR2 | 4000 |  |  | ADDNL_DESC3 |
| ADDNL_DESC4 | VARCHAR2 | 4000 |  |  | ADDNL_DESC4 |
| ADDNL_DESC5 | VARCHAR2 | 4000 |  |  | ADDNL_DESC5 |
| ADDNL_DATE1 | DATE |  |  |  | ADDNL_DATE1 |
| ADDNL_DATE2 | DATE |  |  |  | ADDNL_DATE2 |
| ADDNL_DATE3 | DATE |  |  |  | ADDNL_DATE3 |
| ADDNL_DATE4 | DATE |  |  |  | ADDNL_DATE4 |
| ADDNL_DATE5 | DATE |  |  |  | ADDNL_DATE5 |
| ADDNL_NUMBER1 | NUMBER |  |  |  | ADDNL_NUMBER1 |
| ADDNL_NUMBER2 | NUMBER |  |  |  | ADDNL_NUMBER2 |
| ADDNL_NUMBER3 | NUMBER |  |  |  | ADDNL_NUMBER3 |
| ADDNL_NUMBER4 | NUMBER |  |  |  | ADDNL_NUMBER4 |
| ADDNL_NUMBER5 | NUMBER |  |  |  | ADDNL_NUMBER5 |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_DOC_IMAGES_N1 | Non Unique | Default | MAPPING_TABLE_NAME, MAPPING_COLUMN_NAME |
| BEN_DOC_IMAGES_U1 | Unique | Default | BEN_DOC_IMG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
