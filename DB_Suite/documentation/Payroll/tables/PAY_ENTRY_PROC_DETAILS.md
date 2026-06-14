# PAY_ENTRY_PROC_DETAILS

This table contains internal processing details for certain types of element entries.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payentryprocdetails-13237.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payentryprocdetails-13237.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ENTRY_PROC_DETAILS_PK | ENTRY_PROC_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTRY_PROC_DETAIL_ID | NUMBER |  | 18 | Yes | ENTRY_PROC_DETAIL_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | ELEMENT_ENTRY_ID |
| RETRO_COMPONENT_ID | NUMBER |  | 18 |  | RETRO_COMPONENT_ID |
| SOURCE_ELEMENT_TYPE_ID | NUMBER |  | 30 |  | SOURCE_ELEMENT_TYPE_ID |
| SOURCE_REL_ACTION_ID | NUMBER |  | 18 |  | SOURCE_REL_ACTION_ID |
| SOURCE_ENTRY_ID | NUMBER |  | 18 |  | SOURCE_ENTRY_ID |
| SOURCE_RUN_RESULT_ID | NUMBER |  | 18 |  | SOURCE_RUN_RESULT_ID |
| RUN_RESULT_ID | NUMBER |  | 18 |  | RUN_RESULT_ID |
| ORIGINAL_RETRO_RUN_RESULT_ID | NUMBER |  | 18 |  | ORIGINAL_RETRO_RUN_RESULT_ID |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |
| TAX_UNIT_ID | NUMBER |  |  |  | TAX_UNIT_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| DIR_CARD_COMP_ID | NUMBER |  | 18 |  | DIR_CARD_COMP_ID |
| PROCESSING_SPAN | NUMBER |  | 18 |  | PROCESSING_SPAN |
| ADJUSTMENT_TYPE | VARCHAR2 | 30 |  |  | ADJUSTMENT_TYPE |
| PROCESS_PATH | VARCHAR2 | 2000 |  |  | PROCESS_PATH |
| ENTRY_PROCESS_PATH | VARCHAR2 | 2000 |  |  | ENTRY_PROCESS_PATH |
| SOURCE_START_DATE | DATE |  |  |  | SOURCE_START_DATE |
| SOURCE_END_DATE | DATE |  |  |  | SOURCE_END_DATE |
| SOURCE_RUN_TYPE | NUMBER |  | 18 |  | SOURCE_RUN_TYPE |
| SOURCE_TRIGGER_ENTRY | NUMBER |  | 18 |  | SOURCE_TRIGGER_ENTRY |
| STOPPED_DATE | DATE |  |  |  | STOPPED_DATE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ENTRY_PROC_DETAILS_FK1 | Non Unique | Default | SOURCE_REL_ACTION_ID |
| PAY_ENTRY_PROC_DETAILS_FK2 | Non Unique | Default | ELEMENT_ENTRY_ID, RETRO_COMPONENT_ID |
| PAY_ENTRY_PROC_DETAILS_N1 | Non Unique | Default | SOURCE_ENTRY_ID |
| PAY_ENTRY_PROC_DETAILS_PK | Unique | Default | ENTRY_PROC_DETAIL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
