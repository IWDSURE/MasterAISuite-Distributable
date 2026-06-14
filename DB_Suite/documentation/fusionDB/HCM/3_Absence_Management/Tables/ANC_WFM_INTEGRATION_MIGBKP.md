# ANC_WFM_INTEGRATION_MIGBKP

Table for storing anc otl migration data like absence entry id,absence type entry id,time record group id

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancwfmintegrationmigbkp-24375.html#ancwfmintegrationmigbkp-24375](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancwfmintegrationmigbkp-24375.html#ancwfmintegrationmigbkp-24375)

## Primary Key

| Name | Columns |
|------|----------|
| anc_wfm_integration_migbkp_PK | ANC_WFM_MIG_BACKUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANC_WFM_MIG_BACKUP_ID | NUMBER |  | 18 | Yes | ANC_WFM_MIG_BACKUP_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_ENTRY_ID |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 |  | PER_ABS_TYPE_ENTRY_ID |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | TM_REC_GRP_ID |
| OLD_TM_REC_GRP_ID | NUMBER |  | 18 |  | OLD_TM_REC_GRP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_WFM_INTEGRATION_MIGBKP_N2 | Non Unique | ANC_WFM_INTEGRATION_MIGBKP_N2 | OLD_TM_REC_GRP_ID |
| anc_wfm_integration_migbkp_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |
| anc_wfm_integration_migbkp_U1 | Unique | Default | ANC_WFM_MIG_BACKUP_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
