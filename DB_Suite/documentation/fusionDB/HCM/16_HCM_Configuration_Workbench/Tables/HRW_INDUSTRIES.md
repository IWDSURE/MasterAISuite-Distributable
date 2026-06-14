# HRW_INDUSTRIES

Table contains seeded industry list

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwindustries-22208.html#hrwindustries-22208](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwindustries-22208.html#hrwindustries-22208)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_INDUSTRIES_PK | CODE |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| CODE | VARCHAR2 | 20 | Yes | CODE |
| GROUP_CODE | VARCHAR2 | 20 |  | GROUP_CODE |
| DEFAULT_ADVICE | VARCHAR2 | 20 |  | DEFAULT_ADVICE |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_INDUSTRIES_U1 | Unique | Default | CODE, ORA_SEED_SET1 |
| HRW_INDUSTRIES_U11 | Unique | Default | CODE, ORA_SEED_SET2 |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
