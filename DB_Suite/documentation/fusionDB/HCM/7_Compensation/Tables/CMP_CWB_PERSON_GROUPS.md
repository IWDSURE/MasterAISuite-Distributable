# CMP_CWB_PERSON_GROUPS

Tables Stores Person Groups records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersongroups-3116.html#cmpcwbpersongroups-3116](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersongroups-3116.html#cmpcwbpersongroups-3116)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PERSON_GROUPS_PK | GROUP_PER_IN_LER_ID, GROUP_PL_ID, GROUP_OIPL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GROUP_PER_IN_LER_ID | NUMBER |  | 18 | Yes | Group Per In Ler Id. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| GROUP_PL_ID | NUMBER |  | 18 | Yes | Group Plan . |
| GROUP_OIPL_ID | NUMBER |  | 18 | Yes | Group Option. |
| LF_EVT_OCRD_DT | DATE |  |  | Yes | Life Event Occured Date. |
| BDGT_POP_CD | VARCHAR2 | 30 |  |  | Budget Population Code . |
| DUE_DT | DATE |  |  |  | Due Date . |
| ACCESS_CD | VARCHAR2 | 30 |  |  | Access Code . |
| APPROVAL_CD | VARCHAR2 | 30 |  |  | Approval Code . |
| APPROVAL_DATE | DATE |  |  |  | Approval Date . |
| APPROVAL_COMMENTS | VARCHAR2 | 2000 |  |  | Approval Comment. |
| SUBMIT_CD | VARCHAR2 | 30 |  |  | Submit Code. |
| SUBMIT_DATE | DATE |  |  |  | Submit Date . |
| SUBMIT_COMMENTS | VARCHAR2 | 2000 |  |  | SubmitComments. |
| DIST_BDGT_VAL | NUMBER |  |  |  | Distribution Budget Value . |
| WS_BDGT_VAL | NUMBER |  |  |  | Worksheet Budget Value . |
| RSRV_VAL | NUMBER |  |  |  | Reserve Budget Value . |
| DIST_BDGT_MN_VAL | NUMBER |  |  |  | Distribution Budget Min Value |
| DIST_BDGT_MX_VAL | NUMBER |  |  |  | Distribution Budget Max Value |
| DIST_BDGT_INCR_VAL | NUMBER |  |  |  | Distribution Budget Incr Value |
| WS_BDGT_MN_VAL | NUMBER |  |  |  | Worksheet Budget Min Value |
| WS_BDGT_MX_VAL | NUMBER |  |  |  | Worksheet Budget Max Value |
| WS_BDGT_INCR_VAL | NUMBER |  |  |  | Worksheet Budget Incr Value |
| RSRV_MN_VAL | NUMBER |  |  |  | Reserve Budget Min Value |
| RSRV_MX_VAL | NUMBER |  |  |  | Reserve Budget Max Value |
| RSRV_INCR_VAL | NUMBER |  |  |  | Reserve Budget Incr Value |
| DIST_BDGT_ISS_VAL | NUMBER |  |  |  | Distribution Budget Issued Value |
| WS_BDGT_ISS_VAL | NUMBER |  |  |  | Worksheet Budget Issued Value |
| DFLT_DIST_BDGT_VAL | NUMBER |  |  |  | Default Distribution Bugdet Value |
| DFLT_WS_BDGT_VAL | NUMBER |  |  |  | Worksheet Distribution Budget Value. |
| DIST_BDGT_ISS_DATE | DATE |  |  |  | Distribution Budget Issued Date |
| WS_BDGT_ISS_DATE | DATE |  |  |  | Worksheet Budget Issued Date |
| WS_BDGT_VAL_LAST_UPD_DATE | DATE |  |  |  | Worksheet Budget Update Date |
| DIST_BDGT_VAL_LAST_UPD_DATE | DATE |  |  |  | Distribution Budget Update Date |
| RSRV_VAL_LAST_UPD_DATE | DATE |  |  |  | Reserve Budget Update Date |
| WS_BDGT_VAL_LAST_UPD_BY | NUMBER |  | 18 |  | Worksheet Budget Updated by Person |
| DIST_BDGT_VAL_LAST_UPD_BY | NUMBER |  | 18 |  | Distribution Budget Updated by Person |
| RSRV_VAL_LAST_UPD_BY | NUMBER |  | 18 |  | Reserve Budget Updated by Person |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PERSON_GROUPS_UK1 | Unique | Default | GROUP_PER_IN_LER_ID, GROUP_PL_ID, GROUP_OIPL_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
