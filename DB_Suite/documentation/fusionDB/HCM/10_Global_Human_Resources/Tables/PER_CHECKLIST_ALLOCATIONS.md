# PER_CHECKLIST_ALLOCATIONS

Table to store allocation configuration which will be used for mass assigning journeys.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistallocations-20710.html#perchecklistallocations-20710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistallocations-20710.html#perchecklistallocations-20710)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_ALLOCATIONS_PK | CHECKLIST_ALLOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHECKLIST_ALLOCATION_ID | NUMBER |  | 18 | Yes | CHECKLIST_ALLOCATION_ID |  |
| NAME | VARCHAR2 | 240 |  | Yes | NAME | Obsolete |
| CHECKLIST_ALLOCATION_CODE | VARCHAR2 | 240 |  | Yes | CHECKLIST_ALLOCATION_CODE |  |
| DESCRIPTION | VARCHAR2 | 400 |  |  | DESCRIPTION | Obsolete |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | CHECKLIST_ID |  |
| INITIATOR_PERSON_ID | NUMBER |  | 18 | Yes | INITIATOR_PERSON_ID |  |
| COMMENTS | VARCHAR2 | 4000 |  |  | COMMENTS |  |
| START_DATE | DATE |  |  | Yes | START_DATE |  |
| ALLOCATION_TYPE | VARCHAR2 | 30 |  | Yes | ALLOCATION_TYPE |  |
| CHECKLIST_SCHEDULE_ID | NUMBER |  | 18 | Yes | CHECKLIST_SCHEDULE_ID |  |
| STATUS | VARCHAR2 | 80 |  | Yes | STATUS |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_CHECKLIST_ALLOCATIONS_N1 | Non Unique | Default | UPPER("NAME") | Obsolete |
| PER_CHECKLIST_ALLOCATIONS_PK | Unique | Default | CHECKLIST_ALLOCATION_ID |  |
| PER_CHECKLIST_ALLOCATIONS_U1 | Unique | Default | CHECKLIST_ALLOCATION_CODE |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
