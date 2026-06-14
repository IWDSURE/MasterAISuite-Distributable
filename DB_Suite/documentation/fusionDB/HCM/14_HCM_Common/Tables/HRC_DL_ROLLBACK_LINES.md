# HRC_DL_ROLLBACK_LINES

This table will store the information required for Object Roll Back. This will store the object information for each business object in the hierarchy.

Few Important columns are  :

a) BO Version Number - Product table OVN
b)  ESD - ESD of Product Table
c)  EED - EED of Product Table

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrollbacklines-28509.html#hrcdlrollbacklines-28509](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrollbacklines-28509.html#hrcdlrollbacklines-28509)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ROLLBACK_LINES_PK | ROLLBACK_LINES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLLBACK_LINES_ID | NUMBER |  |  | Yes | ROLLBACK_LINES_ID |
| ROLLBACK_INFO_ID | NUMBER |  |  | Yes | ROLLBACK_INFO_ID |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BO_OVN | NUMBER |  |  | Yes | BO_OBJECT_VERSION_NUMBER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  |  | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_ROLLBACK_LINES_N1 | Non Unique | Default | ROLLBACK_INFO_ID |
| HRC_DL_ROLLBACK_LINES_U1 | Unique | Default | ROLLBACK_LINES_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
