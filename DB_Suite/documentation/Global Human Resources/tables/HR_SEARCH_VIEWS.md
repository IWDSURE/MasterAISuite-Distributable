# HR_SEARCH_VIEWS

This table stores the Search Configuration views

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** HR_SEARCH_VIEWS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrsearchviews-19524.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrsearchviews-19524.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_SEARCH_VIEWS_PK | SEARCH_VIEW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_VIEW_ID | NUMBER |  |  | Yes | The Unique Identifier for the Search View |
| NAME | VARCHAR2 | 200 |  |  | Name of the Search View |
| SEARCH_VIEW_CODE | VARCHAR2 | 50 |  |  | Stores the Search View Code |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the Search View |
| OBJECT | VARCHAR2 | 100 |  |  | Object Name against which the Search VIew has been associated with |
| APPLICATION | VARCHAR2 | 100 |  |  | Application Name against which the Search VIew has been associated with |
| FLOW | VARCHAR2 | 100 |  |  | Flow Name for the Search View |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Determines whether the Search View is enabled or not |
| DEFAULT_FLAG | VARCHAR2 | 1 |  |  | Determines whether the Search View is default or not |
| BLINDQUERY_FLAG | VARCHAR2 | 1 |  |  | Determines whether the Blind Query search is enabled or not |
| RESULTS_LAYOUT | VARCHAR2 | 10 |  |  | Stores the layout type for the Search View |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_SEARCH_VIEWS_PK | Unique | Default | SEARCH_VIEW_ID, ORA_SEED_SET1 |
| HR_SEARCH_VIEWS_PK1 | Unique | Default | SEARCH_VIEW_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
