# HRC_DL_BUSINESS_OBJECTS

HRC_DL_BUSINESS_OBJECTS is seeded as the main driving table that holds all supported objects at any level of the business objects hierarchy. It holds the ADF framework business components for business objects, remote service access definitions, and can distinguish these across multiple versions of business objects.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusinessobjects-8033.html#hrcdlbusinessobjects-8033](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusinessobjects-8033.html#hrcdlbusinessobjects-8033)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUSINESS_OBJECTS_PK | BUSINESS_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| DYNAMIC_HIERARCHY | VARCHAR2 | 1 |  |  | DYNAMIC_HIERARCHY |
| PRODUCT_AREA | VARCHAR2 | 30 |  |  | PRODUCT_AREA |
| UI_BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | UI_BUSINESS_OBJECT_ID |
| BUSINESS_OBJECT_VO_FQ_NAME | VARCHAR2 | 256 |  | Yes | BUSINESS_OBJECT_VO_FQ_NAME |
| DYN_BUS_OBJ_KEY | VARCHAR2 | 100 |  |  | DYN_BUS_OBJ_KEY |
| BUS_OBJ_FILE_DISCRIMINATOR | VARCHAR2 | 100 |  | Yes | BUS_OBJ_FILE_DISCRIMINATOR |
| BUS_OBJ_TOP_DISCRIMINATOR | VARCHAR2 | 100 |  | Yes | BUS_OBJ_TOP_DISCRIMINATOR |
| BUS_OBJ_SERVICE_VERSION | VARCHAR2 | 32 |  | Yes | BUS_OBJ_SERVICE_VERSION |
| PARENT_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | PARENT_BUSINESS_OBJECT_ID |
| PROCESSING_ORDER | NUMBER |  | 18 |  | PROCESSING_ORDER |
| VALID_OPERATIONS | VARCHAR2 | 32 |  |  | VALID_OPERATIONS |
| FSM_DISPLAY_ORDER | NUMBER |  | 18 |  | FSM_DISPLAY_ORDER |
| LEGISLATION_CODE | VARCHAR2 | 32 |  |  | LEGISLATION_CODE |
| USING_APP_FQ_NAME | VARCHAR2 | 256 |  |  | USING_APP_FQ_NAME |
| USING_APP_CONFIG | VARCHAR2 | 100 |  |  | USING_APP_CONFIG |
| USING_APP_VIEWUSAGE_NAME | VARCHAR2 | 100 |  | Yes | USING_APP_VIEWUSAGE_NAME |
| WS_CONNECTION_QNAME | VARCHAR2 | 256 |  |  | WS_CONNECTION_QNAME |
| CALLBACK_CONNECTION_QNAME | VARCHAR2 | 256 |  |  | CALLBACK_CONNECTION_QNAME |
| GROUP_BY_EXPRESSION | VARCHAR2 | 2000 |  |  | GROUP_BY_EXPRESSION |
| ORDER_BY_EXPRESSION | VARCHAR2 | 2000 |  |  | ORDER_BY_EXPRESSION |
| CUSTOM_ORDERING_PROCEDURE | VARCHAR2 | 256 |  |  | CUSTOM_ORDERING_PROCEDURE |
| POST_PROC_TYPE | VARCHAR2 | 100 |  |  | POST_PROC_TYPE |
| POST_PROC_JOB_FQ_DEFN_NAME | VARCHAR2 | 256 |  |  | POST_PROC_JOB_FQ_DEFN_NAME |
| POST_PROC_JOB_FQ_CLASS_NAME | VARCHAR2 | 256 |  |  | POST_PROC_JOB_FQ_CLASS_NAME |
| POST_PROC_TASK_NAMES | VARCHAR2 | 1000 |  |  | POST_PROC_TASK_NAMES |
| VALIDATION_ENABLED | VARCHAR2 | 1 |  |  | VALIDATION_ENABLED |
| ROLLBACK_ENABLED | VARCHAR2 | 1 |  |  | Roll back Enabled Flag, indicates if rollback is enabled for current business object hierarchy. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| EA_PROFILE_OPTION_NAME | VARCHAR2 | 80 |  |  | EA_PROFILE_OPTION_NAME |
| EA_PROFILE_OPTION_TYPE | VARCHAR2 | 32 |  |  | EA_PROFILE_OPTION_TYPE |
| EA_PROFILE_OPTION_HASH_STRING | VARCHAR2 | 256 |  |  | EA_PROFILE_OPTION_HASH_STRING |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BUSINESS_OBJECTS_PK | Unique | Default | BUSINESS_OBJECT_ID, ORA_SEED_SET1 |
| HRC_DL_BUSINESS_OBJECTS_PK1 | Unique | Default | BUSINESS_OBJECT_ID, ORA_SEED_SET2 |
| HRC_DL_BUSINESS_OBJECTS_U1 | Unique | Default | BUS_OBJ_FILE_DISCRIMINATOR, BUS_OBJ_TOP_DISCRIMINATOR, BUS_OBJ_SERVICE_VERSION, ORA_SEED_SET1 |
| HRC_DL_BUSINESS_OBJECTS_U11 | Unique | Default | BUS_OBJ_FILE_DISCRIMINATOR, BUS_OBJ_TOP_DISCRIMINATOR, BUS_OBJ_SERVICE_VERSION, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
