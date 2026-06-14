# HWM_GRP_TYPE

A type of time record group.  For example, an absence header, which contains a collection of absence entries.  Or, a time card, containing a collection of days, or a day, which contains a collection of time records.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrptype-18783.html#hwmgrptype-18783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrptype-18783.html#hwmgrptype-18783)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_GRP_PK | GROUP_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GROUP_ROW_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| GRP_TYPE_ID | NUMBER |  | 18 | Yes | Unique group type Id |
| PARENT_GRP_ID | NUMBER |  | 18 |  | The building block id for the parent block in the time structure hierarchy. |
| GRP_LEVEL | NUMBER |  |  | Yes | Group Level |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAYER_ID | NUMBER |  | 18 | Yes | TM_LAYER_ID |
| NAME | VARCHAR2 | 255 |  | Yes | For Range type of building blocks, the stop time of the block. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| GRP_TYPE | VARCHAR2 | 30 |  |  | Explicit or Implicit |
| IS_TM_REC | VARCHAR2 | 30 |  | Yes | IS_TM_REC |
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
| HWM_GRP_TYPE_N20 | Non Unique | Default | SGUID |
| HWM_GRP_TYPE_PK | Unique | FUSION_TS_TX_DATA | GROUP_ROW_ID, ORA_SEED_SET1 |
| HWM_GRP_TYPE_PK1 | Unique | FUSION_TS_TX_DATA | GROUP_ROW_ID, ORA_SEED_SET2 |
| HWM_GRP_TYPE_U1 | Unique | Default | GRP_TYPE_ID, ORA_SEED_SET1 |
| HWM_GRP_TYPE_U11 | Unique | Default | GRP_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
