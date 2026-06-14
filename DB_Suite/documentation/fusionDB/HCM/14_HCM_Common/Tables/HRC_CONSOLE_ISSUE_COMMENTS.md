# HRC_CONSOLE_ISSUE_COMMENTS

This table holds the comments related to an issue

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcconsoleissuecomments-4950.html#hrcconsoleissuecomments-4950](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcconsoleissuecomments-4950.html#hrcconsoleissuecomments-4950)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_CONSOLE_ISSUE_COMMENT_PK | ISSUE_COMMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ISSUE_COMMENT_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| CONSOLE_TRANSACTION_ID | NUMBER |  | 18 | Yes | Foreign key to FND_CONSOLE_TRANSACTION_INFO |
| ISSUE_ID | NUMBER |  | 18 | Yes | Foreign key to FND_CONSOLE_ISSUE |
| TRANSACTION_ID | NUMBER |  | 18 | Yes | Foreign key to HRC_TXN_HEADER table |
| USER_NAME | VARCHAR2 | 64 |  | Yes | UserId of User who posted this comment |
| COMMENT_SEQUENCE | NUMBER |  | 18 | Yes | This Comment's place in the sequence of comments |
| DATE_TIME | TIMESTAMP |  |  |  | The date and time this Comment was posted |
| COMMENTS | CLOB |  |  |  | The text of the Users comments |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to

HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_CONSOLE_ISSUE_COMMENTS_UK | Unique | Default | ISSUE_COMMENT_ID, COMMENT_SEQUENCE |
| HRC_ISSUE_COMMENTS_N1 | Non Unique | Default | CONSOLE_TRANSACTION_ID |
| HRC_ISSUE_COMMENTS_N2 | Non Unique | Default | ISSUE_ID |
| HRC_ISSUE_COMMENTS_N3 | Non Unique | Default | TRANSACTION_ID |
| HRC_ISSUE_COMMENTS_U1 | Unique | Default | ISSUE_COMMENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
