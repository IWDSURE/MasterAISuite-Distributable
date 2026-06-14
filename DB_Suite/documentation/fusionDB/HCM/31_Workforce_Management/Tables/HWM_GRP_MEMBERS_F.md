# HWM_GRP_MEMBERS_F

Contains Group Membership Information

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpmembersf-29169.html#hwmgrpmembersf-29169](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpmembersf-29169.html#hwmgrpmembersf-29169)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRP_MEMBERS_F_PK | GRP_MEMBER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_MEMBER_ID | NUMBER |  | 18 | Yes | GRP_MEMBER_ID |
| GRP_ID | NUMBER |  | 18 |  | GRP_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| MEMBER_ID | NUMBER |  | 18 |  | MEMBER_ID |
| GRP_EVAL_PROCESS_ID | NUMBER |  | 18 |  | GRP_EVAL_PROCESS_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REMARKS | VARCHAR2 | 500 |  |  | Remarks only for errored members |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRP_MEMBERS_F_N1 | Non Unique | FUSION_TS_TX_DATA | GRP_ID, MEMBER_ID, GRP_EVAL_PROCESS_ID |
| HWM_GRP_MEMBERS_F_N2 | Non Unique | Default | MEMBER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HWM_GRP_MEMBERS_F_N3 | Non Unique | FUSION_TS_TX_DATA | ASSIGNMENT_ID, GRP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HWM_GRP_MEMBERS_F_U1 | Unique | FUSION_TS_TX_DATA | GRP_MEMBER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
