# HTS_SCHED_VIOLATION_OBJ_REFS

This table is associated with a specific violation message and represents the objects that contributed to the violation.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedviolationobjrefs-28218.html#htsschedviolationobjrefs-28218](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedviolationobjrefs-28218.html#htsschedviolationobjrefs-28218)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_VIOLATION_OBJ_PK | SCHED_VIOLATION_OBJ_REF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_VIOLATION_OBJ_REF_ID | NUMBER |  | 18 | Yes | The unique ID of the violation object reference. |
| SCHED_VIOLATION_ID | NUMBER |  | 18 | Yes | The identifier of the associated validation violation the object, pointed by the reference, is contributing to. |
| SCHED_FULL_VALIDATION_ID | NUMBER |  | 18 | Yes | The ID of the schedule validation execution having generated the violation associated with the object reference. |
| OBJECT_ID | NUMBER |  | 18 | Yes | The key referring to the object. |
| OBJECT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The code identifying the type of the object referred to by the reference. |
| NATIVE_FLAG | VARCHAR2 | 1 |  | Yes | A flag indicating if the object, pointed to by the reference, belongs to the validated schedule. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | EnterpriseId |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_VIOLATION_OBJS_N1 | Non Unique | Default | SCHED_VIOLATION_ID |
| HTS_SCHED_VIOLATION_OBJS_N2 | Non Unique | Default | SCHED_FULL_VALIDATION_ID |
| HTS_SCHED_VIOLATION_OBJS_PK | Unique | Default | SCHED_VIOLATION_OBJ_REF_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
