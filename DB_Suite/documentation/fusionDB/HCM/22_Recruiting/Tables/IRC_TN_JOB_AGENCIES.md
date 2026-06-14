# IRC_TN_JOB_AGENCIES

This table stores the results of the availability context .

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobagencies-14391.html#irctnjobagencies-14391](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobagencies-14391.html#irctnjobagencies-14391)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_AGENCIES_PK | JOB_AGENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_AGENCY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| TN_JOB_ID | NUMBER |  | 18 | Yes | Store the job id.Foreign key to the irc_tn_jobs_b table |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | Stores the Subscriber Id. Foreign key to the irc_tn_subscribers table |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agency.Foreign key to the irc_agencies table |
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
| IRC_TN_JOB_AGENCIES_FK1 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_JOB_AGENCIES_FK2 | Non Unique | Default | AGENCY_ID |
| IRC_TN_JOB_AGENCIES_FK3 | Non Unique | Default | TN_JOB_ID |
| IRC_TN_JOB_AGENCIES_PK | Unique | Default | JOB_AGENCY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
