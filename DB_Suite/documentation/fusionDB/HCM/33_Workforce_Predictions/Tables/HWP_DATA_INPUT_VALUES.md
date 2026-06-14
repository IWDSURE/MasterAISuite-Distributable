# HWP_DATA_INPUT_VALUES

This table contains data input values for predictives.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdatainputvalues-24650.html#hwpdatainputvalues-24650](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdatainputvalues-24650.html#hwpdatainputvalues-24650)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_DATA_INPUT_VALUES_PK | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID, ATTR_CODE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Data input values Process ID. |
| PERSON_ID | NUMBER |  | 18 | Yes | Data input values person ID. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Data input values assignment ID. |
| VALUE_DATE | DATE |  |  |  | Data input values value date. |
| ATTR_CODE | VARCHAR2 | 200 |  | Yes | Data input values attribute code. |
| ATTR_VALUE | VARCHAR2 | 2000 |  |  | Data input values attribute value. |
| ATTR_VALUE_DATA | VARCHAR2 | 2000 |  |  | Data input values attribute data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_DATA_INPUT_VALUES_N1 | Non Unique | Default | ASSIGNMENT_ID, ATTR_CODE |
| HWP_DATA_INPUT_VALUES_PK | Unique | Default | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID, ATTR_CODE |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
