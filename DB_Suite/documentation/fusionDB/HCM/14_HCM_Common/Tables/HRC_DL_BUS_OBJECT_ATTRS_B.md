# HRC_DL_BUS_OBJECT_ATTRS_B

HRC_DL_BUS_OBJECT_ATTRS_B is a standard base table describing attributes that belong to a specific view object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusobjectattrsb-24372.html#hrcdlbusobjectattrsb-24372](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusobjectattrsb-24372.html#hrcdlbusobjectattrsb-24372)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_OBJECT_ATTRS_B_PK | BUS_OBJECT_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUS_OBJECT_ATTR_ID | NUMBER |  | 18 | Yes | BUS_COMM_ATTR_ID |
| VO_ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | VO_ATTRBUTE_NAME |
| COMMON_KEY | VARCHAR2 | 150 |  |  | COMMON_KEY |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
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
| HRC_DL_BUS_OBJECT_ATTRS_B_N20 | Non Unique | Default | SGUID |
| HRC_DL_BUS_OBJECT_ATTRS_B_U1 | Unique | Default | BUS_OBJECT_ATTR_ID, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJECT_ATTRS_B_U11 | Unique | Default | BUS_OBJECT_ATTR_ID, ORA_SEED_SET2 |
| HRC_DL_BUS_OBJECT_ATTRS_B_U2 | Unique | Default | BUSINESS_OBJECT_ID, VO_ATTRIBUTE_NAME, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJECT_ATTRS_B_U21 | Unique | Default | BUSINESS_OBJECT_ID, VO_ATTRIBUTE_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
