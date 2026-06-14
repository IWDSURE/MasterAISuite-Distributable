# IRC_TN_JOB_APP_BID_INFO

This is the table for storing job applications bid information on Talent Network.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobappbidinfo-8840.html#irctnjobappbidinfo-8840](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobappbidinfo-8840.html#irctnjobappbidinfo-8840)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_APP_BID_INFO_PK | JOB_APP_BID_INFO |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_APP_BID_INFO | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | To store the subscriber id. Foreign Key to IRC_TN_SUBSCRIBERS. |
| JOB_APP_ID | NUMBER |  | 18 | Yes | To store the job app id. Foreign Key to IRC_TN_JOB_APPLICATIONS. |
| BID_RATE | NUMBER |  |  |  | Stores the bid rate for this job application. |
| BID_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Stores the currency code for the bid for this job application as a lookup code. |
| PAY_BASIS_CODE | VARCHAR2 | 30 |  |  | Stores the pay frequency as a lookup code. |
| COMMENTS | VARCHAR2 | 1000 |  |  | Stores comments about this job application bid information. |
| REF_FA_SUBMISSION_ID | VARCHAR2 | 1000 |  |  | Stores the reference submission id that is provided with this job application bid information. |
| AGENCY_PROFILE_URL | VARCHAR2 | 1000 |  |  | Stores the agency provided profile url of the candidate for this job application bid information. |
| DISPLAY_RATE | VARCHAR2 | 1000 |  |  | Stores the formatted rate information of this job application bid information. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_APP_BID_INFO_FK1 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_JOB_APP_BID_INFO_FK2 | Non Unique | Default | JOB_APP_ID |
| IRC_TN_JOB_APP_BID_INFO_PK | Unique | Default | JOB_APP_BID_INFO |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
