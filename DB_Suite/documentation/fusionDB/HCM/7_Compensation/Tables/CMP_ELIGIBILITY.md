# CMP_ELIGIBILITY

Stores the linkage between plan/components and eligibility profiles.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpeligibility-14355.html#cmpeligibility-14355](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpeligibility-14355.html#cmpeligibility-14355)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ELIGIBILITY_PK | ELIGIBILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIGIBILITY_ID | NUMBER |  | 18 | Yes | ELIGIBILITY_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| COMP_TYPE | VARCHAR2 | 30 |  |  | COMP_TYPE |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | ELIGIBILITY_PROFILE_ID |
| REQUIRED_FLAG | VARCHAR2 | 1 |  |  | REQUIRED_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ELIGIBILITY_N2 | Non Unique | Default | COMPONENT_ID |
| CMP_ELIGIBILITY_U1 | Unique | Default | PLAN_ID, COMPONENT_ID, ELIGIBILITY_PROFILE_ID |
| CMP_ELIGIBILITY_UK1 | Unique | Default | ELIGIBILITY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
