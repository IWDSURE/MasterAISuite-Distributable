# IRC_CAND_PROFILE_USAGES_M

This table contains  reference to candidates profile information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandprofileusagesm-26953.html#irccandprofileusagesm-26953](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandprofileusagesm-26953.html#irccandprofileusagesm-26953)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_PROFILE_USAGES_M_PK | CAND_PROFILE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_SEQUENCE, EFFECTIVE_LATEST_CHANGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_PROFILE_USAGE_ID | NUMBER |  | 18 | Yes | Surrogate ID for this table CAND_PROFILE_USAGES_M. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to table IRC_CANDIDATES PERSON_ID. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to profiles table HRT_PROIFLES_B. |
| PROFILE_TYPE | VARCHAR2 | 30 |  | Yes | HRT Profile Type. Talent Profile Type or Candidate Profile Type |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_PROFILE_USAGES_M_FK1 | Non Unique | Default | PERSON_ID |
| IRC_CAND_PROFILE_USAGES_M_FK2 | Non Unique | Default | PROFILE_ID |
| IRC_CAND_PROFILE_USAGES_M_PK | Unique | Default | CAND_PROFILE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_SEQUENCE, EFFECTIVE_LATEST_CHANGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
