# WLF_SCORM_OBJ_PERFORMANCES

Performance on an Objective onduring an Attemp

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormobjperformances-29687.html#wlfscormobjperformances-29687](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormobjperformances-29687.html#wlfscormobjperformances-29687)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_OBJ_PERFS_PK | OBJECTIVE_PERFORMANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECTIVE_PERFORMANCE_ID | NUMBER |  | 18 | Yes | OBJECTIVE_PERFORMANCE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to the PER_PERSONS table. |
| OBJECTIVE_ID | NUMBER |  | 18 | Yes | OBJECTIVE_ID |
| LOCAL_SCOPE_ID | NUMBER |  | 18 |  | CLASS_ID |
| STATUS | VARCHAR2 | 1 |  | Yes | STATUS |
| SCORE | VARCHAR2 | 80 |  | Yes | SCORE |
| SUCCESS_STATUS | VARCHAR2 | 1 |  |  | SUCCESS_STATUS |
| COMPLETION_STATUS | VARCHAR2 | 1 |  |  | COMPLETION_STATUS |
| SCALED_SCORE | NUMBER |  |  |  | SCALED_SCORE |
| MIN_SCORE | NUMBER |  |  |  | MIN_SCORE |
| MAX_SCORE | NUMBER |  |  |  | MAX_SCORE |
| PROGRESS_MEASURE | NUMBER |  |  |  | PROGRESS_MEASURE |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SCORM_OBJ_PERFS_N1 | Non Unique | Default | PERSON_ID, OBJECTIVE_ID, LOCAL_SCOPE_ID |
| WLF_SCORM_OBJ_PERFS_PK | Unique | FUSION_TS_TX_DATA | OBJECTIVE_PERFORMANCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
