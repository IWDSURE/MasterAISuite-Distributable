# IRC_SOURCE_TRACKING

The IRC_SOURCE_TRACKING will contain all the tracking information about the Source of Application.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsourcetracking-10240.html#ircsourcetracking-10240](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsourcetracking-10240.html#ircsourcetracking-10240)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SOURCE_TRACKING_PK | SOURCE_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_TRACKING_ID | NUMBER |  | 18 | Yes | Primary key for the Source tracking table. |
| AGENCY_NAME | VARCHAR2 | 240 |  |  | Column to store Name for Agency. |
| AGENT_NAME | VARCHAR2 | 300 |  |  | Full Name of an Agent. |
| SOURCE_LEVEL | VARCHAR2 | 30 |  |  | will contain the source level value for the given record |
| DIMENSION_ID | NUMBER |  | 18 |  | Foreign key to the dimension definition. (IRC_DIMENSION_DEF_B) |
| CAMPAIGN_CODE | VARCHAR2 | 64 |  |  | The campaign code pointing to the IRC_CAMPAIGNS_B table. |
| REQUISITION_ID | NUMBER |  | 18 |  | The requisition ID that is stored in the IRC_REQUISITIONS_B table. |
| FROM_REQUISITION_ID | NUMBER |  | 18 |  | The requisition ID that is stored in the IRC_REQUISITIONS_B table. Used for the add to req from another requisition. |
| TOKEN_ID | NUMBER |  | 18 |  | The related token ID to is stored in IRC_CX_CNDT_EMAIL_TKNS table. |
| SUBMISSION_ID | NUMBER |  | 18 |  | The submission ID that is stored in the IRC_SUBMISSIONS table. |
| PROSPECT_ID | NUMBER |  | 18 |  | The related token ID to is stored in IRC_PROSPECTS table. |
| REFERRAL_ID | NUMBER |  | 18 |  | The referral ID that is stored in the IRC_RF_REFERRALS table. |
| RECRUITER_ID | NUMBER |  | 18 |  | The person id related to the recruiter that is stored in the PER_PERSONS table. |
| POOL_ID | NUMBER |  | 18 |  | The pool id that is stored in the HRT_POOLS_B table. |
| CANDIDATE_NUMBER | VARCHAR2 | 30 |  |  | The person id related to the internal candidate that is stored in the IRC_CANDIDATES table. |
| SHARE_ID | NUMBER |  | 18 |  | The share id that is stored IRC_RF_SHARES table. |
| PARENT_SOURCE_TRACKING_ID | NUMBER |  | 18 |  | The parent source tracking id pointing to the same table IRC_SOURCE_TRACKING. table. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FROM_POOL_ID | NUMBER |  | 18 |  | The pool ID that is stored in the HRT_POOLS_B table. Used for the add to pool action from another candidate pool. |
| POOL_MEMBER_ID | NUMBER |  | 18 |  | The pool member id related to pool member that is stored in the IRC_CAND_POOL_MEMBERS table. |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Foreign key to the IRC_CX_SITES_B table. |
| AGENT_ID | NUMBER |  | 18 |  | The Agent Id that is stored in the IRC_AGENTS |
| AGENCY_ID | NUMBER |  | 18 |  | The Agency Id that is stored in the IRC_AGENCIES |
| REFERRED_DATE | DATE |  |  |  | Date of referral by the Agency |
| CAMPAIGN_POST_ID | NUMBER |  | 18 |  | Post id of the social campaign posts. Foreign key to IRC_CAMP_ASSETS_B |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the status of the of the Source tracking record |
| EVENT_ID | NUMBER |  | 18 |  | The id of the event that the candidate is currently part of. The Event ID that is stored in the IRC_REC_EVENTS_B table. |
| FROM_EVENT_ID | NUMBER |  | 18 |  | The id of the event from which the candidate is added. Foreign key to IRC_REC_EVENTS_B. |
| INACTIVATION_DATE | DATE |  |  |  | Date on which the Sourectracking record is inactivated |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SOURCE_TRACKING_FK1 | Non Unique | Default | PARENT_SOURCE_TRACKING_ID |
| IRC_SOURCE_TRACKING_FK10 | Non Unique | Default | SHARE_ID |
| IRC_SOURCE_TRACKING_FK11 | Non Unique | Default | SUBMISSION_ID |
| IRC_SOURCE_TRACKING_FK12 | Non Unique | Default | FROM_POOL_ID |
| IRC_SOURCE_TRACKING_FK13 | Non Unique | Default | POOL_MEMBER_ID |
| IRC_SOURCE_TRACKING_FK14 | Non Unique | Default | SITE_NUMBER |
| IRC_SOURCE_TRACKING_FK15 | Non Unique | Default | AGENT_ID |
| IRC_SOURCE_TRACKING_FK16 | Non Unique | Default | AGENCY_ID |
| IRC_SOURCE_TRACKING_FK17 | Non Unique | Default | EVENT_ID |
| IRC_SOURCE_TRACKING_FK18 | Non Unique | Default | FROM_EVENT_ID |
| IRC_SOURCE_TRACKING_FK2 | Non Unique | Default | CAMPAIGN_CODE |
| IRC_SOURCE_TRACKING_FK3 | Non Unique | Default | CANDIDATE_NUMBER |
| IRC_SOURCE_TRACKING_FK4 | Non Unique | Default | RECRUITER_ID |
| IRC_SOURCE_TRACKING_FK5 | Non Unique | Default | REFERRAL_ID |
| IRC_SOURCE_TRACKING_FK6 | Non Unique | Default | REQUISITION_ID |
| IRC_SOURCE_TRACKING_FK7 | Non Unique | Default | DIMENSION_ID, CANDIDATE_NUMBER |
| IRC_SOURCE_TRACKING_FK8 | Non Unique | Default | TOKEN_ID |
| IRC_SOURCE_TRACKING_FK9 | Non Unique | Default | POOL_ID |
| IRC_SOURCE_TRACKING_N1 | Non Unique | Default | PROSPECT_ID |
| IRC_SOURCE_TRACKING_PK | Unique | Default | SOURCE_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
