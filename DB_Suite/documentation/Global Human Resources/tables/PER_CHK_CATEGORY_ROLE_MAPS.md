# PER_CHK_CATEGORY_ROLE_MAPS

Table storing role access information for a checklist category.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcategoryrolemaps-7719.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcategoryrolemaps-7719.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_CATEGORY_ROLE_MAPS_PK | CATEGORY_ROLE_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_ROLE_MAP_ID | NUMBER |  | 18 | Yes | CATEGORY_ROLE_MAP_ID |
| ROLE_ID | NUMBER |  | 18 | Yes | ROLE_ID |
| CHECKLIST_CATEGORY | VARCHAR2 | 60 |  | Yes | CHECKLIST_CATEGORY |
| ACTIVE_STATUS | VARCHAR2 | 4 |  | Yes | ACTIVE_STATUS |
| ALL_CATEGORIES_ACCESS | VARCHAR2 | 4 |  | Yes | ALL_CATEGORIES_ACCESS |
| ERROR_INFORMATION | VARCHAR2 | 4000 |  |  | ERROR_INFORMATION |
| GRANT_GEN_STATUS | VARCHAR2 | 4 |  |  | GRANT_GEN_STATUS |
| GRANT_GEN_DETAILS | VARCHAR2 | 4000 |  |  | GRANT_GEN_DETAILS |
| EXTRA_INFORMATION | VARCHAR2 | 1000 |  |  | EXTRA_INFORMATION |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_CATEGORY_ROLE_MAPS_N1 | Non Unique | Default | ROLE_ID, CHECKLIST_CATEGORY |
| PER_CHK_CATEGORY_ROLE_MAPS_PK | Unique | Default | CATEGORY_ROLE_MAP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
