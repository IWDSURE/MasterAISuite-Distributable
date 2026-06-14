# WLF_RECOMMENDATION_PROFILES

This table stores the details of the recommendation profiles.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** wlf_recommendation_profiles

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendationprofiles-18331.html#wlfrecommendationprofiles-18331](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendationprofiles-18331.html#wlfrecommendationprofiles-18331)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOMMENDATION_PROFILE_PK | RECOMMENDATION_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMENDATION_PROFILE_ID | NUMBER |  | 18 | Yes | System-generated unique identifier1 |
| RECOMMENDATION_PROFILE_NUMBER | VARCHAR2 | 30 |  | Yes | Unique number identifier for profile. |
| RECOMMENDATION_TYPE | VARCHAR2 | 30 |  |  | Represents the type of recommendation , system generated or user created. |
| PRIORITY | VARCHAR2 | 30 |  | Yes | Specifies priority for the recommendation profile. |
| STATUS | VARCHAR2 | 30 |  |  | Status of the recommendation profile. |
| ATTRIBUTION_ID | NUMBER |  | 18 |  | Represnts the id of the urecommender. |
| ATTRIBUTION_TYPE | VARCHAR2 | 30 |  |  | Represnts the type of the recoemmender |
| ATTRIBUTION_LOOKUP_CODE | VARCHAR2 | 30 |  |  | Represents the lookup code for the recommender |
| RECOMMENDATION_COMMENTS | VARCHAR2 | 4000 |  |  | Represnets the comments for recoomendation profile. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| NAME | VARCHAR2 | 250 |  |  | Represents the name of the recommendation profile |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Represents the description of the recommendation profile |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Represent the source type of the recommendation profile |
| SOURCE_ID | VARCHAR2 | 20 |  |  | Represent the source id of the recommendation profile |
| SCHEDULE_TYPE | VARCHAR2 | 30 |  |  | Represents recommendation expansion One-time or Ongoing |
| SCHEDULE_START | TIMESTAMP |  |  |  | Represents recommendation scehdule start date |
| SCHEDULE_END | TIMESTAMP |  |  |  | Represents recommendation scehdule end date for reconcile |
| SKILL_VARIANT_CONFIG_ID | NUMBER |  | 18 |  | Reference to SKILL_VARIANT_CONFIG_ID from WLF_SKILL_VARIANT_CONFIG, applicable for "Gaps"/"skills" recommenders |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Flag to indicate elastic index is reconciled with latest changes. |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason for recommendation profile status change |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the object. |
| STATUS_CHANGE_COMMENTS | VARCHAR2 | 4000 |  |  | Represents the comments for status change on recommendation profile. |
| GAP_RECOM_INCL_UNC_ROLE_SKILLS | VARCHAR2 | 1 |  |  | Specifies if the uncurated skills should be included related to roles (i.e., Job/position profile) for "Gaps in Current Role" and "Gaps in Careers of Interest" recommenders. |
| GAP_RECOM_INCL_UNC_RES_SKILLS | VARCHAR2 | 1 |  |  | Specifies if the uncurated skills should be included related to resources (e.g., learning item, journey, etc.,) for "Gaps in Current Role" and "Gaps in Careers of Interest" recommenders. |
| INCL_CATALOG_SEARCH_RESULTS | VARCHAR2 | 1 |  |  | Specifies whether to use catalog search to suggest resources that fulfill skill gaps. |
| PROCESS_JOB_ID | NUMBER |  | 18 |  | ESS request id that processed the recommendation profile. |
| INCL_RES_WITH_OUTCOME_ONLY | VARCHAR2 | 1 |  |  | Specifies whether to consider only the resources that writes to profile i.e., have an outcome. |
| INCL_REQ_ROLE_SKILL_QUAL_ONLY | VARCHAR2 | 1 |  |  | Specifies whether to consider only skills and qualifications that are marked as required in the role profile. |
| ADDITIONAL_INFO | CLOB |  |  |  | Captures recommendation profile additional metadata information |
| INCL_RES_MATCH_SKILL_SYNONYM | VARCHAR2 | 1 |  |  | Specifies whether to consider Include resources profiled with skill synonyms |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOMMENDATION_PROFILES_U1 | Unique | WLF_RECOMMENDATION_PROFILES_U1 | RECOMMENDATION_PROFILE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
