# CMP_INTERCEPT_APPROVERS

Stores Intercept information for plan approvals. Intercept information allow users to introduce additional or substitute approvers into the approval process

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpinterceptapprovers-19733.html#cmpinterceptapprovers-19733](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpinterceptapprovers-19733.html#cmpinterceptapprovers-19733)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_INTERCEPT_APPROVERS_PK | INTERCEPT_APPROVER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERCEPT_APPROVER_ID | NUMBER |  | 18 | Yes | INTERCEPT_APPROVER_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| INTERCEPT_GROUP_ID | NUMBER |  | 18 | Yes | INTERCEPT_GROUP_ID |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | MANAGER_ASSIGNMENT_ID |
| APPROVER_ASSIGNMENT_ID | NUMBER |  | 18 |  | APPROVER_ASSIGNMENT_ID |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_INTERCEPT_APPROVERS_N1 | Non Unique | Default | INTERCEPT_GROUP_ID |
| CMP_INTERCEPT_APPROVERS_N2 | Non Unique | Default | MANAGER_ASSIGNMENT_ID |
| CMP_INTERCEPT_APPROVERS_N3 | Non Unique | Default | APPROVER_ASSIGNMENT_ID |
| CMP_INTERCEPT_APPROVERS_UK1 | Unique | Default | INTERCEPT_APPROVER_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
