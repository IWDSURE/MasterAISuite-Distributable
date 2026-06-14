# HTS_ICAL_FEEDS

Stores the employee calendar feed preferences, along with feed security properties, rate limiting settings etc.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsicalfeeds-30284.html#htsicalfeeds-30284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsicalfeeds-30284.html#htsicalfeeds-30284)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_ICAL_FEEDS_PK | ICAL_FEED_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ICAL_FEED_ID | NUMBER |  | 18 | Yes | Application-generated primary key |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Indicates if the feed is active |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person associated with the feed |
| SALT | VARCHAR2 | 512 |  |  | Base64-encoded 128-bit randomly generated value used to enhance the security of person id and expiration time |
| TOKEN | VARCHAR2 | 1000 |  |  | URL encoded security token generated when creating the feed |
| EXPIRATION_TIME | TIMESTAMP |  |  |  | Feed or URL expiration time |
| RANGE_LEFT_EXTENT | NUMBER |  | 3 |  | Number of pastweeks to consider relative to the request instant |
| RANGE_RIGHT_EXTENT | NUMBER |  | 3 |  | Number of future weeks to consider relative the the request instant |
| INCL_SHIFTS_FLAG | VARCHAR2 | 1 |  |  | Boolean indicating if the calendar content contains events corresponding to schedule shifts |
| INCL_ABSENCES_FLAG | VARCHAR2 | 1 |  |  | Boolean indicating if the calendar content contains events denoting absences intersecting the datarange |
| INCL_PUBLIC_HOLIDAYS_FLAG | VARCHAR2 | 1 |  |  | Boolean indicating if the calendar content contains public holidays |
| FIXED_WINDOW_START_TIME | TIMESTAMP |  |  |  | Start time for the current fixed time window |
| FIXED_WINDOW_END_TIME | TIMESTAMP |  |  |  | End time for the current fixed time window |
| ACCESS_COUNT | NUMBER |  | 6 |  | Counter used to limit access within the fixed window |
| LAST_ACCESS_TIME | TIMESTAMP |  |  |  | When the most recent access to the ical feed was requested |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id or Business group id to identify in a multi tenant system |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_ICAL_FEEDS_U1 | Unique | Default | ICAL_FEED_ID |
| HTS_ICAL_FEEDS_U2 | Unique | Default | PERSON_ID, CASE WHEN "ACTIVE_FLAG" = 'Y' OR "ACTIVE_FLAG" IS NULL THEN 'Y' ELSE TO_CHAR("ICAL_FEED_ID") END |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
