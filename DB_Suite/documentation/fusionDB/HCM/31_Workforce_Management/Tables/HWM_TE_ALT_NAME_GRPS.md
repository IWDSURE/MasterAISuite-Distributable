# HWM_TE_ALT_NAME_GRPS

This table keeps information about the actual values that are used in the repository when a user selects an alternate name.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtealtnamegrps-20459.html#hwmtealtnamegrps-20459](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtealtnamegrps-20459.html#hwmtealtnamegrps-20459)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TE_ALT_NAME_GRPS_PK | TE_ALT_NAME_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TE_ALT_NAME_GRP_ID | NUMBER |  | 18 | Yes | TE_ALT_NAME_GRP_ID |
| GRP_ID | NUMBER |  | 18 | Yes | GRP_ID |
| TE_ALT_NAME_VAL_ID | NUMBER |  | 18 | Yes | TE_ALT_NAME_VAL_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TE_ALT_NAME_GRPS_N20 | Non Unique | Default | SGUID |
| HWM_TE_ALT_NAME_GRPS_U1 | Unique | Default | TE_ALT_NAME_VAL_ID, GRP_ID |
| HWM_TE_ALT_NAME_GRPS_U2 | Unique | Default | TE_ALT_NAME_GRP_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
