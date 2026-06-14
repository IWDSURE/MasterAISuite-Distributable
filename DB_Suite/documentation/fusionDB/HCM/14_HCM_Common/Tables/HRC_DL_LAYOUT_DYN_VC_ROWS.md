# HRC_DL_LAYOUT_DYN_VC_ROWS

This table contains information about custom viewcriteria rows for an attribute configured.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutdynvcrows-22802.html#hrcdllayoutdynvcrows-22802](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutdynvcrows-22802.html#hrcdllayoutdynvcrows-22802)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_LYT_DYN_VC_ROWS_PK | LAYOUT_DYN_VC_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LAYOUT_DYN_VC_ROW_ID | NUMBER |  | 18 | Yes | LAYOUT_DYN_VC_ROW_ID |
| LAYOUT_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | LAYOUT_ATTRIBUTE_ID |
| ITEM_GROUP_ID | NUMBER |  |  | Yes | ITEM_GROUP_ID |
| ITEM_GROUP_CONJUNCTION | VARCHAR2 | 10 |  |  | ITEM_GROUP_CONJUNCTION |
| ITEM_CONJUNCTION | VARCHAR2 | 10 |  |  | ITEM_CONJUNCTION |
| ITEM_ATTRIBUTE | VARCHAR2 | 100 |  | Yes | ITEM_ATTRIBUTE |
| ITEM_OPERATOR | VARCHAR2 | 30 |  | Yes | ITEM_OPERATOR |
| ITEM_IGNORE_CASE | VARCHAR2 | 4 |  |  | ITEM_IGNORE_CASE |
| ITEM_OPERAND_TYPE | VARCHAR2 | 100 |  |  | ITEM_OPERAND_TYPE |
| ITEM_OPERAND_VALUE | VARCHAR2 | 255 |  |  | ITEM_OPERAND_VALUE |
| IS_DEFAULT_GRP | VARCHAR2 | 4 |  |  | IS_DEFAULT_GRP |
| IS_DEFAULT_ROW | VARCHAR2 | 4 |  |  | IS_DEFAULT_ROW |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| ITEM_SEQUENCE | NUMBER |  |  | Yes | ITEM_SEQUENCE |
| LIST_VIEW_DEF_NAME | VARCHAR2 | 240 |  | Yes | LIST_VIEW_DEF_NAME |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ITEM_OPERAND_DATE_VALUE | DATE |  |  |  | ITEM_OPERAND_DATE_VALUE |
| ITEM_OPERAND_TMSTAMP_VALUE | TIMESTAMP |  |  |  | ITEM_OPERAND_TMSTAMP_VALUE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_LYT_DYN_VC_ROWS_N1 | Non Unique | Default | LAYOUT_ATTRIBUTE_ID, ITEM_SEQUENCE |
| HRC_DL_LYT_DYN_VC_ROWS_N20 | Non Unique | Default | SGUID |
| HRC_DL_LYT_DYN_VC_ROWS_U1 | Unique | Default | LAYOUT_DYN_VC_ROW_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
