# HR_VBCS_ADV_SAVED_SEARCH

Table that stores the Saved Searches definition for different HCM modules

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrvbcsadvsavedsearch-20690.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrvbcsadvsavedsearch-20690.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_VBCS_ADV_SAVED_SEARCH_PK | SAVED_SEARCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SAVED_SEARCH_ID | NUMBER |  |  | Yes | Saved Search Id |
| CONTEXT | VARCHAR2 | 200 |  |  | Advanced Search feature context against which the saved search belongs to |
| OWNER_ID | NUMBER |  |  |  | Owner ID of the person who saved the search |
| NAME | VARCHAR2 | 200 |  |  | Name of the Saved Search |
| USER_STORED_LANG | VARCHAR2 | 20 |  |  | Indicates the code of the language using which the user saved the search |
| DEFAULT_SEARCH | VARCHAR2 | 1 |  |  | Stores whether the current search is default or not |
| SEARCH_DEFINITION | CLOB |  |  |  | Strores the search definition |
| SEARCH_SCOPE | VARCHAR2 | 20 |  |  | Stores the scope of the Saved Search |
| SEARCH_SHARED | VARCHAR2 | 1 |  |  | Flag to determine if the Saved Search is Shared with others |
| SHARING_TOKEN | VARCHAR2 | 2000 |  |  | A unique token value that will be used for sharing the saved search |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_VBCS_ADV_SAVED_SEARCH_N20 | Non Unique | Default | OWNER_ID |
| HR_VBCS_ADV_SAVED_SEARCH_PK | Unique | Default | SAVED_SEARCH_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
