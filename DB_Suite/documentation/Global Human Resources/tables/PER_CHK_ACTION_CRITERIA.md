# PER_CHK_ACTION_CRITERIA

The table records checklist events action criteria.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkactioncriteria-15625.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkactioncriteria-15625.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ACTION_CRITERIA_PK | CHECKLIST_ACT_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHECKLIST_ACT_CRITERIA_ID | NUMBER |  | 18 | Yes | Primary Key |  |
| CHECKLIST_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_CHECKLIST_ACTIONS |  |
| GROUP_SEQUENCE | NUMBER |  |  | Yes | GROUP_SEQUENCE |  |
| ITEM_SEQUENCE | NUMBER |  |  | Yes | ITEM_SEQUENCE |  |
| ITEM_GROUP_CONJUNCTION | VARCHAR2 | 10 |  |  | Group Conjunction. |  |
| ITEM_CONJUNCTION | VARCHAR2 | 10 |  |  | Item Conjunction. |  |
| ITEM_ATTRIBUTE | VARCHAR2 | 100 |  | Yes | Object Attribute. |  |
| ITEM_OPERATOR | VARCHAR2 | 30 |  | Yes | Operator between ITEM_ATTRIBUTE and ITEM_OPERAND |  |
| ITEM_IGNORE_CASE | VARCHAR2 | 4 |  |  | If case is to be ignored while evaluating the condition. |  |
| ITEM_OPERAND_TYPE | VARCHAR2 | 100 |  |  | ITEM_OPERAND_TYPE |  |
| ITEM_OPERAND_VALUE | VARCHAR2 | 255 |  |  | Other Operand in the condition. |  |
| ITEM_OPERAND_DATE_VALUE | DATE |  |  |  | Column to hold date value of other operand. |  |
| ITEM_OPERAND_TMSTAMP_VALUE | TIMESTAMP |  |  |  | Column to hold timestamp value of other operand. |  |
| IS_DEFAULT_GRP | VARCHAR2 | 4 |  |  | IS_DEFAULT_GRP |  |
| IS_DEFAULT_ROW | VARCHAR2 | 4 |  |  | IS_DEFAULT_ROW |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_ACTION_CRITERIA_PK | Unique | Default | CHECKLIST_ACT_CRITERIA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
