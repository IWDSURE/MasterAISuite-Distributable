# WLF_SAVED_SEARCHES_F

Table to store language-independent information of learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfsavedsearchesf-15317.html#wlfsavedsearchesf-15317](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfsavedsearchesf-15317.html#wlfsavedsearchesf-15317)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SAVED_SEARCHES_F_PK | SAVED_SEARCH_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SAVED_SEARCH_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SAVED_SEARCH_NAME | VARCHAR2 | 240 |  | Yes | SAVED_SEARCH_NAME |
| VO_NAME | VARCHAR2 | 256 |  | Yes | VO_NAME |
| FINAL_CLAUSE | VARCHAR2 | 4000 |  |  | FINAL_CLAUSE |
| OWNER | VARCHAR2 | 64 |  |  | OWNER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SAVED_SEARCH_TYPE | VARCHAR2 | 64 |  |  | Type of saved search either full query or vc where clause |
| AM_PATH | VARCHAR2 | 4000 |  |  | AM full path |
| FULL_QUERY | CLOB |  |  |  | Full Query |
| PARAM_VALUES | CLOB |  |  |  | Full query bind variable name value pairs |
| USAGE_TYPE | VARCHAR2 | 30 |  |  | It can be: ADHOC or GLOBAL |
| VC_NAME | VARCHAR2 | 200 |  |  | View Criteria Name |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SAVED_SEARCHES_F_U1 | Unique | Default | SAVED_SEARCH_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
