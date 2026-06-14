# CEL_PROGRAM_PANEL_MEMBERS

Table to hold committee members of celebrate programs

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogrampanelmembers-31054.html#celprogrampanelmembers-31054](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogrampanelmembers-31054.html#celprogrampanelmembers-31054)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_PROGRAM_PANEL_MEMBERS_PK | PROGRAM_PANEL_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROGRAM_PANEL_MEMBER_ID | NUMBER |  | 18 | Yes | Surrogate Key |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Unique identifier for a celebrate program |
| SELECTOR_FLAG | VARCHAR2 | 1 |  |  | flag to indicate whether committee member is a winner selector or not |
| PERSON_ID | NUMBER |  | 18 | Yes | Unique identifier for a person |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Unique identifier for an assignment |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_PROGRAM_PANEL_MEMBERS_N1 | Non Unique | Default | PROGRAM_ID |
| CEL_PROGRAM_PANEL_MEMBERS_PK | Unique | Default | PROGRAM_PANEL_MEMBER_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
