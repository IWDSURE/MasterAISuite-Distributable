# PER_SENIORITY_DATES_SETUP

This table stores the configuration for the Seniority Items. Whenever the user creates the new Seniority Item then a new  record will be created in this table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persenioritydatessetup-12735.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persenioritydatessetup-12735.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SENIORITY_DATES_SETUP_PK | SENIORITY_DATE_SETUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SENIORITY_DATE_SETUP_ID | NUMBER |  | 18 | Yes | SENIORITY_DATE_SETUP_ID |
| SENIORITY_DATE_CODE | VARCHAR2 | 32 |  |  | SENIORITY_DATE_CODE |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | LEVEL_CODE |
| ALLOW_EDIT_FLAG | VARCHAR2 | 3 |  |  | ALLOW_EDIT_FLAG |
| OBJECT | VARCHAR2 | 30 |  |  | OBJECT |
| TRIGGERING_FIELD | VARCHAR2 | 30 |  |  | TRIGGERING_FIELD |
| TRIGGERING_FIELD_TYPE | VARCHAR2 | 30 |  |  | TRIGGERING_FIELD_TYPE |
| SOURCE_FIELD | VARCHAR2 | 30 |  |  | SOURCE_FIELD |
| ACTIVE_FLAG | VARCHAR2 | 3 |  |  | ACTIVE_FLAG |
| WORKER_TYPE | VARCHAR2 | 200 |  |  | WORKER_TYPE |
| LEGISLATION_CODE | VARCHAR2 | 200 |  |  | LEGISLATION_CODE |
| ACTION_TYPE_CODE | VARCHAR2 | 200 |  |  | ACTION_TYPE_CODE |
| ACTION_CODE | VARCHAR2 | 200 |  |  | ACTION_CODE |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 200 |  |  | SYSTEM_PERSON_TYPE |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 |  | COLLECTIVE_AGREEMENT_ID |
| BARGAINING_UNIT_CODE | VARCHAR2 | 200 |  |  | BARGAINING_UNIT_CODE |
| LENGTH_OF_SERVICE_FORMULA | VARCHAR2 | 500 |  |  | LENGTH_OF_SERVICE_FORMULA |
| HOURS_IN_DAY | NUMBER |  | 18 | Yes | Used for conversion from hours to days and vice versa. It represents number of hours in a day. |
| HOURS_IN_MONTH | NUMBER |  | 18 | Yes | Used for conversion from hours to days and vice versa. It represents number of hours in a month. |
| HOURS_IN_YEAR | NUMBER |  | 18 | Yes | Used for conversion from hours to days and vice versa. It represents number of hours in a year. |
| CONVERSION_FF_ID | NUMBER |  | 18 |  | Used for conversion from hours to days and vice versa. It represents conversion fast formula id. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CUMULATIVE_FLAG | VARCHAR2 | 30 |  |  | CUMULATIVE_FLAG |
| DISPLAY_IN_UI | VARCHAR2 | 30 |  |  | DISPLAY_IN_UI |
| RECORD_CREATOR | VARCHAR2 | 30 |  |  | RECORD_CREATOR |
| SENIORITY_VERSION | VARCHAR2 | 30 |  |  | SENIORITY_VERSION |
| UNION_ID | NUMBER |  | 18 |  | UNION_ID |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |
| SETUP_SENIORITY_BASIS | VARCHAR2 | 30 |  | Yes | SETUP_SENIORITY_BASIS |
| LABOUR_UNION_MEMBER_FLAG | VARCHAR2 | 30 |  |  | LABOUR_UNION_MEMBER_FLAG |
| SELECT_WORKER_TYPE | VARCHAR2 | 500 |  |  | SELECT_WORKER_TYPE |
| SELECT_LEGISLATION_CODE | VARCHAR2 | 500 |  |  | SELECT_LEGISLATION_CODE |
| SELECT_UNION_NAME | VARCHAR2 | 1000 |  |  | SELECT_UNION_NAME |
| SELECT_LEGAL_EMPLOYER_NAME | VARCHAR2 | 1000 |  |  | SELECT_LEGAL_EMPLOYER_NAME |
| SELECT_COLL_AGREEMENT_NAME | VARCHAR2 | 1000 |  |  | SELECT_COLL_AGREEMENT_NAME |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PSDS_U1 | Unique | Default | SENIORITY_DATE_SETUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
