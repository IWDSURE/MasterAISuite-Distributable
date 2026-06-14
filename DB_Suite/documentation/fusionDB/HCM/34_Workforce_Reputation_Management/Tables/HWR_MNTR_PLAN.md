# HWR_MNTR_PLAN

This table stores recommended checklist.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplan-14783.html#hwrmntrplan-14783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplan-14783.html#hwrmntrplan-14783)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_MNTR_PLAN_PK | PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| PLAN_STATUS | VARCHAR2 | 30 |  |  | This holds the current status of the mentor plan. |
| MENTOR_ID | NUMBER |  | 18 | Yes | This is the foreign key to MENTOR_ID in HWR_SKILLS_MENTOR_B table. |
| EXPIRY_DATE | TIMESTAMP |  |  | Yes | Expiry date of the plan. |
| PLAN_ATTR_1 | VARCHAR2 | 400 |  |  | This is the mentor plan attribute 1. |
| PLAN_ATTR_2 | VARCHAR2 | 400 |  |  | This is the mentor plan attribute 2. |
| PLAN_ATTR_3 | VARCHAR2 | 400 |  |  | This is the mentor plan attribute 3. |
| PLAN_ATTR_4 | VARCHAR2 | 400 |  |  | This is the mentor plan attribute 4. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_MNTR_PLAN_U1 | Unique | Default | PLAN_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
