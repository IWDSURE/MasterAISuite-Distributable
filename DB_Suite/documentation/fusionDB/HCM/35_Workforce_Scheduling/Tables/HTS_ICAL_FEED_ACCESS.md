# HTS_ICAL_FEED_ACCESS

Stores the employee calendar feed access times

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsicalfeedaccess-14452.html#htsicalfeedaccess-14452](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsicalfeedaccess-14452.html#htsicalfeedaccess-14452)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_ICAL_FEED_ACCESS_PK | ICAL_FEED_ACCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ICAL_FEED_ACCESS_ID | NUMBER |  | 18 | Yes | Primary Key |
| ICAL_FEED_ID | NUMBER |  | 18 | Yes | Reference to the feed record in the feed details table |
| ACCESS_TIME | TIMESTAMP |  |  | Yes | Time when the most recent access to the ical feed was requested |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id to accomodate multi tenant systems |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_ICAL_FEED_ACCESS_U1 | Unique | Default | ICAL_FEED_ACCESS_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
