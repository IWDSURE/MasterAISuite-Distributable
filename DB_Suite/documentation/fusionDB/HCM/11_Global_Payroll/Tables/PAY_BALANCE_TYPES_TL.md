# PAY_BALANCE_TYPES_TL

This table contains translated information for PAY_BALANCE_TYPES.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancetypestl-28368.html#paybalancetypestl-28368](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancetypestl-28368.html#paybalancetypestl-28368)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_TYPES_TL_PK | BALANCE_TYPE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BALANCE_TYPE_ID | NUMBER |  | 18 | Yes | System-generated primary key column from PAY_BALANCE_TYPES. |
| BALANCE_NAME | VARCHAR2 | 120 |  | Yes | Translated user name of balance. |
| REPORTING_NAME | VARCHAR2 | 120 |  |  | Tanslated user name for reporting purposes. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of the Balance Type. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BALANCE_TYPES_TL_N2 | Non Unique | Default | BALANCE_NAME, LANGUAGE |
| PAY_BALANCE_TYPES_TL_N3 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_BALANCE_TYPES_TL_N4 | Non Unique | Default | UPPER("BALANCE_NAME") |
| PAY_BALANCE_TYPES_TL_PK | Unique | Default | BALANCE_TYPE_ID, LANGUAGE, ORA_SEED_SET1 |
| PAY_BALANCE_TYPES_TL_PK1 | Unique | Default | BALANCE_TYPE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
