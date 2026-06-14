# HWM_ALLOCATION_LN_ATRBS_F

Time Allocations Line Attributes table contains list of attributes and value for each Allocation Line row.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationlnatrbsf-28264.html#hwmallocationlnatrbsf-28264](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationlnatrbsf-28264.html#hwmallocationlnatrbsf-28264)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ALLOCATION_LN_ATRBS_F_PK | ALLOCATION_LN_ATRB_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOCATION_LN_ATRB_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| UI_ATRB_SEQUENCE | NUMBER |  | 9 | Yes | UI_ATRB_SEQUENCE |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| ALLOCATION_RULE_ID | NUMBER |  | 18 | Yes | Foreign Key to the allocation Rule table |
| ALLOCATION_LINE_ID | NUMBER |  | 18 | Yes | Foreign Key to the allocation ALLOCATION_LINE |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | ATTR_ID |
| ATRB_FLD_NAME | VARCHAR2 | 240 |  | Yes | ATRB_FLD_NAME |
| ATRB_DATA_TYPE | VARCHAR2 | 30 |  | Yes | ATRB_DATA_TYPE |
| ATRB_VALUE_TEXT | VARCHAR2 | 250 |  |  | ATTR_VALUE_TEXT |
| ATRB_VALUE_NUMBER | NUMBER |  |  |  | ATTR_VALUE_NUMBER |
| ATRB_VALUE_TIMESTAMP | TIMESTAMP |  |  |  | ATTR_VALUE_TIMESTAMP |
| DATA_LEVEL | NUMBER |  | 9 | Yes | DATA_LEVEL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ALLOCATION_LN_ATRBS_F_N1 | Non Unique | Default | ALLOCATION_RULE_ID |
| HWM_ALLOCATION_LN_ATRBS_F_PK | Unique | FUSION_TS_TX_DATA | ALLOCATION_LN_ATRB_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HWM_ALLOCATION_LN_ATRBS_F_U1 | Unique | Default | ALLOCATION_LINE_ID, EFFECTIVE_START_DATE, TM_ATRB_FLD_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
