# PAY_GENERIC_ANA_ATT_DEFS

This table contains attribute definitions which used by pay generic analysis type.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericanaattdefs-25691.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericanaattdefs-25691.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GENERIC_ANA_ATT_PK | PAY_GEN_ANA_ATTDEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_GEN_ANA_ATTDEF_ID | NUMBER |  | 18 | Yes | Payroll Generic Analytics Attribute Definition Id |
| PAY_GEN_ANA_TYPE_ID | NUMBER |  | 18 | Yes | Payroll Generic Analytics Type Id |
| BASE_ATTRDEF_NAME | VARCHAR2 | 128 |  | Yes | Base Attribute Definition Name, Unique Name for generic ana type. |
| DATA_COLUMN | VARCHAR2 | 64 |  |  | Data Column, Will identify coumn name, like DATA1, DATA2. |
| DISPLAY_SEQUENCE | NUMBER |  | 3 | Yes | Display Sequence, Used by UI display. |
| DISPLAY_LABEL | VARCHAR2 | 256 |  |  | Display Label. Used by UI display. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  | Yes | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_GENERIC_ANA_ATT_U1 | Unique | Default | PAY_GEN_ANA_ATTDEF_ID, ORA_SEED_SET1 |
| PAY_GENERIC_ANA_ATT_U2 | Unique | Default | PAY_GEN_ANA_ATTDEF_ID, ORA_SEED_SET2 |
| PAY_GENERIC_ANA_ATT_U3 | Unique | Default | PAY_GEN_ANA_TYPE_ID, BASE_ATTRDEF_NAME, ORA_SEED_SET1 |
| PAY_GENERIC_ANA_ATT_U4 | Unique | Default | PAY_GEN_ANA_TYPE_ID, BASE_ATTRDEF_NAME, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
