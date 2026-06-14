# HR_API_HOOKS

This table contains data sourced from HR core development, legislation
development teams and legislation vertical market groups. It
contains the list of hook points which are available in each API
module. The data in this table must not be updated by customer code.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapihooks-23008.html#hrapihooks-23008](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapihooks-23008.html#hrapihooks-23008)

## Primary Key

| Name | Columns |
|------|----------|
| HR_API_HOOKS_PK | API_HOOK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| API_HOOK_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| API_MODULE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_API_MODULES |
| API_HOOK_TYPE | VARCHAR2 | 30 |  | Yes | Type of hook |
| HOOK_PACKAGE | VARCHAR2 | 30 |  | Yes | Name of the database package which the business process or row handler calls when the hook point is reached. |
| HOOK_PROCEDURE | VARCHAR2 | 30 |  | Yes | Name of the procedure with HOOK_PACKAGE which the business process or row handler calls when the hook point is reached. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Identifies rows created by legislation group/partners or legislation vertical markets. Will be null for all hooks provided by HR development core products. |
| LEGISLATION_PACKAGE | VARCHAR2 | 30 |  |  | Holds the name of the database package to be called, to derive the legislation code, when legislation specific logic exists and p_business_group_id is not a known parameter to the hook package. |
| LEGISLATION_FUNCTION | VARCHAR2 | 30 |  |  | Name of the function, within the database package LEGISLATION_PACKAGE, to call when the legislation code needs to be known. |
| ENCODED_ERROR | VARCHAR2 | 2000 |  |  | Holds the error text in AOL encoded format if the code to call the legislation_procedure or hook_procedure could not be created by the preprocessor. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_API_HOOKS_PK | Unique | Default | API_HOOK_ID, ORA_SEED_SET1 |
| HR_API_HOOKS_PK1 | Unique | Default | API_HOOK_ID, ORA_SEED_SET2 |
| HR_API_HOOKS_U1 | Unique | Default | API_MODULE_ID, API_HOOK_TYPE, ORA_SEED_SET1 |
| HR_API_HOOKS_U11 | Unique | Default | API_MODULE_ID, API_HOOK_TYPE, ORA_SEED_SET2 |
| HR_API_HOOKS_U2 | Unique | Default | HOOK_PACKAGE, HOOK_PROCEDURE, ORA_SEED_SET1 |
| HR_API_HOOKS_U21 | Unique | Default | HOOK_PACKAGE, HOOK_PROCEDURE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
