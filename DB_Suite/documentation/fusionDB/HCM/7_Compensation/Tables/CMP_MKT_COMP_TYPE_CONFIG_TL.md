# CMP_MKT_COMP_TYPE_CONFIG_TL

Stores translatable inforamtion of CMP_MKT_COMP_TYPE_CONFIG_B table.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomptypeconfigtl-27399.html#cmpmktcomptypeconfigtl-27399](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomptypeconfigtl-27399.html#cmpmktcomptypeconfigtl-27399)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_COMP_TYPE_CONFIG_TL_PK | LANGUAGE, COMP_TYPE_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMP_TYPE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| COMP_TYPE_DISPLAY_NAME | VARCHAR2 | 80 |  |  | Translation display name for Comp Type label |
| MKT_TARGET_DISPLAY_NAME | VARCHAR2 | 80 |  |  | Translation display name for Market Target label |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_COMP_TYPE_CONFIG_TL_U1 | Unique | Default | LANGUAGE, COMP_TYPE_CONFIG_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
