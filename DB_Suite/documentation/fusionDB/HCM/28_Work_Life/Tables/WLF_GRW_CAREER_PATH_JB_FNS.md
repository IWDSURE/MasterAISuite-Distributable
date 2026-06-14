# WLF_GRW_CAREER_PATH_JB_FNS

Table to store the job functions of a career path.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwcareerpathjbfns-19656.html#wlfgrwcareerpathjbfns-19656](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwcareerpathjbfns-19656.html#wlfgrwcareerpathjbfns-19656)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_grw_career_path_jb_fns_PK | CAREER_PATH_JOB_FN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAREER_PATH_JOB_FN_ID | NUMBER |  | 18 | Yes | System generated uniqu identifier. |
| CAREER_PATH_ID | NUMBER |  | 18 | Yes | Foreign key to the career path. |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  | Yes | The job function code. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_CAREER_PATH_JB_FNS_U1 | Unique | Default | CAREER_PATH_JOB_FN_ID |
| WLF_GRW_CAREER_PATH_JB_FNS_U2 | Unique | Default | CAREER_PATH_ID, JOB_FUNCTION_CODE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
