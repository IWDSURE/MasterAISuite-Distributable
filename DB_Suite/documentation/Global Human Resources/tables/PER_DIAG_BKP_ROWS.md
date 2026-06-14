# PER_DIAG_BKP_ROWS

Generic backup table for Customer Self Service Data Integrity.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdiagbkprows-11171.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdiagbkprows-11171.html)

## Columns

| Name | Datatype | Length | Precision | Comments |
|---|---|---|---|---|
| TEST_ID | VARCHAR2 | 32 |  | FND test id |
| EXECUTION_ID | VARCHAR2 | 32 |  | FND test execution id |
| RUN_NAME | VARCHAR2 | 240 |  | FND test run name |
| EXECUTION_DATE | TIMESTAMP |  |  | Timestamp when the test was executed |
| EXECUTION_BY | VARCHAR2 | 64 |  | Username of the person who executed the test |
| RUN_STATUS | VARCHAR2 | 32 |  | Status of test execution |
| COMMENTS | VARCHAR2 | 1000 |  | Comments |
| XML_DATA | CLOB |  |  | XML representation of the backup table row |
| OBJECT_NAME | VARCHAR2 | 30 |  | Table name (Index will be created on OBJECT_NAME and SKID) |
| MODULE_ID | VARCHAR2 | 32 |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SKID | NUMBER |  | 18 | SKID to store surrogate key of the transaction table. (Index will be created on OBJECT_NAME and SKID) |
| ENTERPRISE_ID | NUMBER |  | 18 | enterprise id |
| PVAL001 | VARCHAR2 | 240 |  | Additional VARCHAR2 column. Teams can use this columns as per their requirements |
| PVAL002 | VARCHAR2 | 240 |  | Additional VARCHAR2 column. Teams can use this columns as per their requirements |
| PVAL003 | VARCHAR2 | 240 |  | Additional VARCHAR2 column. Teams can use this columns as per their requirements |
| PVAL004 | VARCHAR2 | 240 |  | Additional VARCHAR2 column. Teams can use this columns as per their requirements |
| PVAL005 | VARCHAR2 | 240 |  | Additional VARCHAR2 column. Teams can use this columns as per their requirements |
| PDATE001 | DATE |  |  | Additional DATE column. Teams can use this columns as per their requirements |
| PDATE002 | DATE |  |  | Additional DATE column. Teams can use this columns as per their requirements |
| PDATE003 | DATE |  |  | Additional DATE column. Teams can use this columns as per their requirements |
| PDATE004 | DATE |  |  | Additional DATE column. Teams can use this columns as per their requirements |
| PDATE005 | DATE |  |  | Additional DATE column. Teams can use this columns as per their requirements |
| PNUMBER001 | NUMBER |  | 18 | Additional NUMBER column. Teams can use this columns as per their requirements |
| PNUMBER002 | NUMBER |  | 18 | Additional NUMBER column. Teams can use this columns as per their requirements |
| PNUMBER003 | NUMBER |  | 18 | Additional NUMBER column. Teams can use this columns as per their requirements |
| PNUMBER004 | NUMBER |  | 18 | Additional NUMBER column. Teams can use this columns as per their requirements |
| PNUMBER005 | NUMBER |  | 18 | Additional NUMBER column. Teams can use this columns as per their requirements |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_DIAG_BKP_ROWS_N1 | Non Unique | FUSION_TS_TX_DATA | OBJECT_NAME, SKID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
