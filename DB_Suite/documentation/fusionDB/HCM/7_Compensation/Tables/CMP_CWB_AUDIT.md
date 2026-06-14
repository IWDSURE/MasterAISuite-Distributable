# CMP_CWB_AUDIT

Stores audit data for changes made to a person's compensation such as their rating or allocation amount.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbaudit-27391.html#cmpcwbaudit-27391](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbaudit-27391.html#cmpcwbaudit-27391)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_AUDIT_PK | AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| AUDIT_ID | NUMBER |  | 18 | Yes | AUDIT_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |  |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |  |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |  |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |  |
| POOL_ID | NUMBER |  | 18 |  | POOL_ID |  |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_NAME |  |
| OLD_VAL_VARCHAR | VARCHAR2 | 200 |  |  | OLD_VAL_VARCHAR | Active |
| NEW_VAL_VARCHAR | VARCHAR2 | 200 |  |  | NEW_VAL_VARCHAR | Active |
| OLD_VAL_NUMBER | NUMBER |  |  |  | OLD_VAL_NUMBER | Active |
| NEW_VAL_NUMBER | NUMBER |  |  |  | NEW_VAL_NUMBER | Active |
| OLD_VAL_DATE | DATE |  |  |  | OLD_VAL_DATE | Active |
| NEW_VAL_DATE | DATE |  |  |  | NEW_VAL_DATE | Active |
| SUPPORTING_INFORMATION | VARCHAR2 | 200 |  |  | SUPPORTING_INFORMATION | Active |
| AUDIT_DATE | TIMESTAMP |  |  |  | AUDIT_DATE |  |
| CHANGE_MADE_BY_PERSON_ID | NUMBER |  | 18 |  | CHANGE_MADE_BY_PERSON_ID | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| EXTERNAL_WORKER_DATA_ID | NUMBER |  | 18 |  | EXTERNAL_WORKER_DATA_ID |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_AUDIT_N1 | Non Unique | Default | PERSON_EVENT_ID |
| CMP_CWB_AUDIT_N2 | Non Unique | Default | PERIOD_ID, PLAN_ID |
| CMP_CWB_AUDIT_N3 | Non Unique | Default | COMPONENT_ID |
| CMP_CWB_AUDIT_N4 | Non Unique | Default | POOL_ID |
| CMP_CWB_AUDIT_N5 | Non Unique | Default | CHANGE_MADE_BY_PERSON_ID |
| CMP_CWB_AUDIT_PK | Unique | Default | AUDIT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
