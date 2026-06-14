# PAY_DIR_CARD_DEFINITIONS

This table contains details of a deduction or set of related deductions, such as a government tax card.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircarddefinitions-26466.html#paydircarddefinitions-26466](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircarddefinitions-26466.html#paydircarddefinitions-26466)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_CARD_DEFINITIONS_PK | DIR_CARD_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DIR_CARD_DEFINITION_ID | NUMBER |  | 18 | Yes | DIR_CARD_DEFINITION_ID |  |
| VO_NAME | VARCHAR2 | 100 |  |  | VO_NAME |  |
| BASE_DISPLAY_NAME | VARCHAR2 | 80 |  | Yes | BASE_DISPLAY_NAME |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| AUTO_GENERATE | VARCHAR2 | 30 |  |  | AUTO_GENERATE |  |
| ASSOCIABLE_TRU | VARCHAR2 | 30 |  |  | ASSOCIABLE_TRU |  |
| ASSOCIABLE_TERM | VARCHAR2 | 30 |  |  | ASSOCIABLE_TERM |  |
| DATE_MODE | VARCHAR2 | 5 |  |  | DATE_MODE |  |
| DEFAULTING_TRU_FLAG | VARCHAR2 | 5 |  |  | DEFAULTING_TRU_FLAG |  |
| BREAKDOWN_COMPONENT_FLAG | VARCHAR2 | 20 |  |  | BREAKDOWN_FLAG |  |
| USER_EXTENSIBLE_FLAG | VARCHAR2 | 5 |  |  | USER_EXTENSIBLE_FLAG |  |
| STARTING_TIME_DEF_ID | NUMBER |  | 18 |  | Time Definition when the Card can start. |  |
| ENDING_TIME_DEF_ID | NUMBER |  | 18 |  | Ending Time Definition when the Card ends. |  |
| KEEP_OPEN | VARCHAR2 | 20 |  |  | Repoen on reverse Termination |  |
| GLB_TRANSFER_RULE | VARCHAR2 | 10 |  |  | Handling the copy of CIR Cards during Global Transfer |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIR_CARD_DEFINITIONS_PK | Unique | Default | DIR_CARD_DEFINITION_ID, ORA_SEED_SET1 |
| PAY_DIR_CARD_DEFINITIONS_PK1 | Unique | Default | DIR_CARD_DEFINITION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
