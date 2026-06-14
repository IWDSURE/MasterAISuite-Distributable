# BEN_CLPSE_LF_EVT

BEN_CLPSE_LF_EVT identifies the life event(s) that will be consolidated into one resulting life even when being evaluated concurrently. It also specifies the number of days apart from each other the group of one or more life events must have occurred, the rule or formula of collapsing and status the collapsed life events should be set to. For example,VOID.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benclpselfevt-3066.html#benclpselfevt-3066](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benclpselfevt-3066.html#benclpselfevt-3066)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CLPSE_LF_EVT_PK | CLPSE_LF_EVT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLPSE_LF_EVT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the logic , mandatory field. |
| DESCRIPTION | VARCHAR2 | 800 |  |  | description of this logic , can be null |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| STATUS_CD | VARCHAR2 | 30 |  | Yes | collapsing logic status(Active,Pending...) |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| SEQ | NUMBER |  | 18 | Yes | Sequence Number |
| EVAL_LER_ID | NUMBER |  | 18 |  | The Resulting Life Event
Foreign key to BEN_LER_F |
| EVAL_CD | VARCHAR2 | 30 |  |  | Handling of Non-winning events code |
| EVAL_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULS_F
Which formula to handling of the non-winning life events. |
| EVAL_LER_DET_CD | VARCHAR2 | 30 |  | Yes | Life Event Occurred Date code |
| EVAL_LER_DET_RL | NUMBER |  | 18 |  | Life Event Occurred Date Formula |
| CLPSE_CD | VARCHAR2 | 30 |  | Yes | Use formula or rule to configure collapse logic code. |
| CLPSE_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F ,collapse logic formula |
| TLRNC_DYS_NUM | NUMBER |  | 18 | Yes | Tolerance Days |
| LER1_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL1_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER2_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL2_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER3_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL3_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER4_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL4_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER5_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL5_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER6_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL6_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER7_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL7_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER8_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL8_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER9_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| BOOL9_CD | VARCHAR2 | 30 |  |  | Boolean code |
| LER10_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLPSE_XTRA_CHAR1 | VARCHAR2 | 240 |  |  | Column for future change |
| CLPSE_XTRA_CHAR2 | VARCHAR2 | 240 |  |  | Column for future change |
| CLPSE_XTRA_CHAR3 | VARCHAR2 | 240 |  |  | Column for future change |
| CLPSE_XTRA_CHAR4 | VARCHAR2 | 240 |  |  | Column for future change |
| CLPSE_XTRA_NUM1 | NUMBER |  |  |  | Column for future change |
| CLPSE_XTRA_NUM2 | NUMBER |  |  |  | Column for future change. |
| CLPSE_XTRA_NUM3 | NUMBER |  |  |  | Column for future change. |
| CLPSE_XTRA_NUM4 | NUMBER |  |  |  | Column for future change. |
| CLPSE_XTRA_DATE1 | DATE |  |  |  | Column for future change |
| CLPSE_XTRA_DATE2 | DATE |  |  |  | Column for future change |
| CLPSE_XTRA_DATE3 | DATE |  |  |  | Column for future change |
| CLPSE_XTRA_DATE4 | DATE |  |  |  | Column for future change |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CLPSE_LF_EVT_PK | Unique | Default | CLPSE_LF_EVT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
