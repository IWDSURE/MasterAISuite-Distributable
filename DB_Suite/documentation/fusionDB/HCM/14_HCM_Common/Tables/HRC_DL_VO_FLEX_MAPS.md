# HRC_DL_VO_FLEX_MAPS

This table is used to store flex information for VO maps

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvoflexmaps-25774.html#hrcdlvoflexmaps-25774](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvoflexmaps-25774.html#hrcdlvoflexmaps-25774)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VO_FLEX_MAP_ID | NUMBER |  | 18 | Yes | VO_FLEX_MAP_ID |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO_MAPPING_ID |
| FLEX_TYPE | VARCHAR2 | 4 |  | Yes | FLEX_TYPE |
| FLEX_CODE | VARCHAR2 | 40 |  | Yes | FLEX_CODE |
| VO_CONTEXT_CODE | VARCHAR2 | 1000 |  | Yes | VO_CONTEXT_CODE |
| VO_CATEGORY_CODE | VARCHAR2 | 1000 |  |  | VO_CATEGORY_CODE |
| VIEW_DEF_NAME | VARCHAR2 | 1000 |  |  | VIEW_DEF_NAME |
| FLEX_ACCESSOR_NAME | VARCHAR2 | 1000 |  |  | FLEX_ACCESSOR_NAME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_VO_FLEX_MAPS_U1 | Unique | Default | VO_FLEX_MAP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
