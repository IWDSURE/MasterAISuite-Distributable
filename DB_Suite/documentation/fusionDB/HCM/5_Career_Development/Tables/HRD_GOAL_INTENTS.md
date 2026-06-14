# HRD_GOAL_INTENTS

It stores association between goal and its intent whcich can be of type development, personal and Organizational.

## Details

**Schema:** FUSION

**Object owner:** HRD

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdgoalintents-19703.html#hrdgoalintents-19703](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdgoalintents-19703.html#hrdgoalintents-19703)

## Primary Key

| Name | Columns |
|------|----------|
| HRD_GOAL_INTENTS_PK | GOAL_INTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_INTENT_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| GOAL_ID | NUMBER |  | 18 | Yes | Foreign key to goal table HRG_GOALS. |
| REFERENCE_TYPE | VARCHAR2 | 30 |  | Yes | Corresponding intent reference type value is either CURRENT_ROLE,
CAREER_OF_INTEREST, ORGANIZATIONAL, PERSONAL. |
| REFERENCE_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_PROFILE_INTERESTS, HRD_PERSONAL_INTENTS |
| PERSON_ID | NUMBER |  | 18 | Yes | To hold the person_id of the person having this Goal Intent |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRD_GOAL_INTENTS_N1 | Non Unique | Default | GOAL_ID |
| HRD_GOAL_INTENTS_N2 | Non Unique | Default | REFERENCE_ITEM_ID, PERSON_ID |
| HRD_GOAL_INTENTS_N3 | Non Unique | Default | PERSON_ID |
| HRD_GOAL_INTENTS_PK | Unique | Default | GOAL_INTENT_ID |

---

[← Back to Index](../5_Career_Development_Tables_Index.md)
