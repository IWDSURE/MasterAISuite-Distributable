# HWR_VLTR_ACTIVITY_B

This table stores base activity info.

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltractivityb-22055.html#hwrvltractivityb-22055](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltractivityb-22055.html#hwrvltractivityb-22055)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_ACTIVITY_B_PK | ACTIVITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ACTIVITY_ID | NUMBER |  | 18 | Yes | ACTIVITY_ID |  |
| VOL_ABS_STATUS | VARCHAR2 | 100 |  |  | VOL_ABS_STATUS |  |
| ABSENCE_ID | NUMBER |  | 18 |  | ABSENCE_ID |  |
| VOLUNTEER_JOB_ID | NUMBER |  | 18 | Yes | VOLUNTEER_JOB_ID |  |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |  |
| VOLUNTEER_ID | NUMBER |  | 18 |  | VOLUNTEER_ID | Obsolete |
| HCM_PERSON_ID | NUMBER |  | 18 |  | HCM_PERSON_ID |  |
| STATE | VARCHAR2 | 100 |  |  | STATE |  |
| START_DATE | TIMESTAMP |  |  |  | START_DATE |  |
| END_DATE | TIMESTAMP |  |  |  | END_DATE |  |
| NO_OF_HOURS | NUMBER |  |  |  | NO_OF_HOURS |  |
| CT_POINTS_STATUS | VARCHAR2 | 200 |  |  | CT_POINTS_STATUS |  |
| CT_POINTS_ERROR | VARCHAR2 | 4000 |  |  | CT_POINTS_ERROR |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_ACTIVITY_B_U1 | Unique | FUSION_TS_TX_IDX | ACTIVITY_ID |
| hwr_vltr_activity_b_U2 | Unique | Default | PROJECT_ID, HCM_PERSON_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
