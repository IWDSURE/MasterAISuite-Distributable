# PAY_ANA_COST_RESULTS

This table contains payroll cost results analytics transactional data.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** pay_ana_cost_results

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payanacostresults-8836.html#payanacostresults-8836](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payanacostresults-8836.html#payanacostresults-8836)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ANA_COST_RESULTS_PK | PAY_ANA_COST_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_ANA_COST_RESULT_ID | NUMBER |  | 18 | Yes | PAY_ANA_COST_RESULT_ID |
| RESULT_LEVEL | VARCHAR2 | 128 |  | Yes | RESULT_LEVEL |
| LEVEL_ID | NUMBER | 18 |  | Yes | LEVEL_ID |
| BASE_CLASSIFICATION_ID | NUMBER |  | 18 |  | BASE_CLASSIFICATION_ID |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_ACTION_ID |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_REL_ACTION_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| STATUS | VARCHAR2 | 32 |  |  | STATUS |
| COSTED_VALUE | NUMBER |  |  |  | COSTED_VALUE |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | CURRENCY_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ANA_COST_RESULTS_PK | Unique | Default | PAY_ANA_COST_RESULT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
