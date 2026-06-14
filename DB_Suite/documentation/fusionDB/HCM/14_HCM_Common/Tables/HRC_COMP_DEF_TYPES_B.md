# HRC_COMP_DEF_TYPES_B

Reference table containing compare definition types of Template, Category, Option and Suggestion Values.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompdeftypesb-11209.html#hrccompdeftypesb-11209](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompdeftypesb-11209.html#hrccompdeftypesb-11209)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEF_TYPE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| IKEY | VARCHAR2 | 128 |  | Yes | Immutable key. Oracle internal use only. |
| PRODUCT_CODE | VARCHAR2 | 30 |  | Yes | This column identifies the owning product. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| DEF_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Specifies the definition type code (Product Template Types, Categories, Options. Suggestion Values). |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ATTR_CHAR1 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |
| ATTR_CHAR2 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |
| ATTR_CHAR3 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |
| ATTR_NUMBER1 | NUMBER |  | 18 |  | Additional column for storing a number. |
| ATTR_NUMBER2 | NUMBER |  | 18 |  | Additional column for storing a number. |
| ATTR_NUMBER3 | NUMBER |  | 18 |  | Additional column for storing a number. |
| ATTR_DATE1 | DATE |  |  |  | Additional column for storing a date. |
| ATTR_DATE2 | DATE |  |  |  | Additional column for storing a date. |
| ATTR_DATE3 | DATE |  |  |  | Additional column for storing a date. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMP_DEF_TYPES_B_N1 | Non Unique | FUSION_TS_TX_DATA | DEF_TYPE_CODE, PRODUCT_CODE, LEGISLATION_CODE |
| HRC_COMP_DEF_TYPES_B_N2 | Non Unique | FUSION_TS_TX_DATA | IKEY |
| HRC_COMP_DEF_TYPES_B_N20 | Non Unique | Default | SGUID |
| HRC_COMP_DEF_TYPES_B_U1 | Unique | FUSION_TS_TX_DATA | DEF_TYPE_ID, ORA_SEED_SET1 |
| HRC_COMP_DEF_TYPES_B_U11 | Unique | FUSION_TS_TX_DATA | DEF_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
