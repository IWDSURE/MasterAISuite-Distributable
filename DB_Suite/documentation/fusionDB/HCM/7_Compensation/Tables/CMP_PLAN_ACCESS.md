# CMP_PLAN_ACCESS

Stores function security information for a plan.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanaccess-21392.html#cmpplanaccess-21392](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanaccess-21392.html#cmpplanaccess-21392)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLAN_ACCESS_PK | PLAN_ACCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ACCESS_ID | NUMBER |  | 18 | Yes | PLAN_ACCESS_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ROLE_TYPE | VARCHAR2 | 1 |  |  | ROLE_TYPE |
| COMP_TYPE | VARCHAR2 | 30 |  |  | COMP_TYPE |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| ACTION_TYPE_ID | NUMBER |  | 18 |  | ACTION_TYPE_ID |
| ROLE_GUID | VARCHAR2 | 64 |  |  | ROLE_GUID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| CUSTOM_ID | NUMBER |  | 18 |  | CUSTOM_ID |
| ACCESS_CODE | VARCHAR2 | 30 |  |  | ACCESS_CODE |
| INSERT_ACCESS_CODE | VARCHAR2 | 30 |  |  | INSERT_ACCESS_CODE |
| UPDATE_ACCESS_CODE | VARCHAR2 | 30 |  |  | UPDATE_ACCESS_CODE |
| EXIT_ACCESS_CODE | VARCHAR2 | 30 |  |  | EXIT_ACCESS_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLAN_ACCESS_N1 | Non Unique | FUSION_TS_TX_DATA | PLAN_ID, ACTION_ID |
| CMP_PLAN_ACCESS_N2 | Non Unique | FUSION_TS_TX_DATA | PLAN_ID, ROLE_GUID |
| CMP_PLAN_ACCESS_N3 | Non Unique | Default | CUSTOM_ID |
| CMP_PLAN_ACCESS_PK | Unique | FUSION_TS_TX_DATA | PLAN_ACCESS_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
