# HRC_MESSAGE_CATEGORIES_B

This table hold details of communication categories

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessagecategoriesb-28686.html#hrcmessagecategoriesb-28686](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessagecategoriesb-28686.html#hrcmessagecategoriesb-28686)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_CATEGORIES_B_PK | CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_ID | NUMBER |  | 18 | Yes | Unique identifier for the categories |
| CATEGORY_CODE | VARCHAR2 | 120 |  | Yes | code for a category which will be functionally used to track a category |
| CATEGORY_NAME_MODIFIED | VARCHAR2 | 120 |  |  | alternate name for a category if proposed by user |
| PARENT_CATEGORY_CODE | VARCHAR2 | 120 |  |  | category code which will represent the parent category for the current category |
| IS_SUB_CATEGORY_MANDATORY | VARCHAR2 | 1 |  |  | flag to determine if sub category selection has to be mandatory if current category is parent |
| IS_ACTIVE | VARCHAR2 | 20 |  |  | flag determinig whether a specific category is active or not |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise id against which this category record has been created |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_CATEGORIES_B_PK | Unique | Default | CATEGORY_ID, ORA_SEED_SET1 |
| HRC_MESSAGE_CATEGORIES_B_PK1 | Unique | Default | CATEGORY_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
