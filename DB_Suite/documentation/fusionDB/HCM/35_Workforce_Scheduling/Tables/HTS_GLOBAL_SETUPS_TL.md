# HTS_GLOBAL_SETUPS_TL

Table containing  translatable name and description of  Schedule Global Setup Options.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupstl-24162.html#htsglobalsetupstl-24162](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupstl-24162.html#htsglobalsetupstl-24162)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_GLOBAL_SETUPS_TL_PK | SETUP_PARAM_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PARAM_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Global Setup Options |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PARAMETER_NAME | VARCHAR2 | 250 |  |  | Parameter Name |
| PARAMETER_DESCRIPTION | VARCHAR2 | 1000 |  |  | Parameter description |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_GLOBAL_SETUPS_TL_U3 | Unique | Default | SETUP_PARAM_ID, LANGUAGE, ORA_SEED_SET1 |
| HTS_GLOBAL_SETUPS_TL_U31 | Unique | Default | SETUP_PARAM_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
