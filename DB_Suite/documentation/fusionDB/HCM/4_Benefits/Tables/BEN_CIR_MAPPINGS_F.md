# BEN_CIR_MAPPINGS_F

BEN_CIR_MAPPINGS_F identifies which Payroll Component is associated to which
Plan or Option in Plan

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencirmappingsf-16126.html#bencirmappingsf-16126](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencirmappingsf-16126.html#bencirmappingsf-16126)

## Primary Key

| Name | Columns |
|------|----------|
| ben_cir_mappings_f_PK | CIR_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CIR_MAPPING_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group Id- LDG of the Payroll Component. |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 |  | Payroll Card Definition Id- Foreign key to  pay_dir_card_definitions |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | Payroll Component Definition Id- Foreign key to pay_dir_card_comp_defs_f |
| MAPPING_ID | NUMBER |  | 18 |  | Payroll Mapping Id- Foreign key to PAY_GI_MAPPINGS |
| PL_ID | NUMBER |  | 18 |  | Plan Id - Plan for which the payroll component is attached |
| OIPL_ID | NUMBER |  | 18 |  | Option in Plan Id - Option in Plan for which the payroll component is attached |
| COSTING_METHOD | VARCHAR2 | 30 |  |  | Costing Method - Determines the method used to distribute the cost |
| DISTRIBUTION_RL | NUMBER |  | 18 |  | Distribution Formula Id -  Formula for Cost Distribution |
| DEDUCTION_METHOD | VARCHAR2 | 30 |  |  | Deduction Method- Determines the method used to allocate the deduction |
| DEDN_DISTRIBUTION_RL | NUMBER |  | 18 |  | Deduction Distribution Formula Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_6 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_7 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_8 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_9 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_10 | DATE |  |  |  | Template date field for future use. |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_6 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_7 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_8 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_9 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_10 | NUMBER |  | 18 |  | Template ID field for future use. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CIR_MAPPINGS_F_N1 | Non Unique | Default | PL_ID |
| BEN_CIR_MAPPINGS_F_N2 | Non Unique | Default | OIPL_ID |
| BEN_CIR_MAPPINGS_F_N3 | Non Unique | Default | MAPPING_ID |
| BEN_CIR_MAPPINGS_F_PK | Unique | Default | CIR_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
