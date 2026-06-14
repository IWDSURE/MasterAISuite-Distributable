# HWR_TEAM_MEMBER

The HWR Team Member Details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteammember-18012.html#hwrteammember-18012](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteammember-18012.html#hwrteammember-18012)

## Primary Key

| Name | Columns |
|------|----------|
| SYS_C002629094 | TEAM_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEAM_MEMBER_ID | NUMBER |  | 19 | Yes | TEAM_MEMBER_ID |
| PERSON_ID | VARCHAR2 | 50 |  | Yes | PERSON_ID |
| TEAM_ID | NUMBER |  | 19 | Yes | TEAM_ID |
| ROLE | VARCHAR2 | 20 |  | Yes | ROLE |
| STATUS | VARCHAR2 | 20 |  | Yes | STATUS |
| IS_DELETED | NUMBER |  | 1 |  | IS_DELETED |
| MEMBER_JOINING_DATE | TIMESTAMP |  |  |  | MEMBER_JOINING_DATE |
| MEMBER_FIRST_JOINING_DATE | TIMESTAMP |  |  |  | MEMBER_FIRST_JOINING_DATE |
| MEMBER_LEAVING_DATE | TIMESTAMP |  |  |  | MEMBER_LEAVING_DATE |
| MEMBER_LAST_LEAVING_DATE | TIMESTAMP |  |  |  | MEMBER_LAST_LEAVING_DATE |
| MEMBER_ACTIVE_DATE | TIMESTAMP |  |  |  | MEMBER_ACTIVE_DATE |
| MEMBER_FIRST_ACTIVE_DATE | TIMESTAMP |  |  |  | MEMBER_FIRST_ACTIVE_DATE |
| MEMBER_INACTIVE_DATE | TIMESTAMP |  |  |  | MEMBER_INACTIVE_DATE |
| MEMBER_LAST_INACTIVE_DATE | TIMESTAMP |  |  |  | MEMBER_LAST_INACTIVE_DATE |
| TEAM_SOURCE_ID | NUMBER |  | 18 |  | to store team source id for the member of that team |
| TEAM_CONVERSATION_ID | VARCHAR2 | 100 |  |  | to store team conversation id for that particular source id and member of that team |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_MEMBER_U1 | Unique | FUSION_TS_TX_DATA | TEAM_MEMBER_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
