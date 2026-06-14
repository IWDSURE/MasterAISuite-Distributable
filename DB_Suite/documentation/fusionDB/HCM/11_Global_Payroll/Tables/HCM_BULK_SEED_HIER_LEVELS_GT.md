# HCM_BULK_SEED_HIER_LEVELS_GT

Global Temporary Table used during bulk seed SQL processing. Oracle internal use only.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hcmbulkseedhierlevelsgt-15698.html#hcmbulkseedhierlevelsgt-15698](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hcmbulkseedhierlevelsgt-15698.html#hcmbulkseedhierlevelsgt-15698)

## Primary Key

| Name | Columns |
|------|----------|
| HCM_BULK_SEED_HIER_LEVEL_PK | TABLE_NAME, SEED_SKID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TABLE_NAME | VARCHAR2 | 30 |  | Yes | Table name. Oracle internal use only. |
| FUSION_SKID | NUMBER |  | 18 |  | Fusion Surrogate Key Id |
| SEED_SKID | NUMBER |  | 18 | Yes | The FUSION_SEED surrogate key identifier. Oracle internal use only. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| LEVEL_NUMBER | NUMBER |  | 5 |  | The dependency level of the row. Oracle internal use only. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| HCM_BULK_SEED_HIER_LEVEL_PK | Unique | TABLE_NAME, SEED_SKID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
