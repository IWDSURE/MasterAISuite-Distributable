# HWM_RULES_CNDL_MBRS

Conditional Rule Members of Time Calculation Rules are stored in this table.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulescndlmbrs-6962.html#hwmrulescndlmbrs-6962](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulescndlmbrs-6962.html#hwmrulescndlmbrs-6962)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULES_CNDL_MBRS_PK | CNDL_RULE_MBR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CNDL_RULE_MBR_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CNDL_RULE_ID | NUMBER |  | 18 |  | Foreign key to HWM_RULES_CNDL table. |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| PROCESSING_ORDER | NUMBER |  | 9 | Yes | Order in which this conditional rule should be applied on the TBB. |
| TCAT_ID | NUMBER |  | 18 | Yes | Time Category Run Condition, which determines if the rule should be applied on a TBB |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULES_CNDL_MBRS_PK | Unique | FUSION_TS_TX_DATA | CNDL_RULE_MBR_ID |
| HWM_RULES_CNDL_MBRS_U1 | Unique | FUSION_TS_TX_DATA | CNDL_RULE_ID, PROCESSING_ORDER |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
