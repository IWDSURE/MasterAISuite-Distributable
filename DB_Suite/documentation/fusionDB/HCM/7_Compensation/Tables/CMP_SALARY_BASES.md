# CMP_SALARY_BASES

Salary Basis is the entity that establishes the period of time for which an employee's salary is quoted, typically either Monthly, Hourly or Annually. Salary Basis also allows a link to a payroll element or a link to a Grade Rate.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybases-19509.html#cmpsalarybases-19509](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarybases-19509.html#cmpsalarybases-19509)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_BASES_PK | SALARY_BASIS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| SALARY_BASIS_ID | NUMBER |  | 18 | Yes | SALARY_BASIS_ID |  |
| ANNUAL_ROUNDING_CODE | VARCHAR2 | 30 |  |  | ANNUAL_ROUNDING_CODE |  |
| RANGE_ROUNDING_CODE | VARCHAR2 | 30 |  |  | RANGE_ROUNDING_CODE |  |
| RANGE_DIFF_METHOD | VARCHAR2 | 30 |  |  | RANGE_DIFF_METHOD |  |
| RANGE_DIFF_ID | NUMBER |  | 18 |  | RANGE_DIFF_ID |  |
| COMPONENT_USAGE | VARCHAR2 | 30 |  |  | COMPONENT_USAGE |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| NAME | VARCHAR2 | 80 |  | Yes | NAME |  |
| SALARY_BASIS_CODE | VARCHAR2 | 30 |  |  | SALARY_BASIS_CODE |  |
| ANNUALIZED_HOURS | NUMBER |  |  |  | ANNUALIZED_HOURS |  |
| AMOUNT_DECIMAL_PRECISION | NUMBER |  |  |  | AMOUNT_DECIMAL_PRECISION |  |
| RANGE_ERROR_WARNING | VARCHAR2 | 30 |  |  | RANGE_ERROR_WARNING |  |
| ELEMENT_ENTRY_VALIDATION | VARCHAR2 | 30 |  |  | ELEMENT_ENTRY_VALIDATION |  |
| SALARY_ANNUALIZATION_FACTOR | NUMBER |  |  |  | SALARY_ANNUALIZATION_FACTOR |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |  |
| GRADE_RATE_BASIS_CODE | VARCHAR2 | 30 |  |  | GRADE_RATE_BASIS_CODE |  |
| GRADE_RATE_ID | NUMBER |  | 18 |  | GRADE_RATE_ID |  |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |  |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |  |
| GRADE_ANNUALIZATION_FACTOR | NUMBER |  |  |  | GRADE_ANNUALIZATION_FACTOR |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |  |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |  |
| AMOUNT_ROUNDING_CODE | VARCHAR2 | 30 |  |  | AMOUNT_ROUNDING_CODE |  |
| AVAILABLE_FROM_DATE | DATE |  |  |  | AVAILABLE_FROM_DATE |  |
| CODE | VARCHAR2 | 80 |  |  | CODE |  |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |  |
| DEFAULT_TYPE | VARCHAR2 | 30 |  |  | DEFAULT_TYPE |  |
| DEFAULT_SOURCE | VARCHAR2 | 30 |  |  | DEFAULT_SOURCE |  |
| DEFAULT_GRADE_RATE_ID | NUMBER |  | 18 |  | DEFAULT_GRADE_RATE_ID |  |
| DEFAULT_AMOUNT | NUMBER |  |  |  | DEFAULT_AMOUNT |  |
| DEFAULT_FORMULA_ID | NUMBER |  | 18 |  | DEFAULT_FORMULA_ID |  |
| SALARY_RANGE_SCALE | NUMBER |  | 3 |  | SALARY_RANGE_SCALE |  |
| RANGE_POSITION_SCALE | NUMBER |  | 3 |  | RANGE_POSITION_SCALE |  |
| COMPA_RATIO_FORMAT | VARCHAR2 | 30 |  |  | COMPA_RATIO_FORMAT |  |
| RANGE_ANALYTICS_FOR_EMP | VARCHAR2 | 1 |  |  | RANGE_ANALYTICS_FOR_EMP |  |
| RANGE_ANALYTICS_FOR_MGR | VARCHAR2 | 1 |  |  | RANGE_ANALYTICS_FOR_MGR |  |
| DISABLE_QUARTILE | VARCHAR2 | 1 |  |  | DISABLE_QUARTILE |  |
| DISABLE_QUINTILE | VARCHAR2 | 1 |  |  | DISABLE_QUINTILE |  |
| DISABLE_COMPA_RATIO | VARCHAR2 | 1 |  |  | DISABLE_COMPA_RATIO |  |
| DISABLE_RANGE_POSITION | VARCHAR2 | 1 |  |  | DISABLE_RANGE_POSITION |  |
| CALCULATION_MODE | VARCHAR2 | 30 |  |  | CALCULATION_MODE |  |
| FTE_IMPACT | VARCHAR2 | 30 |  |  | FTE_IMPACT |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Basis Information (CMP_SALARY_BASES) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_BASES_PK | Unique | Default | SALARY_BASIS_ID |
| CMP_SALARY_BASES_U1 | Unique | Default | NAME, BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
