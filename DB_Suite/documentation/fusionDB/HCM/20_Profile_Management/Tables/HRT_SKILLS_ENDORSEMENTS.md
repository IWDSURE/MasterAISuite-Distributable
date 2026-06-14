# HRT_SKILLS_ENDORSEMENTS

This table stores skill endorsement information.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsendorsements-9182.html#hrtskillsendorsements-9182](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsendorsements-9182.html#hrtskillsendorsements-9182)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_ENDORSEMENTS_PK | ENDORSEMENT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENDORSEMENT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SOURCE | VARCHAR2 | 240 |  |  | SOURCE |
| SOURCE_OBJECT_ID | NUMBER |  | 18 |  | SOURCE_OBJECT_ID |
| ENDORSED_BY | VARCHAR2 | 240 |  |  | ENDORSED_BY |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_PROFILE_ITEMS table. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign key to Profiles table |
| REQUESTOR_PERSON_ID | NUMBER |  | 18 | Yes | Stores the PERSON_ID of the endorsement requestor. |
| ENDORSER_PERSON_ID | NUMBER |  | 18 | Yes | Stores the PERSON_ID of the endorser. |
| ENDORSEMENT_TYPE | VARCHAR2 | 30 |  |  | Stores the different endorsement types. Lookup type - ORA_HRT_SKILL_EVIDENCE_TYPE |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Stores the rating level associated to endorsement |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Stores the rating model used for endorsement rating. |
| STATUS | VARCHAR2 | 30 |  | Yes | Stores endorsement status. Lookup type - ORA_HRT_ENDORSEMENT_STATUS. Possible values are Pending, Completed, and Ignored |
| REQUESTED_DATE | TIMESTAMP |  |  | Yes | Stores the date on which endorsement is requested. |
| SKILL_SCORE_CONFIG_ID | NUMBER |  | 18 |  | Foreign key to HRT_SKILLS_SCORE_CONFIG table. |
| EXPIRY_DATE | DATE |  |  |  | Expiry date |
| ENDORSED_DATE | DATE |  |  |  | Endorsement date |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_ENDORSEMENTS_N1 | Non Unique | Default | SKILL_ID, STATUS, ENDORSEMENT_TYPE |
| HRT_SKILLS_ENDORSEMENTS_N2 | Non Unique | Default | ENDORSER_PERSON_ID, REQUESTOR_PERSON_ID |
| HRT_SKILLS_ENDORSEMENTS_U1 | Unique | Default | ENDORSEMENT_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
