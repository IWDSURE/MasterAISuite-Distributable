# HRT_PROFILE_BESTFIT_RESULT

This table is used to populate the matching best fit results for the Profiles

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilebestfitresult-4090.html#hrtprofilebestfitresult-4090](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilebestfitresult-4090.html#hrtprofilebestfitresult-4090)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_BESTFIT_RESULT_PK | BESTFIT_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BESTFIT_RESULT_ID | NUMBER |  | 18 | Yes | Unique Identifier for Best Fit Match Results |
| TARGET_PROFILE_ID | NUMBER |  | 18 | Yes | Target Profile ID of Person or Model Profile |
| TARGET_PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | Target Profile Type ID of Person or Model Profile |
| TARGET_PROFILE_TYPE_CODE | VARCHAR2 | 120 |  |  | Target Profile Type Code of Person or Model Profile |
| SEARCH_INSTANCE_ID | NUMBER |  | 18 |  | Search Instance ID of Person or Model profile |
| PERSON_ID | NUMBER |  | 18 |  | PERSON ID of a Person Profile |
| SOURCE_PROFILE_ID | NUMBER |  | 18 | Yes | Source Profile ID of Person or Model Profile |
| SOURCE_PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | Source Profile Type ID of Person or Model Profile |
| SOURCE_PROFILE_TYPE_CODE | VARCHAR2 | 120 |  |  | Source Profile Type Code of Person or Model Profile |
| COMPETENCY_SCORE | NUMBER |  | 10 |  | Matching score for Comptencies |
| LANGUAGE_SCORE | NUMBER |  | 10 |  | Matching score for Languages |
| CERTIFICATION_SCORE | NUMBER |  | 10 |  | Matching score for Certification |
| AWARDS_SCORE | NUMBER |  | 10 |  | Matching score for Awards |
| MEMBERSHIP_SCORE | NUMBER |  | 10 |  | Matching score for Membership |
| DEGREE_SCORE | NUMBER |  | 10 |  | Matching score for Degrees |
| WORKREQ_SCORE | NUMBER |  | 10 |  | Matching score for Work Requirements |
| WEIGHTED_SCORE | NUMBER |  | 10 |  | Overall Weighted Matching Score |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_BESTFIT_RES_N1 | Non Unique | Default | SOURCE_PROFILE_ID, TARGET_PROFILE_TYPE_CODE |
| HRT_PROFILE_BESTFIT_RES_PK | Unique | Default | BESTFIT_RESULT_ID |
| HRT_PROFILE_BESTFIT_RES_U1 | Unique | Default | TARGET_PROFILE_ID, SOURCE_PROFILE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
