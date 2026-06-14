# HWR_VLTR_GOAL_VOLNTR_XREF

This table stores volunteering goal xref information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoalvolntrxref-27200.html#hwrvltrgoalvolntrxref-27200](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoalvolntrxref-27200.html#hwrvltrgoalvolntrxref-27200)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_GL_VNTR_XREF_PK | GOAL_ID, VOLUNTEER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | This is the primary key for the wellness user goal table. |
| VOLUNTEER_ID | NUMBER |  | 18 | Yes | This is the primary key for the (Volunteer) Person Profile table (HWR_VLTR_PER_PROFILE_B and HWR_VLTR_PER_PROFILE_TL). |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_GOAL_VOLNTR_XREF_U1 | Unique | FUSION_TS_TX_IDX | GOAL_ID, VOLUNTEER_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
