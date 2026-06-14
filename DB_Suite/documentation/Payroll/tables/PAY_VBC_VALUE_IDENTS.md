# PAY_VBC_VALUE_IDENTS

This table contains the definitions of Values in Value By Criteria.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvbcvalueidents-16851.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvbcvalueidents-16851.html)

## Primary Key

| Name | Columns |
|------|----------|
| pay_vbc_value_idents_PK | VBC_VALUE_IDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VBC_VALUE_IDENT_ID | NUMBER |  | 18 | Yes | VBC_VALUE_IDENT_ID |
| VBC_DEFINITION_ID | NUMBER |  | 18 | Yes | VBC_DEFINITION_ID |
| BASE_NAME | VARCHAR2 | 30 |  | Yes | BASE_NAME |
| ALLOW_RANGE | VARCHAR2 | 30 |  | Yes | ALLOW_RANGE |
| CALC_TYPE_ID | NUMBER |  | 18 | Yes | CALC_TYPE_ID |
| REQUIRED_FLAG | VARCHAR2 | 30 |  | Yes | REQUIRED_FLAG |
| ENTERABLE_FLAG | VARCHAR2 | 30 |  | Yes | ENTERABLE_FLAG |
| FLEXIBLE_FLAG | VARCHAR2 | 30 |  | Yes | FLEXIBLE_FLAG |
| VBC_CRITERIA_ID | NUMBER |  | 18 |  | VBC_CRITERIA_ID |
| DATE_MODE | VARCHAR2 | 5 |  |  | DATE_MODE |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | Currency Code |
| UOM | VARCHAR2 | 30 |  |  | Unit of Measure |
| PERIODICITY | VARCHAR2 | 30 |  |  | Periodicity |
| PERIODICITY_TYPE | VARCHAR2 | 5 |  |  | Periodicity Type |
| VALUE_SET_CODE | VARCHAR2 | 200 |  |  | VALUE_SET_ID |
| VALUE_SET_CODE2 | VARCHAR2 | 200 |  |  | VALUE_SET_CODE2 |
| VALUE_SET_CODE3 | VARCHAR2 | 200 |  |  | VALUE_SET_CODE3 |
| VO_NAME | VARCHAR2 | 100 |  |  | VO_NAME |
| VO_NAME2 | VARCHAR2 | 100 |  |  | VO_NAME2 |
| VO_NAME3 | VARCHAR2 | 100 |  |  | VO_NAME3 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
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
| PAY_VBC_VALUE_IDENTS_N20 | Non Unique | Default | SGUID |
| PAY_VBC_VALUE_INDENTS_PK | Unique | Default | VBC_VALUE_IDENT_ID, ORA_SEED_SET1 |
| PAY_VBC_VALUE_INDENTS_PK1 | Unique | Default | VBC_VALUE_IDENT_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
