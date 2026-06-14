# HWM_DATA_SOURCE_ATTRIBUTES

This table stores the information about the attributes of Data Source.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdatasourceattributes-25976.html#hwmdatasourceattributes-25976](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdatasourceattributes-25976.html#hwmdatasourceattributes-25976)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_DATA_SOURCE_ATTRIBUTES_PK | DATA_SOURCE_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_SOURCE_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | DATA_SOURCE_ATTRIBUTE_ID |
| DATA_SOURCE_ID | NUMBER |  | 18 | Yes | DATA_SOURCE_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 80 |  | Yes | ATTRIBUTE_NAME |
| ATTRIBUTE_TYPE | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_TYPE |
| DATA_TYPE | VARCHAR2 | 30 |  | Yes | DATA_TYPE |
| CUSTOMIZED_FLAG | VARCHAR2 | 1 |  | Yes | CUSTOMIZED_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_DATA_SOURCE_ATTRIBUTES_N1 | Non Unique | Default | DATA_SOURCE_ID |
| HWM_DATA_SOURCE_ATTRIBUTES_U1 | Unique | Default | DATA_SOURCE_ATTRIBUTE_ID, ORA_SEED_SET1 |
| HWM_DATA_SOURCE_ATTRIBUTES_U11 | Unique | Default | DATA_SOURCE_ATTRIBUTE_ID, ORA_SEED_SET2 |
| HWM_DATA_SOURCE_ATTRIBUTE_N20 | Non Unique | Default | SGUID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
