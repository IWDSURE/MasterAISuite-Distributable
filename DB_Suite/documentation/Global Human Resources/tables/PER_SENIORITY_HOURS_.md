# PER_SENIORITY_HOURS_

This is transactional table for storing seniority hours from Payroll or OTL.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perseniorityhours-23666.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perseniorityhours-23666.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SENIORITY_HOURS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SENIORITY_HOUR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SENIORITY_HOUR_ID | NUMBER |  | 18 | Yes | SENIORITY_HOUR_ID | Active |
| FROM_DATE | DATE |  |  |  | FROM_DATE | Active |
| TO_DATE | DATE |  |  |  | TO_DATE | Active |
| HOURS | NUMBER |  | 18 |  | HOURS | Active |
| BASE_HOURS | NUMBER |  | 18 |  | BASE_HOURS | Active |
| SOURCE | VARCHAR2 | 20 |  |  | SOURCE | Active |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID | Active |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VESION_NUMBER | NUMBER |  | 9 |  | OBJECT_VESION_NUMBER | Active |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | PERIOD_OF_SERVICE_ID | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. | Active |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. | Active |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SENIORITY_HOURS_U1_ | Unique | FUSION_TS_TX_IDX | LAST_UPDATE_DATE, LAST_UPDATED_BY, SENIORITY_HOUR_ID |
| PSHN1_ | Non Unique | FUSION_TS_TX_IDX | SENIORITY_HOUR_ID, LAST_UPDATE_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
