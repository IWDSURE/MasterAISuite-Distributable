# HRT_PROFILE_MATCH_CRIT

This table stores the Profile Items of the Source Profile that form the Match Criteria in the Profile Best Fit.

This table will act as a kind of temporary table storing the Matching Criteria so that the final query to match the Source Profile with the Target profiles is efficient and simpler. This table will have a structure similar to the HRT_PROFILE_ITEMS table with certain additional columns needed for Match.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilematchcrit-14595.html#hrtprofilematchcrit-14595](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilematchcrit-14595.html#hrtprofilematchcrit-14595)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_MATCH_CRIT_PK | PROFILE_MATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_MATCH_ID | NUMBER |  | 18 | Yes | System generated primary key |
| SEARCH_INSTANCE_ID | NUMBER |  | 18 | Yes | Unique ID to identify the Source criteria Profile items for a particular instance of Match |
| SEARCH_ATTRIBUTE_COUNT | NUMBER |  | 18 |  | Column to identify the number of not-null columns that are to be matched between the Source Profile and the Target profiles |
| SEARCH_IMPORTANCE_PERCENT | NUMBER |  | 5 |  | Column to store the particular Profile Item Row Importance Percent value, derived by dividing the Item Importance Value with the Total Importance for the Profile |
| SEARCH_RATING_USAGE | VARCHAR2 | 30 |  |  | Column to store if the particular Profile Item Row uses any Rating Model |
| SEARCH_NUMERIC_RATING1 | NUMBER |  | 5 |  | Numeric Tating Level value for the corresponding Rating Level |
| SEARCH_NUMERIC_RATING2 | NUMBER |  | 5 |  | Numeric Tating Level value for the corresponding Rating Level |
| SEARCH_NUMERIC_RATING3 | NUMBER |  | 5 |  | Numeric Tating Level value for the corresponding Rating Level |
| PROFILE_ITEM_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILE_ITEMS |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| MANAGER_ID | NUMBER |  | 18 |  | MANAGER_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_BUSINESS_GROUPS |
| PARENT_PROFILE_ITEM_ID | NUMBER |  | 18 |  | Parent Profile Item Id |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILES_B |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_CONTENT_TYPES_B |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foriegn Key to HRT_CONTENT_ITEMS_B |
| SOURCE_ID | NUMBER |  | 18 |  | Syndication source profile ID. Use this property to display the source profile of a syndicated item |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source Type. For example, IRC, OTA |
| SOURCE_KEY1 | NUMBER |  | 18 |  | Alternative Source Key |
| SOURCE_KEY2 | NUMBER |  | 18 |  | Alternative Source Key |
| SOURCE_KEY3 | NUMBER |  | 18 |  | Alternative Source Key |
| DATE_FROM | DATE |  |  | Yes | Date From |
| DATE_TO | DATE |  |  |  | Date To |
| QUALIFIER_ID1 | NUMBER |  | 18 |  | The instance qualifier to use for the item |
| QUALIFIER_ID2 | NUMBER |  | 18 |  | The instance qualifier to use for the item |
| RATING_MODEL_ID1 | NUMBER |  | 18 |  | The rating model |
| RATING_MODEL_ID2 | NUMBER |  | 18 |  | The rating model |
| RATING_MODEL_ID3 | NUMBER |  | 18 |  | The rating model |
| RATING_LEVEL_ID1 | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |
| RATING_LEVEL_ID2 | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |
| RATING_LEVEL_ID3 | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |
| INTEREST_LEVEL | VARCHAR2 | 30 |  |  | Interest level |
| MANDATORY | VARCHAR2 | 30 |  |  | A generic mandatory check box |
| IMPORTANCE | VARCHAR2 | 30 |  |  | Relative importance. This field is used in Search and Compare Profiles |
| ITEM_TEXT240_1 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_2 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_3 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_4 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_5 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_6 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_7 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_8 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_9 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_10 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_11 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_12 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_13 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_14 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT240_15 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |
| ITEM_TEXT2000_1 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |
| ITEM_TEXT2000_2 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |
| ITEM_TEXT2000_3 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |
| ITEM_TEXT2000_4 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |
| ITEM_TEXT2000_5 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |
| ITEM_TEXT30_1 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_2 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_3 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_4 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_5 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_6 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_7 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_8 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_9 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_10 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_11 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_12 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_13 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_14 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_TEXT30_15 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |
| ITEM_DATE_1 | DATE |  |  |  | A generic date field |
| ITEM_DATE_2 | DATE |  |  |  | A generic date field |
| ITEM_DATE_3 | DATE |  |  |  | A generic date field |
| ITEM_DATE_4 | DATE |  |  |  | A generic date field |
| ITEM_DATE_5 | DATE |  |  |  | A generic date field |
| ITEM_DATE_6 | DATE |  |  |  | A generic date field |
| ITEM_DATE_7 | DATE |  |  |  | A generic date field |
| ITEM_DATE_8 | DATE |  |  |  | A generic date field |
| ITEM_DATE_9 | DATE |  |  |  | A generic date field |
| ITEM_DATE_10 | DATE |  |  |  | A generic date field |
| ITEM_NUMBER_1 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_2 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_3 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_4 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_5 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_6 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_7 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_8 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_9 | NUMBER |  | 18 |  | A generic number field |
| ITEM_NUMBER_10 | NUMBER |  | 18 |  | A generic number field |
| ITEM_DECIMAL_1 | NUMBER |  | 15 |  | A generic decimal field |
| ITEM_DECIMAL_2 | NUMBER |  | 15 |  | A generic decimal field |
| ITEM_DECIMAL_3 | NUMBER |  | 15 |  | A generic decimal field |
| ITEM_DECIMAL_4 | NUMBER |  | 15 |  | A generic decimal field |
| ITEM_DECIMAL_5 | NUMBER |  | 15 |  | A generic decimal field |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_MATCH_CRIT_N1 | Non Unique | Default | SEARCH_INSTANCE_ID |
| HRT_PROFILE_MATCH_CRIT_N3 | Non Unique | Default | CONTENT_TYPE_ID, BUSINESS_GROUP_ID |
| HRT_PROFILE_MATCH_CRIT_PK | Unique | Default | PROFILE_MATCH_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
