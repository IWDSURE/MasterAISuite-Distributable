# HWR_RESUME_GBL_PRFL_X

This cross reference (xref) table stores relationship between resume and global profile.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresumegblprflx-30414.html#hwrresumegblprflx-30414](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresumegblprflx-30414.html#hwrresumegblprflx-30414)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RESUME_GBL_PRFL_X_PK | SOURCE_ID, RESUME_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the resume. |  |
| RESUME_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the resume table. |  |
| GLOBAL_PROFILE_ID | VARCHAR2 | 400 |  | Yes | The Id of the global profile which has the resume. | Obsolete |
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | The Id of the global profile which has the resume. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_RESUME_GBL_PRFL_X_N1 | Non Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID |
| HWR_RESUME_GBL_PRFL_X_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, RESUME_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
