# HWM_TM_COST_OVERRIDE_ATRBS

Attributes values for related versions of Cost override

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmcostoverrideatrbs-24284.html#hwmtmcostoverrideatrbs-24284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmcostoverrideatrbs-24284.html#hwmtmcostoverrideatrbs-24284)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_cost_override_atrb_PK | TM_COST_OVERRIDE_ATRB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_COST_OVERRIDE_ATRB_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updatable. |
| TM_COST_OVERRIDE_ID | NUMBER |  | 18 | Yes | Foreign Key column from HWM_TM_COST_OVERRIDES table |
| TM_CARD_FLD_ID | NUMBER |  | 18 | Yes | Time Card Field Identifier |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | Time Attribute Field Identifier |
| DATE_FROM | TIMESTAMP |  |  | Yes | validity start time of the row |
| DATE_TO | TIMESTAMP |  |  | Yes | validity end time of the row |
| DATA_TYPE | VARCHAR2 | 20 |  | Yes | Type of the attribute : Number, Varchar, Date and Timestamp |
| VALUE_TEXT | VARCHAR2 | 150 |  |  | Value of the attribute if its type is Varchar, null otherwise |
| VALUE_NUMBER | NUMBER |  |  |  | Value of the attribute if its type is Number, null otherwise |
| VALUE_TIMESTAMP | TIMESTAMP |  |  |  | Value of the attribute if it is of type Date or Timestamp, null otherwise |
| IS_DEFAULT_VALUE | VARCHAR2 | 1 |  | Yes | Indicates whether the attribute value is a default value that has not been overridden by the user. Value: Y/N |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_COST_OVERRIDE_ATRBS_N1 | Non Unique | Default | TM_COST_OVERRIDE_ID, DATE_FROM, DATE_TO |
| HWM_TM_COST_OVERRIDE_ATRBS_U1 | Unique | Default | TM_COST_OVERRIDE_ATRB_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
