# WLF_RECOMMENDATIONS

This table stores the details of the recommendations in different recommendation categores.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendations-30134.html#wlfrecommendations-30134](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendations-30134.html#wlfrecommendations-30134)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOMMENDATIONS_PK | RECOMMENDATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMENDATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| RECOMMENDATION_SUMMARY_ID | NUMBER |  | 18 | Yes | Reference to the recommendation summary row. |
| RECOMMENDATION_NUMBER | VARCHAR2 | 30 |  | Yes | System generated unique identifier for the recommendation. |
| STATUS | VARCHAR2 | 30 |  | Yes | Specifies the status for the recommendation. |
| STATUS_SCOPE_ID | NUMBER |  | 18 |  | Identifier for the status scope used to derive the recommendation status. |
| RECOMMENDATION_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies the category for the recommendation. |
| RECOMMENDATION_RANK | NUMBER |  |  |  | Specifies the order of the recommendation in a given recommendation category. |
| RECOMMENDATION_SCORE | NUMBER |  |  |  | Specifies the score for the recommendation in a given recommendation category. |
| RECOMMENDED_ON_DATE | TIMESTAMP |  |  | Yes | Specifies the date recommendation is effective. |
| WITHDRAWN_DATE | DATE |  |  |  | Specifies the date recommendation is withdrawn. |
| REASON_CODE | VARCHAR2 | 30 |  |  | Specifies the reason for withdrawing the recommendation. |
| ATTRIBUTION_ID | NUMBER |  | 18 |  | Identifier for the assigner of the recommendation. |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  | Yes | Specifies the persona used to create the recommendation. |
| ATTRIBUTION_LOOKUP_CODE | VARCHAR2 | 30 |  |  | Specifies the attribution type for the assigner of the recommendation. |
| STATUS_CHANGE_TYPE | VARCHAR2 | 30 |  |  | Specifies the type of status change for the recommendation. |
| STATUS_CHANGE_COMMENT | VARCHAR2 | 4000 |  |  | Comments to be captured during the status change. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RELATION_ID | NUMBER |  | 18 |  | Represents the Relation Id of the recommendation profile. |
| RECOMMENDATION_PROFILE_ID | NUMBER |  | 18 |  | Represents the recommendation profile id |
| ESS_JOB_ID | NUMBER |  | 18 |  | Represents ESS job id that created or modified the recommendation. |
| RECOMMENDATION_COMMENTS | VARCHAR2 | 4000 |  |  | Represnets the comments for recoomendation. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOMMENDATIONS_N1 | Non Unique | Default | RECOMMENDATION_SUMMARY_ID |
| WLF_RECOMMENDATIONS_N2 | Non Unique | Default | STATUS |
| WLF_RECOMMENDATIONS_N3 | Non Unique | Default | RECOMMENDATION_CATEGORY |
| WLF_RECOMMENDATIONS_N4 | Non Unique | Default | RECOMMENDATION_NUMBER |
| WLF_RECOMMENDATIONS_N5 | Non Unique | Default | RECOMMENDED_ON_DATE |
| WLF_RECOMMENDATIONS_N6 | Non Unique | Default | TRUNC("RECOMMENDED_ON_DATE") |
| WLF_RECOMMENDATIONS_N7 | Non Unique | Default | ATTRIBUTION_ID, ATTRIBUTION_TYPE |
| WLF_RECOMMENDATIONS_N8 | Non Unique | Default | ATTRIBUTION_TYPE |
| WLF_RECOMMENDATIONS_N9 | Non Unique | Default | ESS_JOB_ID |
| WLF_RECOMMENDATIONS_U1 | Unique | Default | RECOMMENDATION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
