# IRC_LI_JOB_SUBMISSION_MAPPING

Stores the job application submission between ORC and LinkedIn

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclijobsubmissionmapping-7201.html#irclijobsubmissionmapping-7201](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclijobsubmissionmapping-7201.html#irclijobsubmissionmapping-7201)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_JOB_SUBMISSION_MAPP_PK | SUBMISSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Primary Key for the table and also foreign key to IRC_SUBMISSIONS. |
| LI_SUBMISSION_ID | VARCHAR2 | 255 |  | Yes | The unique job application submission id on LinkedIn |
| ADDITIONAL_INFO1 | VARCHAR2 | 2000 |  |  | To store additional info for the job application submission |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_JOB_SUBMISSION_MAPP_N1 | Non Unique | Default | UPPER("LI_SUBMISSION_ID") |
| IRC_LI_JOB_SUBMISSION_MAPP_PK | Unique | Default | SUBMISSION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
