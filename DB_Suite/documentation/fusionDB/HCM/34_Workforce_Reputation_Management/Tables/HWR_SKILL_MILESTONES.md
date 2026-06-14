# HWR_SKILL_MILESTONES

This table holds the milestones

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillmilestones-27023.html#hwrskillmilestones-27023](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillmilestones-27023.html#hwrskillmilestones-27023)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SKILL_MILESTONES_PK | MILESTONE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MILESTONE_ID | NUMBER |  | 18 | Yes | It holds the milestone id |
| MILESTONE_NAME | VARCHAR2 | 200 |  | Yes | This column holds the milestone name |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This column contains the milestone description |
| TARGET_COMPLETION_DATE | DATE |  |  | Yes | This column holds the target completion date |
| TOPIC_ID | NUMBER |  | 18 | Yes | This column holds the topic id |
| STATUS | VARCHAR2 | 5 |  | Yes | This holds the status of the milestone |
| GLBL_PRFL_ID | NUMBER |  | 18 |  | This column holds the global profile id |
| PERSON_ID | NUMBER |  | 18 | Yes | This column contains person id |
| MILESTONES_ATTR_1 | VARCHAR2 | 200 |  |  | MILESTONES_ATTR_1.This is the extra attribute in case if needed |
| MILESTONES_ATTR_2 | VARCHAR2 | 200 |  |  | MILESTONES_ATTR_2.This is the extra attribute in case if needed |
| MILESTONES_ATTR_3 | NUMBER |  | 18 |  | MILESTONES_ATTR_3.This is the extra attribute in case if needed |
| MILESTONES_ATTR_4 | NUMBER |  | 18 |  | MILESTONES_ATTR_4.This is the extra attribute in case if needed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SKILL_MILESTONES_U1 | Unique | FUSION_TS_TX_DATA | MILESTONE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
