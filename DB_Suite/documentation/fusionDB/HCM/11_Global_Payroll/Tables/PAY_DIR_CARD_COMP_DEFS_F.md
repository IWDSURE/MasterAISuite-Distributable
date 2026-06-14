# PAY_DIR_CARD_COMP_DEFS_F

This table contains deduction component definitions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircardcompdefsf-16507.html#paydircardcompdefsf-16507](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircardcompdefsf-16507.html#paydircardcompdefsf-16507)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_CARD_COMP_DEFS_F_PK | DIR_CARD_COMP_DEF_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 | Yes | DIR_CARD_COMP_DEF_ID |  |
| NAVIGATION_USE | VARCHAR2 | 30 |  |  | NAVIGATION_USE |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 | Yes | DIR_CARD_DEFINITION_ID |  |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | DEDUCTION_TYPE_ID | Active |
| DEDUCTION_GROUP_ID | NUMBER |  | 18 |  | DEDUCTION_GROUP_ID | Active |
| DEFAULTING_TRU_COMP_FLAG | VARCHAR2 | 30 |  |  | DEFAULTING_TRU_COMP_FLAG |  |
| BREAKDOWN_COMPONENT_FLAG | VARCHAR2 | 30 |  |  | BREAKDOWN_COMPONENT_FLAG |  |
| USER_EXTENSIBLE_FLAG | VARCHAR2 | 5 |  |  | USER_EXTENSIBLE_FLAG |  |
| ATTACHMENT_ENTITY_NAME | VARCHAR2 | 40 |  |  | Captures attachment entity name |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |  |
| REQUIRED | VARCHAR2 | 30 |  |  | REQUIRED |  |
| MULTIPLE_ALLOWED | VARCHAR2 | 30 |  |  | MULTIPLE_ALLOWED |  |
| BASE_COMPONENT_NAME | VARCHAR2 | 80 |  |  | BASE_COMPONENT_NAME |  |
| ASSOCIABLE_TRU | VARCHAR2 | 30 |  |  | ASSOCIABLE_TRU |  |
| ASSOCIABLE_TERM | VARCHAR2 | 30 |  |  | ASSOCIABLE_TERM |  |
| KEEP_OPEN | VARCHAR2 | 20 |  |  | Reopen Component on reverse Termination. |  |
| AUDIT_RECORDING | VARCHAR2 | 30 |  |  | Record in the Process Changes |  |
| STARTING_TIME_DEF_ID | NUMBER |  | 18 |  | Time Definition for when the Component Starts. |  |
| ENDING_TIME_DEF_ID | NUMBER |  | 18 |  | Time Definition for when the Component Ends. |  |
| GLB_TRANSFER_RULE | VARCHAR2 | 10 |  |  | Handling the copy of CIR Cards during Global Transfer |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |
| KEEP_OPEN_ON_PROCD_REC | VARCHAR2 | 20 |  |  | Prevents End date component processed in a payroll run. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIR_CARD_COMP_DEFS_F_N1 | Non Unique | Default | DIR_CARD_DEFINITION_ID |
| PAY_DIR_CARD_COMP_DEFS_F_N2 | Non Unique | Default | DIR_CARD_COMP_DEF_ID, DIR_CARD_DEFINITION_ID |
| PAY_DIR_CARD_COMP_DEFS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_CARD_COMP_DEFS_F_PK | Unique | Default | DIR_CARD_COMP_DEF_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_DIR_CARD_COMP_DEFS_F_PK1 | Unique | Default | DIR_CARD_COMP_DEF_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
