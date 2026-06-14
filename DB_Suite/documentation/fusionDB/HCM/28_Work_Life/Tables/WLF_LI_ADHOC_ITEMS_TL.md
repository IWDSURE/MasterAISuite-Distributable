# WLF_LI_ADHOC_ITEMS_TL

Table to store language-dependent information of adhoc resource objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliadhocitemstl-8085.html#wlfliadhocitemstl-8085](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliadhocitemstl-8085.html#wlfliadhocitemstl-8085)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_ADHOC_ITEMS_TL_PK | ADHOC_ITEM_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADHOC_ITEM_ID | NUMBER |  | 18 | Yes | Adhoc item Id |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 250 |  | Yes | NAME |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_ADHOC_ITEMS_TL_N1 | Non Unique | Default | LANGUAGE, NAME |
| WLF_LI_ADHOC_ITEMS_TL_U1 | Unique | Default | ADHOC_ITEM_ID, LANGUAGE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
