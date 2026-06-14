# CMP_CWB_APPROVAL_HISTORY

This Table stores the Approval History for all the managers

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbapprovalhistory-29766.html#cmpcwbapprovalhistory-29766](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbapprovalhistory-29766.html#cmpcwbapprovalhistory-29766)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_APPROVAL_HISTORY_PK | APPROVAL_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| APPROVAL_HISTORY_ID | NUMBER |  | 18 | Yes | APPROVAL_HISTORY_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | MGR_PERSON_EVENT_ID |  |
| EMP_PERSON_EVENT_ID | NUMBER |  | 18 | Yes | EMP_PERSON_EVENT_ID |  |
| MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | MGR_ASSIGNMENT_ID |  |
| ACTION_CODE | VARCHAR2 | 30 |  | Yes | APPR_ACTION |  |
| ACTION_DATE | TIMESTAMP |  |  | Yes | ACTION_DATE |  |
| COMMENTS | CLOB |  |  |  | COMMENTS |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| POOL_ID | NUMBER |  | 18 |  | POOL_ID |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_APPROVAL_HISTORY_N1 | Non Unique | FUSION_TS_TX_DATA | EMP_PERSON_EVENT_ID, MGR_ASSIGNMENT_ID |
| CMP_CWB_APPROVAL_HISTORY_PK | Unique | FUSION_TS_TX_DATA | APPROVAL_HISTORY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
