# HWM_TM_STATUS_DEF_B

This table contains the definition of a status. We will support 2 types of statuses, ATOMIC statuses which are set directly, and derived statuses which are derived from other statuses.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatusdefb-8062.html#hwmtmstatusdefb-8062](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatusdefb-8062.html#hwmtmstatusdefb-8062)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_STATUS_DEF_B_PK | TM_STATUS_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_STATUS_DEF_ID | NUMBER |  | 18 | Yes | Row Identifier |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TM_STATUS_TYPE | VARCHAR2 | 30 |  |  | TM_STATUS_TYPE |
| TCSMRS_ID | NUMBER |  | 18 |  | TCSMRS_ID |
| SCOPE | VARCHAR2 | 30 |  |  | SCOPE |
| REPOSITORY_TYPE | VARCHAR2 | 32 |  |  | Repository type like Group/Record |
| VALUE_IF_TRUE | VARCHAR2 | 30 |  |  | VALUE_IF_TRUE |
| VALUE_IF_FALSE | VARCHAR2 | 30 |  |  | VALUE_IF_FALSE |
| VALUE_DERIVED_FLAG | VARCHAR2 | 30 |  | Yes | Discriminator flag |
| STATUS_DEF_CD | VARCHAR2 | 30 |  | Yes | STATUS_DEF_CD |
| TRUE_VALUE | NUMBER |  | 18 |  | True Value |
| FALSE_VALUE | NUMBER |  | 18 |  | False Value |
| ALLOWABLE_VALUES | VARCHAR2 | 30 |  |  | ALLOWABLE_VALUES |
| DEFINITIONCODE | VARCHAR2 | 32 |  |  | CODE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| VISIBILITY | VARCHAR2 | 32 |  |  | VISIBILITY |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_STATUS_DEF_B_PK | Unique | Default | TM_STATUS_DEF_ID, ORA_SEED_SET1 |
| HWM_TM_STATUS_DEF_B_PK1 | Unique | Default | TM_STATUS_DEF_ID, ORA_SEED_SET2 |
| HWM_TM_STATUS_DEF_B_U1 | Unique | Default | DEFINITIONCODE, TCSMRS_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| HWM_TM_STATUS_DEF_B_U11 | Unique | Default | DEFINITIONCODE, TCSMRS_ID, ENTERPRISE_ID, ORA_SEED_SET2 |
| HWM_TM_STATUS_DEF_B_U2 | Unique | Default | STATUS_DEF_CD, ENTERPRISE_ID, TM_STATUS_DEF_ID, ORA_SEED_SET1 |
| HWM_TM_STATUS_DEF_B_U21 | Unique | Default | STATUS_DEF_CD, ENTERPRISE_ID, TM_STATUS_DEF_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
