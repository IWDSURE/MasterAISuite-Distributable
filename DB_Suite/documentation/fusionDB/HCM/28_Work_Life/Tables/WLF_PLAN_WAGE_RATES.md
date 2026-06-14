# WLF_PLAN_WAGE_RATES

Table to store information on learner wage rate and currency

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfplanwagerates-20073.html#wlfplanwagerates-20073](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfplanwagerates-20073.html#wlfplanwagerates-20073)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PLAN_WAGE_RATES_PK | PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | This indicates  person Id of a learner. |
| WAGE_RATE | NUMBER |  |  |  | This indicates the Wage Rate for a Learner. |
| WAGE_RATE_CURRENCY | VARCHAR2 | 30 |  |  | Currency for Wage Rate for a Learner |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PLAN_WAGE_RATES_U1 | Unique | Default | PERSON_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
