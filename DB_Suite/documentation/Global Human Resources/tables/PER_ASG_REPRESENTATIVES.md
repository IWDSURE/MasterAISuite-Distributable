# PER_ASG_REPRESENTATIVES

This is a de-normalized table which will hold mapping between worker & its representatives which are active and effective as of today.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgrepresentatives-11352.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgrepresentatives-11352.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASG_REPRESENTATIVES_PK | REPRESENTATIVE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPRESENTATIVE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| RESPONSIBILITY_ID | NUMBER |  | 18 | Yes | The foreign key for areas of responsibility record. |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  | Yes | The responsibility type for which this record is holding the criteria. |
| REPRESENTATIVE_PERSON_ID | NUMBER |  | 18 | Yes | The person id of worker representative. |
| REPRESENTATIVE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | The assignment id of worker representative |
| WORKER_PERSON_ID | NUMBER |  | 18 | Yes | The person id of worker |
| WORKER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | The assignment id of worker |
| WORK_CONTACTS_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether to include this row in work contacts evaluation |
| APPROVALS_FLAG | VARCHAR2 | 1 |  |  | Responsibility will be included with Approvals processing. |
| CHECKLISTS_FLAG | VARCHAR2 | 1 |  |  | Responsibility will be included with Checklist processing. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASG_REPRESENTATIVES_N1 | Non Unique | Default | RESPONSIBILITY_TYPE, REPRESENTATIVE_PERSON_ID, REPRESENTATIVE_ASSIGNMENT_ID |
| PER_ASG_REPRESENTATIVES_N2 | Non Unique | Default | RESPONSIBILITY_TYPE, WORKER_PERSON_ID, WORKER_ASSIGNMENT_ID |
| PER_ASG_REPRESENTATIVES_PK | Unique | Default | REPRESENTATIVE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
