# CMP_HISTORY

CMP_HISTORY table stores recurring and nonrecurring elements which will be viewed in person compensation history user interface.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmphistory-10607.html#cmphistory-10607](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmphistory-10607.html#cmphistory-10607)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_HISTORY_PK | CMP_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CMP_HISTORY_ID | NUMBER |  | 18 | Yes | CMP_HISTORY_ID |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | ELEMENT_TYPE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 120 |  |  | LEGISLATION_CODE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | INPUT_VALUE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_HISTORY_U1 | Unique | Default | CMP_HISTORY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
