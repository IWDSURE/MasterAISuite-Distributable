# CMP_VC_PER_ELIG_PLANS

Variable Compesnation holds eligible plan rows in this table for every person it processes

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpvcpereligplans-12305.html#cmpvcpereligplans-12305](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpvcpereligplans-12305.html#cmpvcpereligplans-12305)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_VC_PER_ELIG_PLANS_PK | VC_PER_ELIG_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VC_PER_ELIG_PLAN_ID | NUMBER |  | 18 | Yes | VC_PER_ELIG_PLAN_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 |  | PLAN_ATTRIBUTE_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  |  | ATTRIBUTE_NAME |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| START_DATE_CODE | VARCHAR2 | 30 |  |  | START_DATE_CODE |
| END_DATE_CODE | VARCHAR2 | 30 |  |  | END_DATE_CODE |
| START_DATE_RULE | NUMBER |  | 18 |  | START_DATE_RULE |
| END_DATE_RULE | NUMBER |  | 18 |  | END_DATE_RULE |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| NON_MONETARY_UOM | VARCHAR2 | 30 |  |  | NON_MONETARY_UOM |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | ELEMENT_TYPE_ID |
| ELIG_FLAG | VARCHAR2 | 18 |  | Yes | ELIG_FLAG |
| ELEMENT_ELIG_FLAG | VARCHAR2 | 30 |  | Yes | ELEMENT_ELIG_FLAG |
| INELIG_REASON_CD | VARCHAR2 | 30 |  |  | INELIG_REASON_CD |
| ELIG_OVERRIDE_FLAG | VARCHAR2 | 30 |  |  | ELIG_OVERRIDE_FLAG |
| ELIG_OVERRIDE_THRU_DT | DATE |  |  |  | ELIG_OVERRIDE_THRU_DT |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_VC_PER_ELIG_PLANS_PK | Unique | Default | VC_PER_ELIG_PLAN_ID |
| CMP_VC_PER_ELIG_PLANS_U1 | Unique | Default | PERSON_ID, ASSIGNMENT_ID, LEGAL_ENTITY_ID, PLAN_ID, COMPONENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
