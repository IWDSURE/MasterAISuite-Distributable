# CMP_MKT_COMPOSITE_CONFIG_B

Stores the display configuration Market Survey Composite column labels for Market Data.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcompositeconfigb-9110.html#cmpmktcompositeconfigb-9110](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcompositeconfigb-9110.html#cmpmktcompositeconfigb-9110)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_COMPOSITE_CONFIG_PK | COMPOSITE_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPOSITE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for the table |
| COMP_TYPE_CONFIG_ID | NUMBER |  | 18 | Yes | Referrence to COMP_TYPE_CONFIG Table |
| COMPOSITE_COLUMN_KEY | VARCHAR2 | 30 |  | Yes | Lookup Code of Composite Column |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | Display sequence composite attribute to be displayed in view Market Data |
| ENABLE_FLAG | VARCHAR2 | 1 |  |  | Label enable status for Composite column |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_COMPOSITE_CONFIG_N1 | Non Unique | Default | COMP_TYPE_CONFIG_ID |
| CMP_MKT_COMPOSITE_CONFIG_U1 | Unique | Default | COMPOSITE_CONFIG_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
