# ANC_MX_INPUT_PARAMS

Absence Matrix Input Params Base Table

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancmxinputparams-23906.html#ancmxinputparams-23906](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancmxinputparams-23906.html#ancmxinputparams-23906)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_MX_INPUT_PARAMS_PK | MX_INPUT_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MX_INPUT_PARAM_ID | NUMBER |  | 18 | Yes | Matrix  Input  Input Param |
| INPUT_VALUE | VARCHAR2 | 100 |  | Yes | Matrix  Input  Input Value |
| MATRIX_SOURCE_ID | NUMBER |  | 18 | Yes | Matrix  Input  Source |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ANC_MX_INPUT_PARAMS_ALTCD | VARCHAR2 | 240 |  | Yes | ANC_MX_INPUT_PARAMS_ALTCD |
| DATA_TYPE_CD | VARCHAR2 | 30 |  |  | Matrix  Input  Data Type Code |
| INPUT_TYPE_CD | VARCHAR2 | 30 |  | Yes | Matrix  Input  Type Code |
| NODE_GROUP_VALUE | VARCHAR2 | 100 |  | Yes | Matrix  Input  Node Group Value |
| VIEW_OBJECT_NAME | VARCHAR2 | 100 |  |  | Matrix  Input  View Object Name |
| VIEW_CRITERIA_NAME | VARCHAR2 | 100 |  |  | Matrix  Input  View Criteria Name |
| VIEW_ATTRIBUTE_NAME | VARCHAR2 | 100 |  |  | Matrix  Input  View Attribute Name |
| PLSQL_PACKAGE | VARCHAR2 | 100 |  |  | Matrix  Input  PLSQL Package |
| PLSQL_METHOD | VARCHAR2 | 200 |  |  | Matrix  Input  PLSQL Method |
| DERIVED_PARAM_KEY | NUMBER |  | 18 |  | Matrix  Input  Derived Param Key |
| JAVA_CLASS | VARCHAR2 | 240 |  |  | Matrix  Input  Java Class |
| JAVA_METHOD | VARCHAR2 | 200 |  |  | Matrix  Input  Java Method |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LOV_SWITCHER_CD | VARCHAR2 | 30 |  |  | Matrix  Input  LOV Swicher Code |
| LOOKUP_TYPE | VARCHAR2 | 30 |  |  | Matrix  Input  Lookup Type |
| VALUE_SET_ID | NUMBER |  | 18 |  | Matrix  Input  Value Set |
| LOV_SQL | VARCHAR2 | 1000 |  |  | Matrix  Input  List Of Values SQL |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_MX_INPUT_PARAMS_N1 | Non Unique | Default | UPPER("INPUT_VALUE") |
| ANC_MX_INPUT_PARAMS_N2 | Non Unique | Default | UPPER("NODE_GROUP_VALUE") |
| ANC_MX_INPUT_PARAMS_U1 | Unique | Default | MX_INPUT_PARAM_ID, ORA_SEED_SET1 |
| ANC_MX_INPUT_PARAMS_U11 | Unique | Default | MX_INPUT_PARAM_ID, ORA_SEED_SET2 |
| ANC_MX_INPUT_PARAMS_U2 | Unique | Default | INPUT_VALUE, NODE_GROUP_VALUE, ENTERPRISE_ID, ORA_SEED_SET1 |
| ANC_MX_INPUT_PARAMS_U21 | Unique | Default | INPUT_VALUE, NODE_GROUP_VALUE, ENTERPRISE_ID, ORA_SEED_SET2 |
| ANC_MX_INPUT_PARAMS_U3 | Unique | Default | INPUT_VALUE, ENTERPRISE_ID, ORA_SEED_SET1 |
| ANC_MX_INPUT_PARAMS_U31 | Unique | Default | INPUT_VALUE, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
