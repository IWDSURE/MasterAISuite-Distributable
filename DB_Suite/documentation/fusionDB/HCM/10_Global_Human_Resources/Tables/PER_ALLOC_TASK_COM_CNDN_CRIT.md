# PER_ALLOC_TASK_COM_CNDN_CRIT

Table to store completion condition criteria for an allocated task

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peralloctaskcomcndncrit-21047.html#peralloctaskcomcndncrit-21047](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peralloctaskcomcndncrit-21047.html#peralloctaskcomcndncrit-21047)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOC_TASK_COM_CNDN_CR_PK | ALLOC_TASK_COM_COND_CRIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOC_TASK_COM_COND_CRIT_ID | NUMBER |  | 18 | Yes | ALLOC_TASK_COM_COND_CRIT_ID |
| ALLOC_TASK_COM_CONDITION_ID | NUMBER |  | 18 | Yes | ALLOC_TASK_COM_CONDITION_ID |
| CONDITION_TYPE | VARCHAR2 | 30 |  | Yes | CONDITION_TYPE |
| TASK_COM_COND_CRITERIA_ID | NUMBER |  | 18 |  | TASK_COM_COND_CRITERIA_ID |
| GROUP_SEQUENCE | NUMBER |  | 5 | Yes | GROUP_SEQUENCE |
| ITEM_SEQUENCE | NUMBER |  | 5 | Yes | ITEM_SEQUENCE |
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
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALLOC_TASK_COM_CNDN_CR_PK | Unique | Default | ALLOC_TASK_COM_COND_CRIT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
