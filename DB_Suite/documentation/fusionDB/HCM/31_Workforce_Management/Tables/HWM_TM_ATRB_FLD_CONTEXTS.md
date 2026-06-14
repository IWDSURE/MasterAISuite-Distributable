# HWM_TM_ATRB_FLD_CONTEXTS

A new table to store all contexts of data dictionary attributes.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldcontexts-20077.html#hwmtmatrbfldcontexts-20077](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmatrbfldcontexts-20077.html#hwmtmatrbfldcontexts-20077)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_ATRB_FLD_CONTEXTS_PK | TM_ATRB_FLD_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_ATRB_FLD_CONTEXT_ID | NUMBER |  | 18 | Yes | Primary key of the Time Attribute Field Contexts. |
| CXT_CODE | VARCHAR2 | 64 |  |  | Name of application that uses attributes (like TimeCardFields, TimeCategory etc) |
| CXT_CATEGORY | VARCHAR2 | 64 |  |  | This could be used to group multiple contexts |
| FILTER_ATTRIBUTES | VARCHAR2 | 1 |  | Yes | This is to specify if we need to filter attributes for this consumer or not. Default is N |
| USAGE_METHOD | VARCHAR2 | 64 |  |  | This is a function that can be called to create Usages at runtime. The idea is to allow consumers to define their own function/logic to create usage for new attributes |
| DEFAULT_NAME | VARCHAR2 | 64 |  |  | We could support some default naming convention for a consumer( something like camelCase, UpperCamelCase etc ) |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_ATRB_FLD_CONTEXTS_N20 | Non Unique | Default | SGUID |
| HWM_TM_ATRB_FLD_CONTEXTS_U1 | Unique | Default | TM_ATRB_FLD_CONTEXT_ID, ORA_SEED_SET1 |
| HWM_TM_ATRB_FLD_CONTEXTS_U11 | Unique | Default | TM_ATRB_FLD_CONTEXT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
