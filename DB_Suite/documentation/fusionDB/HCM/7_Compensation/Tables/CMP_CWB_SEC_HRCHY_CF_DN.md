# CMP_CWB_SEC_HRCHY_CF_DN

Denoramlized table of CMP_CWB_SEC_HRCHY table for OTBI reporting.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsechrchycfdn-28386.html#cmpcwbsechrchycfdn-28386](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbsechrchycfdn-28386.html#cmpcwbsechrchycfdn-28386)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_SEC_HRCHY_CF_DN_PK | SEC_HRCHY_CF_DN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOP_MGR_PERSON_EVENT_ID | NUMBER |  | 18 | Yes | TOP_MGR_PERSON_EVENT_ID |
| TOP_MGR_PERSON_ID | NUMBER |  | 18 | Yes | TOP_MGR_PERSON_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| TOP_PLAN_ID | NUMBER |  | 18 | Yes | TOP_PLAN_ID |
| TOP_PERIOD_ID | NUMBER |  | 18 | Yes | TOP_PERIOD_ID |
| SEC_HRCHY_CF_DN_ID | NUMBER |  | 18 | Yes | SEC_HRCHY_CF_DN_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| LEVEL1_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL1_PERSON_EVENT_ID |
| LEVEL1_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL1_MGR_PERSON_ID |
| LEVEL2_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL2_PERSON_EVENT_ID |
| LEVEL2_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL2_MGR_PERSON_ID |
| LEVEL3_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL3_PERSON_EVENT_ID |
| LEVEL3_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL3_MGR_PERSON_ID |
| LEVEL4_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL4_PERSON_EVENT_ID |
| LEVEL4_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL4_MGR_PERSON_ID |
| LEVEL5_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL5_PERSON_EVENT_ID |
| LEVEL5_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL5_MGR_PERSON_ID |
| LEVEL6_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL6_PERSON_EVENT_ID |
| LEVEL6_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL6_MGR_PERSON_ID |
| LEVEL7_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL7_PERSON_EVENT_ID |
| LEVEL7_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL7_MGR_PERSON_ID |
| LEVEL8_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL8_PERSON_EVENT_ID |
| LEVEL8_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL8_MGR_PERSON_ID |
| LEVEL9_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL9_PERSON_EVENT_ID |
| LEVEL9_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL9_MGR_PERSON_ID |
| LEVEL10_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL10_PERSON_EVENT_ID |
| LEVEL10_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL10_MGR_PERSON_ID |
| LEVEL11_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL11_PERSON_EVENT_ID |
| LEVEL11_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL11_MGR_PERSON_ID |
| LEVEL12_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL12_PERSON_EVENT_ID |
| LEVEL12_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL12_MGR_PERSON_ID |
| LEVEL13_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL13_PERSON_EVENT_ID |
| LEVEL13_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL13_MGR_PERSON_ID |
| LEVEL14_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL14_PERSON_EVENT_ID |
| LEVEL14_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL14_MGR_PERSON_ID |
| LEVEL15_PERSON_EVENT_ID | NUMBER |  | 18 |  | LEVEL15_PERSON_EVENT_ID |
| LEVEL15_MGR_PERSON_ID | NUMBER |  | 18 |  | LEVEL15_MGR_PERSON_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_SEC_HRCHY_CF_DN_N1 | Non Unique | Default | TOP_PLAN_ID, TOP_PERIOD_ID |
| CMP_CWB_SEC_HRCHY_CF_DN_U1 | Unique | Default | SEC_HRCHY_CF_DN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
