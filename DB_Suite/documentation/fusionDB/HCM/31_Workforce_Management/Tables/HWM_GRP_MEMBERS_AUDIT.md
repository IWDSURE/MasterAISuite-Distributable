# HWM_GRP_MEMBERS_AUDIT

Contains group members table updation Information.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpmembersaudit-11038.html#hwmgrpmembersaudit-11038](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpmembersaudit-11038.html#hwmgrpmembersaudit-11038)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRP_MEMBERS_AUDIT_PK | GRP_MEMBERS_AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_MEMBERS_AUDIT_ID | NUMBER |  | 18 | Yes | GRP_MEMBERS_AUDIT_ID |
| GRP_MEMBER_ID | NUMBER |  | 18 | Yes | GRP_MEMBER_ID |
| GRP_ID | NUMBER |  | 18 |  | GRP_ID |
| MEMBER_ID | NUMBER |  | 18 |  | MEMBER_ID |
| ORIG_EFF_START_DATE | DATE |  |  |  | ORIG_EFF_START_DATE |
| NEW_EFF_START_DATE | DATE |  |  |  | NEW_EFF_START_DATE |
| ORIG_EFF_END_DATE | DATE |  |  |  | ORIG_EFF_END_DATE |
| NEW_EFF_END_DATE | DATE |  |  |  | NEW_EFF_END_DATE |
| ACTION_TYPE | VARCHAR2 | 30 |  |  | ACTION_TYPE |
| REASON_CODE | VARCHAR2 | 30 |  |  | REASON_CODE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRP_MEMBERS_AUDIT_U1 | Unique | Default | GRP_MEMBERS_AUDIT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
