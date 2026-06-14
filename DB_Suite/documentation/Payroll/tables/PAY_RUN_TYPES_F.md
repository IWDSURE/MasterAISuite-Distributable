# PAY_RUN_TYPES_F

The different types of Payroll Run processing

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruntypesf-22567.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruntypesf-22567.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RUN_TYPES_PK | RUN_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_TYPE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BASE_RUN_TYPE_NAME | VARCHAR2 | 80 |  | Yes | BASE_RUN_TYPE_NAME |
| RUN_METHOD | VARCHAR2 | 30 |  | Yes | Run type category, either 'Normal', 'Separate Payment','Process Separately' or 'Cumulative'. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SHORTNAME | VARCHAR2 | 30 |  |  | A shortname or label for the run type. |
| SRS_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate if a run type can be used in Standard Report Submission |
| TRANSIENT_FLAG | VARCHAR2 | 30 |  |  | This indicates that the Run Type is temporary and should not conribute to any balances. |
| ELEMENT_RECOVER_FLAG | VARCHAR2 | 30 |  |  | This indicates that the Run Results need to have recovery Elements created in the current period Earning period. |
| COSTING_FLAG | VARCHAR2 | 30 |  |  | This indicates whether this Run Types results should be included in a Costing. |
| RETROPAY_FLAG | VARCHAR2 | 30 |  |  | This indicates whether any Run, Quickpay or Element Rcovery entries can be used in a Retropay. |
| RETRO_INTERLOCK | VARCHAR2 | 30 |  |  | This indicates a special type of Run that interlocks the Retropay |
| OVERRIDE_SHORTNAME | VARCHAR2 | 30 |  |  | This is the Override Short Name, this name will be used in the standard DBIs if populated. |
| INCLUSION_FLAG | VARCHAR2 | 30 |  |  | INCLUSION_FLAG |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RUN_TYPES_F_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_RUN_TYPES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_RUN_TYPES_F_PK | Unique | Default | RUN_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_RUN_TYPES_F_PK1 | Unique | Default | RUN_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
