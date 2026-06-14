# PER_AOR_TEMPLATE_CRITERIA

Stores criteria associated to AoR Template Records. Records stored are Non-Date Effective records.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraortemplatecriteria-14683.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraortemplatecriteria-14683.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_TEMPLATE_CRITERIA_PK | TEMPLATE_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_CRITERIA_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign key to template table PER_AOR_TEMPLATE |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Stores single value of legal employers for which this criteria applies. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Stores single value of country for which this criteria applies |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | Stores single value of system person type for which this criteria applies |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Stores single value of job function code for which this criteria applies |
| BUSINESS_UNIT_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for business units separated by ',' for which this criteria applies |
| LOCATION_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for locations separated by ',' for which this criteria applies |
| DEPARTMENT_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for departments separated by ',' for which this criteria applies |
| JOB_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for jobs separated by ',' for which this criteria applies |
| POSITION_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for positions separated by ',' for which this criteria applies |
| ROLE_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for roles separated by ',' for which this criteria applies |
| JOB_FAMILY_IDS | VARCHAR2 | 4000 |  |  | Stores multiple values for job family ids separated by ',' for which this criteria applies |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_AOR_TEMPLATE_CRITERIA_PK | Unique | Default | TEMPLATE_CRITERIA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
