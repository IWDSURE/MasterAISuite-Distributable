# PER_ACCRUAL_PLANS_TL

Language dependent table . Stores the translated data for PER_ACCRUAL_PLANS_B

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualplanstl-13315.html#peraccrualplanstl-13315](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualplanstl-13315.html#peraccrualplanstl-13315)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACCRUAL_PLANS_TL_PK | ACCRUAL_PLAN_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCRUAL_PLAN_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ACCRUAL_PLANS_B . Identifies the plan for which translations are stored. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ACCRUAL_PLAN_NAME | VARCHAR2 | 80 |  | Yes | User defined accrual plan name . |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of the accrual plan . |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACCRUAL_PLANS_TL_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ACCRUAL_PLANS_TL_PK | Unique | Default | ACCRUAL_PLAN_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
