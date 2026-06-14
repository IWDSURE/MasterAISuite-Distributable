# HRC_DL_REM_TOP_ENTITIES

SEED Data Table for storing Top Level HDL Objects

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtopentities-13746.html#hrcdlremtopentities-13746](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtopentities-13746.html#hrcdlremtopentities-13746)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_TOP_ENTITIES_PK | TOP_ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOP_ENTITY_ID | NUMBER |  |  | Yes | Top Entity Id |
| TOP_BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | FK to HRC_DL_BUSINESS_OBJECTS. Stores the Top level BO Id |
| CATEGORY | VARCHAR2 | 30 |  | Yes | Data Type : Workers/Candidate |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Enabled Flag. Only for Enabled entities Data Disposal will be displayed in the UI |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  | Yes | SGUID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_TOP_ENTITIES_N1 | Non Unique | Default | CATEGORY |
| HRC_DL_REM_TOP_ENTITIES_N2 | Non Unique | Default | TOP_BUSINESS_OBJECT_ID |
| HRC_DL_REM_TOP_ENTITIES_N20 | Non Unique | Default | SGUID |
| HRC_DL_REM_TOP_ENTITIES_U1 | Unique | Default | TOP_ENTITY_ID, ORA_SEED_SET1 |
| HRC_DL_REM_TOP_ENTITIES_U11 | Unique | Default | TOP_ENTITY_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
