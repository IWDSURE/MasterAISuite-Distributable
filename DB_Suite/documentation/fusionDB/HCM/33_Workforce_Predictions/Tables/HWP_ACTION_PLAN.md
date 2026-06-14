# HWP_ACTION_PLAN

This table stores the attributes which are modified and also stores the current and modified values.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpactionplan-5339.html#hwpactionplan-5339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpactionplan-5339.html#hwpactionplan-5339)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_ACTION_PLAN_PK | ACTION_SEQ_NO |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_SEQ_NO | NUMBER |  | 18 | Yes | Action Seq No. |
| SEQ_NO | NUMBER |  | 18 | Yes | Header seq No. |
| ATTRIBUTE_ID | NUMBER |  | 18 |  | Attribute Id, for which the attribute value is modified. |
| CURRENT_ATTR_VALUE | VARCHAR2 | 2000 |  |  | Current Attribute Value. |
| WHATIF_ATTR_VALUE | VARCHAR2 | 2000 |  |  | Modified attribute Value. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_ACTION_PLAN_N1 | Non Unique | Default | SEQ_NO, ATTRIBUTE_ID |
| HWP_ACTION_PLAN_U1 | Unique | Default | ACTION_SEQ_NO |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
