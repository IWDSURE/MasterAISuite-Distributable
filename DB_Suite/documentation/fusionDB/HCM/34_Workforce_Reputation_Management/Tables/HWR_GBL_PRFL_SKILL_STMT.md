# HWR_GBL_PRFL_SKILL_STMT

Table storing weight of each statement, it is used to calculate the score in GBL_PRFL_SKILL table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflskillstmt-8572.html#hwrgblprflskillstmt-8572](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflskillstmt-8572.html#hwrgblprflskillstmt-8572)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GBL_PRFL_SKILL_STMT_PK | GBL_PRFL_SKILL_STMNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GBL_PRFL_SKILL_STMNT_ID | NUMBER |  | 18 | Yes | This is the primary key for the global profile skill table |
| STATEMENT_UUID | VARCHAR2 | 255 |  |  | The universally unique identifier for this statement. |
| GBL_PRFL_SKILL_ID | NUMBER |  | 18 | Yes | The user skill Id. This is a foreign key from the HWR_GBL_PRFL_SKILL tables. |
| STATEMENT_ID | NUMBER |  | 18 |  | The Unique database identifier for this statement. |
| WEIGHT | NUMBER |  |  |  | Weight contributed by the statement to the user skill score |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_GBL_PRFL_SKILL_STMT_N1 | Non Unique | Default | GBL_PRFL_SKILL_ID, WEIGHT |  |
| HWR_GBL_PRFL_SKILL_STMT_N2 | Non Unique | Default | STATEMENT_ID | Obsolete |
| HWR_GBL_PRFL_SKILL_STMT_U1 | Unique | Default | GBL_PRFL_SKILL_STMNT_ID |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
