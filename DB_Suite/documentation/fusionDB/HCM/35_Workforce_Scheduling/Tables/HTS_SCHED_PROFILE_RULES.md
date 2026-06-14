# HTS_SCHED_PROFILE_RULES

Table holding Rules which are to be used for schedule generation

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilerules-27498.html#htsschedprofilerules-27498](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprofilerules-27498.html#htsschedprofilerules-27498)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_PROFILE_RULES_PK | SCHED_PROFILE_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_PROFILE_RULE_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a schedule profile Rules |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SCHED_PROFILE_RULE_CODE | VARCHAR2 | 30 |  | Yes | Schedule Profile Rule Code |
| SCHED_GEN_PROFILE_ID | NUMBER |  | 18 | Yes | foreign key to Schedule Generation Profile table |
| SCHEDULING_RULE_CODE | VARCHAR2 | 30 |  | Yes | Scheduling Rule Code |
| MIN_VALUE_NUM | NUMBER |  |  |  | MIN_VALUE_NUM |
| MAX_VALUE_NUM | NUMBER |  |  |  | MAX_VALUE_NUM |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PROFILE_RULES_PK | Unique | Default | SCHED_PROFILE_RULE_ID |
| HTS_SCHED_PROFILE_RULES_U1 | Unique | Default | SCHED_PROFILE_RULE_CODE |
| HTS_SCHED_PROFILE_RULES_U2 | Unique | Default | SCHED_GEN_PROFILE_ID, SCHEDULING_RULE_CODE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
