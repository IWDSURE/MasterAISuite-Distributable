# PER_ASSIGNMENT_EXTENSIONS_F

To Store TaxReportingUnit Data which will be used to by ESS Job to fetch the the data from the Extension table and create/process the Localization records.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentextensionsf-19452.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentextensionsf-19452.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASSIGNMENT_EXTENSIONS_F_PK | ASSIGNMENT_EXTENSION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_EXTENSION_ID | NUMBER |  | 18 | Yes | System-generated primary key column. Surrogate Key  . |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies person holding an assignment or a set of Employment/Placement Terms. |
| LEGISLATION_CODE | VARCHAR2 | 150 |  |  | Legislation code derived from the Legal Entity. Might be null for Applicants. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies an assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |
| TRU_ID | NUMBER |  | 18 | Yes | Tax Reporting Unit Id passed through hdl. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| TRU_PROCESSED_FLAG | VARCHAR2 | 30 |  | Yes | Tax Reporting Unit Processed Flag will be used to validate whether to  process this record by payroll ESS or not |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Stores the ESS process request Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| RECORD_CREATOR | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASSIGNMENT_EXTENSIONS_F_PK | Unique | Default | ASSIGNMENT_EXTENSION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
