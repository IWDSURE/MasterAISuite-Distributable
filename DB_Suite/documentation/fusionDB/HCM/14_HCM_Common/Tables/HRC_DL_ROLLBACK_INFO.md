# HRC_DL_ROLLBACK_INFO

This table will store the information required for Object Roll Back. This will store the object information for each business object in the hierarchy.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrollbackinfo-15386.html#hrcdlrollbackinfo-15386](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrollbackinfo-15386.html#hrcdlrollbackinfo-15386)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ROLLBACK_INFO_PK | ROLLBACK_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLLBACK_INFO_ID | NUMBER |  |  | Yes | ROLLBACK_INFO_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  |  | Yes | DATA_SET_BUS_OBJ_ID |
| LOGICAL_LINE_ID | NUMBER |  |  | Yes | LOGICAL_LINE_ID |
| BUSINESS_OBJECT_ID | NUMBER |  |  |  | BUSINESS_OBJECT_ID |
| TABLE_NAME | VARCHAR2 | 50 |  |  | TABLE_NAME |
| SURROGATE_ID | NUMBER |  |  | Yes | SURROGATE_ID |
| COLUMN_NAME | VARCHAR2 | 100 |  |  | COLUMN_NAME |
| ROLLBACK_FLAG | VARCHAR2 | 30 |  |  | ROLLBACK_FLAG |
| ACTION | VARCHAR2 | 30 |  |  | ACTION |
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
| HRC_DL_ROLLBACK_INFO_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID, LOGICAL_LINE_ID |
| HRC_DL_ROLLBACK_INFO_U1 | Unique | Default | ROLLBACK_INFO_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
