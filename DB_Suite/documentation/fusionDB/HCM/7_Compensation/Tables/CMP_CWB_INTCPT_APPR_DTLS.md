# CMP_CWB_INTCPT_APPR_DTLS

Stores approval details of intercept approvers in a compensation plan period.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbintcptapprdtls-28611.html#cmpcwbintcptapprdtls-28611](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbintcptapprdtls-28611.html#cmpcwbintcptapprdtls-28611)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_INTCPT_APPR_DTLS_PK | MGR_PERSON_EVENT_ID, APPROVER_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MGR_PERSON_EVENT_ID | NUMBER |  | 18 | Yes | MGR_PERSON_EVENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| APPROVER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | APPROVER_ASSIGNMENT_ID |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | MANAGER_ASSIGNMENT_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| APPROVAL_CODE | VARCHAR2 | 30 |  |  | APPROVAL_CODE |
| APPROVAL_DATE | DATE |  |  |  | APPROVAL_DATE |
| APPROVAL_COMMENTS | CLOB |  |  |  | APPROVAL_COMMENTS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_INTCPT_APPR_DTLS_N1 | Non Unique | Default | PERIOD_ID, PLAN_ID |
| CMP_CWB_INTCPT_APPR_DTLS_N2 | Non Unique | Default | MANAGER_ASSIGNMENT_ID |
| CMP_CWB_INTCPT_APPR_DTLS_PK | Unique | Default | MGR_PERSON_EVENT_ID, APPROVER_ASSIGNMENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
