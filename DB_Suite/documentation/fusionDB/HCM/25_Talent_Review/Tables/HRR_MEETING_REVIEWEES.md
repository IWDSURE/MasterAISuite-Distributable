# HRR_MEETING_REVIEWEES

This meeting table includes the list of reviewees for the meeting.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingreviewees-31749.html#hrrmeetingreviewees-31749](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingreviewees-31749.html#hrrmeetingreviewees-31749)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_MEETING_REVIEWEES_PK | MEETING_REVIEWEE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEETING_REVIEWEE_ID | NUMBER |  | 18 | Yes | Primary key to this table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_MEETINGS |
| REVIEWEE_PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID of the reviewer. |
| REVIEWEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | REVIEWEE_ASSIGNMENT_ID |
| REVIEWER_PERSON_ID | NUMBER |  | 18 |  | Person Id if reviwer who will review the meeting content of the reviewee |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_MEETING_REVIEWEES_FK1 | Non Unique | FUSION_TS_TX_DATA | MEETING_ID |
| HRR_MEETING_REVIEWEES_PK | Unique | FUSION_TS_TX_DATA | MEETING_REVIEWEE_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
