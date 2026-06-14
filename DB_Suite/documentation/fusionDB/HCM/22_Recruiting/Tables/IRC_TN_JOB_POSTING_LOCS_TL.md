# IRC_TN_JOB_POSTING_LOCS_TL

Table for storing the flattened posting location information of the requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobpostinglocstl-17850.html#irctnjobpostinglocstl-17850](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobpostinglocstl-17850.html#irctnjobpostinglocstl-17850)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_POSTING_LOCS_TL_PK | TN_JOB_POSTING_LOC_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_POSTING_LOC_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| FA_GEOGRAPHY_NAME | VARCHAR2 | 360 |  | Yes | Geography Name from FA. |
| LOCATION_FQN | VARCHAR2 | 4000 |  |  | Fully Qualified Name of Posting Location from FA |
| CITY_FQN | VARCHAR2 | 4000 |  |  | Fully Qualified Name of Posting Location which includes CITY, STATE AND COUNTRY |
| STATE_FQN | VARCHAR2 | 4000 |  |  | Fully Qualified Name of Posting Location which includes STATE AND COUNTRY |
| COUNTRY | VARCHAR2 | 360 |  | Yes | Country Name from FA. |
| STATE | VARCHAR2 | 360 |  |  | State Name from FA. |
| CITY | VARCHAR2 | 360 |  |  | City Name from FA. |
| FA_GEO_LEVEL_NAMES | VARCHAR2 | 4000 |  |  | All geography structure level names from FA. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_POSTING_LOCS_TL_PK | Unique | Default | TN_JOB_POSTING_LOC_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
