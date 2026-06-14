# HRC_CONSOLE_ISSUE_ASSIGNMENT

This table holds the issue assignment to user details

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcconsoleissueassignment-6398.html#hrcconsoleissueassignment-6398](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcconsoleissueassignment-6398.html#hrcconsoleissueassignment-6398)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_CONSOLE_ISSUE_ASSIGNM_PK | ISSUE_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ISSUE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| PRIORITY | VARCHAR2 | 60 |  |  | Priority assigned to issue in Admin Console. |
| CONSOLE_TRANSACTION_ID | NUMBER |  | 18 | Yes | Foreign key to FND_CONSOLE_TRANSACTION_INFO |
| ISSUE_ID | NUMBER |  | 18 | Yes | Foreign key to FND_CONSOLE_ISSUE |
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Foreign key to HRC_TXN_HEADER table |
| ASSIGNED_TO | NUMBER |  | 18 |  | UserId of user this is currently assigned to |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_CONSOLE_ISSUE_ASSIGN_N1 | Non Unique | Default | CONSOLE_TRANSACTION_ID |
| HRC_CONSOLE_ISSUE_ASSIGN_N2 | Non Unique | Default | ISSUE_ID |
| HRC_CONSOLE_ISSUE_ASSIGN_N3 | Non Unique | Default | TRANSACTION_ID |
| HRC_CONSOLE_ISSUE_ASSIGN_U1 | Unique | Default | ISSUE_ASSIGNMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
