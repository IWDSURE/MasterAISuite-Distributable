# HRC_DL_ARC_FILE_UK_ROWS

This table is created to store list of Multiple user keys for a given business object

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlarcfileukrows-15679.html#hrcdlarcfileukrows-15679](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlarcfileukrows-15679.html#hrcdlarcfileukrows-15679)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ARC_FILE_UK_ROWS_PK | UK_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UK_ROW_ID | NUMBER |  | 18 | Yes | USER_KEY_ROW_ID, Primary Key for the table |
| KEY_LIST_INDEX | NUMBER |  | 2 | Yes | User key index |
| HEADER_ID | NUMBER |  | 18 | Yes | Foreign key reference from HRC_DL_FILE_HEADERS.HEADER_ID |
| ROW_ID | NUMBER |  | 18 | Yes | Foreign key reference from HRC_DL_FILE_ROWS.ROW_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| UKVAL001 | VARCHAR2 | 500 |  |  | User key column 1 to store low precision user key |
| UKVAL002 | VARCHAR2 | 500 |  |  | User key column 2  to store low precision user key |
| UKVAL003 | VARCHAR2 | 500 |  |  | User key column 3 to store low precision user key |
| UKVAL004 | VARCHAR2 | 500 |  |  | User key column 4  to store low precision user key |
| UKVAL005 | VARCHAR2 | 500 |  |  | User key column 5  to store low precision user key |
| UKVAL006 | VARCHAR2 | 500 |  |  | User key column 6  to store low precision user key |
| UKVAL007 | VARCHAR2 | 500 |  |  | User key column 7 to store low precision user key |
| UKVAL008 | VARCHAR2 | 500 |  |  | User key column 8  to store low precision user key |
| UKVAL009 | VARCHAR2 | 500 |  |  | User key column 9 to store low precision user key |
| UKVAL010 | VARCHAR2 | 500 |  |  | User key column 10  to store low precision user key |
| UKVAL011 | VARCHAR2 | 500 |  |  | User key column 11 to store low precision user key |
| UKVAL012 | VARCHAR2 | 500 |  |  | User key column 12 to store low precision user key |
| UKVAL013 | VARCHAR2 | 500 |  |  | User key column 13  to store low precision user key |
| UKVAL014 | VARCHAR2 | 500 |  |  | User key column 14 to store low precision user key |
| UKVAL015 | VARCHAR2 | 500 |  |  | User key column 15 to store low precision user key |
| UKVAL016 | VARCHAR2 | 500 |  |  | User key column 16 to store low precision user key |
| UKHPVAL001 | VARCHAR2 | 4000 |  |  | User key column 1 to store high precision user key |
| UKHPVAL002 | VARCHAR2 | 4000 |  |  | User key column 2  to store high precision user key |
| UKHPVAL003 | VARCHAR2 | 4000 |  |  | User key column 3 to store high precision user key |
| UKHPVAL004 | VARCHAR2 | 4000 |  |  | User key column 4  to store high precision user key |
| UKHPVAL005 | VARCHAR2 | 4000 |  |  | User key column 5  to store high precision user key |
| UKHPVAL006 | VARCHAR2 | 4000 |  |  | User key column 6  to store high precision user key |
| UKHPVAL007 | VARCHAR2 | 4000 |  |  | User key column 7 to store high precision user key |
| UKHPVAL008 | VARCHAR2 | 4000 |  |  | User key column 8  to store high precision user key |
| UKHPVAL_SECURE001 | VARCHAR2 | 4000 |  |  | UKHPVAL_SECURE001 |
| UKHPVAL_SECURE002 | VARCHAR2 | 4000 |  |  | UKHPVAL_SECURE002 |
| UKHPVAL_SECURE003 | VARCHAR2 | 4000 |  |  | UKHPVAL_SECURE003 |
| UKHPVAL_SECURE004 | VARCHAR2 | 4000 |  |  | UKHPVAL_SECURE004 |
| UKVAL_SECURE001 | VARCHAR2 | 500 |  |  | UKVAL_SECURE001 |
| UKVAL_SECURE002 | VARCHAR2 | 500 |  |  | UKVAL_SECURE002 |
| UKVAL_SECURE003 | VARCHAR2 | 500 |  |  | UKVAL_SECURE003 |
| UKVAL_SECURE004 | VARCHAR2 | 500 |  |  | UKVAL_SECURE004 |
| UKVAL_SECURE005 | VARCHAR2 | 500 |  |  | UKVAL_SECURE005 |
| UKVAL_SECURE006 | VARCHAR2 | 500 |  |  | UKVAL_SECURE006 |
| UKVAL_SECURE007 | VARCHAR2 | 500 |  |  | UKVAL_SECURE007 |
| UKVAL_SECURE008 | VARCHAR2 | 500 |  |  | UKVAL_SECURE008 |
| UKVAL_SECURE009 | VARCHAR2 | 500 |  |  | UKVAL_SECURE009 |
| UKVAL_SECURE010 | VARCHAR2 | 500 |  |  | UKVAL_SECURE010 |
| UKDATE001 | DATE |  |  |  | User key column 1 to store DATE values |
| UKDATE002 | DATE |  |  |  | User key column 2 to store DATE values |
| UKDATE003 | DATE |  |  |  | User key column 3 to store DATE values |
| UKDATE004 | DATE |  |  |  | User key column 4 to store DATE values |
| UKDATE005 | DATE |  |  |  | User key column 5 to store DATE values |
| UKDATE006 | DATE |  |  |  | User key column 6  to store DATE values |
| UKDATE007 | DATE |  |  |  | User key column 7 to store DATE values |
| UKDATE008 | DATE |  |  |  | User key column 8 to store DATE values |
| UKDATE_SECURE001 | DATE |  |  |  | UKDATE_SECURE001 |
| UKDATE_SECURE002 | DATE |  |  |  | UKDATE_SECURE002 |
| UKDATE_SECURE003 | DATE |  |  |  | UKDATE_SECURE003 |
| UKDATE_SECURE004 | DATE |  |  |  | UKDATE_SECURE004 |
| UKDATE_SECURE005 | DATE |  |  |  | UKDATE_SECURE005 |
| UKTIMESTAMP001 | TIMESTAMP |  |  |  | User key column 1 to store TIMESTAMP values |
| UKTIMESTAMP002 | TIMESTAMP |  |  |  | User key column 2 to store TIMESTAMP values |
| UKTIMESTAMP003 | TIMESTAMP |  |  |  | User key column 3  to store TIMESTAMP values |
| UKTIMESTAMP004 | TIMESTAMP |  |  |  | User key column 4 to store TIMESTAMP values |
| UKTIMESTAMP005 | TIMESTAMP |  |  |  | User key column 5 to store TIMESTAMP values |
| UKTIMESTAMP_SECURE001 | TIMESTAMP |  |  |  | UKTIMESTAMP_SECURE001 |
| UKTIMESTAMP_SECURE002 | TIMESTAMP |  |  |  | UKTIMESTAMP_SECURE002 |
| UKTIMESTAMP_SECURE003 | TIMESTAMP |  |  |  | UKTIMESTAMP_SECURE003 |
| UK_HASH | VARCHAR2 | 100 |  |  | UK_HASH |
| REF_TYPE | VARCHAR2 | 30 |  |  | REF_TYPE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_ARC_FILE_UK_ROWS_N1 | Non Unique | Default | HEADER_ID |
| HRC_DL_ARC_FILE_UK_ROWS_U1 | Unique | Default | UK_ROW_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
