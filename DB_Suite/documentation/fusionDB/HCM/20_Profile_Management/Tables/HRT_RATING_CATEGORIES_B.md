# HRT_RATING_CATEGORIES_B

Profile Management Rating Categories Table.  Used in capturing the Rating categories and boundaries for Performance Management ninebox requirements.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratingcategoriesb-15980.html#hrtratingcategoriesb-15980](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratingcategoriesb-15980.html#hrtratingcategoriesb-15980)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_RATING_CATEGORIES_B_PK | CATEGORY_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_ID | NUMBER |  | 18 | Yes | Unique identifier of Rating Category |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| RATING_MODEL_ID | NUMBER |  | 18 | Yes | Foreign key to Rating Model table |
| LOWER_BOUNDARY | NUMBER |  | 5 |  | Define the lower boundary |
| UPPER_BOUNDARY | NUMBER |  | 5 |  | Define the upper boundary |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_RATING_CATEGORIES_B_N1 | Non Unique | Default | RATING_MODEL_ID |
| HRT_RATING_CATEGORIES_B_PK | Unique | Default | CATEGORY_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
