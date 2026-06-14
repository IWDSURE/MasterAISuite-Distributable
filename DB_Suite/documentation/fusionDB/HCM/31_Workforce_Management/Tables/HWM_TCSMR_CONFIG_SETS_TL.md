# HWM_TCSMR_CONFIG_SETS_TL

A consumer configuration set represents a group of time consumers registering interest in time.  This is used in a setup option such that the time entered by users is identified as required by consumers specified in this set.  Futher attribution is kept on the set to identify when consumers should receive time, when consumer validation should execute and under what conditions time should be transferred to the consumer.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrconfigsetstl-26372.html#hwmtcsmrconfigsetstl-26372](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcsmrconfigsetstl-26372.html#hwmtcsmrconfigsetstl-26372)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCSMR_CONFIG_SETS_TL_PK | TCSMR_CONFIG_SET_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCSMR_CONFIG_SET_ID | NUMBER |  | 18 | Yes | TCSMR_CONFIG_SET_ID |
| NAME | VARCHAR2 | 255 |  |  | NAME |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCSMR_CONFIG_SETS_TL_U1 | Unique | FUSION_TS_TX_DATA | TCSMR_CONFIG_SET_ID, LANGUAGE, ORA_SEED_SET1 |
| HWM_TCSMR_CONFIG_SETS_TL_U11 | Unique | FUSION_TS_TX_DATA | TCSMR_CONFIG_SET_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
