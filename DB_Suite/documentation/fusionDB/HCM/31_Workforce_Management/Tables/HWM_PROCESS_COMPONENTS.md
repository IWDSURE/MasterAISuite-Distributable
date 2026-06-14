# HWM_PROCESS_COMPONENTS

Table can be used to add components to a  process.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmprocesscomponents-17603.html#hwmprocesscomponents-17603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmprocesscomponents-17603.html#hwmprocesscomponents-17603)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_PROCESS_COMPONENTS_PK | PROCESS_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_COMPONENT_ID | NUMBER |  | 18 | Yes | PROCESS_COMPONENT_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PARENT_PROCESS_ID | NUMBER |  | 18 |  | PARENT_PROCESS_ID |
| PROCESS_ID | NUMBER |  | 18 |  | PROCESS_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VESION_NUMBER | NUMBER |  | 9 | Yes | OBJECT_VESION_NUMBER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_PROCESS_COMPONENTS_N20 | Non Unique | Default | SGUID |
| HWM_PROCESS_COMPONENTS_N3 | Non Unique | Default | PARENT_PROCESS_ID |
| HWM_PROCESS_COMPONENTS_U1 | Unique | Default | PROCESS_COMPONENT_ID, ORA_SEED_SET1 |
| HWM_PROCESS_COMPONENTS_U11 | Unique | Default | PROCESS_COMPONENT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
