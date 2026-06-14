# HRC_DL_SO_PARENT_M

Parent Level Object for Sample Object to test HDL Flow

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsoparentm-5893.html#hrcdlsoparentm-5893](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsoparentm-5893.html#hrcdlsoparentm-5893)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_SO_PARENT_M_PK | PARENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_SEQUENCE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARENT_ID | NUMBER |  | 18 | Yes | PARENT_ID |
| PARENT_NUMBER | VARCHAR2 | 30 |  | Yes | PARENT_NUMBER |
| PARENT_CODE | VARCHAR2 | 30 |  | Yes | PARENT_CODE |
| START_DATE | DATE |  |  |  | START_DATE |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| PARENT_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | PARENT_BUSINESS_OBJECT_ID |
| CHILD_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | CHILD_BUSINESS_OBJECT_ID |
| ATTR_CHAR1 | VARCHAR2 | 30 |  |  | ATTR_CHAR1 |
| ATTR_CHAR2 | VARCHAR2 | 30 |  |  | ATTR_CHAR2 |
| ATTR_NUMBER1 | NUMBER |  | 18 |  | ATTR_NUMBER1 |
| ATTR_NUMBER2 | NUMBER |  | 18 |  | ATTR_NUMBER2 |
| ATTR_DATE1 | DATE |  |  |  | ATTR_DATE1 |
| ATTR_DATE2 | DATE |  |  |  | ATTR_DATE2 |
| ATTR_DECIMAL1 | NUMBER |  | 8 |  | ATTR_DECIMAL1 |
| ATTR_DECIMAL2 | NUMBER |  | 8 |  | ATTR_DECIMAL2 |
| ATTR_TIMESTAMP1 | TIMESTAMP |  |  |  | ATTR_TIMESTAMP1 |
| ATTR_TIMESTAMP2 | TIMESTAMP |  |  |  | ATTR_TIMESTAMP2 |
| ATTR_HIDDEN | VARCHAR2 | 30 |  |  | ATTR_HIDDEN |
| ATTR_DEPRECATED | VARCHAR2 | 30 |  |  | ATTR_DEPRECATED |
| ATTR_CLOB | CLOB |  |  |  | ATTR_CLOB |
| ATTR_BLOB | BLOB |  |  |  | ATTR_BLOB |
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
| HRC_DL_SO_PARENT_M_U1 | Unique | Default | PARENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_SEQUENCE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_END_DATE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
