# HXT_TCLAYFLD_CXT_DEPT

The table HXT_TCLAYFLD_CXT_DEPT table contains the values of the parent LC when the dependent LC should be enabled. This is used to solve the content sensitive dependent LC problem.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayfldcxtdept-11392.html#hxttclayfldcxtdept-11392](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayfldcxtdept-11392.html#hxttclayfldcxtdept-11392)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TCLAYFLD_CXT_DEPT_PK | TCLAYFLD_CXT_DEPT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCLAYFLD_CXT_DEPT_ID | NUMBER |  | 18 | Yes | TCLAYFLD_CXT_DEPT_ID |
| TCLAYFLD_CXT_DEPT_CD | VARCHAR2 | 100 |  |  | TCLAYFLD_CXT_DEPT_CD |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCLAYFLD_DEFNS_ID | NUMBER |  | 18 | Yes | TCLAYFLD_DEFNS_ID |
| TCLAYFLD_VALUE | VARCHAR2 | 150 |  |  | Value of the parent LC |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| USG_TYPE | VARCHAR2 | 50 |  |  | USG_TYPE |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TCLAYFLD_CXT_DEPT_N1 | Non Unique | Default | TCLAYFLD_DEFNS_ID |
| HXT_TCLAYFLD_CXT_DEPT_N20 | Non Unique | Default | SGUID |
| HXT_TCLAYFLD_CXT_DEPT_PK | Unique | Default | TCLAYFLD_CXT_DEPT_ID, ORA_SEED_SET1 |
| HXT_TCLAYFLD_CXT_DEPT_PK1 | Unique | Default | TCLAYFLD_CXT_DEPT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
