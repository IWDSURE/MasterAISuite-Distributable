# PER_CHK_TASK_CONDN_CRIT

PER_CHK_TASK_CONDN_CRIT: Stores the criteria forming the condition.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchktaskcondncrit-22884.html#perchktaskcondncrit-22884](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchktaskcondncrit-22884.html#perchktaskcondncrit-22884)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_TASK_CONDN_CRIT_PK | TASK_CONDN_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_CONDN_CRITERIA_ID | NUMBER |  | 18 | Yes | TASK_CONDN_CRITERIA_ID |
| TASK_CONDITION_ID | NUMBER |  | 18 | Yes | TASK_CONDITION_ID |
| GROUP_SEQUENCE | NUMBER |  |  | Yes | GROUP_SEQUENCE |
| ITEM_SEQUENCE | NUMBER |  |  | Yes | ITEM_SEQUENCE |
| ITEM_GROUP_CONJUNCTION | VARCHAR2 | 10 |  |  | ITEM_GROUP_CONJUNCTION |
| ITEM_CONJUNCTION | VARCHAR2 | 10 |  |  | ITEM_CONJUNCTION |
| ITEM_ATTRIBUTE | VARCHAR2 | 100 |  | Yes | ITEM_ATTRIBUTE |
| ITEM_OPERATOR | VARCHAR2 | 30 |  | Yes | ITEM_OPERATOR |
| ITEM_IGNORE_CASE | VARCHAR2 | 4 |  |  | ITEM_IGNORE_CASE |
| ITEM_OPERAND_TYPE | VARCHAR2 | 100 |  |  | ITEM_OPERAND_TYPE |
| ITEM_OPERAND_VALUE | VARCHAR2 | 255 |  |  | ITEM_OPERAND_VALUE |
| ITEM_OPERAND_DATE_VALUE | DATE |  |  |  | ITEM_OPERAND_DATE_VALUE |
| ITEM_OPERAND_TMSTAMP_VALUE | TIMESTAMP |  |  |  | ITEM_OPERAND_TMSTAMP_VALUE |
| IS_DEFAULT_GRP | VARCHAR2 | 4 |  |  | IS_DEFAULT_GRP |
| IS_DEFAULT_ROW | VARCHAR2 | 4 |  |  | IS_DEFAULT_ROW |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_TASK_CONDN_CRIT_PK | Unique | Default | TASK_CONDN_CRITERIA_ID, ORA_SEED_SET1 |
| PER_CHK_TASK_CONDN_CRIT_PK1 | Unique | Default | TASK_CONDN_CRITERIA_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
