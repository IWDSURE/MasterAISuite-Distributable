# PAY_REPORT_DEFINITIONS

report definition, containing information about mreporting block to be processed

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportdefinitions-21086.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportdefinitions-21086.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REPORT_DEFINITION_PK | REPORT_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPORT_DEFINITION_ID | NUMBER |  | 18 | Yes | REPORT_DEFINITION_ID |
| REPORT_GROUP_ID | NUMBER |  | 18 | Yes | REPORT_GROUP_ID |
| REPORT_NAME | VARCHAR2 | 80 |  | Yes | REPORT_NAME |
| REPORT_TYPE | VARCHAR2 | 30 |  |  | REPORT_TYPE |
| REPORT_BLOCK_ID | NUMBER |  | 18 |  | REPORT_BLOCK_ID |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | EXT_DEFINITION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| APPLICATION_SHORT_NAME | VARCHAR2 | 30 |  |  | APPLICATION_SHORT_NAME |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REPORT_DEFINITIONS_N1 | Non Unique | Default | REPORT_GROUP_ID |
| PAY_REPORT_DEFINITION_PK | Unique | Default | REPORT_DEFINITION_ID, ORA_SEED_SET1 |
| PAY_REPORT_DEFINITION_PK1 | Unique | Default | REPORT_DEFINITION_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
