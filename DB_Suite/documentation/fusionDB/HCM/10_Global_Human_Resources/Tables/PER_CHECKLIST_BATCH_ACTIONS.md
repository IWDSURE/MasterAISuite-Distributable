# PER_CHECKLIST_BATCH_ACTIONS

This table stores batch actions

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistbatchactions-16639.html#perchecklistbatchactions-16639](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistbatchactions-16639.html#perchecklistbatchactions-16639)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_BATCH_ACTIONS_PK | CHECKLIST_BATCH_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_BATCH_ACTION_ID | NUMBER |  | 18 | Yes | CHECKLIST_BATCH_ACTION_ID |
| CHECKLIST_PERIOD_ID | NUMBER |  | 18 |  | CHECKLIST_PERIOD_ID |
| BATCH_TYPE | VARCHAR2 | 30 |  |  | BATCH_TYPE |
| CHECKLIST_ALLOCATION_ID | NUMBER |  | 18 |  | CHECKLIST_ALLOCATION_ID |
| CHECKLIST_ID | NUMBER |  | 18 |  | CHECKLIST_ID |
| BATCH_NAME | VARCHAR2 | 4000 |  |  | BATCH_NAME |
| BATCH_SOURCE | VARCHAR2 | 30 |  |  | BATCH_SOURCE |
| ASSIGNED_DATE | DATE |  |  |  | ASSIGNED_DATE |
| COMMENTS | VARCHAR2 | 4000 |  |  | COMMENTS |
| POPULATION_COUNT | NUMBER |  | 9 |  | POPULATION_COUNT |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| INITIATOR_PERSON_ID | NUMBER |  | 18 |  | INITIATOR_PERSON_ID |
| INITIATION_DATE | DATE |  |  |  | INITIATION_DATE |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | PROCESSING_STATUS |
| BATCH_SOURCE_ID | NUMBER |  | 18 |  | BATCH_SOURCE_ID |
| OBJECT_SOURCE | VARCHAR2 | 30 |  |  | OBJECT_SOURCE |
| ACTION_DATE_SOURCE | VARCHAR2 | 30 |  |  | ACTION_DATE_SOURCE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| END_DATE | DATE |  |  |  | END_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_BATCH_ACTIONS_N1 | Non Unique | Default | CHECKLIST_ALLOCATION_ID, INITIATOR_PERSON_ID |
| PER_CHECKLIST_BATCH_ACTIONS_PK | Unique | Default | CHECKLIST_BATCH_ACTION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
