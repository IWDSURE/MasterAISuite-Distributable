# BEN_CLPSE_LF_EVT_F

BEN_CLPSE_LF_EVT_F  identifies the life event(s) that will be consolidated into one  resulting life even when being evaluated concurrently.  It also specifies the number of days apart from each other the group of one or more life events must have occurred, and status the  collapsed life events should be set to.  For example,Voided.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benclpselfevtf-31354.html#benclpselfevtf-31354](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benclpselfevtf-31354.html#benclpselfevtf-31354)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CLPSE_LF_EVT_F_PK | CLPSE_LF_EVT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLPSE_LF_EVT_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_CLPSE_LF_EVT_F. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LER9_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| SEQ | NUMBER |  | 18 | Yes | Sequence. |
| LER10_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| EVAL_LER_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_LER_F. |
| BOOL1_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER1_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_LER_F. |
| BOOL2_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER2_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL3_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER3_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL4_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER4_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL5_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER5_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL6_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER6_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL7_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER7_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL8_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| LER8_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| BOOL9_CD | VARCHAR2 | 30 |  |  | Boolean code. |
| EVAL_CD | VARCHAR2 | 30 |  | Yes | Life event evaluation code. |
| EVAL_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| TLRNC_DYS_NUM | NUMBER |  | 18 |  | Tolerance days. |
| EVAL_LER_DET_CD | VARCHAR2 | 30 |  | Yes | Life event determination date code. |
| EVAL_LER_DET_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CLPSE_LF_EVT_F_N10 | Non Unique | Default | LER9_ID |
| BEN_CLPSE_LF_EVT_F_N11 | Non Unique | Default | LER10_ID |
| BEN_CLPSE_LF_EVT_F_N12 | Non Unique | Default | EVAL_LER_ID |
| BEN_CLPSE_LF_EVT_F_N2 | Non Unique | Default | LER1_ID |
| BEN_CLPSE_LF_EVT_F_N3 | Non Unique | Default | LER2_ID |
| BEN_CLPSE_LF_EVT_F_N4 | Non Unique | Default | LER3_ID |
| BEN_CLPSE_LF_EVT_F_N5 | Non Unique | Default | LER4_ID |
| BEN_CLPSE_LF_EVT_F_N6 | Non Unique | Default | LER5_ID |
| BEN_CLPSE_LF_EVT_F_N7 | Non Unique | Default | LER6_ID |
| BEN_CLPSE_LF_EVT_F_N8 | Non Unique | Default | LER7_ID |
| BEN_CLPSE_LF_EVT_F_N9 | Non Unique | Default | LER8_ID |
| BEN_CLPSE_LF_EVT_F_PK | Unique | Default | CLPSE_LF_EVT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
