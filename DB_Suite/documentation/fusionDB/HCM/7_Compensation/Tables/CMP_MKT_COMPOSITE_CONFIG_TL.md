# CMP_MKT_COMPOSITE_CONFIG_TL

Stores translatable inforamtion of CMP_MKT_COMPOSITE_CONFIG_B table.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcompositeconfigtl-5554.html#cmpmktcompositeconfigtl-5554](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcompositeconfigtl-5554.html#cmpmktcompositeconfigtl-5554)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_COMPOSITE_CONFIG_TL_PK | COMPOSITE_CONFIG_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPOSITE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key of the base table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| DISPLAY_NAME | VARCHAR2 | 80 |  |  | Translation display name for Composite column label |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_COMPOSITE_CONFIG_TL_U1 | Unique | Default | COMPOSITE_CONFIG_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
