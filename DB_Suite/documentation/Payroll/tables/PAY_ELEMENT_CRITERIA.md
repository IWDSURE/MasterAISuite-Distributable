# PAY_ELEMENT_CRITERIA

This table contains combinations of eligibility criteria that are referenced by element eligibilty (PAY_ELEMENT_LINKS_F) and payroll relationship, assigned payroll, and payroll assignment records. There is one record for each unique combination (for example a specific PAYROLL_ID and JOB_ID).

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementcriteria-25418.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementcriteria-25418.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_CRITERIA_PK | ELEMENT_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEMENT_CRITERIA_ID | NUMBER |  | 18 | Yes | ELEMENT_CRITERIA_ID |
| LINK_TO_ALL_PAYROLLS_FLAG | VARCHAR2 | 30 |  | Yes | LINK_TO_ALL_PAYROLLS_FLAG |
| CRITERIA_TYPE | VARCHAR2 | 30 |  | Yes | CRITERIA_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LINK_LEVEL | VARCHAR2 | 30 |  |  | LINK_LEVEL |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 |  | COLLECTIVE_AGREEMENT_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 30 |  |  | EMPLOYMENT_CATEGORY |
| PEOPLE_GROUP_ID | NUMBER |  | 18 |  | PEOPLE_GROUP_ID |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |
| RELATIONSHIP_TYPE_ID | NUMBER |  | 18 |  | RELATIONSHIP_TYPE_ID |
| PAYROLL_STAT_UNIT_ID | NUMBER |  | 18 |  | PAYROLL_STAT_UNIT_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| BARGAINING_UNIT_CODE | VARCHAR2 | 30 |  |  | BARGAINING_UNIT_CODE |
| LABOUR_UNION_MEMBER_FLAG | VARCHAR2 | 30 |  |  | LABOUR_UNION_MEMBER_FLAG |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELEMENT_CRITERIA_N2 | Non Unique | Default | JOB_ID, LEGAL_EMPLOYER_ID, PAYROLL_STAT_UNIT_ID, CRITERIA_TYPE |
| PAY_ELEMENT_CRITERIA_N3 | Non Unique | Default | LOCATION_ID, LEGAL_EMPLOYER_ID, PAYROLL_STAT_UNIT_ID |
| PAY_ELEMENT_CRITERIA_N4 | Non Unique | Default | ORGANIZATION_ID, LEGAL_EMPLOYER_ID, PAYROLL_STAT_UNIT_ID |
| PAY_ELEMENT_CRITERIA_PK | Unique | Default | ELEMENT_CRITERIA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
