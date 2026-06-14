# PAY_DIR_COMP_FLEX_RSHIPS_F

This table contains the hierarchy of structures (parent/child) and the sequence in which they can be displayed.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircompflexrshipsf-28070.html#paydircompflexrshipsf-28070](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircompflexrshipsf-28070.html#paydircompflexrshipsf-28070)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_COMP_FLEX_RSHIPS_F_PK | DIR_COMP_FLEX_RSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_COMP_FLEX_RSHIP_ID | NUMBER |  | 18 | Yes | DIR_COMP_FLEX_RSHIP_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 | Yes | DIR_CARD_COMP_DEF_ID |
| PARENT_DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | PARENT_DIR_CARD_COMP_DEF_ID |
| DIR_COMP_FLEX_ID | NUMBER |  | 18 |  | DIR_COMP_FLEX_ID |
| PARENT_DIR_COMP_FLEX_ID | NUMBER |  | 18 |  | PARENT_DIR_COMP_FLEX_ID |
| GROUP_DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 |  | GROUP_DIR_CARD_COMP_DEF_ID |
| SEQUENCE | NUMBER |  | 18 | Yes | SEQUENCE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIR_COMP_FLEX_RSHIPS_F_N1 | Non Unique | Default | DIR_CARD_COMP_DEF_ID |
| PAY_DIR_COMP_FLEX_RSHIPS_F_PK | Unique | Default | DIR_COMP_FLEX_RSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_DIR_COMP_FLEX_RSHIPS_F_PK1 | Unique | Default | DIR_COMP_FLEX_RSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_DIR_COMP_FLEX_RSHIPS_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
