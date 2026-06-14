# HRC_DL_BUS_FLEX_ATTRIBUTES

HRC_DL_BUS_FLEX_ATTRIBUTES is used to store flex field attributes

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusflexattributes-16708.html#hrcdlbusflexattributes-16708](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusflexattributes-16708.html#hrcdlbusflexattributes-16708)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_FLEX_ATTRIBUTE_PK | FLEX_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLEX_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | FLEX_ATTRIBUTE_ID |
| FLEX_CONTEXT_ID | NUMBER |  | 18 | Yes | FLEX_CONTEXT_ID |
| FLEX_VO_ATTR_NAME | VARCHAR2 | 100 |  | Yes | FLEX_VO_ATTR_NAME |
| FLEX_SEGMENT_CODE | VARCHAR2 | 100 |  |  | FLEX_SEGMENT_CODE |
| DISPLAY_ATTRIBUTE | VARCHAR2 | 1 |  |  | DISPLAY_ATTRIBUTE |
| MANDATORY | VARCHAR2 | 1 |  |  | If a flex field attribute is mandatory - Y else N |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| ATTRIBUTE_DATATYPE | VARCHAR2 | 30 |  |  | ATTRIBUTE_DATATYPE |
| DISPLAY_TYPE | VARCHAR2 | 240 |  |  | DISPLAY_TYPE |
| LIST_VIEW_DEF_NAME | VARCHAR2 | 240 |  |  | LIST_VIEW_DEF_NAME |
| DISPLAY_ATTR_LIST | VARCHAR2 | 240 |  |  | DISPLAY_ATTR_LIST |
| RETURN_ATTR_NAME | VARCHAR2 | 1000 |  |  | RETURN_ATTR_NAME |
| LIST_VIEW_CRIT_LIST | VARCHAR2 | 4000 |  |  | LIST_VIEW_CRIT_LIST |
| LIST_BIND_MAP | VARCHAR2 | 4000 |  |  | LIST_BIND_MAP |
| LIST_QUERY_CRITERIA | VARCHAR2 | 240 |  |  | LIST_QUERY_CRITERIA |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BUS_FLEX_ATTRIBUTES_U1 | Unique | Default | FLEX_CONTEXT_ID, FLEX_VO_ATTR_NAME, ENTERPRISE_ID |
| HRC_DL_BUS_FLEX_ATTRIBUTE_PK | Unique | Default | FLEX_ATTRIBUTE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
