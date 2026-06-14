# HRC_DL_BO_ROLE_MAP

Table to store mapping between an individual business object or a group of business objects and a Job or a Duty Role that will have access to perform HDL load on those objects

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_dl_bo_role_map

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlborolemap-17194.html#hrcdlborolemap-17194](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlborolemap-17194.html#hrcdlborolemap-17194)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BO_ROLE_MAP_PK | ROLE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ID | NUMBER |  | 18 | Yes | ROLE_MAPPING_ID |
| ROLE_ID | NUMBER |  | 18 | Yes | ROLE_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| PRODUCT_AREA | VARCHAR2 | 100 |  |  | PRODUCT_AREA |
| ALL_BUS_OBJ_ACCESS | VARCHAR2 | 10 |  |  | ALL_BUS_OBJ_ACCESS |
| ALL_UNRESTRICTED_OBJ | VARCHAR2 | 10 |  |  | ALL_UNRESTRICTED_OBJ |
| EXTRA_INFO | VARCHAR2 | 1000 |  |  | EXTRA_INFO |
| ERROR_INFORMATION | VARCHAR2 | 4000 |  |  | ERROR_INFORMATION |
| GRANT_GEN_STATUS | VARCHAR2 | 4 |  |  | GRANT_GEN_STATUS |
| GRANT_GEN_DETAILS | VARCHAR2 | 4000 |  |  | GRANT_GEN_DETAILS |
| ACTIVE_STATUS | VARCHAR2 | 4 |  |  | ACTIVE_STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| EXCLUDE_BUSINESS_OBJECT | VARCHAR2 | 4000 |  |  | List of business object identifiers excluded from the product area |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BO_ROLE_MAP_N1 | Non Unique | HRC_DL_BO_ROLE_MAP_N1 | ROLE_ID |
| HRC_DL_BO_ROLE_MAP_N2 | Non Unique | HRC_DL_BO_ROLE_MAP_N2 | BUSINESS_OBJECT_ID, PRODUCT_AREA, ALL_BUS_OBJ_ACCESS, ALL_UNRESTRICTED_OBJ |
| HRC_DL_BO_ROLE_MAP_PK | Unique | HRC_DL_BO_ROLE_MAP_PK | ROLE_MAPPING_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
