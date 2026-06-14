# HRC_SDL_ATTR_MAP_DEFAULTS

This table would store attribute defaults for metadata attributes of HSDL.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlattrmapdefaults-25439.html#hrcsdlattrmapdefaults-25439](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlattrmapdefaults-25439.html#hrcsdlattrmapdefaults-25439)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_ATTR_MAP_DEFAULTS_PK | ATTR_MAP_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTR_MAP_DEF_ID | NUMBER |  | 18 | Yes | ATTR_MAP_DEF_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | ATTRIBUTE_NAME |
| FLEXFIELD_CODE | VARCHAR2 | 40 |  |  | FLEXFIELD_CODE |
| FLEXFIELD_CONTEXT_CODE | VARCHAR2 | 80 |  |  | FLEXFIELD_CONTEXT_CODE |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| ATTRIBUTE_LABEL | VARCHAR2 | 240 |  |  | ATTRIBUTE_LABEL |
| MANDATORY_FLAG | VARCHAR2 | 4 |  |  | MANDATORY_FLAG |
| LOOKUP_TYPE | VARCHAR2 | 30 |  |  | LOOKUP_TYPE |
| LIST_TYPE | VARCHAR2 | 100 |  |  | LIST_TYPE |
| DISPLAY_TYPE | VARCHAR2 | 240 |  |  | DISPLAY_TYPE |
| LIST_VIEW_DEF_NAME | VARCHAR2 | 240 |  |  | LIST_VIEW_DEF_NAME |
| DISPLAY_ATTR_LIST | VARCHAR2 | 240 |  |  | DISPLAY_ATTR_LIST |
| RETURN_ATTR_NAME | VARCHAR2 | 1000 |  |  | RETURN_ATTR_NAME |
| LIST_VIEW_CRIT_LIST | VARCHAR2 | 4000 |  |  | LIST_VIEW_CRIT_LIST |
| LIST_BIND_MAP | VARCHAR2 | 4000 |  |  | LIST_BIND_MAP |
| LIST_QUERY_CRITERIA | VARCHAR2 | 240 |  |  | LIST_QUERY_CRITERIA |
| DATA_LENGTH | NUMBER |  | 4 |  | DATA_LENGTH |
| ACTIVE_FLAG | VARCHAR2 | 4 |  |  | ACTIVE_FLAG |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DEPENDENT_ATTR_NAMES | VARCHAR2 | 1000 |  |  | DEPENDENT_ATTR_NAMES |
| ATTR_DETAILS | VARCHAR2 | 1000 |  |  | ATTR_DETAILS |
| BUS_OBJ_FILE_DISCRIMINATOR | VARCHAR2 | 100 |  |  | BUS_OBJ_FILE_DISCRIMINATOR |
| BUS_OBJ_TOP_DISCRIMINATOR | VARCHAR2 | 100 |  |  | BUS_OBJ_TOP_DISCRIMINATOR |
| BUS_OBJ_SERVICE_VERSION | VARCHAR2 | 32 |  |  | BUS_OBJ_SERVICE_VERSION |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_ATTR_MAP_DEFAULTS_N1 | Non Unique | Default | BUS_OBJ_FILE_DISCRIMINATOR, BUS_OBJ_TOP_DISCRIMINATOR, BUS_OBJ_SERVICE_VERSION |
| HRC_SDL_ATTR_MAP_DEFAULTS_U1 | Unique | Default | ATTR_MAP_DEF_ID, ORA_SEED_SET1 |
| HRC_SDL_ATTR_MAP_DEFAULTS_U11 | Unique | Default | ATTR_MAP_DEF_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
