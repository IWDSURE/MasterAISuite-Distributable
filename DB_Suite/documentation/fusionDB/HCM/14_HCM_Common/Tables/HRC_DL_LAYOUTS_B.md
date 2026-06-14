# HRC_DL_LAYOUTS_B

This table stores template information.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutsb-23349.html#hrcdllayoutsb-23349](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdllayoutsb-23349.html#hrcdllayoutsb-23349)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_LAYOUTS_B_PK | LAYOUT_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LAYOUT_ID | NUMBER |  | 18 | Yes | LAYOUT_ID |
| RUN_MODE | VARCHAR2 | 50 |  |  | RUN_MODE |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| LAYOUT_CODE | VARCHAR2 | 80 |  | Yes | LAYOUT_CODE |
| LAYOUT_TYPE | VARCHAR2 | 30 |  | Yes | LAYOUT_TYPE |
| LAYOUT_CATEGORY_CODE | VARCHAR2 | 30 |  |  | LAYOUT_CATEGORY_CODE |
| LAYOUT_MODE | VARCHAR2 | 120 |  |  | LAYOUT_MODE |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| TOP_BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | TOP_BUSINESS_OBJECT_ID |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| HASH_VALUE | VARCHAR2 | 100 |  | Yes | HASH_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| VALIDATION_STATUS | VARCHAR2 | 30 |  |  | VALIDATION_STATUS |
| KEY_PREFERENCE | VARCHAR2 | 30 |  |  | KEY_PREFERENCE |
| LAYOUT_DETAILS | VARCHAR2 | 1000 |  |  | LAYOUT_DETAILS |
| LAYOUT_INFO1 | VARCHAR2 | 1000 |  |  | Added for future usage |
| LAYOUT_INFO2 | VARCHAR2 | 1000 |  |  | Added for future usage |
| RUN_IN_DEBUG_MODE | VARCHAR2 | 20 |  |  | Indicates whether template running in debug mode or not. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_LAYOUTS_B_N20 | Non Unique | Default | SGUID |
| HRC_DL_LAYOUTS_B_U1 | Unique | Default | LAYOUT_ID, ORA_SEED_SET1 |
| HRC_DL_LAYOUTS_B_U11 | Unique | Default | LAYOUT_ID, ORA_SEED_SET2 |
| HRC_DL_LAYOUTS_B_U2 | Unique | Default | LAYOUT_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_DL_LAYOUTS_B_U21 | Unique | Default | LAYOUT_ID, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
