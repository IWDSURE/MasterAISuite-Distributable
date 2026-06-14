# HWM_PROCESS_USAGES

Identifies which process components are used in a particular process mode.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmprocessusages-28502.html#hwmprocessusages-28502](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmprocessusages-28502.html#hwmprocessusages-28502)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_PROCESS_USAGES_PK | PROCESS_USAGES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_USAGES_ID | NUMBER |  | 18 | Yes | PROCESS_USAGES_ID |
| PROCESS_MODE_ID | NUMBER |  | 18 | Yes | PROCESS_MODE_ID |
| PROCESS_COMPONENT_ID | NUMBER |  | 18 | Yes | PROCESS_COMPONENT_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENABLED | VARCHAR2 | 30 |  |  | Column to identify whether a Process Component is allowed or not |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_PROCESS_USAGES_N20 | Non Unique | Default | SGUID |
| HWM_PROCESS_USAGES_N3 | Non Unique | Default | PROCESS_MODE_ID |
| HWM_PROCESS_USAGES_U1 | Unique | Default | PROCESS_USAGES_ID, ORA_SEED_SET1 |
| HWM_PROCESS_USAGES_U11 | Unique | Default | PROCESS_USAGES_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
