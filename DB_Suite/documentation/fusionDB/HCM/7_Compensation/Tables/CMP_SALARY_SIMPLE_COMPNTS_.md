# CMP_SALARY_SIMPLE_COMPNTS_

Child entity for salary simple rates defined for salary record

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarysimplecompnts-23544.html#cmpsalarysimplecompnts-23544](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarysimplecompnts-23544.html#cmpsalarysimplecompnts-23544)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_SIMPLE_COMPNTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SIMPLE_SALARY_COMPNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SIMPLE_SALARY_COMPNT_ID | NUMBER |  | 18 | Yes | Primary unique indentifier |
| PERSON_ID | NUMBER |  | 18 |  | Person unique ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Person Assignment unique ID |
| SALARY_ID | NUMBER |  | 18 |  | Salary unique ID |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | Salary Basis unique ID |
| SALARY_DATE_FROM | DATE |  |  |  | Salary Start Date |
| SALARY_DATE_TO | DATE |  |  |  | Salary End Date |
| BASIS_SIMPLE_COMPONENT_ID | NUMBER |  | 18 |  | Unique key of setup entity cmp_basis_simple_components |
| DISPLAY_SEQUENCE | NUMBER |  | 3 |  | Display sequence will be used display in ascending order |
| PROCESSING_SEQUENCE | NUMBER |  | 3 |  | Processing order of the rates user entered will usually be first and then computed rates |
| COMPONENT_TYPE | VARCHAR2 | 30 |  |  | Simple Rate type as defined in the salary basis |
| COMPONENT_CODE | VARCHAR2 | 30 |  |  | Rate component code which is user defined lookup code |
| BASED_ON_COMPONENT_CODE | VARCHAR2 | 30 |  |  | If Rate is percentage based then the rate on which the amount will be computed during allocation time. |
| OVERALL_SALARY_AFFECT | VARCHAR2 | 30 |  |  | If the rate amount would be added to the overall salary rate if present in the salary basis definition. |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Input Value Id of the element type attached to salary basis to which the element entry will be created. |
| USER_SELECTED_COMPONENT | VARCHAR2 | 30 |  |  | If the simple rate is a user selected one from the salary basis which are defined as user selectable at allocation time |
| DEFAULT_AMOUNT | NUMBER |  |  |  | Default Amount if defined in the setup for the simple rate |
| PREV_AMOUNT | NUMBER |  |  |  | Pervious component amount for the same salary basis |
| PREV_ADJUSTMENT_AMOUNT | NUMBER |  |  |  | Previous Adjustment Amount for the component for the same salary basis, it will be null for first salary record. |
| PREV_ADJUSTMENT_PERCENT | NUMBER |  |  |  | Previous Adjustment Percentage for the component of the same salary basis. |
| AMOUNT | NUMBER |  |  |  | Rate Amount which can be user entered or computed |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | Currency Code as defined in the salary basis |
| FREQUENCY_CODE | VARCHAR2 | 30 |  |  | Frequency as defined in the salary basis |
| SCALE | NUMBER |  | 3 |  | Rate number of decimal points as defined in the salary basis |
| ROUNDING_CODE | VARCHAR2 | 20 |  |  | Rounding Code as defined in the salary basis |
| ADJUSTMENT_AMOUNT | NUMBER |  |  |  | Adjustment Amount with respect to previous salary record provided it also has the same basis and simple rate |
| ADJUSTMENT_PERCENT | NUMBER |  |  |  | Adjustment Percent with respect to previous salary record provided it also has the same basis and simple rate |
| PERCENTAGE | NUMBER |  |  |  | Rate Percentage user entered or fixed |
| ANNUAL_FACTOR | NUMBER |  |  |  | Annual Factor as defined in salary basis |
| ANNUAL_AMOUNT | NUMBER |  |  |  | Annual Amount with FTE applied |
| ANNUAL_FT_AMOUNT | NUMBER |  |  |  | Annual Amount without the FTE applied i.e. full-time amount |
| MINIMUM_AMOUNT | NUMBER |  |  |  | Minimum check for the Rate Amount entered or computed. |
| MAXIMUM_AMOUNT | NUMBER |  |  |  | Maximum check for the Rate Amount entered or computed. |
| OVERRIDE_GSP_RATE | VARCHAR2 | 30 |  |  | OVERRIDE_GSP_RATE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_SALARY_SIMPLE_COMPNTN1_ | Non Unique | Default | SIMPLE_SALARY_COMPNT_ID, LAST_UPDATE_DATE |
| CMP_SALARY_SIMPLE_COMPNTS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SIMPLE_SALARY_COMPNT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
