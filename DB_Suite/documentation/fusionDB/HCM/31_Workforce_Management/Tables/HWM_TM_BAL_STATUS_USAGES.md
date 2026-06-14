# HWM_TM_BAL_STATUS_USAGES

Time statuses that are included in a time balance.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmbalstatususages-22601.html#hwmtmbalstatususages-22601](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmbalstatususages-22601.html#hwmtmbalstatususages-22601)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_BAL_STATUS_USAGES_PK | TM_BAL_STATUS_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_BAL_STATUS_USAGE_ID | NUMBER |  | 18 | Yes | Primary Key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LOOKUP_TYPE | VARCHAR2 | 30 |  | Yes | The lookup which defines which statuses that should be included in a time balance. |
| LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | The lookup code that specifically defines which combination of statuses that should be included in the time balance. |
| STATUS_DEF_CD | VARCHAR2 | 30 |  | Yes | The status definition that corresponds to the status to include in the time balance. |
| STATUS_VALUE | VARCHAR2 | 30 |  | Yes | The status code that corresponds to the status to include in the time balance. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_BAL_STATUS_USAGES_U1 | Unique | Default | TM_BAL_STATUS_USAGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
