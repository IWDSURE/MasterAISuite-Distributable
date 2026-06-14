# HRM_PLAN_INCUMBENTS

This table is used to store Plan Incumbents.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanincumbents-21206.html#hrmplanincumbents-21206](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanincumbents-21206.html#hrmplanincumbents-21206)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_PLAN_INCUMBENTS_PK | PLAN_INCUMBENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_INCUMBENT_ID | NUMBER |  | 18 | Yes | Primary Key to HRM_PLAN_INCUMBENTS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PLAN_ID | NUMBER |  | 18 | Yes | The succession plan where the person is listed as an candidate. |
| INCUMBENT_PERSON_ID | NUMBER |  | 18 | Yes | Person id of the plan incumbent. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_PLAN_INCUMBENTS_N1 | Non Unique | Default | PLAN_ID, INCUMBENT_PERSON_ID |
| HRM_PLAN_INCUMBENTS_U1 | Unique | Default | PLAN_INCUMBENT_ID |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
