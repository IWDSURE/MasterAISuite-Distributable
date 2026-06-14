# WLF_ASSIGNMENT_CATEGORIES

Table to store details of assignment categories.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentcategories-19763.html#wlfassignmentcategories-19763](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentcategories-19763.html#wlfassignmentcategories-19763)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ASSIGNMENT_CATEGORIES_PK | CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| CATEGORY_NUMBER | VARCHAR2 | 30 |  | Yes | This column stores category number that uniquely identifies the category |
| CATEGORY_CODE | VARCHAR2 | 30 |  | Yes | CATEGORY_CODE |
| CATEGORY_TYPE | VARCHAR2 | 30 |  | Yes | CATEGORY_TYPE |
| THUMBNAIL_ID | NUMBER |  | 18 |  | This column stores thumbnail identifier that a reference key to WLF_THUMBNAILS |
| COVER_ART_THUMBNAIL_ID | NUMBER |  | 18 |  | This column stores thumbnail identifier for cover art on a recommender and a reference key to WLF_THUMBNAILS |
| STATUS | VARCHAR2 | 30 |  |  | This column stores status of the category. Possible values are ORA_ACTIVE and ORA_INACTIVE. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ASSIGNMENT_CATEGORIES_U1 | Unique | Default | CATEGORY_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
