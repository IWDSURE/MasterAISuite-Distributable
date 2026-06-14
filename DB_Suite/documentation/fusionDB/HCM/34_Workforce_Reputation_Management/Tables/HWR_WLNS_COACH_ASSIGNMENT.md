# HWR_WLNS_COACH_ASSIGNMENT

This table stores the coaching assignment request details.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoachassignment-3479.html#hwrwlnscoachassignment-3479](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoachassignment-3479.html#hwrwlnscoachassignment-3479)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_COACH_ASSIGNMENT_PK | ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | This is the primary key for the coaching assignments tables. |
| COACH_ID | NUMBER |  | 18 |  | This column indicates the id of the coach assigned for the record. |
| COACHING_TOPIC_ID | NUMBER |  | 18 |  | This column indicates the id of the coaching topic for which the coaching request is raised. |
| COACHEE_PERSON_ID | NUMBER |  | 18 | Yes | This column indicates the person id of the requester/coachee. |
| STATUS | VARCHAR2 | 64 |  | Yes | This column indicates status of the coaching assignment record. |
| START_DATE | TIMESTAMP |  |  |  | This column indicates the date at the beginning of coaching assignment with a coach. |
| END_DATE | TIMESTAMP |  |  |  | This column indicates the date at the end of coaching assignment with a coach. |
| SOURCE_ID | NUMBER |  | 18 |  | This column is used to store the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column is used to store the id of conversation. |
| ASSIGNMENT_ATTR_1 | VARCHAR2 | 400 |  |  | This column for extra coaching assignment attribute 1. |
| ASSIGNMENT_ATTR_2 | VARCHAR2 | 400 |  |  | This column for storing extra coaching assignment attribute 2. |
| ASSIGNMENT_ATTR_3 | VARCHAR2 | 400 |  |  | This column for storing extra coaching assignment attribute 3. |
| ASSIGNMENT_ATTR_4 | NUMBER |  | 18 |  | This column for storing extra coaching assignment attribute 4. |
| ASSIGNMENT_ATTR_5 | NUMBER |  | 18 |  | This column for storing extra coaching assignment attribute 5. |
| ASSIGNMENT_ATTR_6 | TIMESTAMP |  |  |  | This column for storing extra coaching assignment attribute 6. |
| ASSIGNMENT_ATTR_7 | TIMESTAMP |  |  |  | This column for storing extra coaching assignment attribute 7. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_COACH_ASSIGNMENT_U1 | Unique | Default | ASSIGNMENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
