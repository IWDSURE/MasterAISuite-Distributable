# WLF_GRW_GUIDE_ASSIGNMENTS

Table to store Assignment Records for Guide.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguideassignments-10748.html#wlfgrwguideassignments-10748](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguideassignments-10748.html#wlfgrwguideassignments-10748)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_GUIDE_ASSIGN_PK | GUIDE_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GUIDE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| GUIDE_ID | NUMBER |  | 18 | Yes | Guide Id for which assignment is created |
| GUIDE_TYPE | VARCHAR2 | 30 |  | Yes | Represents the type of guide Id |
| GUIDE_ASSIGNMENT_TYPE | VARCHAR2 | 30 |  | Yes | Guide assignment type |
| GUIDE_ASSIGNMENT_NUMBER | VARCHAR2 | 30 |  | Yes | User friendly uniquely identifying number for assignment |
| GUIDE_ASSIGNMENT_STATUS | VARCHAR2 | 30 |  | Yes | Status of the Guide assignment (e.g Active,InActive,Errored etc.) |
| STATUS_CHANGED_DATE | TIMESTAMP |  |  |  | Date to be captured during status change. For example during Withdrawal or Completion. |
| STATUS_CHANGE_COMMENT | VARCHAR2 | 4000 |  |  | Comments to be captured during status change. For example during Withdrawal or Completion. |
| STATUS_CHANGE_TYPE | VARCHAR2 | 30 |  |  | To capture the change in status like Withdrawal or Completion. |
| ASSIGNED_ON_DATE | TIMESTAMP |  |  | Yes | The date that the assignment is assigned to the Guide user. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id for which Guide assignment record |
| WORK_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Person work assignment id  for which Guide assignment record is. |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason for assignment status change. Example: useful when errored (if Person work assignment is part of multiple) Guide assignment created |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_GUIDE_ASSIGN_U1 | Unique | Default | GUIDE_ASSIGNMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
