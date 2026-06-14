# PER_CHK_OBJECT_GROUPS

Table to store checklist object groups.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkobjectgroups-27868.html#perchkobjectgroups-27868](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkobjectgroups-27868.html#perchkobjectgroups-27868)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_OBJECT_GROUPS_PK | GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GROUP_ID | NUMBER |  | 18 | Yes | GROUP_ID |
| GROUP_CODE | VARCHAR2 | 64 |  | Yes | GROUP_CODE |
| GROUP_NAME | VARCHAR2 | 240 |  | Yes | GROUP_NAME |
| GROUP_TYPE | VARCHAR2 | 64 |  | Yes | GROUP_TYPE |
| GROUP_CATEGORY | VARCHAR2 | 64 |  | Yes | GROUP_CATEGORY |
| ACTIVE_FLAG | VARCHAR2 | 4 |  | Yes | ACTIVE_FLAG |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| PARENT_OBJECT_ID | NUMBER |  | 18 |  | PARENT_OBJECT_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_OBJECT_GROUPS_PK | Unique | Default | GROUP_ID |
| PER_CHK_OBJECT_GROUPS_U1 | Unique | Default | PARENT_OBJECT_ID, GROUP_CODE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
