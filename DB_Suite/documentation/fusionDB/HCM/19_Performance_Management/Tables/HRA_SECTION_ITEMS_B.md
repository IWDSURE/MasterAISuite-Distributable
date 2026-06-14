# HRA_SECTION_ITEMS_B

This table contains items for a section definition. For example, a Technical Competencies section definition contains section Items of Java Skills and PL/SQL Skills.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrasectionitemsb-29643.html#hrasectionitemsb-29643](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrasectionitemsb-29643.html#hrasectionitemsb-29643)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_SECTION_ITEMS_B_PK | ITEM_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ITEM_ID | NUMBER |  | 18 | Yes | System generated primary key id for item. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| SECTION_DEF_ID | NUMBER |  | 18 | Yes | Foreign key to section definition |  |
| PARENT_ITEM_ID | NUMBER |  | 18 |  | This field indicates the parent item. |  |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | This field contains the content item id of the content item in content library in profile mgmt. |  |
| TARGET_PROF_REV_RATING_ID | NUMBER |  | 18 |  | This is the target proficiency rating for the item. |  |
| TARGET_PERF_REV_RATING_ID | NUMBER |  | 18 |  | This is the target performance rating for the item. |  |
| PROF_RATING_MODEL_ID | NUMBER |  | 18 |  | This is the rating model for proficiency for each item |  |
| PERF_RATING_MODEL_ID | NUMBER |  | 18 |  | This is the rating model for performance for the item. |  |
| DUE_DATE | DATE |  |  |  | This is the due date for the item. |  |
| REMINDER_DATE | DATE |  |  |  | This is the reminder date for the item. |  |
| OWNED_BY | VARCHAR2 | 30 |  |  | This field indicates the ownership and responsibility for a particular item. |  |
| MANDATORY_FLAG | VARCHAR2 | 30 |  |  | This field indicates that the item is mandatory and cannot be updated or deleted by any user, at the performance document. |  |
| CRITICAL_FLAG | VARCHAR2 | 30 |  |  | This field indicates that the item is critical, at the performance document.  Critical status serves to highlight the item to the worker and the manager, but there is no other processing around the Critical flag. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| WEIGHT | NUMBER |  | 20 |  | This is the weight of the item. |  |
| MIN_WEIGHT | NUMBER |  | 20 |  | This is the minimum weight of the item. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_SECTION_ITEMS_B_PK | Unique | Default | ITEM_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
