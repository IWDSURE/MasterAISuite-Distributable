# HWR_WLNS_ELIG_PROFILE

This table stores eligibility profile details for wellness objects like goal, task, etc.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnseligprofile-19866.html#hwrwlnseligprofile-19866](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnseligprofile-19866.html#hwrwlnseligprofile-19866)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_ELIG_PROFILE_PK | ELIG_PRFL_ID, WLNS_OBJ_ID, WLNS_ELIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WLNS_ELIG_ID | NUMBER |  | 18 | Yes | This is the Id identifying the entry in this table. |
| WLNS_OBJ_TYPE | VARCHAR2 | 100 |  | Yes | This enum is the type of wellness object created on profile, like GOAL, CONTEST, TASK, etc. |
| WLNS_OBJ_ID | NUMBER |  | 18 | Yes | This is the id of wellness object which can be used to map to goal and competition table. |
| ELIG_PRFL_NAME | VARCHAR2 | 200 |  | Yes | This is the Eligibility Profile name which the entity is created. |
| ELIG_PRFL_ID | NUMBER |  | 18 | Yes | This is the Eligibility Profile ID which the entity is created. |
| ELIG_OBJ_ID | NUMBER |  | 18 | Yes | This is the Eligibility Object ID for which profiles are attached. This is generated from eligibility objects table. |
| ELIG_ESS_JOB_REQUEST_ID | NUMBER |  | 18 | Yes | This is the Eligibility ESS job Request ID for which the eligibility object profiles need to be evaluated. |
| IS_PRFL_RESULT_AVAILABLE | NUMBER |  | 18 | Yes | This determines if the Eligibility ESS evaluation job is completed and Eligibility profiles result is available. |
| LAST_PROCESSED_DATE | TIMESTAMP |  |  |  | This determines the last trigerred time of Evaluate Eligibility ESS for this wlns_obj_id. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_ELIG_PROFILE_U1 | Unique | Default | ELIG_PRFL_ID, WLNS_OBJ_ID, WLNS_ELIG_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
