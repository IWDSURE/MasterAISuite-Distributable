# HRC_EVT_SRC_OBJ_ATTRIBUTES

An source object attribute is an attribute or column that exists within an Entity Object or a PLSQL row Handle

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtsrcobjattributes-14800.html#hrcevtsrcobjattributes-14800](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtsrcobjattributes-14800.html#hrcevtsrcobjattributes-14800)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_SRC_OBJ_ATTRS_PK | SOURCE_OBJECT_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_OBJECT_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Unique Identifier of Source Object |
| NAME | VARCHAR2 | 80 |  | Yes | Attribute Name |
| DATA_TYPE | VARCHAR2 | 30 |  | Yes | Attribute Type |
| PRIMARY_KEY | VARCHAR2 | 30 |  | Yes | Indication of whether the attribute represents a Primary Key column (N.B. this does not include Date Effective Columns or Date Effective Sequence) |
| PK_SEQUENCE | NUMBER |  | 9 |  | Sequence number of the primary key |
| DATE_EFFECTIVE_START_DATE | VARCHAR2 | 30 |  |  | Indication of whether the attribute is the Date Effective Start Date |
| DATE_EFFECTIVE_END_DATE | VARCHAR2 | 30 |  |  | Indication of whether the attribute is the Date Effective End Date |
| DATE_EFFECTIVE_SEQUENCE | VARCHAR2 | 30 |  |  | Indication of whether the attribute is the Date Effective Sequence |
| COLUMN_NAME | VARCHAR2 | 30 |  |  | Name of column that the source object attribute is based on |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| HRC_EVT_SRC_OBJ_ATTRIBUTE_N20 | Non Unique | Default | SGUID, DATE_EFFECTIVE_START_DATE, DATE_EFFECTIVE_END_DATE |
| HRC_EVT_SRC_OBJ_ATTRS_PK | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ATTRIBUTE_ID, ORA_SEED_SET1 |
| HRC_EVT_SRC_OBJ_ATTRS_PK1 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ATTRIBUTE_ID, ORA_SEED_SET2 |
| HRC_EVT_SRC_OBJ_ATTRS_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID, NAME, ORA_SEED_SET1 |
| HRC_EVT_SRC_OBJ_ATTRS_U11 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID, NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
