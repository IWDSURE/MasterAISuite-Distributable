# HRR_MEETING_SUCCPLANS

This table includes the list of succession plans for the meeting.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingsuccplans-28763.html#hrrmeetingsuccplans-28763](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingsuccplans-28763.html#hrrmeetingsuccplans-28763)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_MEETING_SUCCPLANS_PK | BUSINESS_GROUP_ID, MEETING_SUCCPLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| MEETING_SUCCPLAN_ID | NUMBER |  | 18 | Yes | System generated Primary key to this table. |
| MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_MEETINGS table |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan Id of the succession plan tied to the meeting. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_MEETING_SUCCPLANS_FK1 | Non Unique | FUSION_TS_TX_DATA | MEETING_ID |
| HRR_MEETING_SUCCPLANS_PK | Unique | FUSION_TS_TX_DATA | BUSINESS_GROUP_ID, MEETING_SUCCPLAN_ID |
| HRR_MEETING_SUCCPLANS_UK1 | Unique | FUSION_TS_TX_DATA | BUSINESS_GROUP_ID, MEETING_ID, PLAN_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
