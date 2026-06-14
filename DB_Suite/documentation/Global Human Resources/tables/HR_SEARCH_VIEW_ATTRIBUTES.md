# HR_SEARCH_VIEW_ATTRIBUTES

This table stores the search view attributes

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** HR_SEARCH_VIEW_ATTRIBUTES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrsearchviewattributes-4173.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrsearchviewattributes-4173.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_SEARCH_VIEW_ATTRS_PK | SEARCH_VIEW_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_VIEW_ATTRIBUTE_ID | NUMBER |  |  | Yes | Unique identifier for the Search View Attributes |
| SEARCH_VIEW_ID | NUMBER |  |  |  | Uniquely identifies the Search View record |
| TYPE | VARCHAR2 | 20 |  |  | Type of the Search View Attribute |
| ATTRIBUTE_NAME | VARCHAR2 | 500 |  |  | Name of the Search View Attribute |
| ATTRIBUTE_LABEL | VARCHAR2 | 100 |  |  | Stores the label key for the Search View Attribute |
| HIERARCHY | VARCHAR2 | 500 |  |  | Hierarchy of the Search View Attribute |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Stores the enabled state of the Search View Attribute |
| FILTER_TYPE | VARCHAR2 | 20 |  |  | Stores the Filter type for the Filter Search View Attribute |
| SEQUENCE | NUMBER |  |  |  | Stores the sequence of the Search View Attribute |
| CATEGORY | VARCHAR2 | 20 |  |  | Stores the category of the attribute |
| ANCHORED_FLAG | VARCHAR2 | 1 |  |  | Identifies whether the current attribute is anchored in the display results section |
| SHOW_BY_DEFAULT_FLAG | VARCHAR2 | 1 |  |  | Identifies whether the current attribute has to be shown by default in the results section |
| FLEX_CODE | VARCHAR2 | 40 |  |  | Stores the Flex code for the segment |
| FLEX_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Stores the Context code for the segment |
| FLEX_SEGMENT_CODE | VARCHAR2 | 30 |  |  | Stores the Segment code for the segment |
| GROUP_CODE | VARCHAR2 | 20 |  |  | Stores the Group Code for the filter type |
| GROUP_LABEL | VARCHAR2 | 50 |  |  | Stores the Group Label for the filter type |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_SEARCH_VIEW_ATTRS_PK | Unique | Default | SEARCH_VIEW_ATTRIBUTE_ID, ORA_SEED_SET1 |
| HR_SEARCH_VIEW_ATTRS_PK1 | Unique | Default | SEARCH_VIEW_ATTRIBUTE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
