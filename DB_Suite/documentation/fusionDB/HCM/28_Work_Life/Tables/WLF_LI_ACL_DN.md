# WLF_LI_ACL_DN

This table stores learner access control list of learning items.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliacldn-9370.html#wlfliacldn-9370](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliacldn-9370.html#wlfliacldn-9370)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACL_DN_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PERSON_ID | NUMBER |  | 18 | Yes | Indicates PersonId |
| USER_ID | NUMBER |  | 18 | Yes | Indicates UserId |
| SS_CAN_ACCESS | CLOB |  |  |  | This clob object is to store Learning Items list the person has access to |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_ACL_DN_N1 | Non Unique | Default | PERSON_ID |
| WLF_LI_ACL_DN_U1 | Unique | Default | ACL_DN_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
