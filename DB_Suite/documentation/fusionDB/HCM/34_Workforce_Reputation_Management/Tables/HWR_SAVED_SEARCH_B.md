# HWR_SAVED_SEARCH_B

The SAVED_SEARCH table is used to store SavedSearches for a user for a screen or a report.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsavedsearchb-28560.html#hwrsavedsearchb-28560](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsavedsearchb-28560.html#hwrsavedsearchb-28560)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SAVED_SEARCH_B_PK | SEARCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_ID | NUMBER |  | 18 | Yes | This is the primary key for the SAVED_SEARCH tables. The number should be generated from the sequence. |
| SEARCH_OWNER | VARCHAR2 | 64 |  |  | The user name of the owner of this SavedSearch object. It can be null for seeded data. |
| COMPONENT_KEY | VARCHAR2 | 30 |  | Yes | This string key identifies the use of this SavedSearch. |
| SEARCH_MODE | NUMBER |  |  | Yes | The search mode for this SavedSearch, identifies a basic (1) or advanced (2) search. A 0 value means that search mode is not known. |
| FILTER | CLOB |  |  |  | The XML serialized CompositeFilter for this SavedSearch. |
| SEARCH_ORDER | CLOB |  |  |  | The XML serialized OrderInfo for this SavedSearch. |
| IS_AUTO_RUN | VARCHAR2 | 4 |  | Yes | A flag indicating that this saved search is to be executed automatically by the UI. Use Y for true or N for false. |
| IS_DEFAULT | VARCHAR2 | 4 |  | Yes | A flag indicating that this saved search is the default for this user and component key. Use Y for true or N for false. |
| IS_HIDDEN | VARCHAR2 | 4 |  | Yes | A flag indicating that this saved search is to be hidden from the user. Use Y for true or N for false. |
| IS_SEEDED_DATA | VARCHAR2 | 4 |  | Yes | A flag indicating seeded data. Use Y for seeded data or N for customer data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SAVED_SEARCH_B_U1 | Unique | FUSION_TS_TX_DATA | SEARCH_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
