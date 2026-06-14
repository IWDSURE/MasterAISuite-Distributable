# CMP_MKT_COMP_TYPE_CONFIG_B

Table stores the display configuration of Compensation Types for Market data.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomptypeconfigb-21426.html#cmpmktcomptypeconfigb-21426](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomptypeconfigb-21426.html#cmpmktcomptypeconfigb-21426)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_COMP_TYPE_CONFIG_B_PK | COMP_TYPE_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMP_TYPE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for the table |
| COMPENSATION_OBJECT | VARCHAR2 | 30 |  | Yes | Configuration for which Compensation Object - WFC, Salary, Individual Compensation or Compensation Info |
| COMP_TYPE_ID | NUMBER |  | 18 | Yes | Compensation type for which label is configured |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | Display sequence for Comp types display in view Market Data |
| ENABLE_COMP_TYPE_FLAG | VARCHAR2 | 1 |  |  | Label enable status for Comp Type |
| ENABLE_MKT_TARGET_FLAG | VARCHAR2 | 1 |  |  | Label enable status for Market Target |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_COMP_TYPE_CONFIG_B_U1 | Unique | Default | COMP_TYPE_CONFIG_ID |
| CMP_MKT_COMP_TYPE_CONFIG_B_U2 | Unique | Default | COMPENSATION_OBJECT, COMP_TYPE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
