# HRC_DL_SO_CHILD_LEVEL_ONE

Child Level One Object for testing Sample HDL flow.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsochildlevelone-15955.html#hrcdlsochildlevelone-15955](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsochildlevelone-15955.html#hrcdlsochildlevelone-15955)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_SO_CHILD_LEVEL_ONE_PK | CHILD_LEVEL_ONE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHILD_LEVEL_ONE_ID | NUMBER |  | 18 | Yes | CHILD_LEVEL_ONE_ID |
| CHILD_LEVEL_ONE_NUMBER | VARCHAR2 | 64 |  | Yes | CHILD_LEVEL_ONE_NUMBER |
| PARENT_ID | NUMBER |  | 18 | Yes | PARENT_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| ATTR_CHAR1 | VARCHAR2 | 30 |  |  | ATTR_CHAR1 |
| ATTR_CHAR2 | VARCHAR2 | 30 |  |  | ATTR_CHAR2 |
| ATTR_NUM1 | NUMBER |  | 10 |  | ATTR_NUM1 |
| ATTR_NUM2 | NUMBER |  | 10 |  | ATTR_NUM2 |
| ATTR_DATE1 | DATE |  |  |  | ATTR_DATE1 |
| ATTR_DATE2 | DATE |  |  |  | ATTR_DATE2 |
| ENTERPRISE_ID | NUMBER |  | 18 |  | This is the unique identifier for the enterprise. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_SO_CHILD_LEVEL_ONE_U1 | Unique | Default | CHILD_LEVEL_ONE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
