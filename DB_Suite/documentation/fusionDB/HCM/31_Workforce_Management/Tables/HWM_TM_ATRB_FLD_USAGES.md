# HWM_TM_ATRB_FLD_USAGES

A Table to identify the usages of attributes for the corresponding consumers.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldusages-14960.html#hwmtmatrbfldusages-14960](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldusages-14960.html#hwmtmatrbfldusages-14960)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_ATRB_FLD_USAGES_PK | TM_ATRB_FLD_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ATRB_FLD_USAGE_ID | NUMBER |  | 18 | Yes | Primary key of the Time Attribute Field Usages |
| TM_ATRB_FLD_CONTEXT_ID | NUMBER |  | 18 |  | Foreign Key to HWM_TM_ATRB_FLD_CONTEXTS |
| TM_ATRB_FLD_ID | NUMBER |  | 18 |  | Foreign key to HWM_TM_ATRB_FLDS_B |
| NAME | VARCHAR2 | 240 |  |  | Overridden Name (optional) |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ATRB_FLD_USAGES_U1 | Unique | Default | TM_ATRB_FLD_USAGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
