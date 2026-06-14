# PAY_COST_ALLOC_KEYFLEX

This table contains the combinations for the cost allocation key flexfield for each of the typical accounts maintained by an enterprise such as cost, offset, liability, cash, default, and suspense accounts.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostallockeyflex-7325.html#paycostallockeyflex-7325](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostallockeyflex-7325.html#paycostallockeyflex-7325)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COST_ALLOC_KEYFLEX_PK | COST_ALLOCATION_KEYFLEX_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  | 18 | Yes | COST_ALLOCATION_KEYFLEX_ID |
| CONCATENATED_SEGMENTS | VARCHAR2 | 2000 |  |  | CONCATENATED_SEGMENTS |
| ID_FLEX_NUM | NUMBER |  | 18 | Yes | ID_FLEX_NUM |
| SUMMARY_FLAG | VARCHAR2 | 1 |  |  | SUMMARY_FLAG |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | ENABLED_FLAG |
| START_DATE_ACTIVE | DATE |  |  |  | START_DATE_ACTIVE |
| END_DATE_ACTIVE | DATE |  |  |  | END_DATE_ACTIVE |
| SEGMENT1 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT2 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT3 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT4 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT5 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT6 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT7 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT8 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT9 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT10 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT11 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT12 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT13 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT14 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT15 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT16 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT17 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT18 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT19 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT20 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT21 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT22 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT23 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT24 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT25 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT26 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT27 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT28 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT29 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT30 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_COST_ALLOC_KEYFLEX_PK | Unique | Default | COST_ALLOCATION_KEYFLEX_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
