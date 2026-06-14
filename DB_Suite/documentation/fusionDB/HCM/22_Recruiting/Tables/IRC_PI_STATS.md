# IRC_PI_STATS

This table logs the profile importer calls from Oracle Recruiting Cloud.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpistats-15307.html#ircpistats-15307](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpistats-15307.html#ircpistats-15307)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_PI_STATS_PK | STAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STAT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| EVENT_DATE | DATE |  |  |  | Store the event date |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| PHASE_CODE | VARCHAR2 | 30 |  |  | Stores code identifying the category phase to which the service belongs. |
| STATUS | VARCHAR2 | 30 |  |  | Stores status of the service calls |
| STATUS_CODE | NUMBER |  | 5 |  | Stores HTTP status of the response. |
| HITS | NUMBER |  | 18 |  | Number of hits |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_PI_STATS_N1 | Non Unique | Default | EVENT_DATE |
| IRC_PI_STATS_PK | Unique | Default | STAT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
