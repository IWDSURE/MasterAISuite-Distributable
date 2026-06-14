# HRG_GOAL_ALIGNMENTS

This table stores the information on goal alignment. The table stores the goal id and the aligned goal id.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalalignments-14504.html#hrggoalalignments-14504](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrggoalalignments-14504.html#hrggoalalignments-14504)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_GOAL_ALIGNMENTS_PK | GOAL_ALIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ALIGNMENT_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOALS, which holds the ID of goal. It forms the left side of the goal alignment association where as the "ALIGNED_GOAL_ID" column in this table forms the right side of the alignment association |
| ALIGNED_GOAL_ID | NUMBER |  | 18 | Yes | Foreign key to HRG_GOALS, which holds the ID of goal. It forms the right side of the goal alignment association where as the "GOAL_ID" column in this table form the left side of the alignment association |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_GOAL_ALIGNMENTS_FK1 | Non Unique | Default | GOAL_ID |
| HRG_GOAL_ALIGNMENTS_FK2 | Non Unique | Default | ALIGNED_GOAL_ID |
| HRG_GOAL_ALIGNMENTS_PK | Unique | Default | GOAL_ALIGNMENT_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
