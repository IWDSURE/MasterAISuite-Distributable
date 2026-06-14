# CMP_TCS_ALL_OBJECTS_IN_CAT

Setup table that stores informtion of each column in a category

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsallobjectsincat-23489.html#cmptcsallobjectsincat-23489](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsallobjectsincat-23489.html#cmptcsallobjectsincat-23489)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ALL_OBJECTS_IN_CA_PK | ALL_OBJECTS_IN_CAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALL_OBJECTS_IN_CAT_ID | NUMBER |  | 18 | Yes | System generated primary key
                                               column. |
| CAT_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_CAT |
| ITEM_ID | NUMBER |  | 18 |  | Compensation item present in the
                                               category. |
| COL_IN_CAT_ID | NUMBER |  | 18 | Yes | Foreign Key to CMP_TCS_COL_IN_CAT |
| ROW_IN_CAT_ID | NUMBER |  | 18 | Yes | Foreign Key to CMP_TCS_ROW_IN_CAT |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_ALL_OBJECTS_IN_CAT_N1 | Non Unique | Default | ROW_IN_CAT_ID, ITEM_ID |
| CMP_TCS_ALL_OBJ_IN_CAT_FK1 | Non Unique | Default | ITEM_ID |
| CMP_TCS_ALL_OBJ_IN_CAT_FK2 | Non Unique | Default | CAT_ID |
| CMP_TCS_ALL_OBJ_IN_CAT_PK | Unique | Default | ALL_OBJECTS_IN_CAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
