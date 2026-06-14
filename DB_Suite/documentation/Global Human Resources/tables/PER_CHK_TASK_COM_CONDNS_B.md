# PER_CHK_TASK_COM_CONDNS_B

Table to store completion conditions for a task

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchktaskcomcondnsb-15682.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchktaskcomcondnsb-15682.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_TASK_COM_CONDNS_B_PK | TASK_COM_CONDITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_COM_CONDITION_ID | NUMBER |  | 18 | Yes | TASK_COM_CONDITION_ID |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | TASK_IN_CHECKLIST_ID |
| BUSINESS_OBJECT_NAME | VARCHAR2 | 120 |  | Yes | BUSINESS_OBJECT_NAME |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | ENABLED_FLAG |
| BUSINESS_OBJECT_CRITERIA1 | VARCHAR2 | 4000 |  |  | BUSINESS_OBJECT_CRITERIA1 |
| BUSINESS_OBJECT_CRITERIA2 | VARCHAR2 | 4000 |  |  | BUSINESS_OBJECT_CRITERIA2 |
| BUSINESS_OBJECT_CRITERIA3 | VARCHAR2 | 4000 |  |  | BUSINESS_OBJECT_CRITERIA3 |
| BUSINESS_OBJECT_CRITERIA4 | VARCHAR2 | 4000 |  |  | BUSINESS_OBJECT_CRITERIA4 |
| BUSINESS_OBJECT_CRITERIA5 | VARCHAR2 | 4000 |  |  | BUSINESS_OBJECT_CRITERIA5 |
| ROW_COUNT_LOWER_LIMIT | NUMBER |  | 5 |  | ROW_COUNT_LOWER_LIMIT |
| ROW_COUNT_UPPER_LIMIT | NUMBER |  | 5 |  | ROW_COUNT_UPPER_LIMIT |
| PERSON_CRITERIA1 | VARCHAR2 | 4000 |  |  | PERSON_CRITERIA1 |
| PERSON_CRITERIA2 | VARCHAR2 | 4000 |  |  | PERSON_CRITERIA2 |
| PERSON_CRITERIA3 | VARCHAR2 | 4000 |  |  | PERSON_CRITERIA3 |
| PERSON_CRITERIA4 | VARCHAR2 | 4000 |  |  | PERSON_CRITERIA4 |
| PERSON_CRITERIA5 | VARCHAR2 | 4000 |  |  | PERSON_CRITERIA5 |
| PERSON_RULE_ID | NUMBER |  | 18 |  | PERSON_RULE_ID |
| OBJECT_RULE_ID | NUMBER |  | 18 |  | OBJECT_RULE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHK_TASK_COM_CONDNS_B_PK | Unique | Default | TASK_COM_CONDITION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
