# HRC_COMP_TEMPLATES_B

Defines a compare template for comparison which comprises of the comparison type (e.g. Benefit Medical Plans), highlights, footnotes, features and grouping of features.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccomptemplatesb-10656.html#hrccomptemplatesb-10656](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccomptemplatesb-10656.html#hrccomptemplatesb-10656)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| COMP_DEF_VAL_ID | NUMBER |  | 18 | Yes | Specifies the template comparison definition value identifier. Foreign key to hrc_comp_def_vals. |  |
| IKEY | VARCHAR2 | 128 |  | Yes | Immutable key. Oracle internal use only. |  |
| DATE_FROM | DATE |  |  | Yes | Indicates the date from the template is active. |  |
| DATE_TO | DATE |  |  | Yes | Indicates the date the template is active to. |  |
| COMP_DEF_TYPE_ID | NUMBER |  | 18 | Yes | Specifies the template comparison definition type identifier. Foreign key to hrc_comp_def_types. |  |
| PRODUCT_CODE | VARCHAR2 | 30 |  | Yes | This column identifies the owning product. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| USE_GROUPS_FLAG | VARCHAR2 | 30 |  | Yes | Specifies if the template use groups Y or N. |  |
| USE_CAT_FLAG | VARCHAR2 | 30 |  | Yes | Specifies if the template use categories Y or N. |  |
| CAT_DEF_TYPE_ID | NUMBER |  | 18 |  | Specifies the category definition type identifier. Foreign key to hrc_comp_def_types_b. |  |
| USE_OPT_FLAG | VARCHAR2 | 30 |  | Yes | Specifies if the template use options Y or N. |  |
| OPT_DEF_TYPE_ID | NUMBER |  | 18 |  | Specifies the options definition type identifier. Foreign key to hrc_comp_def_types. |  |
| USE_HD_FLAG | VARCHAR2 | 30 |  | Yes | Specifies if the template uses header description  Y or N. |  |
| HD_TYPE | VARCHAR2 | 30 |  |  | Specifies the header description type to be used. |  |
| HD_CODE | VARCHAR2 | 30 |  |  | Specifies the header code to be used. |  |
| USE_SUGV_FLAG | VARCHAR2 | 30 |  | Yes | Specifies if the template use common suggestion values  Y or N. |  |
| SUGV_DEF_TYPE_ID | NUMBER |  | 18 |  | Specifies the common suggestion values  definition type identifier. Foreign key to hrc_comp_def_types. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| ATTR_CHAR1 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |  |
| ATTR_CHAR2 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |  |
| ATTR_CHAR3 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |  |
| ATTR_NUMBER1 | NUMBER |  | 18 |  | Additional column for storing a number. |  |
| ATTR_NUMBER2 | NUMBER |  | 18 |  | Additional column for storing a number. |  |
| ATTR_NUMBER3 | NUMBER |  | 18 |  | Additional column for storing a number. |  |
| ATTR_DATE1 | DATE |  |  |  | Additional column for storing a date. |  |
| ATTR_DATE2 | DATE |  |  |  | Additional column for storing a date. |  |
| ATTR_DATE3 | DATE |  |  |  | Additional column for storing a date. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Active |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMP_TEMPLATES_B_N1 | Non Unique | FUSION_TS_TX_DATA | COMP_DEF_TYPE_ID, DATE_FROM, LEGISLATION_CODE |
| HRC_COMP_TEMPLATES_B_N2 | Non Unique | FUSION_TS_TX_DATA | IKEY |
| HRC_COMP_TEMPLATES_B_N20 | Non Unique | Default | SGUID |
| HRC_COMP_TEMPLATES_B_U1 | Unique | FUSION_TS_TX_DATA | TEMPLATE_ID, ORA_SEED_SET1 |
| HRC_COMP_TEMPLATES_B_U11 | Unique | FUSION_TS_TX_DATA | TEMPLATE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
