# WLF_GRW_ASSIGNMENT_TASKS

Table to store Assignment tasks for  Assignment Records of  Guide.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwassignmenttasks-3312.html#wlfgrwassignmenttasks-3312](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwassignmenttasks-3312.html#wlfgrwassignmenttasks-3312)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_ASSIGNMENT_TASKS_PK | ASSIGNMENT_TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_TASK_ID | NUMBER |  | 18 | Yes | System generated unique identifier to represent a row. |
| GUIDE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment record id of guide for which tasks are related. |
| TASK_OWNER_ID | NUMBER |  | 18 |  | Who is responsible to finish the task. |
| TASK_DUE_DATE | TIMESTAMP |  |  |  | Stores task due date.. |
| TASK_STATUS | VARCHAR2 | 30 |  |  | Stores status of the task. |
| TASK_GUIDE_RELATION_ID | NUMBER |  | 18 |  | Stores the task relation id with guide. |
| GUIDE_ID | NUMBER |  | 18 |  | To track parent guide id of the task |
| GUIDE_TYPE | VARCHAR2 | 30 |  |  | To track parent guide id type of the task |
| SOURCE_OBJECT_ID | NUMBER |  | 18 |  | To track the source object id (example Learning assignment record id ,Journey task Id) of the record creation for this table |
| SOURCE_OBJECT_TYPE | VARCHAR2 | 30 |  |  | To track the source object type (example Learn,Journey) of the record creation for this table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_ASSIGNMENT_TASKS_U1 | Unique | Default | ASSIGNMENT_TASK_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
