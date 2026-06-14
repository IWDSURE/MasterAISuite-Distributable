# PER_SEARCH_FILTERS_

Table to store public person security profile search filter.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persearchfilters-30892.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persearchfilters-30892.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SEARCH_FILTERS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, FILTER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILTER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_ID | NUMBER |  | 18 |  | Fnd object Id. |
| SEARCH_FILTER | VARCHAR2 | 4000 |  |  | Search filter. |
| SEARCH_FILTER2 | CLOB |  |  |  | Search filter pwa2. |
| FILTER_TYPE | VARCHAR2 | 32 |  |  | Filter type. OSCS or BOSS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SEARCH_FILTERSN1_ | Non Unique | Default | FILTER_ID |
| PER_SEARCH_FILTERSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, FILTER_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
