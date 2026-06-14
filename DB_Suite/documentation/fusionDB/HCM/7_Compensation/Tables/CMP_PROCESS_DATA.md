# CMP_PROCESS_DATA

Stores information about compensation process runs.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpprocessdata-4546.html#cmpprocessdata-4546](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpprocessdata-4546.html#cmpprocessdata-4546)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PROCESS_DATA_PK | TWU_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TWU_ROW_ID | NUMBER |  | 18 | Yes | TWU_ROW_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ROW_TYPE_ID | NUMBER |  | 18 |  | ROW_TYPE_ID |
| ROW_TYPE_CD | VARCHAR2 | 30 |  |  | ROW_TYPE_CD |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| EVENT_DATE | DATE |  |  |  | EVENT_DATE |
| ROW_ATTRIBUTE1 | VARCHAR2 | 30 |  |  | ROW_ATTRIBUTE1 |
| ROW_ATTRIBUTE2 | VARCHAR2 | 30 |  |  | ROW_ATTRIBUTE2 |
| NUM_1 | NUMBER |  | 18 |  | NUM_1 |
| NUM_2 | NUMBER |  | 18 |  | NUM_2 |
| NUM_3 | NUMBER |  | 18 |  | NUM_3 |
| NUM_4 | NUMBER |  | 18 |  | NUM_4 |
| NUM_5 | NUMBER |  | 18 |  | NUM_5 |
| DATE_1 | DATE |  |  |  | DATE_1 |
| DATE_2 | DATE |  |  |  | DATE_2 |
| DATE_3 | DATE |  |  |  | DATE_3 |
| TXT_1 | VARCHAR2 | 240 |  |  | TXT_1 |
| TXT_2 | VARCHAR2 | 240 |  |  | TXT_2 |
| TXT_3 | VARCHAR2 | 240 |  |  | TXT_3 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PROCESS_DATA_N1 | Non Unique | Default | PERSON_EVENT_ID |
| CMP_PROCESS_DATA_N2 | Non Unique | Default | PLAN_ID, PERIOD_ID, ROW_TYPE_ID |
| CMP_PROCESS_DATA_PK | Unique | Default | TWU_ROW_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
