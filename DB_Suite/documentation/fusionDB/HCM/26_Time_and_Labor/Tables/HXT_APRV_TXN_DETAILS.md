# HXT_APRV_TXN_DETAILS

This table has all entries keyed by the approval record group header

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtaprvtxndetails-20607.html#hxtaprvtxndetails-20607](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtaprvtxndetails-20607.html#hxtaprvtxndetails-20607)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_APRV_TXN_DETAILS_PK | TM_ENTRY_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ENTRY_ROW_ID | NUMBER |  | 18 | Yes | TM_ENTRY_ROW_ID |
| ENTRY_DEPARTMENT_MANAGER | VARCHAR2 | 240 |  |  | ENTRY_DEPARTMENT_MANAGER |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| APRV_TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Approval Time Record Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| UNIT_OF_MEASURE | VARCHAR2 | 20 |  |  | UNIT_OF_MEASURE |
| MEASURE | NUMBER |  | 9 |  | MEASURE |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| STOP_TIME | TIMESTAMP |  |  |  | STOP_TIME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PROJECT_MANAGER | VARCHAR2 | 80 |  |  | PROJECT_MANAGER |
| ATTRIBUTE_NUMBER1 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| TIMERECORDTBBID | NUMBER |  | 18 |  | TimeRecordTbbId |
| PROJECT_ORG | VARCHAR2 | 240 |  |  | Project Organization Name |
| PROJECT_BU | VARCHAR2 | 240 |  |  | Project Owning Business Unit Name |
| LEGAL_ENTITY | VARCHAR2 | 240 |  |  | Legal Entity Name |
| SPONSORED_FLAG | VARCHAR2 | 1 |  |  | Sponsored Flag |
| PROJECT_ROLE | VARCHAR2 | 240 |  |  | Project Role |
| WORK_TYPE | VARCHAR2 | 240 |  |  | Work Type Name |
| PROJECT_TYPE | VARCHAR2 | 240 |  |  | Project Type Name |
| PROJECT_CURRENCY | VARCHAR2 | 15 |  |  | Project Currency Code |
| PROJECT_LEDGER_CURRENCY | VARCHAR2 | 15 |  |  | Project Ledger Currency Code |
| TASK_ORG | VARCHAR2 | 240 |  |  | Task Organization Name |
| TASK_MANAGER | VARCHAR2 | 240 |  |  | Task Manager |
| AWARD_BU | VARCHAR2 | 240 |  |  | Award Owning BU Name |
| AWARD_ORG | VARCHAR2 | 240 |  |  | Award Organization Name |
| PRINCIPAL_INVESTIGATOR | VARCHAR2 | 240 |  |  | Principal Investigator |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR6 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR7 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR8 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR9 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR10 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR11 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR12 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR13 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR14 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR15 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR16 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR17 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR18 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR19 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR20 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR21 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR22 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR23 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR24 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR25 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR26 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR27 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR28 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR29 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR30 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR31 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR32 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR33 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR34 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR35 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR36 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR37 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR38 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR39 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR40 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR41 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR42 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR43 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR44 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR45 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR46 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR47 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR48 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR49 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR50 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER21 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER22 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER23 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER24 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER25 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER26 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER27 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER28 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER29 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER30 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER31 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER32 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER33 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER34 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER35 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER36 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER37 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER38 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER39 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER40 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER41 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER42 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER43 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER44 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER45 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER46 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER47 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER48 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER49 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER50 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hxt_aprv_txn_details_N1 | Non Unique | Default | APRV_TM_REC_GRP_ID |
| hxt_aprv_txn_details_U1 | Unique | Default | TM_ENTRY_ROW_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
