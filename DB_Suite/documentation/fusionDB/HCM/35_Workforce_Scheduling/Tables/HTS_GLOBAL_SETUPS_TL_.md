# HTS_GLOBAL_SETUPS_TL_

Table containing  translatable name and description of  Schedule Global Setup Options.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupstl-28455.html#htsglobalsetupstl-28455](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupstl-28455.html#htsglobalsetupstl-28455)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_GLOBAL_SETUPS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SETUP_PARAM_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PARAM_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Global Setup Options |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Standard Enterprise Identifier column for multi tenancy support |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PARAMETER_NAME | VARCHAR2 | 250 |  |  | Parameter Name |
| PARAMETER_DESCRIPTION | VARCHAR2 | 1000 |  |  | Parameter description |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_GLOBAL_SETUPS_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SETUP_PARAM_ID, LANGUAGE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
