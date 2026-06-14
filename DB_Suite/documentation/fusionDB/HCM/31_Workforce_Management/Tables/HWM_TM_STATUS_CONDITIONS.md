# HWM_TM_STATUS_CONDITIONS

This table contains the definition of the conditions of a derived status (atomic statuses will not have a row in this table). It is basically a list of conditions (on other statuses) that need to be met for the derived status to be true.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatusconditions-23907.html#hwmtmstatusconditions-23907](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatusconditions-23907.html#hwmtmstatusconditions-23907)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_STATUS_CONDITIONS_PK | TM_STATUS_CONDITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_STATUS_CONDITION_ID | NUMBER |  | 18 | Yes | TM_STATUS_CONDITION_ID |
| STATUS_COND_CD | VARCHAR2 | 80 |  | Yes | STATUS_COND_CD |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PARENT_STATUS_DEF_ID | NUMBER |  | 18 |  | PARENT_STATUS_DEF_ID |
| STATUS_DEF_ID | NUMBER |  | 18 |  | STATUS_DEF_ID |
| PARENT_STATUS_VALUE | VARCHAR2 | 120 |  |  | PARENT_STATUS_VALUE |
| OPERATOR | VARCHAR2 | 20 |  |  | OPERATOR |
| STATUS_VALUE | VARCHAR2 | 120 |  |  | STATUS_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_STATUS_CONDITIONS_PK | Unique | Default | TM_STATUS_CONDITION_ID, ORA_SEED_SET1 |
| HWM_TM_STATUS_CONDITIONS_PK1 | Unique | Default | TM_STATUS_CONDITION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
