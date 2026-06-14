# CMP_SALARY_COMPONENTS

Salary holds details of salary proposals for Employee or Contingent worker assignments. A salary proposal may have one or more components, held in Salary Components. There can be  one/multiple unapproved salary proposal(s) at any time. 

The details of Salary Components cannot be updated or inserted if the overall proposal has already been approved. A Salary may have one or multiple components associated with it. Approval of all components are handled in one transaction and cannot be addressed separately.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarycomponents-8985.html#cmpsalarycomponents-8985](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarycomponents-8985.html#cmpsalarycomponents-8985)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_SALARY_COMPONENTS_PK | SALARY_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| SALARY_COMPONENT_ID | NUMBER |  | 18 | Yes | Salary Component Primary key. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F |  |
| SALARY_ID | NUMBER |  | 18 | Yes | Foreign Key to CMP_SALARY. |  |
| COMPONENT_APPROVED | VARCHAR2 | 30 |  |  | If the component is approved or not. When a salary proposal is approved then all the saalry components are also approved. |  |
| COMPONENT_REASON_CODE | VARCHAR2 | 30 |  |  | Change reason for the component. |  |
| CHANGE_AMOUNT | NUMBER |  |  |  | The change or increase expressed in amount for a salary component. For eaxmple, a person salary increase may consists of two components one for promotion $500.00 and other for Contract Agreement increase of $400.00. |  |
| CHANGE_PERCENTAGE | NUMBER |  | 18 |  | The change or increase expressed in percentage. |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |  |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |  |
| SALARY_DATE_FROM | DATE |  |  |  | SALARY_DATE_FROM |  |
| SALARY_DATE_TO | DATE |  |  |  | SALARY_DATE_TO |  |
| SALARY_BASIS_TYPE | VARCHAR2 | 30 |  |  | SALARY_BASIS_TYPE |  |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |  |
| CHANGE_AMOUNT_SCALE | NUMBER |  | 3 |  | CHANGE_AMOUNT_SCALE |  |
| CHANGE_PERCENT_SCALE | NUMBER |  | 3 |  | CHANGE_PERCENT_SCALE |  |
| AMOUNT_ROUNDING_CODE | VARCHAR2 | 30 |  |  | AMOUNT_ROUNDING_CODE |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Salary Component Information (CMP_SALARY_COMPONENTS) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| CMP_SALARY_COMPONENTS_N1 | Non Unique | Default | BUSINESS_GROUP_ID | Obsolete |
| CMP_SALARY_COMPONENTS_PK | Unique | Default | SALARY_COMPONENT_ID |  |
| CMP_SALARY_COMPONENTS_U1 | Unique | Default | SALARY_ID, COMPONENT_REASON_CODE |  |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
