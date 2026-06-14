# PAY_POPULATION_RANGES

This table contains ranges of people to be inserted as assignment actions, used to manage parallel running of payroll processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypopulationranges-30175.html#paypopulationranges-30175](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypopulationranges-30175.html#paypopulationranges-30175)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_POPULATION_RANGES_PK | PAYROLL_ACTION_ID, CHUNK_NUMBER, SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| CHUNK_NUMBER | NUMBER |  | 18 | Yes | CHUNK_NUMBER |
| RANGE_STATUS | VARCHAR2 | 1 |  | Yes | RANGE_STATUS |
| RAND_CHUNK_NUMBER | NUMBER |  | 18 |  | RAND_CHUNK_NUMBER |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_POPULATION_RANGES_N1 | Non Unique | Default | PAYROLL_ACTION_ID, RANGE_STATUS |
| PAY_POPULATION_RANGES_PK | Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER, SOURCE_ID |
| PAY_POPULATION_RANGES_UK1 | Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER, SOURCE_ID, PERSON_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
