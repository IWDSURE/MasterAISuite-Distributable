# WLF_ATTEMPT_RELATIONS

Table to store attempt relations with tasks,assignments and learning items

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattemptrelations-6648.html#wlfattemptrelations-6648](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattemptrelations-6648.html#wlfattemptrelations-6648)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ATTEMPT_RELATIONS_PK | ATTEMPT_RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTEMPT_RELATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| ATTEMPT_ID | NUMBER |  | 18 |  | Refers to root attempt id of attempts table |
| ATTEMPT_TYPE | VARCHAR2 | 30 |  |  | Refers to attempt type of attempts table |
| ATTEMPTED_BY_ID | NUMBER |  | 18 | Yes | Refers to attempt owner id |
| ATTEMPTED_BY_TYPE | VARCHAR2 | 30 |  | Yes | Attempts owner type like learner , admin , system |
| ATTEMPT_CREATION_DATE | TIMESTAMP |  |  | Yes | Creation date of attempt relation |
| ATTEMPT_COMPLETION_DATE | TIMESTAMP |  |  |  | Refers to attempt completion date |
| RELATED_OBJECT_ID | NUMBER |  | 18 | Yes | Refers to related object like task,assignment identifier |
| RELATED_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Refers to type of related object like task or assignment |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Refers to learning item on which relation entry is added |
| LEARNING_ITEM_TYPE | VARCHAR2 | 30 |  | Yes | Type of the learning item |
| LEARNER_ID | NUMBER |  | 18 | Yes | Learner Id of the learning item |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the attempt , could be FAILED or COMPLETED |
| ATTEMPT_OUTCOME | VARCHAR2 | 30 |  |  | Column to store attempt outcome when saving (before submit). |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SCORE | NUMBER |  |  |  | Learner score for the attempt |
| EFFORT_SEC | NUMBER |  |  |  | Effort spent by learner in seconds |
| ATTEMPT_RELATION_NUMBER | VARCHAR2 | 30 |  |  | UserKey to uniquely identify attempt (on content) relation with assignment task. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ATTEMPT_RELATIONS_N1 | Non Unique | Default | ATTEMPT_ID |
| WLF_ATTEMPT_RELATIONS_N2 | Non Unique | Default | LEARNER_ID |
| WLF_ATTEMPT_RELATIONS_N3 | Non Unique | Default | RELATED_OBJECT_ID, RELATED_OBJECT_TYPE |
| WLF_ATTEMPT_RELATIONS_U1 | Unique | Default | ATTEMPT_RELATION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
