# HWM_ALLOCATION_ATTRIBUTE_F

Time Allocations attributes table contains list of all Attributes used by allocation UI , by Rule level.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationattributef-26575.html#hwmallocationattributef-26575](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationattributef-26575.html#hwmallocationattributef-26575)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ALLOCATION_ATTRIBUTE_F_PK | ALLOCATION_ATTRIBUTE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATION_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| DATA_SOURCE_USAGE_ID | NUMBER |  | 18 |  | DATA_SOURCE_USAGE_ID |
| ALLOCATION_RULE_ID | NUMBER |  | 18 | Yes | Foreign Key to the allocation Rule table |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| ALLOCATION_ID | NUMBER |  | 18 | Yes | Foreign Key to the allocation Rule table |
| UI_ATRB_SEQUENCE | NUMBER |  | 9 | Yes | UI_ATRB_SEQUENCE |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | ATTR_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ALLOCATION_ATTRIBUTE_F_PK | Unique | FUSION_TS_TX_DATA | ALLOCATION_ATTRIBUTE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HWM_ALLOCATION_ATTRIBUTE_F_U1 | Unique | Default | ALLOCATION_ID, ALLOCATION_RULE_ID, TM_ATRB_FLD_ID, EFFECTIVE_START_DATE, DATA_SOURCE_USAGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
