# HWM_TCSMR_CONFIGS

Each Time Consumer Configuration Set has a row in this table for each of the Time Consumers that is a member of the set. A row in this table details the configuration information for that Time Consumer, such as the Time Category to be used for deciding to process a Time Entry

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrconfigs-20149.html#hwmtcsmrconfigs-20149](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrconfigs-20149.html#hwmtcsmrconfigs-20149)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCSMR_CONFIGS_PK | TCSMR_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCSMR_CONFIG_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number. This column is not updateable. |
| APRVL_REC_GRP_TYP_CD | VARCHAR2 | 30 |  |  | APRVL_REC_GRP_TYP_CD |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCSMR_CONFIG_SET_ID | NUMBER |  | 18 |  | Time Consumer Configuration Set parent |
| TCAT_ID | NUMBER |  | 18 |  | foreign key to HWM_TIME_CATEGORIES.TCAT_ID This indicates which Time Category should be checked against each Time Entry to see if the Time Entry should be processed by the Time Consumer stored in TCSMR_ID |
| APPROVAL_PERIOD_ID | NUMBER |  | 18 |  | key to HWM_REPEATING_PERIODS.REPEATING_PERIOD_ID. The approval period to be used for the Time Consumer being configured |
| TCSMRS_ID | NUMBER |  | 18 |  | key to HWM_TCNSMRS.TCSMR_ID. The Time Consumer for which this row specifies the configuration |
| VALIDATE_ON_SAVE | VARCHAR2 | 12 |  |  | Needs to be correlated with the Transfer Status picked for any Transfer Processes belong to the Time Consumer. For example, if you say you are not going to validation on save for the Payroll application you CANNOT then transfer on save - since time always needs to be validated before being Xfrd. |
| TIME_REQUIRED | VARCHAR2 | 12 |  |  | Used in reporting. |
| ENABLE_ENTRY_LEVEL_APRVL | VARCHAR2 | 30 |  |  | Used in approval. |
| PROCESS_TIME | VARCHAR2 | 30 |  |  | Used In Payroll Processing |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCSMR_CONFIGS_N20 | Non Unique | Default | SGUID |
| HWM_TCSMR_CONFIGS_N3 | Non Unique | Default | TCSMRS_ID |
| HWM_TCSMR_CONFIGS_U1 | Unique | FUSION_TS_TX_DATA | TCSMR_CONFIG_ID, ORA_SEED_SET1 |
| HWM_TCSMR_CONFIGS_U11 | Unique | FUSION_TS_TX_DATA | TCSMR_CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
