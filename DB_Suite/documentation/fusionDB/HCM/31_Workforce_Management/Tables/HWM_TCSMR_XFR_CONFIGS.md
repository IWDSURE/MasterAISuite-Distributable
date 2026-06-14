# HWM_TCSMR_XFR_CONFIGS

For each Time Consumer in the Time Consumer Configuration Set there is typically a transfer process that needs to be configured. The data model allows for more than a single transfer process for each Time Consumer. This table contains a set of rows (where a set contains a row for each Time Consumer in the Time Consumer Configuration Set) for each transfer process linked to a given time consumer configuration

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrxfrconfigs-22729.html#hwmtcsmrxfrconfigs-22729](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrxfrconfigs-22729.html#hwmtcsmrxfrconfigs-22729)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCSMR_XFR_CONFIGS_PK | TCMSR_XFR_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCMSR_XFR_CONFIG_ID | NUMBER |  | 18 | Yes | Primary Key |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCSMR_CONFIG_ID | NUMBER |  | 18 |  | key to HWM_TCSMR_CONFIGS.TCSMR_CONFIG_ID. Identifies the Time Consumer Configuration to which this configuration of the transfer process belongs |
| TCSMR_XFR_PROCESS_ID | NUMBER |  | 18 |  | key to HWM_TCSMR_XFR_PROCESSES.TCSMR_XFR_PROCESS_ID. The transfer process this row is configuring |
| XFR_ON_SAVE | VARCHAR2 | 12 |  |  | Whether you can transfer as soon as a timecard is saved |
| XFR_ON_SUBMIT | VARCHAR2 | 12 |  |  | Whether the timecard needs to be submitted for transfer |
| APPROVAL_REQD | VARCHAR2 | 12 |  |  | if XFR_ON_SUBMIT is Y then this column is used to indicate if approval is required for each of the Time Consumers being Configured |
| APPROVAL_REQD_TCSMR_ID | NUMBER |  | 18 |  | key to HWM_TCSMS.TCSMR_ID. Indicates which Time Consumer the APPROVAL_REQD pertains to |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCSMR_XFR_CONFIGS_N20 | Non Unique | Default | SGUID |
| HWM_TCSMR_XFR_CONFIGS_U1 | Unique | FUSION_TS_TX_DATA | TCMSR_XFR_CONFIG_ID, ORA_SEED_SET1 |
| HWM_TCSMR_XFR_CONFIGS_U11 | Unique | FUSION_TS_TX_DATA | TCMSR_XFR_CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
