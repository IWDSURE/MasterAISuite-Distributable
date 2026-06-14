# PER_CHECKLIST_SLOTS

Table to store slots for schedules

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistslots-20516.html#perchecklistslots-20516](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistslots-20516.html#perchecklistslots-20516)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_SLOTS_PK | CHECKLIST_SLOT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_SLOT_ID | NUMBER |  | 18 | Yes | Primary Key |
| CHECKLIST_SCHEDULE_ID | NUMBER |  | 18 | Yes | Parent Key - Identifier for the checklist schedule row |
| SLOT_TIME_VALUE | NUMBER |  | 5 | Yes | Indicates the time of the slot in minutes |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | Indicates whether the use has selected the slot or not |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_SLOTS_PK | Unique | Default | CHECKLIST_SLOT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
