# PER_KEYWORDS

This table is used to save data collected by the keyword search crawler.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perkeywords-27384.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perkeywords-27384.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_KEYWORDS_PK | KEYWORD_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| KEYWORD_ID | NUMBER |  | 18 | Yes | This column stores the keyword id. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | This column stores the Person Identifier. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| LANGUAGE | VARCHAR2 | 30 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| XML_KEYWORDS | CLOB |  |  |  | This is a XML CLOB object to store info about the person to be used in OracleText queries |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_ASSIGNMENTS_M table. |  |
| JOB_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOBS_F table. |  |
| DEPARTMENT_ID | NUMBER |  | 18 |  | This is the department of the  Person's assignment |  |
| PERSON_NAME | VARCHAR2 | 300 |  |  | Name of the person. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_KEYWORDS_N6 | Non Unique | Default | ASSIGNMENT_ID, LANGUAGE |
| PER_KEYWORDS_PK | Unique | Default | KEYWORD_ID, LANGUAGE |
| PER_KEYWORDS_U1 | Unique | Default | PERSON_ID, ASSIGNMENT_ID, LANGUAGE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
