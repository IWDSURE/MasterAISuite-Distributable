# HMO_MODEL_PLANS_TL

The  language-dependent table for HMO_MODEL_PLANS_B .

## Details

**Schema:** FUSION

**Object owner:** HMO

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hmomodelplanstl-21457.html#hmomodelplanstl-21457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hmomodelplanstl-21457.html#hmomodelplanstl-21457)

## Primary Key

| Name | Columns |
|------|----------|
| HMO_MODEL_PLANS_TL_PK | MODEL_PLAN_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_PLAN_ID | NUMBER |  | 18 | Yes | Model Plan Id. Foreign Key to HMO_MODEL_PLANS_B |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id. Foeign key to PER_ENTERPRISES . |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| MODEL_PLAN_NAME | VARCHAR2 | 80 |  | Yes | Name of the model plan. Translatable column. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Detal description of the model plan . Translatable column. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HMO_MODEL_PLANS_TL_PK | Unique | Default | MODEL_PLAN_ID, LANGUAGE |

---

[← Back to Index](../32_Workforce_Modeling_Tables_Index.md)
