# PAY_VBC_CRITERIA_DEFS

This table holds the definition of Criteria in Value by Criteria.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvbccriteriadefs-12160.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvbccriteriadefs-12160.html)

## Primary Key

| Name | Columns |
|------|----------|
| pay_vbc_criteria_defs_PK | VBC_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VBC_CRITERIA_ID | NUMBER |  | 18 | Yes | VBC_CRITERIA_ID |
| VBC_DEFINITION_ID | NUMBER |  | 18 | Yes | VBC_DEFINITION_ID |
| BASE_NAME | VARCHAR2 | 120 |  | Yes | BASE_NAME |
| CRITERIA_TYPE | VARCHAR2 | 30 |  | Yes | CRITERIA_TYPE |
| CRITERIA_ID | NUMBER |  | 18 | Yes | CRITERIA_ID |
| DEFAULT_ALLOWED | VARCHAR2 | 30 |  | Yes | DEFAULT_ALLOWED |
| FLEXIBLE_FLAG | VARCHAR2 | 30 |  | Yes | FLEXIBILE_FLAG |
| EXPRESSION | VARCHAR2 | 30 |  | Yes | EXPRESSION |
| PARENT_CRITERIA_DEF_ID | NUMBER |  | 18 |  | PARENT_CRITERIA_DEF_ID |
| VALUE_SET_CODE | VARCHAR2 | 200 |  |  | VALUE_SET_CODE |
| VO_NAME | VARCHAR2 | 100 |  |  | VO_NAME |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_VBC_CRITERIA_DEFS_N20 | Non Unique | Default | SGUID |
| PAY_VBC_CRITERIA_DEFS_PK | Unique | Default | VBC_CRITERIA_ID, ORA_SEED_SET1 |
| PAY_VBC_CRITERIA_DEFS_PK1 | Unique | Default | VBC_CRITERIA_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
