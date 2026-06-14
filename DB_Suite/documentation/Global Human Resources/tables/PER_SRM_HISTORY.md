# PER_SRM_HISTORY

The table stores the role hierarchy changes processed by Generate Role Hierarchy process in policy store.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persrmhistory-6016.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persrmhistory-6016.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SRM_HISTORY_PK | SRM_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SRM_HISTORY_ID | NUMBER |  | 38 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 38 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SRM_RUN_ID | NUMBER |  | 18 | Yes | SRM_RUN_ID |
| MEMBERSHIP_ID | NUMBER |  | 18 | Yes | MEMBERSHIP_ID |
| IMPLEMENTED_FLAG | VARCHAR2 | 30 |  | Yes | IMPLEMENTED_FLAG |
| APP_NAME | VARCHAR2 | 64 |  |  | APP_NAME |
| STATUS | VARCHAR2 | 64 |  |  | STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SRM_HISTORY_N1 | Non Unique | Default | MEMBERSHIP_ID |
| PER_SRM_HISTORY_N2 | Non Unique | Default | SRM_RUN_ID |
| PER_SRM_HISTORY_PK | Unique | Default | SRM_HISTORY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
