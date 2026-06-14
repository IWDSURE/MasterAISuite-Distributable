# HRT_PROFILE_COI_JOBSUBSC

This table is used to maintain the job subscription data for a person for different job profiles.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilecoijobsubsc-15106.html#hrtprofilecoijobsubsc-15106](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilecoijobsubsc-15106.html#hrtprofilecoijobsubsc-15106)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_COI_JOBSUBSC_PK | JOB_SUBSCRIPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_SUBSCRIPTION_ID | NUMBER |  | 18 | Yes | JOB_SUBSCRIPTION_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PROFILE_ID | NUMBER |  | 18 | Yes | PROFILE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| JOB_ID | NUMBER |  | 18 | Yes | JOB_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_COI_JOBSUBSC_U1 | Unique | Default | JOB_SUBSCRIPTION_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
