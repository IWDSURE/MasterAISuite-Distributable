# PAY_CONSOLIDATION_SETS

This table contains details of groups used to consolidate the results of multiple payroll processes. The consolidation group is used as a parameter to identify the set of results for further processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payconsolidationsets-23306.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payconsolidationsets-23306.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CONSOLIDATION_SETS_PK | CONSOLIDATION_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONSOLIDATION_SET_ID | NUMBER |  | 18 | Yes | Consolidation set primary key. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CONSOLIDATION_SET_NAME | VARCHAR2 | 60 |  | Yes | Consolidation set name. |
| CONSOLIDATION_SET_CODE | VARCHAR2 | 60 |  |  | Consolidation set code. |
| COMMENTS | CLOB |  |  |  | Descriptive information about the consolidation set. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_CONSOLIDATION_SETS_PK | Unique | Default | CONSOLIDATION_SET_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
