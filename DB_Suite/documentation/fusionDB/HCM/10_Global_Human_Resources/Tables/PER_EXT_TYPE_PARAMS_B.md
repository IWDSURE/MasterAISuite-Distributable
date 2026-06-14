# PER_EXT_TYPE_PARAMS_B

Parameters defined for an extract type.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexttypeparamsb-27186.html#perexttypeparamsb-27186](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexttypeparamsb-27186.html#perexttypeparamsb-27186)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_TYPE_PARAMS_B_PK | EXT_TYPE_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_TYPE_PARAM_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| DEFAULT_HIDE_FLAG | VARCHAR2 | 3 |  |  | DEFAULT_HIDE_FLAG |
| EXT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Denotes the extract type code. |
| BASE_TYPE_PARAM_NAME | VARCHAR2 | 80 |  | Yes | Base Name of the Parameter |
| ESS_TYPE_PARAM_NAME | VARCHAR2 | 80 |  |  | ESS Parameter Name |
| XML_TAG_NAME | VARCHAR2 | 80 |  |  | XML Tag Name of Paramter |
| DATA_TYPE | VARCHAR2 | 80 |  |  | Data Type of the Parameter |
| ALLOWED_IN_EXPRESSION | VARCHAR2 | 1 |  |  | Identifies certain standard auto-generated parameters as not being accessible within expressions. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EXT_TYPE_PARAMS_B_PK | Unique | FUSION_TS_TX_DATA | EXT_TYPE_PARAM_ID, ORA_SEED_SET1 |
| PER_EXT_TYPE_PARAMS_B_PK1 | Unique | FUSION_TS_TX_DATA | EXT_TYPE_PARAM_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
