# WLF_RECOMMENDER_CONFIG

This table stores the recommender configuration details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommenderconfig-21283.html#wlfrecommenderconfig-21283](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommenderconfig-21283.html#wlfrecommenderconfig-21283)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOMMENDER_CONFIG_PK | RECOMMENDER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMENDER_CONFIG_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| RECOMMENDATION_PROFILE_ID | NUMBER |  | 18 | Yes | References RECOMMENDATION_PROFILE_ID from WLF_RECOMMENDATION_PROFILES table. |
| RECOMMENDATION_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies the recommendation category specific to system recommenders. Must be a value from Lookup "ORA_WLF_RECOMND_CATEGORY". |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STATUS | VARCHAR2 | 30 |  | Yes | This column represents status of the row. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Indicates the date when the row is added |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Indicates the date when row is removed |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOMMENDER_CONFIG_N1 | Non Unique | WLF_RECOMMENDER_CONFIG_N1 | RECOMMENDATION_CATEGORY |
| WLF_RECOMMENDER_CONFIG_N2 | Non Unique | WLF_RECOMMENDER_CONFIG_N2 | RECOMMENDATION_PROFILE_ID |
| WLF_RECOMMENDER_CONFIG_U1 | Unique | Default | RECOMMENDER_CONFIG_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
