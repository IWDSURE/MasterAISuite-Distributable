# PER_SENIORITY_HOURS

This is transactional table for storing seniority hours from Payroll or OTL.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perseniorityhours-26934.html#perseniorityhours-26934](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perseniorityhours-26934.html#perseniorityhours-26934)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SENIORITY_HOURS_PK | SENIORITY_HOUR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SENIORITY_HOUR_ID | NUMBER |  | 18 | Yes | Primary Key of SeniorityHours | Active |
| FROM_DATE | DATE |  |  | Yes | Date from which this record is valid | Active |
| TO_DATE | DATE |  |  | Yes | Date to which this record is valid | Active |
| HOURS | NUMBER |  | 18 | Yes | Number of hours recorded from external data source | Active |
| BASE_HOURS | NUMBER |  | 18 |  | First loaded value of Hours retained on change of hours | Active |
| SOURCE | VARCHAR2 | 20 |  | Yes | Data source if this record. For example HDL | Active |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Reference to the parent Assignment record | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Reference to the parent Person record | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business group refernce of the parent enterpirse | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VESION_NUMBER | NUMBER |  | 9 | Yes | Mandatory column to track changes of the physical record | Active |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | Reference to the parent Period Of Service record | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_SENIORITY_HOURS_U1 | Unique | FUSION_TS_TX_IDX | SENIORITY_HOUR_ID | Active |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
