# PAY_RATE_DEFINITIONS_F

This table contains the definition of a rate to be used by the rate engine.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratedefinitionsf-18350.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratedefinitionsf-18350.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RATE_DEFINITIONS_F_PK | RATE_DEFINITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RATE_DEFINITION_ID | NUMBER |  | 18 | Yes | Primary Key for the Rate Definition |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SHORT_NAME | VARCHAR2 | 256 |  |  | Short name |
| MANAGEMENT_TYPE_CD | VARCHAR2 | 30 |  |  | MANAGEMENT_TYPE_CD |
| PAY_RATE_DEFINITIONS_F_ALTCD | VARCHAR2 | 240 |  | Yes | PAY_RATE_DEFINITIONS_F_ALTCD |
| STATUS | VARCHAR2 | 30 |  |  | Pay rate status |
| BASE_NAME | VARCHAR2 | 256 |  | Yes | Name of the Rate Definition |
| TYPE | VARCHAR2 | 10 |  | Yes | The Type of Rate Definition, Derived Rate or Rate by Criteria |
| STORAGE_TYPE | VARCHAR2 | 230 |  |  | Storage type: Amount or Percentage |
| PERIODICITY_TYPE | VARCHAR2 | 5 |  |  | This identifies the type of periodicity of the Rate. For example is it Time base in an Annual amount, Monthly Amount, Hourly Amount, etc or is it Unit based, $50 per widget, $15 per meal, etc. |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | DIR_CARD_COMP_DEF_ID |
| VALUE_BY_CRITERIA_ID | NUMBER |  | 18 |  | Foreign Key to the Value by Criteria Definition |
| VBC_VALUE_IDENTIFIER | VARCHAR2 | 30 |  |  | Value Identifier for the leaf node to be used by for the Value by Criteria. |
| CALCULATION_FORMULA_ID | NUMBER |  | 18 |  | Formula used for the calculation. |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to Element Types |
| BASE_SALARY_FLAG | VARCHAR2 | 30 |  |  | Indicate that this can be used as the Base Salary Rate. |
| OVERALL_SALARY_FLAG | VARCHAR2 | 30 |  |  | Indicates that this is the Overall Salary. |
| REPORTING_RATE_FLAG | VARCHAR2 | 30 |  |  | Determines if the Rate is a Reporting Rate, hence stored for Rate Reporting. |
| USE_REPORT_VALUE_FOR_CALC | VARCHAR2 | 30 |  |  | Determines if the Rate Value from the Reporting Table maybe returned as the value. |
| RETURN_PRECISION | NUMBER |  | 18 |  | Precision of the return Amount |
| RETURN_ROUNDING | VARCHAR2 | 30 |  |  | The Rounding type to be used on the Return |
| DEFAULT_RTN_PERIODICITY | VARCHAR2 | 30 |  |  | The Periodicity that should be returned by this Rate by default. |
| DEFAULT_RTN_CURRENCY | VARCHAR2 | 30 |  |  | Return Currency Code |
| DEFAULT_CALC_PERIODICITY | VARCHAR2 | 30 |  |  | The default periodicity that should be used for the calculation |
| DEFAULT_CALC_CURRENCY | VARCHAR2 | 30 |  |  | Calculation Currency |
| DEFAULT_BAL_DIMENSION_ID | NUMBER |  | 18 |  | The Balance Dimension used by default in the calculation |
| DEFAULT_FACTOR_TYPE | VARCHAR2 | 5 |  |  | The type of factor that is to be used |
| DEFAULT_FACTOR | VARCHAR2 | 30 |  |  | The Value that is to be used as the Factor |
| DEFAULT_FACTOR_IDENTIFIER | VARCHAR2 | 30 |  |  | Default Factors of VBC can have an Identifier for the leaf node name. |
| RETURN_FACTOR_TYPE | VARCHAR2 | 5 |  |  | RETURN_FACTOR_TYPE |
| RETURN_FACTOR_VALUE | VARCHAR2 | 30 |  |  | RETURN_FACTOR_VALUE |
| RETURN_FACTOR_IDENTIFIER | VARCHAR2 | 30 |  |  | Return factors of VBC may need an Identifier to determine a leaf node to return. |
| LIMIT_MODE | VARCHAR2 | 30 |  |  | Behavior when the rate is outside the minimum rate |
| MAX_LIMIT_MODE | VARCHAR2 | 30 |  |  | Behavior when the rate is outside the maximum rate |
| MIN_TYPE | VARCHAR2 | 30 |  |  | The type that the Min Value is |
| MIN_VALUE | VARCHAR2 | 30 |  |  | The Value of tne Minimum, based on the Min Type |
| MIN_VALUE_IDENTIFIER | VARCHAR2 | 30 |  |  | Minimum Value VBCs may need an identifier to determine the leaf node value. |
| MAX_TYPE | VARCHAR2 | 30 |  |  | The Maximum Value Type |
| MAX_VALUE | VARCHAR2 | 30 |  |  | This is the value of the Maximum Value based on the Type |
| MAX_VALUE_IDENTIFIER | VARCHAR2 | 30 |  |  | Max Value VBCs may require an identifier to determine a leaf node. |
| CONVERSION_FORMULA_ID | NUMBER |  | 18 |  | This is a Fast Formula of Type Rate Conversion and will be used to convert the periodicities used in this Rate Definition |
| CONVERSION_VBC_ID | NUMBER |  |  |  | A Value By Criteria Id that contains the factor values for the annualisation functions. |
| FACTOR_ENTERABLE | VARCHAR2 | 30 |  |  | Idicates whether the Primary Rates values are user enterable |
| AMOUNT_ENTERABLE | VARCHAR2 | 30 |  |  | Indicates whether a Primary Rate Amount is enterable. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| DEFAULT_SOURCE_TYPE | VARCHAR2 | 30 |  |  | This indicates how  the default value is calculated  for a Primary Rate. |
| DEFAULT_SOURCE_VALUE | VARCHAR2 | 30 |  |  | This is the amount or an ID used to calculate the default Amount. |
| VALIDATION_FORMULA_ID | NUMBER |  | 18 |  | The Foromula Id of a formula that validates the Amount being entered. |
| DEFAULT_FTE_FLAG | VARCHAR2 | 30 |  |  | DEFAULT_FTE_FLAG |
| FTE_FLAG | VARCHAR2 | 30 |  |  | FTE_FLAG |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RATE_DEFINITIONS_F_N1 | Non Unique | Default | RATE_DEFINITION_ID |
| PAY_RATE_DEFINITIONS_F_N2 | Non Unique | Default | BASE_NAME, SHORT_NAME, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_RATE_DEFINITIONS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_RATE_DEFINITIONS_F_N3 | Non Unique | Default | ELEMENT_TYPE_ID |
| PAY_RATE_DEFINITIONS_F_PK | Unique | Default | RATE_DEFINITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_RATE_DEFINITIONS_F_PK1 | Unique | Default | RATE_DEFINITION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
