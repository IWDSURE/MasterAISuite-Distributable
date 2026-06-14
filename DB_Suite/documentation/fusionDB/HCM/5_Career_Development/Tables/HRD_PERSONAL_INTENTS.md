# HRD_PERSONAL_INTENTS

It will store the personal intents created by the person for associating these intents with goals.

## Details

**Schema:** FUSION

**Object owner:** HRD

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdpersonalintents-17599.html#hrdpersonalintents-17599](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdpersonalintents-17599.html#hrdpersonalintents-17599)

## Primary Key

| Name | Columns |
|------|----------|
| HRD_PERSONAL_INTENTS_PK | PERSONAL_INTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSONAL_INTENT_ID | NUMBER |  | 18 | Yes | System generated primary key for this table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F |
| INTENT_NAME | VARCHAR2 | 400 |  | Yes | Name of the personal intent which will be used for tagging a goal. |
| PRIVACY_FLAG | VARCHAR2 | 30 |  | Yes | Privacy flag for intent to control display of intents to others. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRD_PERSONAL_INTENTS_N1 | Non Unique | Default | PERSON_ID |
| HRD_PERSONAL_INTENTS_PK | Unique | Default | PERSONAL_INTENT_ID |

---

[← Back to Index](../5_Career_Development_Tables_Index.md)
