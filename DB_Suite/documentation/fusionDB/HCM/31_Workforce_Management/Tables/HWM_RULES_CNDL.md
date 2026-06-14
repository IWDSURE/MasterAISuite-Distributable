# HWM_RULES_CNDL

Conditional Rule Set table, which holds the members of conditional Rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulescndl-30557.html#hwmrulescndl-30557](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulescndl-30557.html#hwmrulescndl-30557)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULES_CNDL_PK | CNDL_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CNDL_RULE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CNDL_RULE_NAME | VARCHAR2 | 80 |  | Yes | Name of the Conditional Rule |
| RULE_TYPE | VARCHAR2 | 30 |  | Yes | RULE_TYPE |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Optional description of the Conditional Rule |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULES_CNDL_PK | Unique | FUSION_TS_TX_DATA | CNDL_RULE_ID |
| HWM_RULES_CNDL_U1 | Unique | FUSION_TS_TX_DATA | CNDL_RULE_NAME |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
