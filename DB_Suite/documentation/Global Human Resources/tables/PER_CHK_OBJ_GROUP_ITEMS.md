# PER_CHK_OBJ_GROUP_ITEMS

Table to store checklist object group items.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkobjgroupitems-21907.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkobjgroupitems-21907.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_OBJ_GROUP_ITEMS_PK | GROUP_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GROUP_ITEM_ID | NUMBER |  | 18 | Yes | GROUP_ITEM_ID |
| GROUP_ID | NUMBER |  | 18 | Yes | GROUP_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| USER_GUID | VARCHAR2 | 32 |  |  | USER_GUID |
| ITEM_TYPE | VARCHAR2 | 64 |  | Yes | ITEM_TYPE |
| ACTIVE_FLAG | VARCHAR2 | 4 |  | Yes | ACTIVE_FLAG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_OBJ_GROUP_ITEMS_PK | Unique | Default | GROUP_ITEM_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
