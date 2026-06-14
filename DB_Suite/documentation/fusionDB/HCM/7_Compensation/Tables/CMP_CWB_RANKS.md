# CMP_CWB_RANKS

Stores ranks awarded to employees by managers to recognize performance. For example, the best worker under a manager gets a rank of 1 and the next best worker gets a lower rank of 2. An employee may be ranked by every manager in his/her management chain individually, and so ranks are stored at all levels of the hierarchy.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbranks-14129.html#cmpcwbranks-14129](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbranks-14129.html#cmpcwbranks-14129)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_RANKS_PK | RANK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANK_ID | NUMBER |  | 18 | Yes | RANK_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| MGR_PERSON_EVENT_ID | NUMBER |  | 18 |  | MGR_PERSON_EVENT_ID |
| RANK | NUMBER |  | 18 |  | RANK |
| RANKED_DATE | DATE |  |  |  | RANKED_DATE |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | MGR_ASSIGNMENT_ID |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_RANKS_N1 | Non Unique | Default | PERSON_EVENT_ID |
| CMP_CWB_RANKS_PK | Unique | Default | RANK_ID |
| CMP_CWB_RANKS_U1 | Unique | Default | MGR_PERSON_EVENT_ID, PERSON_EVENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
