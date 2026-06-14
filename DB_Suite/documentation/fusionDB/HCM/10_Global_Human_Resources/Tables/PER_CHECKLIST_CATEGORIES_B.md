# PER_CHECKLIST_CATEGORIES_B

Table to store checklist categories.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcategoriesb-28152.html#perchecklistcategoriesb-28152](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcategoriesb-28152.html#perchecklistcategoriesb-28152)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_CATEGORIES_B_PK | CHECKLIST_CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_CATEGORY_ID | NUMBER |  | 18 | Yes | CHECKLIST_CATEGORY_ID |
| CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | CATEGORY_CODE |
| CATEGORY_TYPE | VARCHAR2 | 30 |  | Yes | CATEGORY_TYPE |
| SUB_CATEGORY_ALLOWED | VARCHAR2 | 1 |  |  | SUB_CATEGORY_ALLOWED |
| SUBJECT_TYPE_CODE | VARCHAR2 | 4 |  | Yes | SUBJECT_TYPE_CODE |
| PARENT_CATEGORY_CODE | VARCHAR2 | 30 |  |  | PARENT_CATEGORY_CODE |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | ENABLED_FLAG |
| TAG | VARCHAR2 | 150 |  |  | TAG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_CATEGORIES_B_U1 | Unique | Default | CHECKLIST_CATEGORY_ID, ORA_SEED_SET1 |
| PER_CHECKLIST_CATEGORIES_B_U11 | Unique | Default | CHECKLIST_CATEGORY_ID, ORA_SEED_SET2 |
| PER_CHECKLIST_CATEGORIES_B_U2 | Unique | Default | CATEGORY_CODE, ORA_SEED_SET1 |
| PER_CHECKLIST_CATEGORIES_B_U21 | Unique | Default | CATEGORY_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
