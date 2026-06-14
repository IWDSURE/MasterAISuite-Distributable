# HRC_DL_LAYOUT_ATTRIBUTES_B

This table contains non translatable information about attributes chosen in a template.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutattributesb-17584.html#hrcdllayoutattributesb-17584](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutattributesb-17584.html#hrcdllayoutattributesb-17584)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_LAYOUT_ATTRIBUTES_PK | LAYOUT_ATTRIBUTE_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LAYOUT_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | LAYOUT_ATTRIBUTE_ID |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle inter
      nal use only. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAYOUT_ID | NUMBER |  | 18 | Yes | LAYOUT_ID |
| SEQUENCE_NUMBER | NUMBER |  | 5 | Yes | SEQUENCE_NUMBER |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | ATTRIBUTE_NAME |
| ATTRIBUTE_TYPE | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_TYPE |
| ATTRIBUTE_SUB_CATEGORY | VARCHAR2 | 30 |  |  | ATTRIBUTE_SUB_CATEGORY |
| ATTRIBUTE_DATATYPE | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_DATATYPE |
| MANDATORY_FLAG | VARCHAR2 | 4 |  | Yes | MANDATORY_FLAG |
| VISIBLE_FLAG | VARCHAR2 | 4 |  | Yes | VISIBLE_FLAG |
| USER_KEY_FLAG | VARCHAR2 | 4 |  | Yes | USER_KEY_FLAG |
| PARENT_USER_KEY_FLAG | VARCHAR2 | 4 |  | Yes | PARENT_USER_KEY_FLAG |
| SOURCE_ATTRIBUTE_ID | NUMBER |  | 18 |  | SOURCE_ATTRIBUTE_ID |
| LIST_TYPE | VARCHAR2 | 100 |  |  | LIST_TYPE |
| DISPLAY_TYPE | VARCHAR2 | 240 |  |  | DISPLAY_TYPE |
| LIST_VIEW_DEF_NAME | VARCHAR2 | 240 |  |  | LIST_VIEW_DEF_NAME |
| DISPLAY_ATTR_LIST | VARCHAR2 | 240 |  |  | DISPLAY_ATTR_LIST |
| RETURN_ATTR_NAME | VARCHAR2 | 1000 |  |  | RETURN_ATTR_NAME |
| LIST_VIEW_CRIT_LIST | VARCHAR2 | 4000 |  |  | LIST_VIEW_CRIT_LIST |
| LIST_BIND_MAP | VARCHAR2 | 4000 |  |  | LIST_BIND_MAP |
| LIST_QUERY_CRITERIA | VARCHAR2 | 240 |  |  | LIST_QUERY_CRITERIA |
| FLEXFIELD_CODE | VARCHAR2 | 40 |  |  | FLEXFIELD_CODE |
| FLEXFIELD_CONTEXT_CODE | VARCHAR2 | 80 |  |  | FLEXFIELD_CONTEXT_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| STAGE_COL_NAME | VARCHAR2 | 30 |  | Yes | STAGE_COL_NAME |
| DEFAULT_VALUE | VARCHAR2 | 500 |  |  | DEFAULT_VALUE |
| ENABLE_FLAG | VARCHAR2 | 4 |  | Yes | ENABLE_FLAG |
| READ_ONLY | VARCHAR2 | 4 |  |  | READ_ONLY |
| DEFAULT_VAL_DATE | DATE |  |  |  | DEFAULT_VAL_DATE |
| DEFAULT_VAL_TMSTMP | TIMESTAMP |  |  |  | DEFAULT_VAL_TMSTMP |
| LAYOUT_BUS_OBJ_ID | NUMBER |  | 18 |  | LAYOUT_BUS_OBJ_ID |
| GROUP_CODE | VARCHAR2 | 50 |  |  | GROUP_CODE |
| INTKEY_HINT_ALLOWED_FLAG | VARCHAR2 | 4 |  |  | INTKEY_HINT_ALLOWED_FLAG |
| ATTRIBUTE_HINT | VARCHAR2 | 30 |  |  | ATTRIBUTE_HINT |
| HINTS | VARCHAR2 | 1000 |  |  | HINTS |
| ATTRIBUTE_SUBTYPE | VARCHAR2 | 30 |  |  | ATTRIBUTE_SUBTYPE |
| PARENT_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | PARENT_BUSINESS_OBJECT_ID |
| PARENT_ATTRIBUTE_NAME | VARCHAR2 | 100 |  |  | PARENT_ATTRIBUTE_NAME |
| USER_KEY_ATTR_NAMES | VARCHAR2 | 4000 |  |  | USER_KEY_ATTR_NAMES |
| SECURE_FLAG | VARCHAR2 | 4 |  |  | SECURE_FLAG |
| DATA_LENGTH | NUMBER |  | 4 |  | DATA_LENGTH |
| REFERENCED_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | REFERENCED_BUSINESS_OBJECT_ID |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| DEPENDENT_ATTR_NAMES | VARCHAR2 | 1000 |  |  | DEPENDENT_ATTR_NAMES |
| ATTRIBUTE_KEY | VARCHAR2 | 500 |  |  | ATTRIBUTE_KEY |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CUSTOM_QUERY_CRITERIA | VARCHAR2 | 4000 |  |  | CUSTOM_QUERY_CRITERIA |
| CUSTOM_VIEW_CRITERIA | VARCHAR2 | 4000 |  |  | CUSTOM_VIEW_CRITERIA |
| CUSTOM_QUERY_HINTS | VARCHAR2 | 4000 |  |  | CUSTOM_QUERY_HINTS |
| CUSTOM_VIEW_HINTS | VARCHAR2 | 4000 |  |  | CUSTOM_VIEW_HINTS |
| DEFAULT_EXPRESSION | VARCHAR2 | 4000 |  |  | DEFAULT_EXPRESSION |
| KEY_PREFERENCE | VARCHAR2 | 200 |  |  | KEY_PREFERENCE |
| ATTRIB_KEY_REF | VARCHAR2 | 4000 |  |  | Dependent attributes for an attribute
eg : ATTR_KEY1 has reference values as ATTR_KEY2\|ATTR_KEY3
This means , when ATTR_KEY1 gets modified , default expression for ATTR_KEY2 and ATTR_KEY3 attributes needs to be evaluated |
| ATTRIB_INFO1 | VARCHAR2 | 1000 |  |  | Added for future usage |
| ATTRIB_INFO2 | VARCHAR2 | 1000 |  |  | Added for future usage |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_LAYOUT_ATTRS_B_N1 | Non Unique | Default | LAYOUT_ID, SOURCE_ATTRIBUTE_ID |
| HRC_DL_LAYOUT_ATTRS_B_N2 | Non Unique | Default | LAYOUT_BUS_OBJ_ID |
| HRC_DL_LAYOUT_ATTRS_B_N20 | Non Unique | Default | SGUID |
| HRC_DL_LAYOUT_ATTRS_B_N3 | Non Unique | Default | ATTRIB_INFO1 |
| HRC_DL_LAYOUT_ATTRS_B_N4 | Non Unique | Default | ATTRIBUTE_KEY |
| HRC_DL_LAYOUT_ATTRS_B_U1 | Unique | Default | LAYOUT_ATTRIBUTE_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_DL_LAYOUT_ATTRS_B_U11 | Unique | Default | LAYOUT_ATTRIBUTE_ID, ENTERPRISE_ID, ORA_SEED_SET2 |
| HRC_DL_LAYOUT_ATTRS_B_U2 | Unique | Default | LAYOUT_ID, ATTRIBUTE_NAME, BUSINESS_OBJECT_ID, LAYOUT_ATTRIBUTE_ID, ORA_SEED_SET1 |
| HRC_DL_LAYOUT_ATTRS_B_U21 | Unique | Default | LAYOUT_ID, ATTRIBUTE_NAME, BUSINESS_OBJECT_ID, LAYOUT_ATTRIBUTE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
